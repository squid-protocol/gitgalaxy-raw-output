# ARCHITECTURAL_BRIEF: angr
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/angr/angr.git` |
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
- **Scope:** 1804 analyzed artifact(s), 233662 LOC.
- **Load-bearing artifact:** `angr/__init__.py` -- 593 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `angr/analyses/decompiler/peephole_optimizations/__init__.py` -- pulls in 63 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `angr/analyses/cfg/cfg_fast.py` at magnitude 5851.88 (structural weight, not risk).
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
| Total Artifacts | 1930 |
| Analyzed Artifacts (Scanned) | 1804 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 126 |
| Total LOC | 233662 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 93.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5412 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2459 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 34.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.682 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 55 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 1426 | 200539 | 79.0% |
| JSON | 326 | 25080 | 18.1% |
| RUST | 15 | 2868 | 0.8% |
| YAML | 8 | 406 | 0.4% |
| SHELL | 6 | 709 | 0.3% |
| PLAINTEXT | 5 | 0 | 0.3% |
| PROTO | 5 | 336 | 0.3% |
| MARKDOWN | 4 | 0 | 0.2% |
| CPP | 4 | 3446 | 0.2% |
| C | 3 | 187 | 0.2% |
| MAKEFILE | 2 | 91 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 1804 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 30%, Large Core Modules (2) 17%, Parameter Forwarders Files 16%, Large Core Modules (3) 9%, Encapsulated Accessors Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1795 | 99.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 126*

**Composition by Extension & Reason:**
- `.rst`: 50x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (Massive Static Asset Blob: 3523 LOC), 1x Excluded (Embedded Array/Matrix Payload: 6009 commas in 813 LOC), 1x Excluded (Embedded Array/Matrix Payload: 1739 commas in 528 LOC)
- `.h`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected), 1x Unsupported Format (.undeterminable)
- `.py`: 2x Excluded (Saturation: Line 27 exceeds 500 chars), 2x Excluded (Saturation: Line 26 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 37 LOC)
- `.pickle`: 6x Excluded (Unsupported Extension: '.pickle')
- `.toml`: 2x Unsupported Format (.toml), 1x Excluded (Unsupported Extension: '.toml')
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.typed`: 1x Excluded (Unsupported Extension: '.typed')
- `.bat`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.2 | 26.7 | 15.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.7 | 45.2 | 52.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 12.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.0 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 18.1 | 8.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 48.2 | 31.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 92.4 | 0.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.2 | 0.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 97.2 | 8.1 | 7.9 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 62.8 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2883 | 474 | 4 | `angr/analyses/decompiler/structuring/phoenix.py` |
| cleanup | 69 | 24 | 0 | `native/unicornlib/sim_unicorn.cpp` |
| guards | 20090 | 943 | 29 | `tests/analyses/decompiler/test_decompiler.py` |
| danger | 5725 | 730 | 8 | `angr/sim_type.py` |
| concurrency | 827 | 85 | 0 | `angr/analyses/decompiler/structured_codegen/c.py` |
| connectivity | 12300 | 1367 | 16 | `tests/analyses/decompiler/test_decompiler.py` |
| io | 1717 | 273 | 2 | `tests/analyses/decompiler/test_decompiler.py` |
| crypto | 1 | 1 | 0 | `angr/ailment/utils.py` |
| ipc | 73 | 12 | 0 | `tests/analyses/test_reassembler.py` |
| time | 63 | 31 | 0 | `angr/rustylib/fuzzer.pyi` |
| serialization | 39 | 16 | 0 | `corpus_tests/scripts/gh_ls.sh` |
| regex | 160 | 30 | 0 | `tests/analyses/decompiler/test_decompiler.py` |
| events | 151 | 43 | 0 | `angr/engines/light/engine.py` |
| tests | 3210 | 271 | 5 | `tests/analyses/decompiler/test_decompiler.py` |
| docs | 4176 | 722 | 6 | `angr/analyses/cfg/cfg_emulated.py` |
| debt | 1826 | 410 | 2 | `angr/sim_type.py` |
| mutation | 101634 | 1321 | 142 | `tests/analyses/decompiler/test_decompiler.py` |
| dead_code | 2513 | 545 | 2 | `tests/analyses/decompiler/test_decompiler.py` |
| credential | 10 | 5 | 0 | `tests/analyses/decompiler/test_decompiler.py` |
| threat | 173 | 29 | 0 | `tests/analyses/reaching_definitions/test_regressions.py` |
| ml_ai | 47 | 10 | 0 | `angr/llm_client.py` |
| ui | 31 | 10 | 0 | `angr/analyses/disassembly.py` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.3333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/analyses/decompiler/test_decompiler.py` (Hits: 220)
- `corpus_tests/scripts/snapshot_diff.sh` (Hits: 80)
- `corpus_tests/scripts/gh_ls.sh` (Hits: 65)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **__init__.py** (`angr/__init__.py`) — 593 inbound connections
2. **project.py** (`angr/project.py`) — 265 inbound connections
3. **solver.py** (`angr/state_plugins/solver.py`) — 206 inbound connections
4. **errors.py** (`angr/errors.py`) — 194 inbound connections
5. **common.py** (`tests/common.py`) — 184 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **__init__.py** (`angr/analyses/decompiler/peephole_optimizations/__init__.py`) — 63 outbound dependencies
2. **__init__.py** (`angr/analyses/__init__.py`) — 52 outbound dependencies
3. **analysis.py** (`angr/analyses/analysis.py`) — 48 outbound dependencies
4. **clinic.py** (`angr/analyses/decompiler/clinic.py`) — 47 outbound dependencies
5. **__init__.py** (`angr/analyses/decompiler/optimization_passes/__init__.py`) — 41 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_try_resolve_targets_load` **(Many-Argument Workhorses)** (@ `angr/analyses/cfg/indirect_jump_resolvers/jumptable.py`) -> Impact: **343.6** | LOC: 371
- `lift_vex` **(Many-Argument Workhorses)** (@ `angr/engines/vex/lifter.py`) -> Impact: **328.2** | LOC: 213
- `__init__` **(Many-Argument Workhorses)** (@ `angr/analyses/cfg/cfg_fast.py`) -> Impact: **320.4** | LOC: 304
- `lift_pcode` **(Many-Argument Workhorses)** (@ `angr/engines/pcode/lifter.py`) -> Impact: **311.5** | LOC: 214
- `_generate_cfgnode` **(Many-Argument Workhorses)** (@ `angr/analyses/cfg/cfg_fast.py`) -> Impact: **299.6** | LOC: 391
  * *Intent:* # # Other methods # """ Generate a CFGNode that starts at `cfg_job.addr`. Since lifting machine code to IRSBs is slow, self._nodes is used as a cache ...
- `_make_switch_cases_core` **(Many-Argument Workhorses)** (@ `angr/analyses/decompiler/structuring/phoenix.py`) -> Impact: **297.6** | LOC: 183
- `_process_vex_irsb` **(Many-Argument Workhorses)** (@ `angr/analyses/stack_pointer_tracker.py`) -> Impact: **283.4** | LOC: 256
- `_unify_local_variables` **(Many-Argument Workhorses)** (@ `angr/analyses/decompiler/ail_simplifier.py`) -> Impact: **264.3** | LOC: 449
  * *Intent:* # # Unifying local variables # """ Find variables that are definitely equivalent and then eliminate unnecessary copies. """
