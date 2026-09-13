# ARCHITECTURAL_BRIEF: gitgalaxy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/squid-protocol/gitgalaxy.git` |
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
| Total Artifacts | 938 |
| Analyzed Artifacts (Scanned) | 363 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 575 |
| Total LOC | 73664 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 38.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7042 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3525 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.3207 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 41 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 319 | 72512 | 87.9% |
| MARKDOWN | 28 | 0 | 7.7% |
| YAML | 11 | 1008 | 3.0% |
| PLAINTEXT | 3 | 0 | 0.8% |
| MAKEFILE | 1 | 122 | 0.3% |
| SHELL | 1 | 22 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 332 | 91.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 31 | 8.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 575*

**Composition by Extension & Reason:**
- `.md`: 392x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 58 LOC), 1x Excluded (Machine-Generated Source Code Signature: 41 LOC)
- `.png`: 59x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 17x Excluded (Explicitly Denied Extension: '.gif')
- `.js`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 578 LOC), 1x Excluded (Saturation: Line 22 exceeds 500 chars)
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 102786 LOC exceeds safe regex boundaries)
- `.html`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.csv`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 83.6 | 18.8 | 12.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 54.6 | 56.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 13.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.7 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 58.4 | 9.1 | 8.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 7.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 18.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 26.6 | 1.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 75.8 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 86.7 | 3.0 | 1.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 17.4 | 14.2 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 26.8 | 14.3 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1000 | 211 | 7 | `gitgalaxy/galaxyscope.py` |
| cleanup | 67 | 36 | 0 | `tests/tools_recorders/test_record_keeper.py` |
| guards | 7027 | 268 | 59 | `tests/core_engine/test_detector.py` |
| danger | 1845 | 244 | 12 | `gitgalaxy/galaxyscope.py` |
| concurrency | 391 | 89 | 3 | `gitgalaxy/standards/language_standards/languages/python.py` |
| connectivity | 2989 | 258 | 21 | `tests/core_engine/test_detector.py` |
| io | 721 | 222 | 5 | `tests/core_engine/test_galaxyscope.py` |
| crypto | 12 | 10 | 0 | `tests/extraction/languages/test_javascript_strict.py` |
| ipc | 158 | 36 | 0 | `gitgalaxy/galaxyscope.py` |
| time | 86 | 17 | 0 | `gitgalaxy/galaxyscope.py` |
| serialization | 1 | 1 | 0 | `tests/extraction/languages/test_python_strict.py` |
| regex | 2458 | 111 | 39 | `gitgalaxy/core/detector.py` |
| events | 519 | 96 | 3 | `gitgalaxy/galaxyscope.py` |
| tests | 3981 | 186 | 31 | `tests/core_engine/test_galaxyscope.py` |
| docs | 2428 | 267 | 16 | `tests/core_engine/test_detector.py` |
| debt | 2122 | 208 | 16 | `gitgalaxy/standards/language_standards/_shared_patterns.py` |
| mutation | 27394 | 277 | 148 | `gitgalaxy/core/detector.py` |
| dead_code | 2616 | 207 | 21 | `tests/core_engine/test_detector.py` |
| credential | 169 | 57 | 2 | `gitgalaxy/standards/language_standards/languages/apex.py` |
| threat | 136 | 42 | 1 | `gitgalaxy/metrics/signal_processor.py` |
| ml_ai | 220 | 52 | 1 | `tests/extraction/languages/test_java.py` |
| ui | 29 | 16 | 0 | `gitgalaxy/standards/language_standards/languages/python.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/core_engine/test_galaxyscope.py` (Hits: 36)
- `gitgalaxy/security/manifest_parser.py` (Hits: 32)
- `tests/extraction/languages/test_swift_strict.py` (Hits: 29)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **json.py** (`gitgalaxy/standards/language_standards/languages/json.py`) — 53 inbound connections
2. **_strict_harness.py** (`tests/extraction/languages/_strict_harness.py`) — 48 inbound connections
3. **_extraction_harness.py** (`tests/extraction/_extraction_harness.py`) — 46 inbound connections
4. **_shared_patterns.py** (`gitgalaxy/standards/language_standards/_shared_patterns.py`) — 44 inbound connections
5. **detector.py** (`gitgalaxy/core/detector.py`) — 25 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **galaxyscope.py** (`gitgalaxy/galaxyscope.py`) — 57 outbound dependencies
2. **test_python_strict.py** (`tests/extraction/languages/test_python_strict.py`) — 28 outbound dependencies
3. **test_galaxyscope.py** (`tests/core_engine/test_galaxyscope.py`) — 23 outbound dependencies
4. **test_embedded_python.py** (`tests/extraction/languages/test_embedded_python.py`) — 20 outbound dependencies
5. **test_network_risk_sensor.py** (`tests/security_auditing/test_network_risk_sensor.py`) — 20 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_slice_by_braces` (@ `gitgalaxy/core/detector.py`) -> Impact: **1131.1** | LOC: 1244
- `_build_markdown` (@ `gitgalaxy/recorders/llm_recorder.py`) -> Impact: **773.7** | LOC: 1029
- `inspect` (@ `gitgalaxy/standards/language_lens.py`) -> Impact: **353.4** | LOC: 407
- `_calculate_block_metrics` (@ `gitgalaxy/core/detector.py`) -> Impact: **314.8** | LOC: 455
- `execute_pipeline` (@ `gitgalaxy/galaxyscope.py`) -> Impact: **275.4** | LOC: 588
  * *Intent:* """ Executes the synthesis protocol with a multi-recorder exit strategy. PIPELINE ONBOARDING (Execution Flow): The method enforces a strict chronologi...
- `splice` (@ `gitgalaxy/core/detector.py`) -> Impact: **266.7** | LOC: 465
- `generate_report` (@ `gitgalaxy/recorders/audit_recorder.py`) -> Impact: **264.4** | LOC: 480
- `calculate_risk_vector` (@ `gitgalaxy/metrics/signal_processor.py`) -> Impact: **250.1** | LOC: 620
- `_slice_by_keywords` (@ `gitgalaxy/core/detector.py`) -> Impact: **241.9** | LOC: 393
- `measure` (@ `tests/tools/tree_sitter_accuracy_audit.py`) -> Impact: **217.8** | LOC: 477
  * *Intent:* """Runs the full pinned-corpus scan + tree-sitter diff, returns the metrics dict."""

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/extraction/languages` | 92 | 12329.74 | 13.24% | 0.0% |
| `gitgalaxy/core` | 9 | 9671.94 | 36.32% | 9.66% |
| `tests/core_engine` | 25 | 5293.44 | 13.07% | 0.0% |
| `gitgalaxy/recorders` | 8 | 3993.42 | 47.17% | 3.08% |
| `gitgalaxy` | 6 | 3067.48 | 30.09% | 0.0% |
| `gitgalaxy/metrics` | 5 | 3002.58 | 44.09% | 4.57% |
| `gitgalaxy/standards` | 7 | 1720.04 | 14.49% | 6.81% |
| `tests/security_auditing` | 15 | 1705.6 | 11.91% | 0.0% |
| `gitgalaxy/security` | 5 | 1535.38 | 30.75% | 0.0% |
| `gitgalaxy/standards/language_standards/languages` | 59 | 1151.0 | 5.86% | 67.52% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `gitgalaxy/standards/language_standards/_shared_patterns.py` -> **100.0%** Exposure
- `gitgalaxy/standards/language_standards/languages/groovy.py` -> **100.0%** Exposure
- `gitgalaxy/standards/language_standards/languages/livecode.py` -> **100.0%** Exposure
- `gitgalaxy/standards/language_standards/languages/rust.py` -> **100.0%** Exposure
- `gitgalaxy/standards/language_standards/languages/swift.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.claude/hooks/pytest_quiet.py` -> **100.0%** Exposure
- `gitgalaxy/cobol_refractor_controller.py` -> **100.0%** Exposure
- `gitgalaxy/cobol_to_java_controller.py` -> **100.0%** Exposure
- `gitgalaxy/core/detector.py` -> **100.0%** Exposure
- `gitgalaxy/core/guidestar_lens.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/core_engine/test_detector.py` -> **135** Orphaned Functions | **0** Duplicates
- `tests/core_engine/test_signal_processor.py` -> **63** Orphaned Functions | **0** Duplicates
- `tests/core_engine/test_galaxyscope.py` -> **59** Orphaned Functions | **0** Duplicates
- `tests/core_engine/test_prism.py` -> **52** Orphaned Functions | **0** Duplicates
- `tests/extraction/languages/test_matlab_strict.py` -> **35** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/security_auditing/test_pii_leak_hunter.py` -> **100.0%** Exposure
- `tests/security_auditing/test_vault_sentinel.py` -> **100.0%** Exposure
- `tests/core_engine/test_aperture.py` -> **99.9998%** Exposure
- `tests/extraction/languages/test_solidity_strict.py` -> **99.3723%** Exposure
- `tests/extraction/languages/test_yaml_strict.py` -> **97.398%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1948` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `gitgalaxy/core/detector.py` (PYTHON) -> Cumulative Risk: **625.15**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 6980.3 | **LOC:** 6888 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 94.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Safety Score (99.4947%)
- **Heaviest Functions:** `_slice_by_braces` (Impact: 1131.1), `_calculate_block_metrics` (Impact: 314.8), `splice` (Impact: 266.7)

### 2. `gitgalaxy/core/prism.py` (PYTHON) -> Cumulative Risk: **586.4**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1276.4 | **LOC:** 1421 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 96.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.6903%), Verification (80.0%)
- **Heaviest Functions:** `_strip_single_line_comments` (Impact: 124.1), `_mask_perl_line` (Impact: 75.4), `_compile_regex_matrix` (Impact: 59.5)

### 3. `gitgalaxy/recorders/llm_recorder.py` (PYTHON) -> Cumulative Risk: **576.91**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2069.44 | **LOC:** 1440 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.911%), Cognitive Load (83.6327%)
- **Heaviest Functions:** `_build_markdown` (Impact: 773.7), `generate_artifacts` (Impact: 37.7), `_generate_sqlite_graph` (Impact: 13.4)

### 4. `gitgalaxy/metrics/signal_processor.py` (PYTHON) -> Cumulative Risk: **558.12**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2043.02 | **LOC:** 2117 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.2029%), Verification (80.0%)
- **Heaviest Functions:** `calculate_risk_vector` (Impact: 250.1), `summarize_galaxy_metrics` (Impact: 193.3), `generate_forensic_report` (Impact: 69.1)

### 5. `gitgalaxy/galaxyscope.py` (PYTHON) -> Cumulative Risk: **555.51**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2523.6 | **LOC:** 3218 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.0431%), Verification (80.0%)
- **Heaviest Functions:** `execute_pipeline` (Impact: 275.4), `_process_file_worker` (Impact: 135.5), `_resolve_dependency_graph` (Impact: 105.8)

### 6. `gitgalaxy/recorders/audit_recorder.py` (PYTHON) -> Cumulative Risk: **542.69**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 589.22 | **LOC:** 581 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.5186%), Cognitive Load (81.1094%)
- **Heaviest Functions:** `generate_report` (Impact: 264.4), `descale` (Impact: 14.1), `format_label` (Impact: 7.6)

### 7. `gitgalaxy/recorders/gpu_recorder.py` (PYTHON) -> Cumulative Risk: **530.92**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 360.44 | **LOC:** 441 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.6164%), Verification (80.0%)
- **Heaviest Functions:** `record_mission` (Impact: 119.0), `__init__` (Impact: 7.2), `_intern` (Impact: 4.2)

### 8. `gitgalaxy/standards/language_lens.py` (PYTHON) -> Cumulative Risk: **530.69**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1342.54 | **LOC:** 1152 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.8699%), Verification (80.0%)
- **Heaviest Functions:** `inspect` (Impact: 353.4), `_tier_4_heuristic_discovery` (Impact: 122.9), `_evaluate_ecosystem_gravity` (Impact: 81.6)

### 9. `gitgalaxy/metrics/statistical_auditor.py` (PYTHON) -> Cumulative Risk: **513.64**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 515.52 | **LOC:** 579 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.8053%), Verification (80.0%)
- **Heaviest Functions:** `audit` (Impact: 151.5), `__init__` (Impact: 10.7), `_is_dead_code` (Impact: 8.0)

### 10. `gitgalaxy/cobol_refractor_controller.py` (PYTHON) -> Cumulative Risk: **507.96**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 297.7 | **LOC:** 434 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.1898%), Verification (80.0%)
- **Heaviest Functions:** `main` (Impact: 31.5), `process_payload` (Impact: 24.7), `record_dead_code` (Impact: 14.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `gitgalaxy/core/detector.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6980.3 | **LOC:** 6888 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 94.0%
- **Risk Profile:** Cognitive Load (69.256%), Tech Debt (15.9965%)
**Top Internal Functions/Classes:**
  * `_slice_by_braces` (Impact: 1131.1)
  * `_calculate_block_metrics` (Impact: 314.8)
  * `splice` (Impact: 266.7)
  * `_slice_by_keywords` (Impact: 241.9)
  * `_build_brace_safe_stream` (Impact: 177.8)
    * *Intent:* """ Shields string/char literals and (for C-family languages) dead #if/#else macro branches so a bra...
