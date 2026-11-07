# ARCHITECTURAL_BRIEF: gitgalaxy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/squid-protocol/gitgalaxy.git` |
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
- **Scope:** 505 analyzed artifact(s), 103527 LOC.
- **Load-bearing artifact:** `gitgalaxy/standards/language_standards/__init__.py` -- 162 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `gitgalaxy/galaxyscope.py` -- pulls in 59 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `gitgalaxy/core/detector.py` at magnitude 8809.34 (structural weight, not risk).
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
| Total Artifacts | 1748 |
| Analyzed Artifacts (Scanned) | 505 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1243 |
| Total LOC | 103527 |
| Volatility Index | 0.008 |
| % Scanned of codebase = | 28.9% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6288 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1943 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1528 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 58 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 430 | 101053 | 85.1% |
| YAML | 35 | 2390 | 6.9% |
| MARKDOWN | 34 | 0 | 6.7% |
| PLAINTEXT | 4 | 0 | 0.8% |
| SHELL | 2 | 84 | 0.4% |

## 4.1 SOURCE ENCODINGS
All 505 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 36%, Data / Markup / Trivial 16%, Declarative / Non-Code 14%, Large Core Modules (3) 7%, Parameter Forwarders Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 467 | 92.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 38 | 7.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1243*

**Composition by Extension & Reason:**
- `.snap`: 373x Excluded (Unsupported Extension: '.snap'), 218x Unsupported Format (.snap)
- `.md`: 437x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 59x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 53x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cpy`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 17x Excluded (Explicitly Denied Extension: '.gif')
- `no_extension`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cbl`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 593 LOC), 1x Excluded (Saturation: Line 22 exceeds 500 chars)
- `.html`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pli`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 84.4 | 18.4 | 12.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.2 | 50.7 | 50.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.2 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 58.8 | 8.8 | 7.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 6.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 17.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.3 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 88.1 | 3.3 | 0.3 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 15.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 33.7 | 22.2 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1722 | 298 | 10 | `gitgalaxy/recorders/record_keeper.py` |
| cleanup | 127 | 54 | 1 | `tests/tools_recorders/test_record_keeper.py` |
| guards | 10493 | 400 | 60 | `tests/core_engine/test_detector.py` |
| danger | 2759 | 350 | 12 | `gitgalaxy/galaxyscope.py` |
| concurrency | 450 | 123 | 2 | `gitgalaxy/standards/language_standards/languages/python.py` |
| connectivity | 4295 | 386 | 22 | `tests/core_engine/test_detector.py` |
| io | 992 | 305 | 5 | `tests/core_engine/test_galaxyscope.py` |
| crypto | 8 | 7 | 0 | `tests/core_engine/test_licensing.py` |
| ipc | 175 | 44 | 0 | `gitgalaxy/galaxyscope.py` |
| time | 89 | 19 | 0 | `gitgalaxy/galaxyscope.py` |
| serialization | 2 | 2 | 0 | `tests/extraction/languages/test_python_strict.py` |
| regex | 2983 | 146 | 32 | `gitgalaxy/core/detector.py` |
| events | 571 | 115 | 2 | `gitgalaxy/galaxyscope.py` |
| tests | 5225 | 263 | 31 | `tests/core_engine/test_galaxyscope.py` |
| docs | 3484 | 392 | 17 | `tests/core_engine/test_detector.py` |
| debt | 2503 | 264 | 15 | `gitgalaxy/standards/language_standards/_shared_patterns.py` |
| mutation | 38783 | 426 | 152 | `gitgalaxy/core/detector.py` |
| dead_code | 3398 | 240 | 21 | `tests/core_engine/test_detector.py` |
| credential | 180 | 66 | 1 | `gitgalaxy/standards/language_standards/languages/apex.py` |
| threat | 11 | 5 | 0 | `tests/cobol_mainframe/test_cobol_etl_unpacker.py` |
| ml_ai | 11 | 8 | 0 | `tests/extraction/languages/test_python_strict.py` |
| ui | 42 | 21 | 0 | `gitgalaxy/standards/language_standards/languages/python.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.1667**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/core_engine/test_galaxyscope.py` (Hits: 44)
- `gitgalaxy/security/manifest_parser.py` (Hits: 32)
- `tests/extraction/languages/test_swift_strict.py` (Hits: 31)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`gitgalaxy/standards/language_standards/__init__.py`) — 162 inbound connections
2. **_strict_harness.py** (`tests/extraction/languages/_strict_harness.py`) — 69 inbound connections
3. **_shared_patterns.py** (`gitgalaxy/standards/language_standards/_shared_patterns.py`) — 64 inbound connections
4. **detector.py** (`gitgalaxy/core/detector.py`) — 55 inbound connections
5. **_extraction_harness.py** (`tests/extraction/_extraction_harness.py`) — 47 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **galaxyscope.py** (`gitgalaxy/galaxyscope.py`) — 59 outbound dependencies
2. **test_import_contract_2875.py** (`tests/extraction/languages/test_import_contract_2875.py`) — 29 outbound dependencies
3. **test_python_strict.py** (`tests/extraction/languages/test_python_strict.py`) — 27 outbound dependencies
4. **test_galaxyscope.py** (`tests/core_engine/test_galaxyscope.py`) — 24 outbound dependencies
5. **cobol_refractor_controller.py** (`gitgalaxy/cobol_refractor_controller.py`) — 19 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_slice_by_braces` **(Many-Argument Workhorses)** (@ `gitgalaxy/core/detector.py`) -> Impact: **1155.8** | LOC: 1315
- `record_mission` **(Many-Argument Workhorses)** (@ `gitgalaxy/recorders/record_keeper.py`) -> Impact: **887.3** | LOC: 1812
- `_build_markdown` **(Many-Argument Workhorses)** (@ `gitgalaxy/recorders/llm_recorder.py`) -> Impact: **838.6** | LOC: 1110
- `splice` **(Many-Argument Workhorses)** (@ `gitgalaxy/core/detector.py`) -> Impact: **477.1** | LOC: 830
- `inspect` **(Many-Argument Workhorses)** (@ `gitgalaxy/standards/language_lens.py`) -> Impact: **382.4** | LOC: 447
- `generate_report` **(Many-Argument Workhorses)** (@ `gitgalaxy/recorders/audit_recorder.py`) -> Impact: **333.6** | LOC: 562
- `_calculate_block_metrics` **(Many-Argument Workhorses)** (@ `gitgalaxy/core/detector.py`) -> Impact: **331.6** | LOC: 431
- `execute_pipeline` **(Many-Argument Workhorses)** (@ `gitgalaxy/galaxyscope.py`) -> Impact: **266.2** | LOC: 647
  * *Intent:* """ Executes the synthesis protocol with a multi-recorder exit strategy. PIPELINE ONBOARDING (Execution Flow): The method enforces a strict chronologi...
- `calculate_risk_vector` **(Many-Argument Workhorses)** (@ `gitgalaxy/metrics/signal_processor.py`) -> Impact: **258.2** | LOC: 647
- `_slice_by_keywords` **(Many-Argument Workhorses)** (@ `gitgalaxy/core/detector.py`) -> Impact: **248.9** | LOC: 427

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `gitgalaxy/core` | 17 | 15916.02 | 39.24% | 8.65% |
| `tests/extraction/languages` | 115 | 14572.96 | 12.4% | 0.0% |
| `tests/core_engine` | 50 | 8437.86 | 14.1% | 0.0% |
| `gitgalaxy/recorders` | 8 | 6255.34 | 48.27% | 3.8% |
| `gitgalaxy/metrics` | 8 | 3499.84 | 39.89% | 9.95% |
| `gitgalaxy` | 6 | 3349.7 | 32.95% | 0.0% |
| `gitgalaxy/standards` | 9 | 2031.26 | 12.5% | 5.45% |
| `tests/security_auditing` | 15 | 1852.62 | 11.99% | 0.0% |
| `gitgalaxy/security` | 7 | 1658.86 | 37.02% | 1.74% |
| `tests/tools_recorders` | 20 | 1528.1 | 9.13% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `gitgalaxy/standards/language_standards/_shared_patterns.py` -> **100.0%** Exposure
- `gitgalaxy/standards/language_standards/languages/groovy.py` -> **100.0%** Exposure
- `gitgalaxy/standards/language_standards/languages/swift.py` -> **100.0%** Exposure
- `gitgalaxy/standards/language_standards/languages/typescript.py` -> **100.0%** Exposure
- `gitgalaxy/standards/language_standards/languages/zig.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.claude/hooks/pytest_quiet.py` -> **100.0%** Exposure
- `gitgalaxy/cobol_refractor_controller.py` -> **100.0%** Exposure
- `gitgalaxy/cobol_to_java_controller.py` -> **100.0%** Exposure
- `gitgalaxy/core/detector.py` -> **100.0%** Exposure
- `gitgalaxy/core/graph_engine.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/core_engine/test_detector.py` -> **177** Orphaned Functions | **2** Duplicates
- `tests/core_engine/test_signal_processor.py` -> **81** Orphaned Functions | **0** Duplicates
- `tests/core_engine/test_galaxyscope.py` -> **67** Orphaned Functions | **0** Duplicates
- `tests/core_engine/test_prism.py` -> **52** Orphaned Functions | **0** Duplicates
- `tests/security_auditing/test_network_risk_sensor.py` -> **43** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/core_engine/test_galaxyscope.py` -> **100.0%** Exposure
- `tests/security_auditing/test_pii_leak_hunter.py` -> **100.0%** Exposure
- `tests/security_auditing/test_vault_sentinel.py` -> **100.0%** Exposure
- `tests/core_engine/test_aperture.py` -> **99.9999%** Exposure
- `tests/extraction/languages/test_solidity_strict.py` -> **99.3723%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2640` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `gitgalaxy/core/detector.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.624)
- **Top Global Matches:** file_cluster_8: 9.624, file_cluster_6: 19.26, file_cluster_3: 19.963
- **Magnitude:** 8809.34 | **LOC:** 9184 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **55** in-repo importer(s); it depends on **15**; blast radius 19.168; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (85.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 21.2264% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_slice_by_braces` **(Many-Argument Workhorses)** (Impact: 1155.8)
  * `splice` **(Many-Argument Workhorses)** (Impact: 477.1)
  * `_calculate_block_metrics` **(Many-Argument Workhorses)** (Impact: 331.6)
  * `_slice_by_keywords` **(Many-Argument Workhorses)** (Impact: 248.9)
  * `_build_brace_safe_stream` **(Many-Argument Workhorses)** (Impact: 178.4)
    * *Intent:* """ Shields string/char literals and (for C-family languages) dead #if/#else macro branches so a bra...