- `_determine` **(Many-Argument Workhorses)** (@ `angr/analyses/typehoon/simple_solver.py`) -> Impact: **263.9** | LOC: 251
- `_resolve` **(Many-Argument Workhorses)** (@ `angr/analyses/cfg/indirect_jump_resolvers/jumptable.py`) -> Impact: **251.2** | LOC: 283
  * *Intent:* # # Private methods #

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `angr/analyses` | 38 | 19781.9 | 59.78% | 26.92% |
| `angr` | 31 | 16848.38 | 47.87% | 14.33% |
| `angr/analyses/decompiler` | 28 | 16494.28 | 50.88% | 8.33% |
| `angr/analyses/cfg` | 10 | 13968.0 | 50.38% | 7.58% |
| `angr/analyses/decompiler/optimization_passes` | 39 | 10752.24 | 66.54% | 5.87% |
| `angr/state_plugins` | 29 | 9247.3 | 51.15% | 23.8% |
| `angr/analyses/decompiler/structuring` | 7 | 7837.62 | 62.36% | 18.28% |
| `angr/analyses/decompiler/peephole_optimizations` | 63 | 6677.38 | 55.83% | 3.28% |
| `tests/analyses/decompiler` | 33 | 5996.12 | 22.79% | 0.0% |
| `angr/analyses/reaching_definitions` | 12 | 5820.74 | 54.0% | 7.55% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/ISSUE_TEMPLATE/bug-report.yml` -> **100.0%** Exposure
- `angr/analyses/identifier/functions/memcmp.py` -> **100.0%** Exposure
- `angr/analyses/identifier/functions/memset.py` -> **100.0%** Exposure
- `angr/analyses/identifier/functions/recv_until.py` -> **100.0%** Exposure
- `angr/analyses/identifier/functions/skip_recv_n.py` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `angr/__main__.py` -> **100.0%** Exposure
- `angr/ailment/block.py` -> **100.0%** Exposure
- `angr/ailment/converter_pcode.py` -> **100.0%** Exposure
- `angr/ailment/expression.py` -> **100.0%** Exposure
- `angr/analyses/analysis.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/analyses/decompiler/test_decompiler.py` -> **219** Orphaned Functions | **0** Duplicates
- `native/unicornlib/sim_unicorn.cpp` -> **97** Orphaned Functions | **0** Duplicates
- `angr/sim_type.py` -> **0** Orphaned Functions | **54** Duplicates
- `tests/analyses/cfg/test_cfgfast.py` -> **53** Orphaned Functions | **0** Duplicates
- `tests/analyses/decompiler/test_ccall_rewriter_arm.py` -> **50** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `7435` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `angr/analyses/cfg/cfg_fast.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.701)
- **Top Global Matches:** file_cluster_6: 7.701, file_cluster_8: 10.273, file_cluster_4: 15.388
- **Magnitude:** 5851.88 | **LOC:** 5547 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 84.6%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **39**; blast radius 0.454; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.3%), Complexity Load (formerly Cognitive Load) (78.5%)
- **Documentation Coverage:** 68.6047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 320.4)
  * `_generate_cfgnode` **(Many-Argument Workhorses)** (Impact: 299.6)
    * *Intent:* # # Other methods # """ Generate a CFGNode that starts at `cfg_job.addr`. Since lifting machine code...
  * `_process_block_arch_specific` **(Many-Argument Workhorses)** (Impact: 242.8)
  * `_create_jobs` **(Many-Argument Workhorses)** (Impact: 172.2)
  * `_remove_redundant_overlapping_blocks` **(Many-Argument Workhorses)** (Impact: 130.0)
    * *Intent:* # Removers """ On some architectures there are sometimes garbage bytes (usually nops) between functi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 776 instances
* *State Mutation (weighted view):* 2502
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1245`, `structural_boundaries: 531`, `args: 130`, `func_start: 125`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 950`, `dead_code: 2`, `planned_debt: 17`, `fragile_debt: 11`
* *Architecture:* `api: 55`, `import: 41`
* *Defense:* `safety: 101`, `doc: 64`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.454
  * `Choke Point (Betweenness):` 0.00301 | `Ripple Effect (Closeness):` 0.147242
  * `Imports (Out-Degree: 37):` .cfg_arch_options, .cfg_base, .indirect_jump_resolvers.jumptable, .meta_structs, __future__, angr, angr.analyses, angr.analyses.decompiler.clinic...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `angr/analyses/decompiler/structured_codegen/c.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.153)
- **Top Global Matches:** file_cluster_4: 6.153, file_cluster_16: 9.468, file_cluster_12: 9.633
- **Magnitude:** 4742.86 | **LOC:** 4373 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 30.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **29**; blast radius 0.534; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.6%)
- **Documentation Coverage:** 95.0495% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_access` **(Many-Argument Workhorses)** (Impact: 138.3)
  * `_handle_Expr_Const` **(Many-Argument Workhorses)** (Impact: 130.2)
  * `full_c_repr_chunks` **(Many-Argument Workhorses)** (Impact: 122.3)
  * `_access_constant_offset` **(Many-Argument Workhorses)** (Impact: 114.4)
  * `c_repr` **(Many-Argument Workhorses)** (Impact: 90.1)
    * *Intent:* """ Creates the C representation of the code and displays it by constructing a large string. This fu...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 521 instances
* *State Mutation (weighted view):* 1771
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 943`, `structural_boundaries: 889`, `args: 272`, `func_start: 264`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 729`, `dead_code: 5`, `planned_debt: 22`, `fragile_debt: 9`, `duplicate_logic: 12`
* *Architecture:* `api: 179`, `import: 30`
* *Defense:* `safety: 225`, `doc: 46`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.534
  * `Choke Point (Betweenness):` 0.00172 | `Ripple Effect (Closeness):` 0.135209
  * `Imports (Out-Degree: 25):` .base, __future__, angr, angr.ailment, angr.ailment.constant, angr.ailment.expression, angr.analyses, angr.analyses.decompiler.notes.deobfuscated_strings...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `angr/analyses/decompiler/structuring/phoenix.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.308)
- **Top Global Matches:** file_cluster_8: 7.308, file_cluster_6: 15.242, file_cluster_3: 22.959
- **Magnitude:** 4430.56 | **LOC:** 3648 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **21**; blast radius 0.605; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.5%)
- **Documentation Coverage:** 93.5897% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_make_switch_cases_core` **(Many-Argument Workhorses)** (Impact: 297.6)
  * `_match_acyclic_switch_cases_address_loaded_from_memory` **(Many-Argument Workhorses)** (Impact: 179.9)
  * `_refine_cyclic_core` **(Many-Argument Workhorses)** (Impact: 178.5)
  * `_match_acyclic_ite` **(Many-Argument Workhorses)** (Impact: 152.8)
    * *Intent:* """ Check if start_node is the beginning of an If-Then-Else region. Create a Condition node if it is...
  * `_find_node_going_to_dst` **(Stateful Encapsulated Methods)** (Impact: 124.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 518 instances
* *State Mutation (weighted view):* 1647
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1013`, `structural_boundaries: 430`, `args: 86`, `func_start: 72`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 611`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `api: 9`, `import: 22`
* *Defense:* `safety: 166`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.605
  * `Choke Point (Betweenness):` 0.001037 | `Ripple Effect (Closeness):` 0.124248
  * `Imports (Out-Degree: 15):` .structurer_base, .structurer_nodes, __future__, angr.ailment.block, angr.ailment.expression, angr.ailment.statement, angr.analyses.decompiler.counters.call_counter, angr.analyses.decompiler.node_replacer...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `angr/sim_type.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 10.598)
- **Top Global Matches:** file_cluster_12: 10.598, file_cluster_4: 10.778, file_cluster_5: 11.134
- **Magnitude:** 4288.46 | **LOC:** 4480 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **93** in-repo importer(s); it depends on **19**; blast radius 15.323; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.1%), Connectivity (formerly Api Exposure) (86.1%), Complexity Load (formerly Cognitive Load) (76.6%)
- **Documentation Coverage:** 90.297% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_decl_to_type` **(Many-Argument Workhorses)** (Impact: 237.4)
  * `parse_file` **(Defensive Guards)** (Impact: 60.8)
  * `from_json` **(Defensive Guards)** (Impact: 54.4)
    * *Intent:* """ Deserialize a type class from a JSON-compatible dictionary. """
  * `c_repr` **(Compute Cores)** (Impact: 48.4)
  * `c_repr` **(Compute Cores)** (Impact: 48.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 541 instances
* *High Risk Execution (weighted view):* 9
* *State Mutation (weighted view):* 1795
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 769`, `structural_boundaries: 864`, `args: 322`, `func_start: 317`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 65`, `high_risk_execution: 13`, `state_mutation: 713`, `planned_debt: 18`, `fragile_debt: 14`, `duplicate_logic: 54`
* *Architecture:* `api: 220`, `import: 21`
* *Defense:* `safety: 140`, `doc: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.323
  * `Choke Point (Betweenness):` 0.003855 | `Ripple Effect (Closeness):` 0.283545
  * `Imports (Out-Degree: 4):` .state_plugins.view, __future__, angr.errors, angr.procedures.definitions, angr.sim_state, archinfo, claripy, collections...
  * `Imported By (In-Degree: 93):` (Excluded from Brief to save tokens)

### `tests/analyses/decompiler/test_decompiler.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.542)
- **Top Global Matches:** file_cluster_15: 7.542, file_cluster_16: 8.213, file_cluster_13: 8.269
- **Magnitude:** 4060.56 | **LOC:** 5443 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 44.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.177; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.2%), Complexity Load (formerly Cognitive Load) (28.6%), Connectivity (formerly Api Exposure) (12.4%)
- **Documentation Coverage:** 93.6123% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_decompiling_rep_stosq` **(Many-Argument Workhorses)** (Impact: 36.2)
  * `_check_rep_stosq` **(Stateful Encapsulated Methods)** (Impact: 34.0)
    * *Intent:* """ Example: for (v7 = 32; v7; v6 += 1) { v7 -= 1; *(v6) = 0; }
  * `test_decompiling_rust_fmt_main` **(Defensive Guards)** (Impact: 33.7)
  * `test_decompiling_msvcrt_setsbuplow` **(Defensive Guards)** (Impact: 31.5)
  * `test_decompiling_1after909_doit` **(Defensive Guards)** (Impact: 29.4)
    * *Intent:* """ The doit() function has an abnormal loop at 0x1d47 - 0x1da1 - 0x1d73. The original source code c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 335 instances
* *State Mutation (weighted view):* 2226
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 496`, `structural_boundaries: 1120`, `args: 228`, `func_start: 228`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1556`, `dead_code: 32`, `planned_debt: 19`, `fragile_debt: 16`, `unreferenced_by_name: 219`
* *Architecture:* `io: 220`, `api: 226`, `import: 22`
* *Defense:* `safety: 762`, `doc: 35`, `test: 223`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.177
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` __future__, angr, angr.ailment, angr.analyses, angr.analyses.complete_calling_conventions, angr.analyses.decompiler, angr.analyses.decompiler.decompilation_options, angr.analyses.decompiler.optimization_passes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `angr/analyses/decompiler/clinic.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.252)
- **Top Global Matches:** file_cluster_8: 9.252, file_cluster_6: 9.269, file_cluster_4: 17.23
- **Magnitude:** 4037.0 | **LOC:** 3763 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 57.1%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **47**; blast radius 0.992; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.3%), Complexity Load (formerly Cognitive Load) (70.1%)
- **Documentation Coverage:** 82.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 188.7)
  * `_link_variables_on_expr` **(Many-Argument Workhorses)** (Impact: 184.4)
  * `_recover_and_link_variables` **(Many-Argument Workhorses)** (Impact: 118.6)
  * `_fix_abnormal_switch_case_heads_case2` **(Many-Argument Workhorses)** (Impact: 113.3)
  * `_recover_calling_conventions` **(Many-Argument Workhorses)** (Impact: 91.7)
    * *Intent:* """ Examine the calling convention and function prototype for each function called. For functions wi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 489 instances
* *State Mutation (weighted view):* 1636
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 863`, `structural_boundaries: 408`, `args: 105`, `func_start: 100`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 658`, `dead_code: 4`, `planned_debt: 9`, `fragile_debt: 5`
* *Architecture:* `api: 21`, `import: 47`
* *Defense:* `safety: 199`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.992
  * `Choke Point (Betweenness):` 0.036621 | `Ripple Effect (Closeness):` 0.179043
  * `Imports (Out-Degree: 53):` .ail_simplifier, .ailgraph_walker, .decompilation_cache, .notes, .optimization_passes, .peephole_optimizations, .return_maker, .semantic_naming...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `native/unicornlib/sim_unicorn.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.297)