**Contextual Mitigations & Amplifications:**
* *Sec High Risk Execution:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 946 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 2986
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1425`, `structural_boundaries: 413`, `args: 65`, `func_start: 61`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 83`, `state_mutation: 1094`, `dead_code: 39`, `planned_debt: 2`, `fragile_debt: 19`
* *Architecture:* `api: 18`, `concurrency: 2`, `import: 14`
* *Defense:* `safety: 35`, `doc: 63`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.03
  * `Choke Point (Betweenness):` 0.000351 | `Ripple Effect (Closeness):` 0.06833
  * `Imports (Out-Degree: 2):` bisect, collections, gitgalaxy.core.spatial_correlation, gitgalaxy.standards.analysis_lens, gitgalaxy.standards.language_standards, hashlib, logging, math...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `gitgalaxy/galaxyscope.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2523.6 | **LOC:** 3218 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (68.7714%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `execute_pipeline` (Impact: 275.4)
    * *Intent:* """ Executes the synthesis protocol with a multi-recorder exit strategy. PIPELINE ONBOARDING (Execut...
  * `_process_file_worker` (Impact: 135.5)
    * *Intent:* """Processes a single file path using the worker's cached hardware modules."""
  * `_resolve_dependency_graph` (Impact: 105.8)
    * *Intent:* """ Pass 1.5: Optimized relational token aggregation & Fuzzy Suffix Matching. Defused O(N^2) Bomb us...
  * `_calculate_risk_exposures` (Impact: 94.2)
    * *Intent:* """ Phase 3: Universal Exposure Framework & Signal Processing. Translates raw Structural Signatures ...
  * `main` (Impact: 90.8)
    * *Intent:* # ============================================================================== # ORCHESTRATOR CORE...
**Contextual Mitigations & Amplifications:**
* *Sec High Risk Execution:* 1 instances
* *Amplified Rce:* 2 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 435 instances
* *Concurrency (weighted view):* 13
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 1470
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 522`, `structural_boundaries: 233`, `args: 35`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 78`, `high_risk_execution: 2`, `state_mutation: 600`, `dead_code: 1`
* *Architecture:* `io: 13`, `api: 6`, `concurrency: 3`, `import: 62`
* *Defense:* `safety: 49`, `doc: 20`, `test: 2`, `immutability_locks: 8`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.171
  * `Choke Point (Betweenness):` 0.001148 | `Ripple Effect (Closeness):` 0.01151
  * `Imports (Out-Degree: 30):` DAG, argparse, collections, concurrent.futures, copy, datetime, gitgalaxy.core.aperture, gitgalaxy.core.detector...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `gitgalaxy/recorders/llm_recorder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2069.44 | **LOC:** 1440 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (83.6327%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_build_markdown` (Impact: 773.7)
  * `generate_artifacts` (Impact: 37.7)
  * `_generate_sqlite_graph` (Impact: 13.4)
  * `__init__` (Impact: 5.8)
  * `_outbound` (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Sec High Risk Execution:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 361 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 1196
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 297`, `structural_boundaries: 61`, `args: 28`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 474`
* *Architecture:* `io: 2`, `api: 3`, `concurrency: 2`, `import: 10`
* *Defense:* `safety: 9`, `doc: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.287
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.010412
  * `Imports (Out-Degree: 1):` collections, gitgalaxy.standards, heapq, json, logging, pathlib, sqlite3, statistics...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `gitgalaxy/metrics/signal_processor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2043.02 | **LOC:** 2117 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (64.6166%), Tech Debt (8.1074%)
**Top Internal Functions/Classes:**
  * `calculate_risk_vector` (Impact: 250.1)
  * `summarize_galaxy_metrics` (Impact: 193.3)
    * *Intent:* # ========================================================================== # GLOBAL SYNTHESIS & 2-...
  * `generate_forensic_report` (Impact: 69.1)
    * *Intent:* # -------------------------------------------------------------------------- # REPORTING UTILITIES #...
  * `_calc_verification` (Impact: 57.2)
  * `_calc_documentation` (Impact: 30.5)
**Contextual Mitigations & Amplifications:**
* *Sec High Risk Execution:* 1 instances
* *Amplified Cascading Flux:* 310 instances
* *State Mutation (weighted view):* 1078
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 342`, `structural_boundaries: 131`, `args: 41`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 458`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 9`, `concurrency: 2`, `import: 10`
* *Defense:* `safety: 35`, `doc: 23`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.98
  * `Choke Point (Betweenness):` 0.00013 | `Ripple Effect (Closeness):` 0.028497
  * `Imports (Out-Degree: 1):` collections.abc, gitgalaxy.standards, gitgalaxy.standards.fidelity_table, logging, math, os, re, statistics...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `tests/core_engine/test_detector.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1638.62 | **LOC:** 3831 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 85.7%
- **Risk Profile:** Cognitive Load (14.9956%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_spatial_mapper_sectorization_and_monolith` (Impact: 15.5)
    * *Intent:* """ Proves the engine correctly groups files into sector constellations by their parent directories,...
  * `test_detector_c_macro_no_space_boundaries_issue_1764` (Impact: 14.2)
    * *Intent:* """ Regression test for a bug where `#if(1)` or `#elif(0)` (valid C preprocessor syntax without a sp...
  * `test_detector_c_macro_static_truth_prunes_branches` (Impact: 13.9)
    * *Intent:* """ Companion to the #1720 fix: statically-decidable #if conditions still prune the dead branch. #if...
  * `test_detector_orphan_census_excludes_synthetic_slicer_names` (Impact: 13.1)
    * *Intent:* """ Regression test for #2547: languages sliced by Mode D (_slice_by_keywords) or Mode E (_slice_by_...
  * `test_detector_mode_d_livecode_script_handlers` (Impact: 11.0)
    * *Intent:* """ #2410: LiveCode had no ScopeParsingRegistry entry, so it fell through to Mode B brace-slicing an...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 204 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 946
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 868`, `args: 190`, `func_start: 138`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 5`, `state_mutation: 538`, `dead_code: 28`, `planned_debt: 2`, `fragile_debt: 9`, `unreferenced_by_name: 135`
* *Architecture:* `io: 4`, `api: 143`, `import: 53`
* *Defense:* `safety: 352`, `doc: 140`, `test: 157`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` gitgalaxy.core.detector, gitgalaxy.core.prism, gitgalaxy.core.spatial_mapper, gitgalaxy.standards.gitgalaxy_config, gitgalaxy.standards.language_standards, logging, math, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/standards/language_lens.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1342.54 | **LOC:** 1152 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (67.7602%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `inspect` (Impact: 353.4)
  * `_tier_4_heuristic_discovery` (Impact: 122.9)
    * *Intent:* # ========================================================================= # THE TIER 4 HEURISTIC D...
  * `_evaluate_ecosystem_gravity` (Impact: 81.6)
  * `_tier_3_lexical_scan` (Impact: 61.1)
  * `_find_balanced_end` (Impact: 28.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 176 instances
* *State Mutation (weighted view):* 545
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 269`, `structural_boundaries: 98`, `args: 19`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 193`
* *Architecture:* `io: 2`, `api: 6`, `import: 9`
* *Defense:* `safety: 6`, `doc: 12`, `sync_locks: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.475
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.015347
  * `Imports (Out-Degree: 1):` contextlib, gitgalaxy.standards.gitgalaxy_config, gitgalaxy.standards.language_standards, logging, math, pathlib, re, time...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `gitgalaxy/core/prism.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1276.4 | **LOC:** 1421 | **CtrlFlow:** 34.2% | **Authorship Centralization:** 96.3%
- **Risk Profile:** Cognitive Load (40.1092%), Tech Debt (61.1719%)
**Top Internal Functions/Classes:**
  * `_strip_single_line_comments` (Impact: 124.1)
    * *Intent:* """ Single-line comment stripper for the "line_exclusive" family, driven by each language's own real...
  * `_mask_perl_line` (Impact: 75.4)
  * `_compile_regex_matrix` (Impact: 59.5)
    * *Intent:* """Safely pre-compiles the standard regex matrix based on dynamic config lengths."""
  * `_strip_segment_comments` (Impact: 44.9)
    * *Intent:* """Surgically strips documentation using an ordered, additive pipeline."""
  * `_partition_embedded_languages` (Impact: 43.8)
    * *Intent:* """Splits content into language segments based on embedded language triggers."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 180 instances
* *State Mutation (weighted view):* 579
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 121`, `args: 36`, `func_start: 33`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 219`, `fragile_debt: 5`, `duplicate_logic: 2`
* *Architecture:* `api: 10`, `import: 4`
* *Defense:* `safety: 3`, `doc: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.024571
  * `Imports (Out-Degree: 0):` gitgalaxy.standards.language_standards, logging, re, typing
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `gitgalaxy/security/manifest_parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1060.58 | **LOC:** 748 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.5578%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `slice_manifest` (Impact: 181.9)
  * `locate_physical_package` (Impact: 129.9)
  * `_parse_pyproject_toml` (Impact: 36.2)
    * *Intent:* """ Audits modern Python manifests (PEP 621 `[project] dependencies` arrays and Poetry's `[tool.poet...
  * `_parse_requirements_txt` (Impact: 25.2)
    * *Intent:* """ Extracts direct Python packages and flags absolute VCS/URI references. """
  * `_parse_pip_conf` (Impact: 23.2)
    * *Intent:* """ Audits Python configuration files (pip.conf, .pypirc) for Dependency Confusion vulnerabilities c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 183 instances
* *State Mutation (weighted view):* 556
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 121`, `args: 11`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 190`
* *Architecture:* `io: 32`, `api: 6`, `import: 6`
* *Defense:* `safety: 7`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.257
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.01625
  * `Imports (Out-Degree: 1):` json, logging, os, pathlib, re, typing
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `tests/core_engine/test_galaxyscope.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 951.16 | **LOC:** 2465 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.2177%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_recorder_exception_survivability` (Impact: 16.3)
    * *Intent:* # ============================================================================== # TEST 23: RECORDER...
  * `test_phase_10_manifest_paths_includes_all_supported_ecosystems` (Impact: 13.4)
    * *Intent:* # ============================================================================== # TEST 33: MANIFEST...
  * `test_cicd_policy_enforcement_gates` (Impact: 12.4)
    * *Intent:* # ============================================================================== # TEST 2: THE CI/CD...
  * `test_sarif_ignored_paths_sanitization` (Impact: 11.6)
    * *Intent:* # ============================================================================== # TEST 19: SARIF IG...
  * `test_synthetic_node_generation` (Impact: 11.2)
    * *Intent:* # ============================================================================== # TEST 17: SYNTHETI...
**Contextual Mitigations & Amplifications:**
* *Sec Hardcoded Secrets:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 54 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 510
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 271`, `args: 65`, `func_start: 65`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 49`, `high_risk_execution: 1`, `state_mutation: 402`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 59`
* *Architecture:* `io: 36`, `api: 65`, `concurrency: 2`, `import: 75`
* *Defense:* `safety: 36`, `doc: 64`, `test: 241`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` concurrent.futures, failure, gitgalaxy.core.aperture, gitgalaxy.core.detector, gitgalaxy.galaxyscope, gitgalaxy.metrics.signal_processor, gitgalaxy.recorders.record_keeper, gitgalaxy.standards...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/core/network_risk_sensor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 600.8 | **LOC:** 593 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (60.8194%), Tech Debt (9.8118%)
**Top Internal Functions/Classes:**
  * `build_dependency_graph` (Impact: 83.6)
    * *Intent:* """ Builds the directed graph and calculates multi-dimensional risk vectors. Modifies the 'telemetry...
  * `_resolve_target` (Impact: 61.1)
  * `_fallback_build_graph` (Impact: 34.5)
  * `extract_test_coverage_mapping` (Impact: 32.5)
    * *Intent:* """ Maps function calls from test files to their imported production targets. Returns a dictionary m...
  * `_build_folded_resolution_map` (Impact: 12.0)
    * *Intent:* """ #2540: derives per-language lowercase-keyed views of the resolution keys so imports from case-in...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 109 instances
* *State Mutation (weighted view):* 343
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 61`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 125`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 4`, `import: 11`
* *Defense:* `safety: 14`, `doc: 8`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.205
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.012628
  * `Imports (Out-Degree: 1):` A, Text.Pandoc.Generic, collections, gitgalaxy.standards.analysis_lens, gitgalaxy.standards.language_standards, logging, math, networkx...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `gitgalaxy/recorders/audit_recorder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 589.22 | **LOC:** 581 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (81.1094%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `generate_report` (Impact: 264.4)
  * `descale` (Impact: 14.1)
    * *Intent:* """Dynamically scales integers back to floats using a fixed-string check."""
  * `format_label` (Impact: 7.6)
    * *Intent:* """Translates raw dictionary keys into descriptive human-readable labels."""
  * `__init__` (Impact: 5.9)
  * `decode_galaxy` (Impact: 1.9)
    * *Intent:* """Standalone decoding logic preserved for CLI compatibility."""
**Contextual Mitigations & Amplifications:**
* *Sec High Risk Execution:* 1 instances
* *Amplified Cascading Flux:* 86 instances
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 29`, `args: 10`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 109`
* *Architecture:* `io: 3`, `api: 6`, `import: 8`
* *Defense:* `safety: 12`, `doc: 5`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.287
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.010412
  * `Imports (Out-Degree: 1):` argparse, gitgalaxy.standards, json, logging, os, pathlib, re, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/core_engine/test_signal_processor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 562.78 | **LOC:** 1628 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (17.5078%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create_synthetic_star` (Impact: 13.3)
    * *Intent:* # ============================================================================== # SYNTHETIC GALAXY ...
  * `test_signal_processor_small_file_scores_on_counts` (Impact: 7.0)
    * *Intent:* """ #2655: the old flat 5.0 small-file floor (`loc < 15`) is gone. A file below the evidence-mass fl...
  * `test_signal_processor_unknown_language_gets_no_language_term` (Impact: 6.4)
    * *Intent:* # ============================================================================== # TEST 47: TIER 3 L...
  * `test_signal_processor_minified_tripwire` (Impact: 6.3)
    * *Intent:* # ============================================================================== # TEST 11: THE MINI...
  * `test_signal_processor_report_fallback` (Impact: 5.4)
    * *Intent:* # ============================================================================== # TEST 42: REPORT G...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 214`, `args: 65`, `func_start: 65`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 245`, `planned_debt: 1`, `fragile_debt: 3`, `unreferenced_by_name: 63`
* *Architecture:* `io: 3`, `api: 65`, `import: 9`
* *Defense:* `safety: 133`, `doc: 65`, `test: 68`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` gitgalaxy.metrics.signal_processor, gitgalaxy.recorders.sarif_recorder, identity, json, logging, os, pytest, tempfile...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/metrics/statistical_auditor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 515.52 | **LOC:** 579 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (73.4007%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `audit` (Impact: 151.5)
    * *Intent:* """Executes statistical gating to identify data-dumps and structural outliers."""
  * `__init__` (Impact: 10.7)
  * `_is_dead_code` (Impact: 8.0)
    * *Intent:* """Determines if an artifact is predominantly dead code or comments."""
  * `_is_threat` (Impact: 7.9)
    * *Intent:* """ Determines if an artifact contains active security threat signatures. Used by the Quarantine Gua...
  * `_is_highly_blended` (Impact: 7.6)
    * *Intent:* """Determines if a file is a Polyglot where the primary language is < 80% of the mass."""
**Contextual Mitigations & Amplifications:**
* *Sec High Risk Execution:* 1 instances
* *Amplified Cascading Flux:* 99 instances
* *State Mutation (weighted view):* 317
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 36`, `args: 8`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 119`
* *Architecture:* `io: 2`, `api: 3`, `import: 4`
* *Defense:* `safety: 7`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.943
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.010412
  * `Imports (Out-Degree: 0):` logging, os, statistics, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `gitgalaxy/recorders/record_keeper.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 475.5 | **LOC:** 1078 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (54.1192%), Tech Debt (10.2037%)
**Top Internal Functions/Classes:**
  * `record_mission` (Impact: 9.5)
  * `__init__` (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Sec Db Hooks:* 1 instances
* *Ai Guardrails:* 1 instances
* *Amplified Cascading Flux:* 131 instances
* *State Mutation (weighted view):* 441
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 19`, `args: 2`, `func_start: 2`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 179`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 4`, `import: 7`
* *Defense:* `safety: 10`, `doc: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.86
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.0136
  * `Imports (Out-Degree: 2):` gitgalaxy.standards.analysis_lens, json, logging, pathlib, sqlite3, statistics, typing
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `gitgalaxy/security/security_auditor.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 418.74 | **LOC:** 436 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (58.6488%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_resolve_dependency_graph` (Impact: 50.2)
    * *Intent:* """ Resolves transitive fragility and Downstream Exposure using C-optimized traversals (NetworkX) if...
  * `audit_repository` (Impact: 36.2)
    * *Intent:* """ Orchestrates the resolution of transitive dependency graphs and executes the XGBoost model again...
  * `_construct_feature_matrix` (Impact: 31.5)
    * *Intent:* """Reconstructs the Pandas DataFrame exactly as train_threat_model.py did."""
  * `__init__` (Impact: 28.2)
    * *Intent:* # Updated default to the new multiclass model
  * `get_nth_degree` (Impact: 10.6)
    * *Intent:* """BFS using collections.deque for O(1) popping."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 77 instances
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 37`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 98`
* *Architecture:* `io: 1`, `api: 4`, `import: 9`
* *Defense:* `safety: 8`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.916
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.016072
  * `Imports (Out-Degree: 1):` collections, gitgalaxy.standards.analysis_lens, logging, networkx, numpy, pandas, pathlib, typing...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `tests/security_auditing/test_network_risk_sensor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 379.02 | **LOC:** 852 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.3212%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_network_ecosystem_roles` (Impact: 12.7)
    * *Intent:* # ============================================================================== # TEST 3: ECOSYSTEM...
  * `test_network_duplicate_filename_ambiguous_import_skipped` (Impact: 9.6)
    * *Intent:* # ============================================================================== # TEST 6: DUPLICATE...
  * `test_network_duplicate_filename_path_qualified_import_resolves` (Impact: 9.5)
    * *Intent:* # ============================================================================== # TEST 7: DUPLICATE...
  * `test_network_exact_case_match_wins_over_folded` (Impact: 9.5)
    * *Intent:* # ============================================================================== # TEST 17: EXACT-CA...
  * `test_network_duplicate_filename_fallback_mode` (Impact: 9.4)
    * *Intent:* # ============================================================================== # TEST 8: DUPLICATE...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 146
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 136`, `args: 36`, `func_start: 36`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 64`, `dead_code: 1`, `unreferenced_by_name: 31`
* *Architecture:* `api: 36`, `import: 4`
* *Defense:* `safety: 69`, `doc: 36`, `test: 72`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` A, Foo, Parser, Text.Pandoc.Generic, and, chain, copy, creates...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/core/guidestar_lens.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 376.5 | **LOC:** 512 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.9817%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_intent_status` (Impact: 22.5)
    * *Intent:* """Returns the specific Intent Lock for a given file path based on strict, pattern, or sector match....
  * `_calculate_documentation_coverage` (Impact: 21.4)
    * *Intent:* # ============================================================================== # galaxyscope:ignor...
  * `__init__` (Impact: 16.5)
  * `_scan_gitattributes` (Impact: 15.2)
    * *Intent:* # ============================================================================== # galaxyscope:ignor...
  * `_deep_inspect_manifest` (Impact: 14.2)
    * *Intent:* """Dispatches files to specific parsers based on their format."""
**Contextual Mitigations & Amplifications:**
* *Sec Io:* 1 instances
* *Amplified Cascading Flux:* 58 instances
* *State Mutation (weighted view):* 181
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 59`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 65`
* *Architecture:* `io: 8`, `api: 5`, `import: 8`
* *Defense:* `safety: 10`, `doc: 16`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.287
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.010412
  * `Imports (Out-Degree: 2):` fnmatch, gitgalaxy.standards.gitgalaxy_config, json, logging, os, pathlib, re, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/core_engine/test_prism.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 375.7 | **LOC:** 1325 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.7214%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_prism_jcl_comment_stripping_details` (Impact: 7.8)
    * *Intent:* """ #2610: JCL `//*` whole-line comments move to the comment stream while everything `//`-statement-...
  * `test_prism_sub_families_fix_the_standard_block_delimiter_gap` (Impact: 5.1)
    * *Intent:* """ Regression test for #621: sqlite, lua, haskell, powershell, and perl were all classified "standa...
  * `test_prism_standard_block_c_family_unaffected_by_sub_family_split` (Impact: 4.8)
    * *Intent:* """ Regression guard for #621: splitting sqlite/lua/haskell/powershell/perl out of "standard_block" ...
  * `test_prism_livecode_string_has_no_backslash_escape` (Impact: 4.3)
    * *Intent:* """ #2419: LiveCode string literals have NO `\\` escapes -- `\\` is an ordinary character. The share...
  * `test_prism_issue_1532_nested_comment_stripping_preserves_line_count` (Impact: 4.2)
    * *Intent:* """ Regression test for #1532: `_strip_nested_comments()` -- shared by every "recursive_block"/"recu...
**Contextual Mitigations & Amplifications:**
* *Obscured Payload:* 1 instances
* *Memory Corruption:* 1 instances
* *Tech Debt:* 1 instances
* *Secrets-Risk:* 1 instances
* *Injection Surface:* 1 instances
* *Everything:* 1 instances
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 9 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 176
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 375`, `args: 56`, `func_start: 53`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 158`, `fragile_debt: 3`, `unreferenced_by_name: 52`
* *Architecture:* `api: 53`, `import: 62`
* *Defense:* `safety: 182`, `doc: 55`, `test: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` gitgalaxy.core.prism, gitgalaxy.standards.gitgalaxy_config, gitgalaxy.standards.language_standards, pytest, re, time, to, unittest.mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/recorders/gpu_recorder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 360.44 | **LOC:** 441 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (55.6507%), Tech Debt (14.4553%)
**Top Internal Functions/Classes:**
  * `record_mission` (Impact: 119.0)
  * `__init__` (Impact: 7.2)
  * `_intern` (Impact: 4.2)
    * *Intent:* """Minifies payload footprints by mapping repetitive strings to integer IDs."""
  * `save_minified` (Impact: 2.5)
    * *Intent:* """Serializes with maximum JSON compression to the provided output path."""
**Contextual Mitigations & Amplifications:**
* *Sec High Risk Execution:* 1 instances
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 23`, `args: 5`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 100`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 4`, `import: 7`
* *Defense:* `safety: 3`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.943
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.010412
  * `Imports (Out-Degree: 2):` gc, gitgalaxy.standards, gitgalaxy.standards.config_resolver, json, logging, pathlib, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/extraction/languages/test_groovy_strict.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 359.0 | **LOC:** 865 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (18.6497%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_groovy_func_start_paren_less_builder_call_false_positive_regression` (Impact: 22.9)
    * *Intent:* """ #2558: found while investigating #2530 -- once that fix correctly excluded `button(...) { ... }`...
  * `test_groovy_func_start_statement_keyword_as_prefix_false_positive_regression` (Impact: 16.3)
    * *Intent:* """ #2676: found while gathering evidence for #2558 -- branch 1 (the >=1-prefix-token branch) alread...
  * `test_groovy_signature_deep_positive_and_negative` (Impact: 10.4)
  * `test_groovy_func_start_markup_builder_dsl_call_false_positive_regression` (Impact: 9.4)
    * *Intent:* """ #2530: func_start's zero-prefix branch (needed to match a real bare constructor, `MyClass(String...
  * `test_groovy_signature_positive_and_negative` (Impact: 8.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 265`, `args: 52`, `func_start: 31`
* *Risk/State:* `state_mutation: 82`, `planned_debt: 1`, `fragile_debt: 17`, `unreferenced_by_name: 31`
* *Architecture:* `io: 1`, `api: 31`, `import: 5`
* *Defense:* `safety: 116`, `doc: 28`, `test: 34`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` _strict_harness, com.example.Foo, com.example.foo.Bar, com.example.gradle.Plugin, gitgalaxy.standards.language_standards, pathlib, pytest, static...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/extraction/languages/test_livecode_strict.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 354.8 | **LOC:** 726 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.0498%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `assert_linear_redos_scaling` (Impact: 20.4)
    * *Intent:* """ Measures pattern.search() time at each size in `sizes` (each isolated in its own subprocess via ...
  * `test_livecode_signature_positive_and_negative` (Impact: 10.4)
  * `test_livecode_dependency_capture_extracts_path` (Impact: 9.9)
    * *Intent:* """ _dependency_capture is paired with `import` and must extract the exact dependency path/module st...
  * `test_livecode_class_start_dotted_module_name_regression` (Impact: 6.8)
    * *Intent:* """ Regression test (Rule 11-class nested/multi-segment coverage): the name capture `["\\'a-zA-Z_]\\...
  * `_measure_scaling_point` (Impact: 6.7)
    * *Intent:* # ============================================================================== # REDOS SCALING VER...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 45 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 156`, `args: 43`, `func_start: 33`
* *Risk/State:* `state_mutation: 75`, `planned_debt: 1`, `fragile_debt: 12`, `unreferenced_by_name: 30`
* *Architecture:* `io: 5`, `api: 31`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 88`, `doc: 26`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` _strict_harness, gitgalaxy.standards.language_standards, multiprocessing, pathlib, pytest, re, shapes, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/extraction/languages/test_perl_strict.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 350.52 | **LOC:** 597 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (17.73%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_perl_args_prototype_falls_through_to_body_idiom_scan` (Impact: 11.6)
    * *Intent:* """ #1607: a legacy Perl PROTOTYPE (`sub Get8u($$)`) is a sequence of bare sigils with NO commas, ev...
  * `test_perl_signature_positive_and_negative` (Impact: 10.4)
  * `test_perl_branch_colon_ambiguity_and_defined_or` (Impact: 8.3)
  * `test_perl_globals_magic_variable_boundary_regression` (Impact: 7.8)
    * *Intent:* """ Regression test: `$$`, `$@`, `$!`, and `$?` were inside the shared trailing \\b group. Each ends...
  * `test_perl_brace_safe_stream_escaped_brace_in_regex_does_not_desync` (Impact: 7.6)
    * *Intent:* """ #1517: an escaped `\\{`/`\\}` inside a bare `/regex/` literal (never shielded at all -- perl reg...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 19 instances
* *Amplified Rce:* 3 instances
* *Amplified Cascading Flux:* 48 instances
* *High Risk Execution (weighted view):* 2
* *Sec Tainted Injection (weighted view):* 3
* *State Mutation (weighted view):* 184
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 192`, `args: 30`, `func_start: 30`
* *Risk/State:* `high_risk_execution: 21`, `state_mutation: 88`, `planned_debt: 2`, `fragile_debt: 4`, `unreferenced_by_name: 30`
* *Architecture:* `io: 2`, `api: 30`, `import: 10`
* *Defense:* `safety: 114`, `doc: 19`, `test: 32`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` _strict_harness, gitgalaxy.core.detector, gitgalaxy.standards.language_standards, pathlib, pytest, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/recorders/sbom_recorder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 340.64 | **LOC:** 359 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.7317%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `generate_report` (Impact: 68.0)
  * `_audit_with_cache` (Impact: 45.6)
    * *Intent:* """ CACHED mode: every candidate file is hashed; verdicts are reused on hash hits and freshly comput...
  * `_audit_capped_sample` (Impact: 17.2)
    * *Intent:* """ LEGACY mode (no cache configured): per-directory capped sampling (#254). Coverage is honestly di...
  * `_iter_candidate_files` (Impact: 11.5)
    * *Intent:* """ Yields every auditable code file in the package in RISK-PRIORITY order: entry-point-named files ...
  * `__init__` (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Sec High Risk Execution:* 1 instances
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 52`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 67`
* *Architecture:* `io: 5`, `api: 2`, `import: 12`
* *Defense:* `safety: 2`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.506
  * `Choke Point (Betweenness):` 4e-05 | `Ripple Effect (Closeness):` 0.012628
  * `Imports (Out-Degree: 4):` datetime, gitgalaxy.security.manifest_parser, gitgalaxy.security.security_lens, gitgalaxy.standards.gitgalaxy_config, gitgalaxy.standards.language_lens, gitgalaxy.standards.language_standards, json, logging...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `gitgalaxy/metrics/chronometer.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 320.58 | **LOC:** 458 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.7431%), Tech Debt (14.7229%)
**Top Internal Functions/Classes:**
  * `_stream_git_log` (Impact: 62.0)
  * `_determine_commit_bounds` (Impact: 26.1)
    * *Intent:* """ [SIGNAL 1: ABSOLUTE BOUNDARIES] Determines the project's start and end dates for temporal normal...
  * `__init__` (Impact: 15.7)
  * `_initialize_history_scan` (Impact: 9.1)
    * *Intent:* """Dispatches the survey engines to establish boundaries and churn cache."""
  * `_load_ignored_revs` (Impact: 7.9)
    * *Intent:* """Loads non-functional cosmetic commits to filter out of the churn math."""
**Contextual Mitigations & Amplifications:**
* *Sec High Risk Execution:* 1 instances
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 51 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 174
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 42`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 6`, `state_mutation: 72`, `fragile_debt: 1`
* *Architecture:* `io: 8`, `api: 3`, `import: 8`
* *Defense:* `safety: 12`, `doc: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.254
  * `Choke Point (Betweenness):` 4.6e-05 | `Ripple Effect (Closeness):` 0.012628
  * `Imports (Out-Degree: 1):` gitgalaxy.standards, gitgalaxy.standards.config_resolver, logging, os, pathlib, shutil, subprocess, time...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/extraction/languages/test_html_strict.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 313.88 | **LOC:** 746 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.2623%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_html_star_ngif_leading_boundary_regression` (Impact: 12.0)
    * *Intent:* """ Regression test for a real bug: `branch`'s `*ngIf` (Angular's structural directive) was inside t...
  * `test_html_single_quote_bug_reproduces_on_old_double_quote_only_patterns` (Impact: 11.3)
    * *Intent:* # NOTE: this test was originally grouped under a shared "cross-language sweep" # section in tests/co...
  * `test_html_signature_positive_and_negative` (Impact: 10.3)
  * `test_html_signature_adversarial` (Impact: 10.3)
  * `test_html_signature_deep` (Impact: 10.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 29 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 27
* *State Mutation (weighted view):* 118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 177`, `args: 27`, `func_start: 27`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 60`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 27`, `unreferenced_by_name: 27`
* *Architecture:* `io: 7`, `api: 27`, `concurrency: 7`, `import: 6`
* *Defense:* `safety: 94`, `doc: 22`, `test: 32`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.542
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` _strict_harness, gitgalaxy.standards.language_standards, pathlib, pytest, re, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `gitgalaxy/core/detector.py` -> Churn: **100.0%** | Cog Load: 69.256% | Debt: 15.9965%
- `gitgalaxy/core/prism.py` -> Churn: **68.03%** | Cog Load: 40.1092% | Debt: 61.1719%
- `gitgalaxy/galaxyscope.py` -> Churn: **55.29%** | Cog Load: 68.7714% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `gitgalaxy/core/detector.py` -> **Joe Esquibel** (94.0% isolated ownership) | Magnitude: 6980.3
- `gitgalaxy/galaxyscope.py` -> **Joe Esquibel** (100.0% isolated ownership) | Magnitude: 2523.6
- `tests/core_engine/test_detector.py` -> **Joe Esquibel** (85.7% isolated ownership) | Magnitude: 1638.62
- `gitgalaxy/core/prism.py` -> **Joe Esquibel** (96.3% isolated ownership) | Magnitude: 1276.4
- `tests/core_engine/test_galaxyscope.py` -> **Joe Esquibel** (100.0% isolated ownership) | Magnitude: 951.16

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `gitgalaxy/galaxyscope.py` -> **Severity: 0.115** (Bridge: 0.0011 * Flux: 100.0%)
- `gitgalaxy/core/detector.py` -> **Severity: 0.035** (Bridge: 0.0004 * Flux: 100.0%)
- `gitgalaxy/standards/config_resolver.py` -> **Severity: 0.014** (Bridge: 0.0001 * Flux: 99.6316%)
- `gitgalaxy/metrics/signal_processor.py` -> **Severity: 0.013** (Bridge: 0.0001 * Flux: 100.0%)
- `gitgalaxy/cobol_refractor_controller.py` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tests/extraction/languages/_strict_harness.py` -> **Severity: 11.116** (Embedded: 0.1326 * Error Risk: 83.8311%)
- `gitgalaxy/standards/language_standards/languages/json.py` -> **Severity: 10.876** (Embedded: 0.1549 * Error Risk: 70.2063%)
- `gitgalaxy/standards/language_standards/_shared_patterns.py` -> **Severity: 9.658** (Embedded: 0.1148 * Error Risk: 84.1131%)
- `tests/extraction/_extraction_harness.py` -> **Severity: 7.984** (Embedded: 0.1271 * Error Risk: 62.8316%)
- `gitgalaxy/core/detector.py` -> **Severity: 6.798** (Embedded: 0.0683 * Error Risk: 99.4947%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/tools/fidelity_table.py` -> **Severity: 673.35** (Blast Radius: 8.978 * Doc Risk: 75.0%)
- `gitgalaxy/standards/config_resolver.py` -> **Severity: 598.305** (Blast Radius: 12.67 * Doc Risk: 47.2222%)
- `tests/tools/tri_comparison_reconcile.py` -> **Severity: 488.72** (Blast Radius: 6.109 * Doc Risk: 80.0%)
- `tests/tools/tree_sitter_accuracy_audit.py` -> **Severity: 387.629** (Blast Radius: 8.011 * Doc Risk: 48.3871%)
- `gitgalaxy/core/detector.py` -> **Severity: 385.137** (Blast Radius: 16.03 * Doc Risk: 24.026%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