**Contextual Mitigations & Amplifications:**
* *Sec High Risk Execution:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 1202 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 3787
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1813`, `structural_boundaries: 550`, `args: 94`, `func_start: 90`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 103`, `state_mutation: 1383`, `dead_code: 7`, `planned_debt: 2`, `fragile_debt: 24`, `duplicate_logic: 2`
* *Architecture:* `api: 19`, `concurrency: 2`, `import: 19`
* *Defense:* `safety: 38`, `doc: 88`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.168
  * `Choke Point (Betweenness):` 0.00233 | `Ripple Effect (Closeness):` 0.101499
  * `Imports (Out-Degree: 5):` bisect, collections, functools, gitgalaxy.core.network_risk_sensor, gitgalaxy.core.rule_prefilter, gitgalaxy.core.spatial_correlation, gitgalaxy.standards.analysis_lens, gitgalaxy.standards.language_standards...
  * `Imported By (In-Degree: 55):` (Excluded from Brief to save tokens)

### `gitgalaxy/recorders/llm_recorder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.733)
- **Top Global Matches:** file_cluster_8: 10.733, file_cluster_6: 11.832, file_cluster_4: 19.283
- **Magnitude:** 2842.02 | **LOC:** 1991 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **12**; blast radius 2.556; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.3%), Complexity Load (formerly Cognitive Load) (81.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 33.9286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_build_markdown` **(Many-Argument Workhorses)** (Impact: 838.6)
  * `_mainframe_facts_lines` **(Stateful Encapsulated Methods)** (Impact: 97.8)
    * *Intent:* """The Named System Facts section (#3200/#3201/#3246) -- ABSENT unless a file carries them. These ar...
  * `_executive_summary_lines` **(Stateful Encapsulated Methods)** (Impact: 58.0)
  * `_generate_sqlite_graph` **(Many-Argument Workhorses)** (Impact: 45.4)
  * `generate_artifacts` **(Many-Argument Workhorses)** (Impact: 37.7)
**Contextual Mitigations & Amplifications:**
* *Sec High Risk Execution:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 473 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 1547
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 461`, `structural_boundaries: 118`, `args: 47`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 601`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `api: 3`, `concurrency: 2`, `import: 10`
* *Defense:* `safety: 17`, `doc: 22`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.556
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.012963
  * `Imports (Out-Degree: 1):` collections, gitgalaxy.standards, heapq, hops, json, logging, pathlib, sqlite3...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `gitgalaxy/galaxyscope.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.995)