- **Top Global Matches:** file_cluster_6: 6.297, file_cluster_4: 6.868, file_cluster_15: 14.652
- **Magnitude:** 3457.64 | **LOC:** 3270 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.177; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.7%), Complexity Load (formerly Cognitive Load) (93.8%), Guard Balance (formerly Safety Score) (80.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `State::process_vex_expr` **(Many-Argument Workhorses)** (Impact: 210.1)
  * `State::handle_write` **(Many-Argument Workhorses)** (Impact: 186.5)
  * `State::propagate_taint_of_mem_read_instr_and_continue` **(Many-Argument Workhorses)** (Impact: 131.4)
  * `State::process_vex_block` **(Many-Argument Workhorses)** (Impact: 126.9)
  * `State::propagate_taint_of_one_stmt` **(Compute Cores)** (Impact: 84.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 566 instances
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 1830
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 708`, `structural_boundaries: 401`, `args: 112`, `func_start: 105`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 5`, `state_mutation: 698`, `dead_code: 24`, `planned_debt: 17`, `fragile_debt: 3`, `unreferenced_by_name: 97`
* *Architecture:* `import: 18`
* *Defense:* `safety: 21`, `immutability_locks: 20`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.177
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` algorithm, cassert, cinttypes, cstdint, cstring, libvex.h, map, memory...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `angr/analyses/cfg/cfg_emulated.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.842)
- **Top Global Matches:** file_cluster_6: 5.842, file_cluster_4: 10.229, file_cluster_8: 15.387
- **Magnitude:** 3367.32 | **LOC:** 3454 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **34**; blast radius 0.475; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (51.6%)
- **Documentation Coverage:** 21.7054% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_try_resolving_indirect_jumps` **(Many-Argument Workhorses)** (Impact: 209.1)
    * *Intent:* """ Resolve indirect jumps specified by sim_successors.addr. :param SimSuccessors sim_successors: Th...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 123.7)
  * `_get_successors` **(Many-Argument Workhorses)** (Impact: 92.1)
    * *Intent:* """ Get a collection of successors out of the current job. :param CFGJob job: The CFGJob instance. :...
  * `_handle_successor` **(Many-Argument Workhorses)** (Impact: 89.9)
    * *Intent:* """ Returns a new CFGJob instance for further analysis, or None if there is no immediate state to pe...
  * `_backward_slice_indirect` **(Many-Argument Workhorses)** (Impact: 86.5)
    * *Intent:* """ Try to resolve an indirect jump by slicing backwards """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 472 instances
* *State Mutation (weighted view):* 1556
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 632`, `structural_boundaries: 299`, `args: 89`, `func_start: 85`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 2`, `state_mutation: 612`, `dead_code: 10`, `planned_debt: 28`, `fragile_debt: 12`
* *Architecture:* `io: 6`, `api: 40`, `import: 38`
* *Defense:* `safety: 44`, `doc: 72`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.475
  * `Choke Point (Betweenness):` 0.000614 | `Ripple Effect (Closeness):` 0.149382
  * `Imports (Out-Degree: 34):` .cfg_base, .cfg_job_base, __future__, angr, angr.analyses, angr.analyses.backward_slice, angr.analyses.cdg, angr.analyses.ddg...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `angr/analyses/cfg/cfg_base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.885)
- **Top Global Matches:** file_cluster_6: 5.885, file_cluster_4: 10.01, file_cluster_8: 15.585
- **Magnitude:** 3282.7 | **LOC:** 3136 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 82.4%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **28**; blast radius 0.831; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (83.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.5%)
- **Documentation Coverage:** 35.5372% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_graph_traversal_handler` **(Many-Argument Workhorses)** (Impact: 212.9)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 197.7)
  * `_normalize_core` **(Many-Argument Workhorses)** (Impact: 158.1)
  * `_executable_memory_regions` **(Many-Argument Workhorses)** (Impact: 110.7)
    * *Intent:* """ Get all executable memory regions from the binaries :param objects: A collection of binary objec...
  * `_is_tail_call_optimization` **(Many-Argument Workhorses)** (Impact: 107.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 423 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1317
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 680`, `structural_boundaries: 363`, `args: 85`, `func_start: 80`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 1`, `state_mutation: 471`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 2`
* *Architecture:* `api: 40`, `import: 29`
* *Defense:* `safety: 61`, `doc: 60`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.831
  * `Choke Point (Betweenness):` 0.006158 | `Ripple Effect (Closeness):` 0.16289
  * `Imports (Out-Degree: 21):` .indirect_jump_resolvers.default_resolvers, __future__, angr.analyses, angr.analyses.stack_pointer_tracker, angr.codenode, angr.engines.vex.lifter, angr.errors, angr.knowledge_plugins.cfg...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `angr/calling_conventions.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.146)
- **Top Global Matches:** file_cluster_4: 8.146, file_cluster_12: 10.158, file_cluster_5: 11.088
- **Magnitude:** 3278.9 | **LOC:** 2808 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **69** in-repo importer(s); it depends on **12**; blast radius 11.461; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.7%), Connectivity (formerly Api Exposure) (93.2%), Complexity Load (formerly Cognitive Load) (83.0%)
- **Documentation Coverage:** 89.6057% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_standardize_value` **(Defensive Guards)** (Impact: 151.4)
    * *Intent:* # # Helper functions #
  * `_classify` **(Defensive Guards)** (Impact: 56.1)
  * `setup_callsite` **(Many-Argument Workhorses)** (Impact: 53.4)
    * *Intent:* """ This function performs the actions of the caller getting ready to jump into a function. :param s...
  * `refine_locs_with_struct_type` **(Many-Argument Workhorses)** (Impact: 48.4)
  * `next_arg` **(Many-Argument Workhorses)** (Impact: 48.0)
    * *Intent:* # https://github.com/riscv-non-isa/riscv-elf-psabi-doc/blob/master/riscv-cc.adoc # TODO: Implement v...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 416 instances
* *State Mutation (weighted view):* 1453
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 607`, `structural_boundaries: 574`, `args: 172`, `func_start: 170`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 621`, `dead_code: 2`, `planned_debt: 32`, `fragile_debt: 23`, `duplicate_logic: 26`
* *Architecture:* `api: 158`, `import: 13`
* *Defense:* `safety: 190`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.461
  * `Choke Point (Betweenness):` 0.006227 | `Ripple Effect (Closeness):` 0.283129
  * `Imports (Out-Degree: 5):` .errors, .sim_type, .state_plugins.sim_action_object, __future__, angr, archinfo, claripy, collections...
  * `Imported By (In-Degree: 69):` (Excluded from Brief to save tokens)

### `angr/analyses/reassembler.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.114)
- **Top Global Matches:** file_cluster_4: 7.114, file_cluster_6: 10.688, file_cluster_12: 11.508
- **Magnitude:** 3209.4 | **LOC:** 2905 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **22**; blast radius 0.483; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.2%)
- **Documentation Coverage:** 58.046% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assembly` **(Many-Argument Workhorses)** (Impact: 201.2)
  * `_initialize` **(Compute Cores)** (Impact: 108.6)
    * *Intent:* # # Private methods # """ Initialize the binary. :return: None """
  * `new_label` **(Many-Argument Workhorses)** (Impact: 72.4)
  * `assembly` **(Many-Argument Workhorses)** (Impact: 63.8)
    * *Intent:* """ :return: """
  * `_initialize` **(Stateful Encapsulated Methods)** (Impact: 58.7)
    * *Intent:* # # Private methods #
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 524 instances
* *State Mutation (weighted view):* 1676
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 629`, `structural_boundaries: 370`, `args: 117`, `func_start: 107`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 628`, `dead_code: 3`, `planned_debt: 10`, `fragile_debt: 3`, `duplicate_logic: 9`
* *Architecture:* `api: 82`, `import: 22`
* *Defense:* `safety: 19`, `doc: 54`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.483
  * `Choke Point (Betweenness):` 0.001601 | `Ripple Effect (Closeness):` 0.189007
  * `Imports (Out-Degree: 12):` .Analysis, .cfg, .cfg.cfg_emulated, .cfg.cfg_fast, .ddg, __future__, angr.analyses, angr.codenode...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `angr/engines/vex/claripy/ccall.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.018)
- **Top Global Matches:** file_cluster_15: 6.018, file_cluster_4: 7.022, file_cluster_16: 7.31
- **Magnitude:** 2517.84 | **LOC:** 2110 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **8**; blast radius 0.481; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.4%), Complexity Load (formerly Cognitive Load) (87.3%), Connectivity (formerly Api Exposure) (81.9%)
- **Documentation Coverage:** 98.4925% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pc_calculate_rdata_all_WRK` **(Many-Argument Workhorses)** (Impact: 65.9)
    * *Intent:* # sanity check cc_op = op_concretize(cc_op) if cc_op == data[platform]["OpTypes"]["G_CC_OP_COPY"]: l...
  * `pc_calculate_condition` **(Many-Argument Workhorses)** (Impact: 62.1)
    * *Intent:* # This function takes a condition that is being checked (ie, zero bit), and basically # returns that...
  * `x86g_use_seg_selector` **(Many-Argument Workhorses)** (Impact: 43.6)
    * *Intent:* # TODO Read/write/exec bit handling def bad(msg): if msg: l.warning("x86g_use_seg_selector: %s", msg...
  * `generic_rotate_with_carry` **(Many-Argument Workhorses)** (Impact: 39.5)
    * *Intent:* # returns cf, of, result # make sure sz is not symbolic if sz.op != "BVV": raise SimError('Hit a sym...
  * `arm64g_calculate_flag_n` **(Many-Argument Workhorses)** (Impact: 36.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 358 instances
* *State Mutation (weighted view):* 1543
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 287`, `args: 101`, `func_start: 101`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 827`, `dead_code: 4`, `planned_debt: 9`, `fragile_debt: 3`
* *Architecture:* `api: 99`, `import: 8`
* *Defense:* `safety: 15`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.481
  * `Choke Point (Betweenness):` 0.000902 | `Ripple Effect (Closeness):` 0.122921
  * `Imports (Out-Degree: 6):` __future__, angr, angr.errors, angr.sim_options, angr.state_plugins.sim_action_object, archinfo.arch_arm, claripy, logging
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `angr/analyses/decompiler/ail_simplifier.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.068)
- **Top Global Matches:** file_cluster_6: 9.068, file_cluster_8: 10.984, file_cluster_4: 16.327
- **Magnitude:** 2473.96 | **LOC:** 2274 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 45.5%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **32**; blast radius 0.288; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.6%)
- **Documentation Coverage:** 88.5246% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_unify_local_variables` **(Many-Argument Workhorses)** (Impact: 264.3)
    * *Intent:* # # Unifying local variables # """ Find variables that are definitely equivalent and then eliminate ...
  * `_remove_dead_assignments` **(Defensive Guards)** (Impact: 130.3)
    * *Intent:* # keeping tracking of statements to remove and statements (as well as dead vvars) to keep allows us ...
  * `_narrowing_needed` **(Many-Argument Workhorses)** (Impact: 70.7)
  * `_fold_call_exprs` **(Many-Argument Workhorses)** (Impact: 64.4)
    * *Intent:* """ Fold a call expression (statement) into other statements if the return value of the call express...
  * `_find_cyclic_dependent_phis_and_dirty_vvars` **(Many-Argument Workhorses)** (Impact: 61.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 377 instances
* *State Mutation (weighted view):* 1179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 617`, `structural_boundaries: 337`, `args: 56`, `func_start: 53`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 425`, `planned_debt: 4`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 15`, `import: 33`
* *Defense:* `safety: 137`, `doc: 17`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.288
  * `Choke Point (Betweenness):` 0.004179 | `Ripple Effect (Closeness):` 0.151376
  * `Imports (Out-Degree: 30):` .ailgraph_walker, .block_simplifier, .ccall_rewriters, .counters.expression_counters, .dirty_rewriters, .expression_narrower, __future__, angr.ailment...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `angr/analyses/typehoon/simple_solver.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.119)
- **Top Global Matches:** file_cluster_6: 8.119, file_cluster_4: 12.366, file_cluster_8: 15.674
- **Magnitude:** 2447.6 | **LOC:** 2141 | **CtrlFlow:** 38.6% | **Authorship Centralization:** 77.8%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.233; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.9%), Complexity Load (formerly Cognitive Load) (69.8%)
- **Documentation Coverage:** 74.1573% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_determine` **(Many-Argument Workhorses)** (Impact: 263.9)
  * `solve` **(Compute Cores)** (Impact: 65.8)
    * *Intent:* """ Steps: For each type variable, - Infer the shape in its sketch - Build the constraint graph - Co...
  * `compute_quotient_graph` **(Defensive Guards)** (Impact: 48.3)
    * *Intent:* """ Compute the quotient graph (the constraint graph modulo ~ in Algorithm E.1 in the retypd paper) ...
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 45.0)
  * `_unify` **(Many-Argument Workhorses)** (Impact: 44.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 323 instances
* *State Mutation (weighted view):* 1031
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 613`, `structural_boundaries: 272`, `args: 74`, `func_start: 70`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 385`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 27`, `import: 13`
* *Defense:* `safety: 207`, `doc: 32`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.233
  * `Choke Point (Betweenness):` 0.000759 | `Ripple Effect (Closeness):` 0.122007
  * `Imports (Out-Degree: 6):` .dfa, .typeconsts, .typevars, .variance, __future__, angr.utils.constants, collections, contextlib...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `angr/analyses/cfg/indirect_jump_resolvers/jumptable.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.666)
- **Top Global Matches:** file_cluster_4: 7.666, file_cluster_12: 9.375, file_cluster_5: 10.683
- **Magnitude:** 2438.58 | **LOC:** 2519 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **31**; blast radius 0.228; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.7%), Guard Balance (formerly Safety Score) (74.8%)
- **Documentation Coverage:** 90.2439% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_try_resolve_targets_load` **(Many-Argument Workhorses)** (Impact: 343.6)
  * `_resolve` **(Many-Argument Workhorses)** (Impact: 251.2)
    * *Intent:* # # Private methods #
  * `_handle_Comparison` **(Many-Argument Workhorses)** (Impact: 66.6)
  * `_all_qualified_load_stmts_in_slice` **(Defensive Guards)** (Impact: 63.0)
    * *Intent:* """ Recognize all qualified load statements in a slice. A qualified load statements refers to those ...
  * `_get_secondary_jumptable_from_transformations` **(Defensive Guards)** (Impact: 46.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 313 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 1033
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 486`, `structural_boundaries: 372`, `args: 87`, `func_start: 83`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 10`, `state_mutation: 407`, `planned_debt: 2`, `fragile_debt: 6`
* *Architecture:* `api: 60`, `import: 32`
* *Defense:* `safety: 148`, `doc: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.228
  * `Choke Point (Betweenness):` 0.001608 | `Ripple Effect (Closeness):` 0.1205
  * `Imports (Out-Degree: 31):` .constant_value_manager, .resolver, __future__, angr, angr.analyses.propagator.top_checker_mixin, angr.annocfg, angr.blade, angr.concretization_strategies...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `angr/ailment/expression.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.803)