- **Top Global Matches:** file_cluster_8: 9.995, file_cluster_6: 12.243, file_cluster_4: 19.996
- **Magnitude:** 2659.06 | **LOC:** 3622 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **59**; blast radius 2.998; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.4%), Guard Balance (formerly Safety Score) (82.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 20.7317% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `execute_pipeline` **(Many-Argument Workhorses)** (Impact: 266.2)
    * *Intent:* """ Executes the synthesis protocol with a multi-recorder exit strategy. PIPELINE ONBOARDING (Execut...
  * `_process_file_worker` **(Many-Argument Workhorses)** (Impact: 145.4)
    * *Intent:* """Processes a single file path using the worker's cached hardware modules."""
  * `_resolve_dependency_graph` **(Compute Cores)** (Impact: 125.7)
    * *Intent:* """ Pass 1.5: Optimized relational token aggregation & Fuzzy Suffix Matching. Defused O(N^2) Bomb us...
  * `_calculate_risk_exposures` **(Many-Argument Workhorses)** (Impact: 106.7)
    * *Intent:* """ Phase 3: Universal Exposure Framework & Signal Processing. Translates raw Structural Signatures ...
  * `main` **(I/O & Config Routines)** (Impact: 102.9)
    * *Intent:* # ============================================================================== # ORCHESTRATOR CORE...
**Contextual Mitigations & Amplifications:**
* *Sec High Risk Execution:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 455 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 1551
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 549`, `structural_boundaries: 250`, `args: 38`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 95`, `high_risk_execution: 2`, `state_mutation: 641`
* *Architecture:* `io: 13`, `api: 7`, `concurrency: 3`, `import: 67`
* *Defense:* `safety: 50`, `doc: 21`, `test: 2`, `immutability_locks: 8`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.998
  * `Choke Point (Betweenness):` 0.0015 | `Ripple Effect (Closeness):` 0.012401
  * `Imports (Out-Degree: 34):` argparse, collections, concurrent.futures, copy, datetime, functools, gitgalaxy.core.aperture, gitgalaxy.core.detector...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `tests/core_engine/test_detector.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.306)
- **Top Global Matches:** file_cluster_12: 7.306, file_cluster_15: 7.41, file_cluster_11: 8.027
- **Magnitude:** 2249.66 | **LOC:** 5456 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 1.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (64.8%), Guard Balance (formerly Safety Score) (51.3%), Complexity Load (formerly Cognitive Load) (15.1%), Connectivity (formerly Api Exposure) (12.2%)
- **Documentation Coverage:** 2.6882% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_spatial_mapper_sectorization_and_monolith` **(Defensive Guards)** (Impact: 15.5)
    * *Intent:* """ Proves the engine correctly groups files into sector constellations by their parent directories,...
  * `test_detector_c_macro_dead_branch_shield` **(Defensive Guards)** (Impact: 14.7)
    * *Intent:* """ Pins that a statically-dead C preprocessor branch is not counted (#2814). `detector._blank_dead_...
  * `test_detector_c_macro_no_space_boundaries_issue_1764` **(Defensive Guards)** (Impact: 14.2)
    * *Intent:* """ Regression test for a bug where `#if(1)` or `#elif(0)` (valid C preprocessor syntax without a sp...
  * `test_detector_c_macro_static_truth_prunes_branches` **(Defensive Guards)** (Impact: 13.9)
    * *Intent:* """ Companion to the #1720 fix: statically-decidable #if conditions still prune the dead branch. #if...
  * `test_detector_orphan_census_excludes_synthetic_slicer_names` **(I/O & Config Routines)** (Impact: 13.1)
    * *Intent:* """ Regression test for #2547: languages sliced by Mode D (_slice_by_keywords) or Mode E (_slice_by_...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 266 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1248
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 312`, `structural_boundaries: 1260`, `args: 244`, `func_start: 186`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 5`, `state_mutation: 716`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 10`, `duplicate_logic: 2`, `unreferenced_by_name: 177`
* *Architecture:* `io: 8`, `api: 191`, `import: 126`
* *Defense:* `safety: 494`, `doc: 187`, `test: 202`, `sync_locks: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` b, gitgalaxy.core.detector, gitgalaxy.core.prism, gitgalaxy.core.spatial_correlation, gitgalaxy.core.spatial_mapper, gitgalaxy.standards.gitgalaxy_config, gitgalaxy.standards.language_standards, logging...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/metrics/signal_processor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.421)
- **Top Global Matches:** file_cluster_4: 9.421, file_cluster_6: 10.58, file_cluster_5: 13.904
- **Magnitude:** 2138.16 | **LOC:** 2321 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **11**; blast radius 5.266; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.6%)
- **Documentation Coverage:** 29.661% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `calculate_risk_vector` **(Many-Argument Workhorses)** (Impact: 258.2)
  * `summarize_galaxy_metrics` **(Many-Argument Workhorses)** (Impact: 191.6)
    * *Intent:* # ========================================================================== # GLOBAL SYNTHESIS & 2-...
  * `generate_forensic_report` **(Many-Argument Workhorses)** (Impact: 60.7)
    * *Intent:* # -------------------------------------------------------------------------- # REPORTING UTILITIES #...
  * `_calc_verification` **(Many-Argument Workhorses)** (Impact: 57.2)
  * `_compute_snapshot_percentiles` **(Stateful Encapsulated Methods)** (Impact: 41.1)
    * *Intent:* """[TIER 2, gitgalaxy#2994] Snapshot percentiles -- the honest 0-100. Ranks each file's 22 Tier-1 su...
**Contextual Mitigations & Amplifications:**
* *Sec High Risk Execution:* 1 instances
* *List:* 1 instances
* *Amplified Cascading Flux:* 324 instances
* *State Mutation (weighted view):* 1114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 368`, `structural_boundaries: 146`, `args: 48`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 466`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 10`, `concurrency: 2`, `import: 12`
* *Defense:* `safety: 30`, `doc: 28`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.266
  * `Choke Point (Betweenness):` 0.000143 | `Ripple Effect (Closeness):` 0.02405
  * `Imports (Out-Degree: 3):` collections.abc, gitgalaxy.core.spatial_correlation, gitgalaxy.metrics, gitgalaxy.standards, gitgalaxy.standards.fidelity_table, logging, math, os...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `gitgalaxy/core/prism.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.15)
- **Top Global Matches:** file_cluster_8: 11.15, file_cluster_6: 12.124, file_cluster_4: 19.379
- **Magnitude:** 1929.2 | **LOC:** 1960 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **25** in-repo importer(s); it depends on **4**; blast radius 8.148; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (45.7%)
- **Documentation Coverage:** 21.1538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_strip_single_line_comments` **(Many-Argument Workhorses)** (Impact: 124.1)
    * *Intent:* """ Single-line comment stripper for the "line_exclusive" family, driven by each language's own real...
  * `_strip_single_line_comments_positional` **(Many-Argument Workhorses)** (Impact: 122.2)
    * *Intent:* """Positional sibling of `_strip_single_line_comments`: same per-line masking and carry-quote discip...
  * `_mask_perl_line_positional` **(Many-Argument Workhorses)** (Impact: 75.4)
  * `_mask_perl_line` **(Many-Argument Workhorses)** (Impact: 75.4)
  * `_strip_positional_comments` **(Many-Argument Workhorses)** (Impact: 59.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 279 instances
* *State Mutation (weighted view):* 887
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 331`, `structural_boundaries: 172`, `args: 47`, `func_start: 44`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 329`, `fragile_debt: 6`, `duplicate_logic: 2`
* *Architecture:* `api: 11`, `import: 4`
* *Defense:* `safety: 4`, `doc: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.148
  * `Choke Point (Betweenness):` 7.1e-05 | `Ripple Effect (Closeness):` 0.050265
  * `Imports (Out-Degree: 1):` gitgalaxy.standards.language_standards, logging, re, typing
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `gitgalaxy/recorders/record_keeper.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.919)
- **Top Global Matches:** file_cluster_8: 7.919, file_cluster_6: 15.033, file_cluster_4: 23.53
- **Magnitude:** 1791.82 | **LOC:** 2249 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **8**; blast radius 8.323; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (88.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.1%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `record_mission` **(Many-Argument Workhorses)** (Impact: 887.3)
  * `_classify_file_archetype` **(Many-Argument Workhorses)** (Impact: 52.6)
    * *Intent:* """Nearest-centroid file archetype from the assembled metrics, mirroring the offline apply_file_clus...
  * `_prep_file_brain` **(Stateful Encapsulated Methods)** (Impact: 36.2)
    * *Intent:* """#ENGINE-PARITY: cache the self-describing FILE archetype brain contract. The engine builds the fi...
  * `_insert_per_file_child` **(Many-Argument Workhorses)** (Impact: 20.8)
  * `_file_feature_kind` **(Stateful Encapsulated Methods)** (Impact: 13.4)
    * *Intent:* """Which value source feeds this FEATURE_NAME, or None if the engine has none."""
**Contextual Mitigations & Amplifications:**
* *Sec Db Hooks:* 1 instances
* *Ai Guardrails:* 1 instances
* *Amplified Cascading Flux:* 219 instances
* *State Mutation (weighted view):* 717
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 300`, `structural_boundaries: 57`, `args: 13`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 279`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 4`, `import: 8`
* *Defense:* `safety: 26`, `doc: 34`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.323
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.032714
  * `Imports (Out-Degree: 1):` gitgalaxy.standards.analysis_lens, json, logging, math, pathlib, sqlite3, statistics, typing
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `gitgalaxy/standards/language_lens.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.815)
- **Top Global Matches:** file_cluster_8: 9.815, file_cluster_6: 14.424, file_cluster_4: 22.449
- **Magnitude:** 1595.24 | **LOC:** 1496 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **9**; blast radius 3.087; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.4%)
- **Documentation Coverage:** 31.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inspect` **(Many-Argument Workhorses)** (Impact: 382.4)
  * `_tier_4_heuristic_discovery` **(Many-Argument Workhorses)** (Impact: 146.2)
    * *Intent:* # ========================================================================= # THE TIER 4 HEURISTIC D...
  * `_evaluate_ecosystem_gravity` **(Many-Argument Workhorses)** (Impact: 90.0)
  * `_tier_3_lexical_scan` **(Many-Argument Workhorses)** (Impact: 61.1)
  * `_resolve_by_sibling_content` **(Many-Argument Workhorses)** (Impact: 37.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 206 instances
* *State Mutation (weighted view):* 639
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 333`, `structural_boundaries: 128`, `args: 27`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 1`, `state_mutation: 227`
* *Architecture:* `io: 3`, `api: 6`, `import: 9`
* *Defense:* `safety: 10`, `doc: 18`, `sync_locks: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.087
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.021875
  * `Imports (Out-Degree: 2):` contextlib, gitgalaxy.standards.gitgalaxy_config, gitgalaxy.standards.language_standards, logging, math, pathlib, re, time...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `gitgalaxy/core/mainframe_boundary.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 12.058)
- **Top Global Matches:** file_cluster_8: 12.058, file_cluster_6: 14.751, file_cluster_4: 22.033
- **Magnitude:** 1494.34 | **LOC:** 1300 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **3**; blast radius 4.348; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.1%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (64.8%)
- **Documentation Coverage:** 6.4516% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_cobol_calls` **(Stateful Encapsulated Methods)** (Impact: 108.3)
    * *Intent:* """Every COBOL invocation site: `CALL`, and CICS `LINK`/`XCTL PROGRAM(...)`."""
  * `_pli_item_attributes` **(Compute Cores)** (Impact: 72.8)
    * *Intent:* """The record_data fields of one item from its attribute tokens, or None when the declaration is not...
  * `_cobol_records` **(Stateful Encapsulated Methods)** (Impact: 68.2)
    * *Intent:* """The DATA DIVISION item tree and FD record layouts of one COBOL file (#3246). Each entry is a flat...
  * `_pli_items` **(Compute Cores)** (Impact: 39.2)
    * *Intent:* """Split one DECLARE body into (offset, level, name, dims, attribute tokens) items. A factored decla...
  * `_pli_records` **(Stateful Encapsulated Methods)** (Impact: 36.0)
    * *Intent:* """The DECLAREd data items of one PL/I file as a record tree (#3250). Same flat, source-ordered shap...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 262 instances
* *State Mutation (weighted view):* 839
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 359`, `structural_boundaries: 106`, `args: 33`, `func_start: 30`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 315`, `duplicate_logic: 3`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 2`, `doc: 26`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.348
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.046779
  * `Imports (Out-Degree: 0):` bisect, re, typing
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `tests/core_engine/test_galaxyscope.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.552)
- **Top Global Matches:** file_cluster_12: 6.552, file_cluster_7: 8.736, file_cluster_5: 9.571
- **Magnitude:** 1126.72 | **LOC:** 2953 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 1.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (100.0%), Guard Balance (formerly Safety Score) (61.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.9%), Complexity Load (formerly Cognitive Load) (22.5%)
- **Documentation Coverage:** 9.8684% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_recorder_exception_survivability` **(Many-Argument Workhorses)** (Impact: 16.3)
    * *Intent:* # ============================================================================== # TEST 23: RECORDER...
  * `test_phase_10_manifest_paths_includes_all_supported_ecosystems` **(Many-Argument Workhorses)** (Impact: 13.4)
    * *Intent:* # ============================================================================== # TEST 33: MANIFEST...
  * `test_cicd_policy_enforcement_gates` **(Many-Argument Workhorses)** (Impact: 12.4)
    * *Intent:* # ============================================================================== # TEST 2: THE CI/CD...
  * `test_delta_scanning_fallbacks` **(Many-Argument Workhorses)** (Impact: 12.0)
    * *Intent:* # ============================================================================== # TEST 24: DELTA SC...
  * `test_sarif_ignored_paths_sanitization` **(Compute Cores)** (Impact: 11.6)
    * *Intent:* # ============================================================================== # TEST 19: SARIF IG...
**Contextual Mitigations & Amplifications:**
* *Sec Hardcoded Secrets:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 72 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 603
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 311`, `args: 78`, `func_start: 74`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 58`, `high_risk_execution: 1`, `state_mutation: 459`, `fragile_debt: 1`, `unreferenced_by_name: 67`
* *Architecture:* `io: 44`, `api: 73`, `concurrency: 2`, `import: 82`
* *Defense:* `safety: 36`, `doc: 73`, `test: 270`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` B, Q, base64, concurrent.futures, failure, gitgalaxy.core.aperture, gitgalaxy.core.detector, gitgalaxy.core.spatial_correlation...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/security/manifest_parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.848)
- **Top Global Matches:** file_cluster_8: 7.848, file_cluster_6: 12.704, file_cluster_4: 21.13
- **Magnitude:** 1060.58 | **LOC:** 748 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 2.83; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.6%)
- **Documentation Coverage:** 20.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `slice_manifest` **(Compute Cores)** (Impact: 181.9)
  * `locate_physical_package` **(Many-Argument Workhorses)** (Impact: 129.9)
  * `_parse_pyproject_toml` **(Many-Argument Workhorses)** (Impact: 36.2)
    * *Intent:* """ Audits modern Python manifests (PEP 621 `[project] dependencies` arrays and Poetry's `[tool.poet...
  * `_parse_requirements_txt` **(Stateful Encapsulated Methods)** (Impact: 25.2)
    * *Intent:* """ Extracts direct Python packages and flags absolute VCS/URI references. """
  * `_parse_pip_conf` **(Stateful Encapsulated Methods)** (Impact: 23.2)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.83
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.013951
  * `Imports (Out-Degree: 0):` json, logging, os, pathlib, re, typing
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `gitgalaxy/core/graph_engine.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 10.108)
- **Top Global Matches:** file_cluster_5: 10.108, file_cluster_4: 10.439, file_cluster_12: 11.121
- **Magnitude:** 943.38 | **LOC:** 783 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 4.232; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (38.8%)
- **Documentation Coverage:** 14.4737% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_louvain_level` **(Many-Argument Workhorses)** (Impact: 53.1)
  * `betweenness_centrality` **(Many-Argument Workhorses)** (Impact: 29.7)
    * *Intent:* """ #3038: exact betweenness centrality, one value per node id: the share of shortest import paths b...
  * `pagerank` **(Many-Argument Workhorses)** (Impact: 27.0)
    * *Intent:* """ Weighted PageRank, one value per node id: the only PageRank the engine runs, in both modes (#302...
  * `closeness_and_path_length` **(Many-Argument Workhorses)** (Impact: 24.4)
  * `_louvain` **(Stateful Encapsulated Methods)** (Impact: 23.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 183 instances
* *State Mutation (weighted view):* 567
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 71`, `args: 25`, `func_start: 25`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 201`
* *Architecture:* `api: 16`, `import: 6`
* *Defense:* `doc: 25`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.232
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.05679
  * `Imports (Out-Degree: 0):` collections, collections.abc, math, operator, random, typing
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `tests/core_engine/test_signal_processor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.771)
- **Top Global Matches:** file_cluster_12: 6.771, file_cluster_15: 6.969, file_cluster_11: 7.753
- **Magnitude:** 782.8 | **LOC:** 2140 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (47.2%), Complexity Load (formerly Cognitive Load) (18.5%), Connectivity (formerly Api Exposure) (11.3%)
- **Documentation Coverage:** 1.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_synthetic_star` **(Many-Argument Workhorses)** (Impact: 13.3)
    * *Intent:* # ============================================================================== # SYNTHETIC GALAXY ...
  * `test_signal_processor_documentation_acceptance_pins` **(Defensive Guards)** (Impact: 10.1)
    * *Intent:* """The #2908 acceptance table, pinned exactly: the rosetta a/b/c shape (3 public units, 0 documented...
  * `test_signal_processor_small_file_scores_on_counts` **(Defensive Guards)** (Impact: 7.0)
    * *Intent:* """ #2655: the old flat 5.0 small-file floor (`loc < 15`) is gone. A file below the evidence-mass fl...
  * `test_signal_processor_unknown_language_gets_no_language_term` **(Defensive Guards)** (Impact: 6.4)
    * *Intent:* # ============================================================================== # TEST 47: TIER 3 L...
  * `test_signal_processor_minified_tripwire` **(Defensive Guards)** (Impact: 6.3)
    * *Intent:* # ============================================================================== # TEST 11: THE MINI...
**Contextual Mitigations & Amplifications:**
* *Suppressions:* 1 instances
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 401
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 306`, `args: 87`, `func_start: 87`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 333`, `planned_debt: 4`, `fragile_debt: 3`, `unreferenced_by_name: 81`
* *Architecture:* `io: 3`, `api: 85`, `import: 10`
* *Defense:* `safety: 194`, `doc: 84`, `test: 87`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` gitgalaxy.metrics.signal_processor, gitgalaxy.recorders, gitgalaxy.recorders.record_keeper, gitgalaxy.recorders.sarif_recorder, json, logging, os, pytest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/recorders/audit_recorder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.97)
- **Top Global Matches:** file_cluster_6: 7.97, file_cluster_4: 12.073, file_cluster_8: 15.939
- **Magnitude:** 758.66 | **LOC:** 736 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 1.974; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.2%), Guard Balance (formerly Safety Score) (80.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 23.0769% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_report` **(Many-Argument Workhorses)** (Impact: 333.6)
  * `_mainframe_facts_block` **(Many-Argument Workhorses)** (Impact: 25.6)
    * *Intent:* """The Named System Facts for one file (#3200/#3201/#3246/#3250), or {} if none. The forensic report...
  * `descale` **(Defensive Guards)** (Impact: 14.1)
    * *Intent:* """Dynamically scales integers back to floats using a fixed-string check."""
  * `format_label` **(Generic / Templated Code)** (Impact: 7.6)
    * *Intent:* """Translates raw dictionary keys into descriptive human-readable labels."""
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Sec High Risk Execution:* 1 instances
* *Amplified Cascading Flux:* 110 instances
* *State Mutation (weighted view):* 353
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 31`, `args: 12`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 133`
* *Architecture:* `io: 3`, `api: 6`, `import: 8`
* *Defense:* `safety: 12`, `doc: 6`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.010204
  * `Imports (Out-Degree: 1):` argparse, gitgalaxy.standards, json, logging, os, pathlib, re, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `gitgalaxy/core/network_risk_sensor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 13.047)
- **Top Global Matches:** file_cluster_5: 13.047, file_cluster_4: 13.282, file_cluster_6: 14.369
- **Magnitude:** 609.72 | **LOC:** 734 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **13**; blast radius 6.964; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (39.7%)
- **Documentation Coverage:** 11.3636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_resolve_target` **(Many-Argument Workhorses)** (Impact: 91.1)
  * `_network_metrics` **(Many-Argument Workhorses)** (Impact: 36.8)
  * `_narrow_ambiguous` **(Many-Argument Workhorses)** (Impact: 34.4)
  * `extract_test_coverage_mapping` **(Many-Argument Workhorses)** (Impact: 32.9)
    * *Intent:* """ Maps function calls from test files to their imported production targets. Returns a dictionary m...
  * `_resolve_edges` **(Stateful Encapsulated Methods)** (Impact: 21.6)
    * *Intent:* """ #2992: resolves every file's raw_imports into directed file-to-file edges, keyed (importer, impo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 92 instances
* *State Mutation (weighted view):* 291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 84`, `args: 20`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 107`
* *Architecture:* `io: 1`, `api: 4`, `import: 11`
* *Defense:* `safety: 9`, `doc: 19`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.964
  * `Choke Point (Betweenness):` 0.001404 | `Ripple Effect (Closeness):` 0.074716
  * `Imports (Out-Degree: 5):` collections, gitgalaxy.core.graph_engine, gitgalaxy.core.invocation_resolver, gitgalaxy.core.path_proximity, gitgalaxy.standards.analysis_lens, gitgalaxy.standards.language_standards, graph, logging...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `gitgalaxy/metrics/statistical_auditor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 12.247)
- **Top Global Matches:** file_cluster_6: 12.247, file_cluster_4: 13.442, file_cluster_5: 16.139
- **Magnitude:** 523.12 | **LOC:** 589 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 1.974; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.6%)
- **Documentation Coverage:** 11.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `audit` **(Many-Argument Workhorses)** (Impact: 151.5)
    * *Intent:* """Executes statistical gating to identify data-dumps and structural outliers."""
  * `__init__` **(Many-Argument Workhorses)** (Impact: 10.7)
  * `_is_dead_code` **(Stateful Encapsulated Methods)** (Impact: 8.0)
    * *Intent:* """Determines if an artifact is predominantly dead code or comments."""
  * `_is_threat` **(Stateful Encapsulated Methods)** (Impact: 7.9)
    * *Intent:* """ Determines if an artifact contains active security threat signatures. Used by the Quarantine Gua...
  * `_is_highly_blended` **(Stateful Encapsulated Methods)** (Impact: 7.6)
    * *Intent:* """Determines if a file is a Polyglot where the primary language is < 80% of the mass."""
**Contextual Mitigations & Amplifications:**
* *Sec High Risk Execution:* 1 instances
* *Amplified Cascading Flux:* 100 instances
* *State Mutation (weighted view):* 320
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 40`, `args: 9`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 120`
* *Architecture:* `io: 2`, `api: 3`, `import: 5`
* *Defense:* `safety: 8`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.010204
  * `Imports (Out-Degree: 1):` gitgalaxy.core.spatial_correlation, logging, os, statistics, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/security_auditing/test_network_risk_sensor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.051)
- **Top Global Matches:** file_cluster_11: 7.051, file_cluster_15: 7.302, file_cluster_16: 7.717
- **Magnitude:** 481.3 | **LOC:** 1016 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 1.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (44.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.9%), Complexity Load (formerly Cognitive Load) (13.8%), Connectivity (formerly Api Exposure) (10.4%)
- **Documentation Coverage:** 3.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_network_ecosystem_roles` **(Defensive Guards)** (Impact: 12.7)
    * *Intent:* # ============================================================================== # TEST 3: ECOSYSTEM...
  * `test_every_graph_metric_is_computed` **(Defensive Guards)** (Impact: 11.2)
    * *Intent:* # ============================================================================== # TEST 5: ZERO-DEPE...
  * `test_network_duplicate_filename_ambiguous_import_skipped` **(Defensive Guards)** (Impact: 9.6)
    * *Intent:* # ============================================================================== # TEST 6: DUPLICATE...
  * `test_network_duplicate_filename_path_qualified_import_resolves` **(Defensive Guards)** (Impact: 9.5)
    * *Intent:* # ============================================================================== # TEST 7: DUPLICATE...
  * `test_network_exact_case_match_wins_over_folded` **(Defensive Guards)** (Impact: 9.5)
    * *Intent:* # ============================================================================== # TEST 17: EXACT-CA...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 184
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 171`, `args: 50`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 84`, `unreferenced_by_name: 43`
* *Architecture:* `io: 2`, `api: 48`, `import: 5`
* *Defense:* `safety: 92`, `doc: 46`, `test: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` A, Foo, chain, copy, failed, gitgalaxy.core.network_risk_sensor, misattributed, must...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/cobol_refractor_controller.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.969)
- **Top Global Matches:** file_cluster_6: 7.969, file_cluster_4: 11.702, file_cluster_8: 16.139
- **Magnitude:** 448.2 | **LOC:** 578 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **19**; blast radius 2.336; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (64.8%)
- **Documentation Coverage:** 42.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_payload` **(Many-Argument Workhorses)** (Impact: 57.8)
  * `main` **(I/O & Config Routines)** (Impact: 49.3)
    * *Intent:* # ============================================================================== # galaxyscope:ignor...
  * `calibrate_ir_medium` **(Many-Argument Workhorses)** (Impact: 17.2)
    * *Intent:* # ============================================================================== # galaxyscope:ignor...
  * `record_dead_code` **(Many-Argument Workhorses)** (Impact: 14.4)
  * `_output_keys` **(Stateful Encapsulated Methods)** (Impact: 9.4)
    * *Intent:* """Each program's name in the clean room's flat output directories and in the IR state: its stem whe...
**Contextual Mitigations & Amplifications:**
* *Sec Db Hooks:* 1 instances
* *Amplified Cascading Flux:* 75 instances
* *Api Near Db Sink:* 2 instances
* *State Mutation (weighted view):* 244
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 66`, `args: 14`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 3`, `state_mutation: 94`
* *Architecture:* `io: 5`, `api: 9`, `import: 19`
* *Defense:* `safety: 3`, `doc: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.336
  * `Choke Point (Betweenness):` 7.5e-05 | `Ripple Effect (Closeness):` 0.003968
  * `Imports (Out-Degree: 10):` argparse, collections, datetime, gitgalaxy.licensing, gitgalaxy.tools.cobol_to_cobol.cobol_agent_task_forge, gitgalaxy.tools.cobol_to_cobol.cobol_dag_architect, gitgalaxy.tools.cobol_to_cobol.cobol_graveyard_finder, gitgalaxy.tools.cobol_to_cobol.cobol_jcl_auditor...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `gitgalaxy/core/rule_prefilter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 13.126)
- **Top Global Matches:** file_cluster_6: 13.126, file_cluster_8: 14.097, file_cluster_4: 19.247
- **Magnitude:** 439.26 | **LOC:** 634 | **CtrlFlow:** 40.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **4**; blast radius 5.623; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.2%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (61.1%)
- **Documentation Coverage:** 7.8947% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_walk_line_local` **(Many-Argument Workhorses)** (Impact: 62.8)
    * *Intent:* """Whitelist walk proving no node of `seq` can consume or anchor past a line boundary. Raises _NotLi...
  * `_walk_seq` **(Stateful Encapsulated Methods)** (Impact: 47.3)
    * *Intent:* """Collect every candidate requirement in a concatenation sequence. A match of the sequence matches ...
  * `derive_literal_gate` **(Many-Argument Workhorses)** (Impact: 41.6)
  * `derive_line_literals` **(Defensive Guards)** (Impact: 17.5)
    * *Intent:* """The per-line analogue of derive_literal_gate: a one-of literal set such that a line containing no...
  * `_in_set_can_match_nl` **(Stateful Encapsulated Methods)** (Impact: 16.7)
    * *Intent:* """Can this IN character set match '\\n'? Unknown items raise."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 187
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 62`, `args: 17`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 63`, `planned_debt: 2`, `fragile_debt: 5`
* *Architecture:* `api: 6`, `import: 4`
* *Defense:* `safety: 13`, `doc: 15`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.067333
  * `Imports (Out-Degree: 0):` re, sre_constants, sre_parse, typing
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `gitgalaxy/security/security_auditor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.184)
- **Top Global Matches:** file_cluster_8: 9.184, file_cluster_6: 18.413, file_cluster_3: 20.797
- **Magnitude:** 385.22 | **LOC:** 469 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **8**; blast radius 2.875; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.3%), Complexity Load (formerly Cognitive Load) (55.9%)
- **Documentation Coverage:** 12.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_construct_feature_matrix` **(Many-Argument Workhorses)** (Impact: 38.6)
    * *Intent:* """Reconstructs the Pandas DataFrame exactly as train_threat_model.py did."""
  * `audit_repository` **(Many-Argument Workhorses)** (Impact: 36.4)
    * *Intent:* """ Orchestrates the resolution of transitive dependency graphs and executes the XGBoost model again...
  * `_resolve_dependency_graph` **(Many-Argument Workhorses)** (Impact: 32.8)
    * *Intent:* """ Resolves each file's transitive fragility and Downstream Exposure. `total_upstream` counts every...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 28.6)
    * *Intent:* # Updated default to the new multiclass model
  * `_or_nan` **(Encapsulated Accessors)** (Impact: 4.4)
    * *Intent:* """None ("not computed") as NaN for the feature matrix; anything else unchanged."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 73 instances
* *State Mutation (weighted view):* 234
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 37`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 88`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 3`, `import: 9`
* *Defense:* `safety: 8`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.00017 | `Ripple Effect (Closeness):` 0.014579
  * `Imports (Out-Degree: 4):` gitgalaxy.core.graph_engine, gitgalaxy.core.network_risk_sensor, gitgalaxy.core.spatial_correlation, gitgalaxy.standards.analysis_lens, importlib, logging, pathlib, typing
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `gitgalaxy/core/guidestar_lens.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.141)
- **Top Global Matches:** file_cluster_12: 9.141, file_cluster_5: 9.22, file_cluster_7: 10.2
- **Magnitude:** 380.14 | **LOC:** 523 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 2.411; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.6%), Complexity Load (formerly Cognitive Load) (36.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.9%)
- **Documentation Coverage:** 5.2632% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_intent_status` **(Compute Cores)** (Impact: 22.5)
    * *Intent:* """Returns the specific Intent Lock for a given file path based on strict, pattern, or sector match....
  * `_calculate_documentation_coverage` **(Stateful Encapsulated Methods)** (Impact: 21.4)
    * *Intent:* # ============================================================================== # galaxyscope:ignor...
  * `__init__` **(Many-Argument Workhorses)** (Impact: 16.8)
  * `_scan_gitattributes` **(Stateful Encapsulated Methods)** (Impact: 15.2)
    * *Intent:* # ============================================================================== # galaxyscope:ignor...
  * `_deep_inspect_manifest` **(Stateful Encapsulated Methods)** (Impact: 14.2)
    * *Intent:* """Dispatches files to specific parsers based on their format."""
**Contextual Mitigations & Amplifications:**
* *Sec Io:* 1 instances
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 184
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 59`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 66`
* *Architecture:* `io: 8`, `api: 5`, `import: 8`
* *Defense:* `safety: 10`, `doc: 16`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.411
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.011563
  * `Imports (Out-Degree: 1):` fnmatch, gitgalaxy.standards.gitgalaxy_config, json, logging, os, pathlib, re, typing
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/core_engine/test_prism.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.305)
- **Top Global Matches:** file_cluster_11: 7.305, file_cluster_15: 7.858, file_cluster_12: 7.94
- **Magnitude:** 375.7 | **LOC:** 1325 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (32.5%), Complexity Load (formerly Cognitive Load) (13.7%), Connectivity (formerly Api Exposure) (11.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (10.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_prism_jcl_comment_stripping_details` **(Defensive Guards)** (Impact: 7.8)
    * *Intent:* """ #2610: JCL `//*` whole-line comments move to the comment stream while everything `//`-statement-...
  * `test_prism_sub_families_fix_the_standard_block_delimiter_gap` **(I/O & Config Routines)** (Impact: 5.1)
    * *Intent:* """ Regression test for #621: sqlite, lua, haskell, powershell, and perl were all classified "standa...
  * `test_prism_standard_block_c_family_unaffected_by_sub_family_split` **(Defensive Guards)** (Impact: 4.8)
    * *Intent:* """ Regression guard for #621: splitting sqlite/lua/haskell/powershell/perl out of "standard_block" ...
  * `test_prism_livecode_string_has_no_backslash_escape` **(Defensive Guards)** (Impact: 4.3)
    * *Intent:* """ #2419: LiveCode string literals have NO `\\` escapes -- `\\` is an ordinary character. The share...
  * `test_prism_issue_1532_nested_comment_stripping_preserves_line_count` **(I/O & Config Routines)** (Impact: 4.2)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` gitgalaxy.core.prism, gitgalaxy.standards.gitgalaxy_config, gitgalaxy.standards.language_standards, pytest, re, time, unittest.mock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/extraction/languages/test_perl_strict.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.066)
- **Top Global Matches:** file_cluster_0: 8.066, file_cluster_11: 8.364, file_cluster_15: 8.466
- **Magnitude:** 366.2 | **LOC:** 664 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 1.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (39.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.9%), Complexity Load (formerly Cognitive Load) (17.4%), Connectivity (formerly Api Exposure) (10.1%)
- **Documentation Coverage:** 37.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_perl_args_prototype_falls_through_to_body_idiom_scan` **(Defensive Guards)** (Impact: 11.6)
    * *Intent:* """ #1607: a legacy Perl PROTOTYPE (`sub Get8u($$)`) is a sequence of bare sigils with NO commas, ev...
  * `test_perl_signature_positive_and_negative` **(Defensive Guards)** (Impact: 10.4)
  * `test_perl_branch_colon_ambiguity_and_defined_or` **(Defensive Guards)** (Impact: 8.3)
  * `test_perl_globals_magic_variable_boundary_regression` **(Defensive Guards)** (Impact: 7.8)
    * *Intent:* """ Regression test: `$$`, `$@`, `$!`, and `$?` were inside the shared trailing \\b group. Each ends...
  * `test_perl_brace_safe_stream_escaped_brace_in_regex_does_not_desync` **(I/O & Config Routines)** (Impact: 7.6)
    * *Intent:* """ #1517: an escaped `\\{`/`\\}` inside a bare `/regex/` literal (never shielded at all -- perl reg...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 19 instances
* *Amplified Cascading Flux:* 48 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 192
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 212`, `args: 32`, `func_start: 32`
* *Risk/State:* `high_risk_execution: 21`, `state_mutation: 96`, `planned_debt: 2`, `fragile_debt: 4`, `unreferenced_by_name: 32`
* *Architecture:* `io: 3`, `api: 32`, `import: 13`
* *Defense:* `safety: 126`, `doc: 22`, `test: 34`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` _strict_harness, gitgalaxy.core.detector, gitgalaxy.standards.language_standards, pathlib, pytest, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/extraction/languages/test_livecode_strict.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.537)
- **Top Global Matches:** file_cluster_15: 7.537, file_cluster_10: 7.843, file_cluster_11: 7.884
- **Magnitude:** 365.4 | **LOC:** 753 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.027; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (41.6%), Concurrency Surface (formerly Concurrency) (38.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.9%), Complexity Load (formerly Cognitive Load) (18.9%)
- **Documentation Coverage:** 24.2424% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assert_linear_redos_scaling` **(Many-Argument Workhorses)** (Impact: 20.4)
    * *Intent:* """ Measures pattern.search() time at each size in `sizes` (each isolated in its own subprocess via ...
  * `test_livecode_signature_positive_and_negative` **(Defensive Guards)** (Impact: 10.4)
  * `test_livecode_dependency_capture_extracts_path` **(Defensive Guards)** (Impact: 10.1)
    * *Intent:* """ _dependency_capture is paired with `import` and must extract the exact dependency path/module st...
  * `test_livecode_class_start_dotted_module_name_regression` **(Defensive Guards)** (Impact: 6.8)
    * *Intent:* """ Regression test (Rule 11-class nested/multi-segment coverage): the name capture `["\\'a-zA-Z_]\\...
  * `_measure_scaling_point` **(Stateful Encapsulated Methods)** (Impact: 6.7)
    * *Intent:* # ============================================================================== # REDOS SCALING VER...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 46 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 167`, `args: 44`, `func_start: 34`
* *Risk/State:* `state_mutation: 79`, `planned_debt: 1`, `fragile_debt: 12`, `unreferenced_by_name: 31`
* *Architecture:* `io: 7`, `api: 32`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 97`, `doc: 26`, `test: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.027
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` _strict_harness, gitgalaxy.standards.language_standards, multiprocessing, pathlib, pytest, re, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gitgalaxy/recorders/gpu_recorder.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 13.493)
- **Top Global Matches:** file_cluster_8: 13.493, file_cluster_6: 14.284, file_cluster_4: 20.787
- **Magnitude:** 361.86 | **LOC:** 449 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 1.974; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (55.6%)
- **Documentation Coverage:** 31.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `record_mission` **(Many-Argument Workhorses)** (Impact: 119.0)
  * `__init__` **(Generic / Templated Code)** (Impact: 7.6)
  * `_intern` **(Encapsulated Accessors)** (Impact: 4.2)
    * *Intent:* """Minifies payload footprints by mapping repetitive strings to integer IDs."""
  * `save_minified` **(Generic / Templated Code)** (Impact: 2.5)
    * *Intent:* """Serializes with maximum JSON compression to the provided output path."""
**Contextual Mitigations & Amplifications:**
* *Sec High Risk Execution:* 1 instances
* *Amplified Cascading Flux:* 59 instances
* *State Mutation (weighted view):* 219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 23`, `args: 5`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 101`, `fragile_debt: 1`
* *Architecture:* `io: 2`, `api: 4`, `import: 7`
* *Defense:* `safety: 3`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.974
  * `Choke Point (Betweenness):` 1.4e-05 | `Ripple Effect (Closeness):` 0.010204
  * `Imports (Out-Degree: 2):` gc, gitgalaxy.standards, gitgalaxy.standards.config_resolver, json, logging, pathlib, typing
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `gitgalaxy/standards/language_standards/languages/perl.py` (PYTHON) | Magnitude: 23.82 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 186, regex_execution: 49, bitwise_ops: 40, generics: 15
- `tests/core_engine/test_handshake_issue_2549.py` (PYTHON) | Magnitude: 79.46 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 56, core_var_decl: 28, design_snake_case: 27
- `tests/extraction/languages/test_scheme_strict.py` (PYTHON) | Magnitude: 213.58 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 273, structural_boundaries: 161, safety: 86, core_var_decl: 66

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/extraction/languages/test_zig_strict.py` (PYTHON) | Magnitude: 221.04 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 206, structural_boundaries: 166, core_var_decl: 110, safety: 105
- `tests/tools_recorders/test_audit_recorder.py` (PYTHON) | Magnitude: 101.12 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 242, structural_boundaries: 61, core_var_decl: 44, design_snake_case: 44
- `tests/extraction/languages/test_ada_strict.py` (PYTHON) | Magnitude: 269.88 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 254, structural_boundaries: 171, state_mutation: 105, safety: 80
- `tests/extraction/languages/test_zig.py` (PYTHON) | Magnitude: 50.34 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 87, core_var_decl: 39, structural_boundaries: 31, test: 26
- `tests/extraction/languages/test_dart_strict.py` (PYTHON) | Magnitude: 174.32 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 210, structural_boundaries: 149, core_var_decl: 84, design_snake_case: 79

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `gitgalaxy/standards/language_standards/languages/kotlin.py` (PYTHON) | Magnitude: 21.08 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 149, regex_execution: 50, bitwise_ops: 33, structural_boundaries: 25
- `tests/extraction/languages/test_groovy.py` (PYTHON) | Magnitude: 43.14 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 115, structural_boundaries: 58, test: 25, args: 19
- `gitgalaxy/core/guidestar_lens.py` (PYTHON) | Magnitude: 380.14 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 288, branch: 77, state_mutation: 66, structural_boundaries: 59
- `tests/extraction/languages/test_matlab_strict.py` (PYTHON) | Magnitude: 269.6 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 325, structural_boundaries: 211, safety: 140, core_var_decl: 111
- `tests/core_engine/test_detector.py` (PYTHON) | Magnitude: 2249.66 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 2766, structural_boundaries: 1260, core_var_decl: 791, design_snake_case: 770

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/extraction/languages/test_css.py` (PYTHON) | Magnitude: 43.28 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 28, test: 19, state_mutation: 12
- `tests/extraction/languages/test_solidity.py` (PYTHON) | Magnitude: 44.86 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 40, test: 25, args: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `tests/extraction/languages/test_shared_patterns_strict.py` (PYTHON) | Magnitude: 19.22 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 39, safety: 31, safety_bypasses: 11
- `tests/extraction/languages/test_mlir_strict.py` (PYTHON) | Magnitude: 4.02 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 8, safety: 6, safety_bypasses: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/security_auditing/test_dependency_audit_cache.py` (PYTHON) | Magnitude: 166.08 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 175, state_mutation: 74, core_var_decl: 64, design_snake_case: 64
- `tests/core_engine/test_no_networkx_runtime.py` (PYTHON) | Magnitude: 6.3 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, import: 4, state_mutation: 3, core_var_decl: 3
- `tests/extraction/languages/test_structure_contract_2856.py` (PYTHON) | Magnitude: 37.64 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 16, core_var_decl: 9, state_mutation: 8
- `tests/core_engine/test_language_strictness.py` (PYTHON) | Magnitude: 51.28 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 48, safety: 21, core_var_decl: 15
- `tests/cobol_mainframe/test_cobol_schema_forge.py` (PYTHON) | Magnitude: 21.54 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 26, safety: 19, core_var_decl: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/extraction/languages/test_cleanup_contract_2888.py` (PYTHON) | Magnitude: 36.02 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 120, structural_boundaries: 24, cleanup: 15, args: 9
- `tests/tools_recorders/test_record_data.py` (PYTHON) | Magnitude: 79.68 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 174, structural_boundaries: 31, state_mutation: 23, core_var_decl: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `.github/workflows/codeql.yml` (YAML) | Magnitude: 17.78 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 4, args: 4, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/cobol_mainframe/test_cobol_compiler_forge.py` (PYTHON) | Magnitude: 23.06 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 23, core_var_decl: 17, safety: 15
- `tests/cobol_mainframe/test_cobol_dag_architect.py` (PYTHON) | Magnitude: 60.14 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 145, structural_boundaries: 38, core_var_decl: 30, design_snake_case: 30
- `gitgalaxy/standards/language_standards/languages/c.py` (PYTHON) | Magnitude: 21.18 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 154, bitwise_ops: 55, regex_execution: 49, branch: 25
- `gitgalaxy/standards/language_standards/languages/go.py` (PYTHON) | Magnitude: 19.88 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 139, bitwise_ops: 55, regex_execution: 50, structural_boundaries: 21
- `tests/cobol_mainframe/test_cobol_jcl_auditor.py` (PYTHON) | Magnitude: 24.5 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 29, core_var_decl: 23, safety: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `gitgalaxy/core/state_rehydrator.py` (PYTHON) | Magnitude: 321.48 | Delta: **0.216** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 271, branch: 86, state_mutation: 43, structural_boundaries: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `tests/test_signal_contract_sheet.py` (PYTHON) | Magnitude: 82.1 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 33, indent_spaces: 33, branch: 22, state_mutation: 15
- `gitgalaxy/core/network_risk_sensor.py` (PYTHON) | Magnitude: 609.72 | Delta: **0.235** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 356, branch: 112, state_mutation: 107, core_var_decl: 99

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `gitgalaxy/standards/language_standards/languages/zig.py` (PYTHON) | Magnitude: 21.38 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 114, bitwise_ops: 54, regex_execution: 43, structural_boundaries: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tests/tools/crucible_check.py` (PYTHON) | Magnitude: 0.2 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 147, core_var_decl: 64, design_snake_case: 59, branch: 48

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `gitgalaxy/core/detector.py` -> Churn: **100.0%** | Cog Load: 67.7729% | Debt: 25.5008%
- `gitgalaxy/recorders/record_keeper.py` -> Churn: **88.42%** | Cog Load: 65.4441% | Debt: 8.5559%
- `gitgalaxy/core/state_rehydrator.py` -> Churn: **78.31%** | Cog Load: 57.9857% | Debt: 0.0%
- `gitgalaxy/galaxyscope.py` -> Churn: **72.11%** | Cog Load: 84.3668% | Debt: 0.0%
- `gitgalaxy/tools/cobol_to_cobol/galaxy_ir.py` -> Churn: **72.11%** | Cog Load: 51.771% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `gitgalaxy/core/detector.py` -> **Joe Esquibel** (100.0% isolated ownership) | Magnitude: 8809.34
- `gitgalaxy/recorders/llm_recorder.py` -> **Joe Esquibel** (100.0% isolated ownership) | Magnitude: 2842.02
- `gitgalaxy/galaxyscope.py` -> **Joe Esquibel** (100.0% isolated ownership) | Magnitude: 2659.06
- `tests/core_engine/test_detector.py` -> **Joe Esquibel** (100.0% isolated ownership) | Magnitude: 2249.66
- `gitgalaxy/recorders/record_keeper.py` -> **Joe Esquibel** (100.0% isolated ownership) | Magnitude: 1791.82

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `gitgalaxy/core/detector.py` -> **Severity: 0.233** (Bridge: 0.0023 * Flux: 100.0%)
- `gitgalaxy/galaxyscope.py` -> **Severity: 0.15** (Bridge: 0.0015 * Flux: 100.0%)
- `gitgalaxy/core/network_risk_sensor.py` -> **Severity: 0.14** (Bridge: 0.0014 * Flux: 100.0%)
- `gitgalaxy/standards/language_standards/__init__.py` -> **Severity: 0.042** (Bridge: 0.004 * Flux: 10.6415%)
- `gitgalaxy/core/invocation_resolver.py` -> **Severity: 0.032** (Bridge: 0.0003 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `gitgalaxy/standards/language_standards/_shared_patterns.py` -> **Severity: 16.813** (Embedded: 0.2654 * Error Risk: 63.3525%)
- `gitgalaxy/standards/language_standards/__init__.py` -> **Severity: 15.758** (Embedded: 0.3028 * Error Risk: 52.0348%)
- `gitgalaxy/standards/language_standards/_lens_config.py` -> **Severity: 9.282** (Embedded: 0.1742 * Error Risk: 53.2839%)
- `gitgalaxy/standards/language_standards/_overrides.py` -> **Severity: 8.785** (Embedded: 0.1742 * Error Risk: 50.431%)
- `gitgalaxy/core/detector.py` -> **Severity: 8.718** (Embedded: 0.1015 * Error Risk: 85.8894%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/tools/tri_comparison_reconcile.py` -> **Severity: 422.48** (Blast Radius: 5.281 * Doc Risk: 80.0%)
- `gitgalaxy/core/detector.py` -> **Severity: 406.868** (Blast Radius: 19.168 * Doc Risk: 21.2264%)
- `gitgalaxy/standards/config_resolver.py` -> **Severity: 357.803** (Blast Radius: 7.577 * Doc Risk: 47.2222%)
- `tests/tools/tree_sitter_accuracy_audit.py` -> **Severity: 270.225** (Blast Radius: 5.773 * Doc Risk: 46.8085%)
- `gitgalaxy/core/spatial_correlation.py` -> **Severity: 253.05** (Blast Radius: 10.122 * Doc Risk: 25.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1061 literal sites + 4 sites through wrappers = 1065

- `_warn_malformed` (function, debug_prints, primitive): 2 call sites in 1 files -- `tests/tools/tri_comparison_ledger.py`
- `run_blurbs` (function, debug_prints, primitive): 1 call sites in 1 files -- `tests/tools/tree_sitter_accuracy_audit.py`
- `run_chart` (function, debug_prints, primitive): 1 call sites in 1 files -- `tests/tools/tree_sitter_accuracy_audit.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 17561 call pairs -- scoped 27.7%, unique 0.0%, ambiguous 4.9%, external 67.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 17552 | 27.8% | 0.0% | 4.9% | 67.3% |
| shell | 9 | 11.1% | 0.0% | 0.0% | 88.9% |

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