- **Top Global Matches:** file_cluster_0: 7.803, file_cluster_15: 7.882, file_cluster_16: 8.429
- **Magnitude:** 2238.46 | **LOC:** 2015 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **152** in-repo importer(s); it depends on **13**; blast radius 15.344; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 62.8)
  * `has_atom` **(Defensive Guards)** (Impact: 37.0)
  * `replace` **(Many-Argument Workhorses)** (Impact: 35.7)
  * `replace` **(Compute Cores)** (Impact: 27.5)
  * `matches` **(Defensive Guards)** (Impact: 27.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 252 instances
* *State Mutation (weighted view):* 840
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 418`, `structural_boundaries: 538`, `args: 202`, `func_start: 202`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 336`, `planned_debt: 2`, `duplicate_logic: 12`
* *Architecture:* `api: 147`, `import: 13`
* *Defense:* `safety: 65`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.344
  * `Choke Point (Betweenness):` 0.004521 | `Ripple Effect (Closeness):` 0.182865
  * `Imports (Out-Degree: 5):` .statement, .tagged_object, .utils, __future__, abc, angr.calling_conventions, angr.sim_type, archinfo...
  * `Imported By (In-Degree: 152):` (Excluded from Brief to save tokens)

### `angr/knowledge_plugins/functions/function.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.538)
- **Top Global Matches:** file_cluster_4: 7.538, file_cluster_12: 9.323, file_cluster_16: 10.038
- **Magnitude:** 2033.32 | **LOC:** 2086 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **43** in-repo importer(s); it depends on **31**; blast radius 2.483; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.8%), Complexity Load (formerly Cognitive Load) (61.1%)
- **Documentation Coverage:** 63.2743% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 120.7)
  * `find_declaration` **(Many-Argument Workhorses)** (Impact: 79.6)
    * *Intent:* """ Find the most likely function declaration from the embedded collection of prototypes, set it to ...
  * `normalize` **(Compute Cores)** (Impact: 63.3)
    * *Intent:* """ Make sure all basic blocks in the transition graph of this function do not overlap. You will end...
  * `local_runtime_values` **(Compute Cores)** (Impact: 37.4)
    * *Intent:* """ Tries to find all runtime values of this function which do not come from inputs. These values ar...
  * `_rust_fmt_node` **(Stateful Encapsulated Methods)** (Impact: 33.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Cascading Flux:* 260 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 874
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 404`, `structural_boundaries: 367`, `args: 119`, `func_start: 118`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 7`, `state_mutation: 354`, `dead_code: 1`, `planned_debt: 6`, `fragile_debt: 3`
* *Architecture:* `io: 1`, `api: 108`, `import: 32`
* *Defense:* `safety: 45`, `doc: 49`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.483
  * `Choke Point (Betweenness):` 0.002051 | `Ripple Effect (Closeness):` 0.167746
  * `Imports (Out-Degree: 14):` .function_parser, __future__, angr.calling_conventions, angr.codenode, angr.errors, angr.knowledge_plugins.cfg.memory_data, angr.knowledge_plugins.functions.function_manager, angr.knowledge_plugins.xrefs.xref...
  * `Imported By (In-Degree: 43):` (Excluded from Brief to save tokens)

### `angr/analyses/bindiff.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.456)
- **Top Global Matches:** file_cluster_6: 9.456, file_cluster_4: 14.196, file_cluster_8: 15.448
- **Magnitude:** 1894.08 | **LOC:** 1512 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **12**; blast radius 0.495; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.4%)
- **Documentation Coverage:** 43.038% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_get_block_matches` **(Many-Argument Workhorses)** (Impact: 94.5)
  * `_compute_diff` **(Stateful Encapsulated Methods)** (Impact: 66.2)
    * *Intent:* # get the initial matches l.info("Getting PLT-based matches...") initial_matches = self._get_plt_mat...
  * `_get_approximate_matches_between_matched_pairs` **(Many-Argument Workhorses)** (Impact: 54.6)
  * `blocks_probably_identical` **(Many-Argument Workhorses)** (Impact: 41.3)
    * *Intent:* """ :param block_a: The first block address. :param block_b: The second block address. :param check_...
  * `_get_function_matches` **(Many-Argument Workhorses)** (Impact: 39.8)
    * *Intent:* """ :param attributes_a: A dict of functions to their attributes :param attributes_b: A dict of func...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 301 instances
* *State Mutation (weighted view):* 963
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 379`, `structural_boundaries: 192`, `args: 60`, `func_start: 54`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 361`, `planned_debt: 5`
* *Architecture:* `api: 28`, `import: 12`
* *Defense:* `safety: 18`, `doc: 32`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.495
  * `Choke Point (Betweenness):` 0.000447 | `Ripple Effect (Closeness):` 0.189007
  * `Imports (Out-Degree: 11):` __future__, angr.analyses, angr.errors, angr.knowledge_plugins, angr.knowledge_plugins.cfg.memory_data, collections, functools, logging...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `angr/state_plugins/unicorn_engine.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.72)
- **Top Global Matches:** file_cluster_4: 6.72, file_cluster_6: 10.808, file_cluster_12: 10.972
- **Magnitude:** 1867.1 | **LOC:** 1920 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **24**; blast radius 0.533; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.5%), Complexity Load (formerly Cognitive Load) (80.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 89.9225% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setup` **(Many-Argument Workhorses)** (Impact: 107.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 97.1)
  * `finish` **(Many-Argument Workhorses)** (Impact: 76.7)
    * *Intent:* # do the superficial synchronization # If succ_state is not None, synchronize it instead of self.sta...
  * `get_regs` **(Many-Argument Workhorses)** (Impact: 52.5)
    * *Intent:* """ loading registers from unicorn. If succ_state is not None, update it instead of self.state. Need...
  * `merge` **(Many-Argument Workhorses)** (Impact: 42.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 272 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 994
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 299`, `structural_boundaries: 201`, `args: 68`, `func_start: 67`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 19`, `state_mutation: 450`, `planned_debt: 4`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `api: 59`, `concurrency: 2`, `import: 24`
* *Defense:* `safety: 14`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.533
  * `Choke Point (Betweenness):` 0.000751 | `Ripple Effect (Closeness):` 0.185282
  * `Imports (Out-Degree: 15):` .plugin, __future__, angr, angr.engines.vex.claripy, angr.engines.vex.claripy.irop, angr.errors, angr.misc.testing, angr.sim_state...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `angr/analyses/disassembly.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.761)
- **Top Global Matches:** file_cluster_4: 7.761, file_cluster_12: 10.978, file_cluster_6: 11.576
- **Magnitude:** 1833.7 | **LOC:** 1351 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **19**; blast radius 0.827; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.8%), Guard Balance (formerly Safety Score) (85.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 96.124% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render` **(Many-Argument Workhorses)** (Impact: 139.4)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 80.8)
  * `_render` **(Many-Argument Workhorses)** (Impact: 74.7)
  * `dissect_instruction_by_default` **(Compute Cores)** (Impact: 51.7)
    * *Intent:* # perform a "smart split" of an operands string into smaller pieces insn_pieces = self.split_op_stri...
  * `_render` **(Stateful Encapsulated Methods)** (Impact: 43.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 279 instances
* *State Mutation (weighted view):* 916
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 319`, `structural_boundaries: 263`, `args: 94`, `func_start: 89`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 358`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* `api: 61`, `import: 19`
* *Defense:* `safety: 53`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.827
  * `Choke Point (Betweenness):` 0.001725 | `Ripple Effect (Closeness):` 0.192596
  * `Imports (Out-Degree: 14):` .Analysis, .disassembly_utils, __future__, angr.analyses, angr.block, angr.codenode, angr.engines, angr.errors...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `angr/knowledge_plugins/variables/variable_manager.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.099)
- **Top Global Matches:** file_cluster_4: 10.099, file_cluster_6: 10.248, file_cluster_5: 14.222
- **Magnitude:** 1766.3 | **LOC:** 1386 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 62.5%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **24**; blast radius 0.929; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.7%)
- **Documentation Coverage:** 74.0741% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assign_unified_variable_names` **(Many-Argument Workhorses)** (Impact: 92.7)
  * `parse_from_cmessage` **(Many-Argument Workhorses)** (Impact: 70.3)
  * `record_variable` **(Many-Argument Workhorses)** (Impact: 52.5)
  * `set_variable_type` **(Many-Argument Workhorses)** (Impact: 50.3)
  * `assign_variable_names` **(Defensive Guards)** (Impact: 50.0)
    * *Intent:* """ Assign default names to all SSA variables. :param labels: Known labels in the binary. :return: N...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 242 instances
* *State Mutation (weighted view):* 769
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 336`, `structural_boundaries: 244`, `args: 83`, `func_start: 72`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 285`, `planned_debt: 3`
* *Architecture:* `api: 66`, `import: 24`
* *Defense:* `safety: 55`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.929
  * `Choke Point (Betweenness):` 0.002272 | `Ripple Effect (Closeness):` 0.156986
  * `Imports (Out-Degree: 15):` .variable_access, __future__, angr, angr.analyses.decompiler.stack_item, angr.code_location, angr.keyed_region, angr.knowledge_plugins.plugin, angr.knowledge_plugins.types...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `angr/analyses/ddg.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.226)
- **Top Global Matches:** file_cluster_4: 7.226, file_cluster_12: 8.037, file_cluster_16: 9.119
- **Magnitude:** 1649.44 | **LOC:** 1671 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **10**; blast radius 1.691; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (41.9%)
- **Documentation Coverage:** 42.2018% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_construct` **(Compute Cores)** (Impact: 62.0)
    * *Intent:* # # Private methods # """ Construct the data dependence graph. We track the following types of depen...
  * `_handle_tmp_write` **(Many-Argument Workhorses)** (Impact: 61.5)
  * `data_sub_graph` **(Many-Argument Workhorses)** (Impact: 41.6)
    * *Intent:* """ Get a subgraph from the data graph or the simplified data graph that starts from node pv. :param...
  * `_handle_operation` **(Stateful Encapsulated Methods)** (Impact: 38.4)
  * `_track` **(Stateful Encapsulated Methods)** (Impact: 36.8)
    * *Intent:* """ Given all live definitions prior to this program point, track the changes, and return a new list...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 225 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 747
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 313`, `structural_boundaries: 216`, `args: 78`, `func_start: 75`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 3`, `state_mutation: 297`, `dead_code: 1`, `planned_debt: 10`, `fragile_debt: 2`
* *Architecture:* `api: 41`, `import: 10`
* *Defense:* `safety: 34`, `doc: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.691
  * `Choke Point (Betweenness):` 0.015807 | `Ripple Effect (Closeness):` 0.208706
  * `Imports (Out-Degree: 7):` __future__, angr.analyses, angr.code_location, angr.errors, angr.sim_variable, claripy, collections, logging...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `angr/analyses/reaching_definitions/engine_ail.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.666)
- **Top Global Matches:** file_cluster_6: 7.666, file_cluster_8: 12.298, file_cluster_4: 14.217
- **Magnitude:** 1641.76 | **LOC:** 1171 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **21**; blast radius 0.188; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.1%), Guard Balance (formerly Safety Score) (83.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.2906% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_handle_stmt_Return` **(Many-Argument Workhorses)** (Impact: 50.2)
  * `_handle_binop_Shr` **(Stateful Encapsulated Methods)** (Impact: 46.7)
  * `_handle_binop_Sar` **(Stateful Encapsulated Methods)** (Impact: 46.7)
  * `_handle_binop_Shl` **(Stateful Encapsulated Methods)** (Impact: 46.5)
  * `_handle_binop_Add` **(Stateful Encapsulated Methods)** (Impact: 41.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 225 instances
* *State Mutation (weighted view):* 785
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 357`, `structural_boundaries: 192`, `args: 63`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 335`, `dead_code: 2`, `planned_debt: 9`, `fragile_debt: 3`
* *Architecture:* `api: 54`, `import: 22`
* *Defense:* `safety: 32`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.188
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.120916
  * `Imports (Out-Degree: 15):` .function_handler, .rd_state, .subject, __future__, angr.ailment, angr.calling_conventions, angr.code_location, angr.engines.light...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `angr/analyses/variable_recovery/engine_base.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.739)
- **Top Global Matches:** file_cluster_8: 10.739, file_cluster_3: 16.972, file_cluster_6: 21.799
- **Magnitude:** 1638.28 | **LOC:** 1305 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 0.203; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.7%)
- **Documentation Coverage:** 79.4872% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_read_from_vvar` **(Many-Argument Workhorses)** (Impact: 112.3)
  * `_load` **(Many-Argument Workhorses)** (Impact: 107.6)
    * *Intent:* """ :param RichR richr_addr: :param size: :return: """
  * `_store_to_global` **(Many-Argument Workhorses)** (Impact: 95.3)
    * *Intent:* # TODO: Create a tv_sp.store.<bits>@N <: typevar type constraint for the stack pointer
  * `_assign_to_vvar` **(Many-Argument Workhorses)** (Impact: 82.7)
  * `_read_from_register` **(Many-Argument Workhorses)** (Impact: 70.7)
    * *Intent:* """ :param offset: :param size: :return: """
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 227 instances
* *State Mutation (weighted view):* 715
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 320`, `structural_boundaries: 116`, `args: 25`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 261`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 15`
* *Architecture:* `api: 13`, `import: 16`
* *Defense:* `safety: 39`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 2.8e-05 | `Ripple Effect (Closeness):` 0.101442
  * `Imports (Out-Degree: 12):` __future__, angr.ailment, angr.analyses.typehoon, angr.analyses.typehoon.typevars, angr.analyses.variable_recovery.variable_recovery_base, angr.code_location, angr.engines.light, angr.engines.light.engine...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `angr/analyses/decompiler/utils.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.48)
- **Top Global Matches:** file_cluster_4: 8.48, file_cluster_6: 10.872, file_cluster_12: 13.245
- **Magnitude:** 1592.86 | **LOC:** 1241 | **CtrlFlow:** 43.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **21**; blast radius 1.171; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (79.7%), Guard Balance (formerly Safety Score) (74.9%)
- **Documentation Coverage:** 79.3814% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decompile_functions` **(Many-Argument Workhorses)** (Impact: 120.8)
  * `insert_node` **(Many-Argument Workhorses)** (Impact: 107.1)
  * `switch_extract_bitwiseand_jumptable_info` **(Defensive Guards)** (Impact: 67.8)
    * *Intent:* """ Check the last statement of the switch-case header node (whose address is loaded from a jump tab...
  * `switch_extract_cmp_bounds_from_condition` **(Defensive Guards)** (Impact: 41.1)
    * *Intent:* # TODO: Add more operations if isinstance(cond, ailment.Expr.BinaryOp): op = cond.op op0, op1 = cond...
  * `switch_extract_switch_expr_from_jump_target` **(Defensive Guards)** (Impact: 38.3)
    * *Intent:* """ Extract the switch expression from the indirect jump target expression. :param target: The targe...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 221 instances
* *State Mutation (weighted view):* 673
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 387`, `structural_boundaries: 260`, `args: 52`, `func_start: 52`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 231`, `dead_code: 2`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 45`, `import: 22`
* *Defense:* `safety: 111`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.171
  * `Choke Point (Betweenness):` 0.003411 | `Ripple Effect (Closeness):` 0.139313
  * `Imports (Out-Degree: 13):` .seq_to_blocks, .structuring.structurer_nodes, __future__, angr, angr.ailment, angr.ailment.block, angr.analyses.decompiler.counters.call_counter, angr.analyses.decompiler.decompilation_options...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `angr/analyses/reaching_definitions/rd_initializer.py` (PYTHON) | Magnitude: 207.28 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 151, structural_boundaries: 49, core_var_decl: 41, branch: 37
- `tests/procedures/glibc/test_ctype_locale.py` (PYTHON) | Magnitude: 83.06 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 52, core_var_decl: 35, design_snake_case: 35, state_mutation: 32
- `angr/ailment/expression.py` (PYTHON) | Magnitude: 2238.46 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1632, structural_boundaries: 538, branch: 418, state_mutation: 336
- `angr/knowledge_base.py` (PYTHON) | Magnitude: 80.36 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 67, args: 16, func_start: 16
- `corpus_tests/conftest.py` (PYTHON) | Magnitude: 27.18 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 8, state_mutation: 6, core_var_decl: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `angr/exploration_techniques/memory_watcher.py` (PYTHON) | Magnitude: 36.6 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 10, branch: 5, state_mutation: 5
- `angr/angrdb/serializers/loader.py` (PYTHON) | Magnitude: 147.52 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 102, structural_boundaries: 45, branch: 31, core_var_decl: 30
- `angr/analyses/decompiler/semantic_naming/call_result_naming.py` (PYTHON) | Magnitude: 89.5 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 122, structural_boundaries: 36, branch: 20, state_mutation: 13
- `corpus_tests/test_corpus.py` (PYTHON) | Magnitude: 41.56 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 13, core_var_decl: 10, design_snake_case: 10
- `angr/analyses/decompiler/region_simplifiers/expr_folding.py` (PYTHON) | Magnitude: 847.26 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 565, branch: 163, structural_boundaries: 161, state_mutation: 132

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/regression/test_regression_memcmp_definite_size.py` (PYTHON) | Magnitude: 26.44 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 10, state_mutation: 7, core_var_decl: 7
- `tests/exploration_techniques/test_threading.py` (PYTHON) | Magnitude: 21.78 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 11, import: 6, state_mutation: 5
- `tests/llm/test_llm_client.py` (PYTHON) | Magnitude: 106.06 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 118, structural_boundaries: 60, test_skip: 55, state_mutation: 52
- `angr/misc/ansi.py` (PYTHON) | Magnitude: 31.48 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 11, core_var_decl: 11, state_mutation: 10, design_snake_case: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/utils/test_bits.py` (PYTHON) | Magnitude: 4.22 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 14, indent_spaces: 10, safety: 6, test: 5
- `angr/procedures/win32/is_bad_ptr.py` (PYTHON) | Magnitude: 13.0 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 15, safety: 6, api: 6
- `tests/storage/test_memory.py` (PYTHON) | Magnitude: 403.5 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 674, core_var_decl: 222, structural_boundaries: 217, design_snake_case: 217
- `native/unicornlib/sim_unicorn.hpp` (CPP) | Magnitude: 253.52 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 563, structural_boundaries: 153, pointers: 89, core_var_decl: 78
- `tests/procedures/posix/test_sim_time.py` (PYTHON) | Magnitude: 16.06 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 15, safety: 8, state_mutation: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `angr/analyses/propagator/engine_base.py` (PYTHON) | Magnitude: 34.58 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 22, state_mutation: 13, core_var_decl: 10
- `angr/analyses/deobfuscator/irsb_reg_collector.py` (PYTHON) | Magnitude: 42.24 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 30, indent_spaces: 29, api: 15, args: 14
- `tests/analyses/reaching_definitions/test_reachingdefinitions.py` (PYTHON) | Magnitude: 328.34 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 352, core_var_decl: 164, design_snake_case: 156, state_mutation: 130
- `angr/storage/memory_mixins/paged_memory/pages/ispo_mixin.py` (PYTHON) | Magnitude: 38.6 | Delta: **0.127** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 26, safety: 10, api: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `angr/storage/memory_mixins/paged_memory/pages/__init__.py` (PYTHON) | Magnitude: 17.46 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 20, indent_spaces: 11, import: 10, api: 1
- `angr/exploration_techniques/__init__.py` (PYTHON) | Magnitude: 19.02 | Delta: **0.132** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 48, indent_spaces: 25, import: 24, api: 1
- `angr/analyses/__init__.py` (PYTHON) | Magnitude: 19.28 | Delta: **0.155** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 104, indent_spaces: 60, import: 52, api: 1
- `angr/knowledge_plugins/__init__.py` (PYTHON) | Magnitude: 17.84 | Delta: **0.166** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 40, import: 20, indent_spaces: 20, api: 1
- `angr/analyses/cfg/indirect_jump_resolvers/__init__.py` (PYTHON) | Magnitude: 17.54 | Delta: **0.196** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 26, import: 13, indent_spaces: 12, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/sim/options/test_unsupported.py` (PYTHON) | Magnitude: 9.98 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 12, safety: 6, state_mutation: 5
- `angr/analyses/decompiler/peephole_optimizations/invert_negated_logical_conjuction_disjunction.py` (PYTHON) | Magnitude: 27.5 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 11, core_var_decl: 11, design_snake_case: 10
- `tests/analyses/cfg/test_cfg_manager.py` (PYTHON) | Magnitude: 14.52 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 12, state_mutation: 8, core_var_decl: 8
- `angr/procedures/java_lang/double.py` (PYTHON) | Magnitude: 17.3 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 9, state_mutation: 5, core_var_decl: 5
- `tests/state_plugins/test_callstack.py` (PYTHON) | Magnitude: 14.02 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 17, safety: 10, state_mutation: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `angr/analyses/loop_analysis/loop_analysis.py` (PYTHON) | Magnitude: 545.6 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 309, branch: 109, structural_boundaries: 102, state_mutation: 90
- `angr/analyses/decompiler/optimization_passes/eager_std_string_eval.py` (PYTHON) | Magnitude: 242.74 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 131, structural_boundaries: 53, branch: 51, state_mutation: 41
- `angr/knowledge_plugins/variables/variable_manager.py` (PYTHON) | Magnitude: 1766.3 | Delta: **0.149** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 981, branch: 336, state_mutation: 285, structural_boundaries: 244

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `angr/analyses/decompiler/semantic_naming/naming_base.py` (PYTHON) | Magnitude: 80.3 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 43, branch: 16, state_mutation: 13
- `angr/analyses/decompiler/peephole_optimizations/__init__.py` (PYTHON) | Magnitude: 21.78 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 129, indent_spaces: 66, import: 63, branch: 6
- `angr/knowledge_plugins/rtdb/rtdb.py` (PYTHON) | Magnitude: 224.2 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 146, structural_boundaries: 65, state_mutation: 42, core_var_decl: 40
- `angr/state_plugins/uc_manager.py` (PYTHON) | Magnitude: 66.8 | Delta: **0.143** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 23, state_mutation: 17, encapsulation: 10
- `angr/utils/algo.py` (PYTHON) | Magnitude: 32.44 | Delta: **0.206** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 9, branch: 6, state_mutation: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `angr/analyses/decompiler/optimization_passes/eager_std_string_concatenation.py` (PYTHON) | Magnitude: 236.28 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 163, structural_boundaries: 63, branch: 52, core_var_decl: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `angr/procedures/win_user32/messagebox.py` (PYTHON) | Magnitude: 49.38 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 20, api: 11, core_var_decl: 9
- `angr/knowledge_plugins/indirect_jumps.py` (PYTHON) | Magnitude: 34.92 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 9, state_mutation: 7, branch: 4
- `angr/exploration_techniques/local_loop_seer.py` (PYTHON) | Magnitude: 53.08 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 17, state_mutation: 11, branch: 7
- `angr/engines/__init__.py` (PYTHON) | Magnitude: 20.98 | Delta: **0.181** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 28, import: 12, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `angr/analyses/decompiler/clinic.py` (PYTHON) | Magnitude: 4037.0 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 2866, branch: 863, core_var_decl: 829, design_snake_case: 765

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tests/analyses/decompiler/test_dogbolt_regressions.py` (PYTHON) | Magnitude: 31.56 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 10, core_var_decl: 9, branch: 8
- `angr/engines/procedure.py` (PYTHON) | Magnitude: 61.1 | Delta: **0.125** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 16, state_mutation: 13, branch: 8

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/coverage.yml` -> Churn: **97.16%** | Cog Load: 5.8999% | Debt: 93.9456%
- `angr/analyses/cfg/cfg_base.py` -> Churn: **82.97%** | Cog Load: 64.9984% | Debt: 10.4636%
- `angr/analyses/cfg/cfg_fast.py` -> Churn: **75.72%** | Cog Load: 78.4621% | Debt: 14.1083%
- `angr/__main__.py` -> Churn: **67.23%** | Cog Load: 62.7436% | Debt: 0.0%
- `angr/analyses/decompiler/ail_simplifier.py` -> Churn: **63.57%** | Cog Load: 86.64% | Debt: 16.9801%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `angr/analyses/cfg/cfg_fast.py` -> **Fish** (84.6% isolated ownership) | Magnitude: 5851.88
- `angr/analyses/cfg/cfg_base.py` -> **Fish** (82.4% isolated ownership) | Magnitude: 3282.7
- `angr/analyses/bindiff.py` -> **pre-commit-ci[bot]** (100.0% isolated ownership) | Magnitude: 1894.08
- `angr/analyses/decompiler/region_identifier.py` -> **Fish** (100.0% isolated ownership) | Magnitude: 1592.06
- `angr/analyses/reaching_definitions/engine_vex.py` -> **Fish** (100.0% isolated ownership) | Magnitude: 1553.08

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `angr/analyses/analysis.py` -> **Severity: 4.359** (Bridge: 0.0436 * Flux: 100.0%)
- `angr/analyses/decompiler/clinic.py` -> **Severity: 3.662** (Bridge: 0.0366 * Flux: 100.0%)
- `angr/project.py` -> **Severity: 3.375** (Bridge: 0.0338 * Flux: 100.0%)
- `angr/__init__.py` -> **Severity: 2.275** (Bridge: 0.144 * Flux: 15.8061%)
- `angr/analyses/decompiler/optimization_passes/__init__.py` -> **Severity: 1.777** (Bridge: 0.0178 * Flux: 99.9008%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `angr/errors.py` -> **Severity: 29.383** (Embedded: 0.3209 * Error Risk: 91.5604%)
- `angr/sim_state.py` -> **Severity: 22.465** (Embedded: 0.274 * Error Risk: 81.9983%)
- `angr/project.py` -> **Severity: 21.983** (Embedded: 0.308 * Error Risk: 71.3694%)
- `angr/calling_conventions.py` -> **Severity: 21.551** (Embedded: 0.2831 * Error Risk: 76.1159%)
- `angr/sim_type.py` -> **Severity: 20.881** (Embedded: 0.2835 * Error Risk: 73.6426%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `angr/errors.py` -> **Severity: 4570.6** (Blast Radius: 45.706 * Doc Risk: 100.0%)
- `angr/sim_state.py` -> **Severity: 1638.273** (Blast Radius: 26.408 * Doc Risk: 62.037%)
- `angr/ailment/expression.py` -> **Severity: 1534.4** (Blast Radius: 15.344 * Doc Risk: 100.0%)
- `angr/knowledge_base.py` -> **Severity: 1443.62** (Blast Radius: 15.196 * Doc Risk: 95.0%)
- `angr/sim_type.py` -> **Severity: 1383.621** (Blast Radius: 15.323 * Doc Risk: 90.297%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 236 literal sites + 7 sites through wrappers = 243
- **`panics_and_aborts`:** 1722 literal sites + 11 sites through wrappers = 1733

- `_get_session` (function, panics_and_aborts, primitive): 11 call sites in 1 files -- `angr/mcp/server.py`
- `banner` (function, debug_prints, primitive): 6 call sites in 1 files -- `tests/analyses/decompiler/test_propagator_loops.py`
- `print_system_info` (function, debug_prints, primitive): 1 call sites in 1 files -- `angr/misc/bug_report.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 47496 call pairs -- scoped 36.3%, unique 0.0%, ambiguous 21.2%, external 42.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 46033 | 37.0% | 0.0% | 21.7% | 41.2% |
| rust | 906 | 5.1% | 0.0% | 5.2% | 89.7% |
| cpp | 430 | 26.7% | 0.0% | 2.1% | 71.2% |
| shell | 102 | 20.6% | 0.0% | 0.0% | 79.4% |
| c | 25 | 16.0% | 0.0% | 0.0% | 84.0% |

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
