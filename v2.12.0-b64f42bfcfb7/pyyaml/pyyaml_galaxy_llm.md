# ARCHITECTURAL_BRIEF: pyyaml
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
- **Scope:** 55 analyzed artifact(s), 8765 LOC.
- **Load-bearing artifact:** `pyyaml-6.0.3/tests/legacy_tests/test_appliance.py` -- 22 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `pyyaml-6.0.3/setup.py` -- pulls in 19 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `pyyaml-6.0.3/yaml/_yaml.pyx` at magnitude 1976.68 (structural weight, not risk).
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
| Total Artifacts | 634 |
| Analyzed Artifacts (Scanned) | 55 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 579 |
| Total LOC | 8765 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 8.7% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4532 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4171 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0784 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 49 | 8494 | 89.1% |
| PLAINTEXT | 2 | 0 | 3.6% |
| MAKEFILE | 1 | 36 | 1.8% |
| MARKDOWN | 1 | 0 | 1.8% |
| YAML | 1 | 227 | 1.8% |
| C | 1 | 8 | 1.8% |

## 4.1 SOURCE ENCODINGS
All 55 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 25%, Parameter Forwarders Files 25%, Large Core Modules (3) 15%, Declarative / Non-Code 11%, Compute Cores Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 52 | 94.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 5.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 579*

**Composition by Extension & Reason:**
- `.data`: 202x Excluded (Unsupported Extension: '.data')
- `no_extension`: 82x Excluded (Unsupported Extension: '.loader-error'), 16x Excluded (Unsupported Extension: '.emitter-error'), 6x Excluded (Unsupported Extension: '.dumper-error')
- `.canonical`: 91x Excluded (Unsupported Extension: '.canonical')
- `.code`: 55x Excluded (Unsupported Extension: '.code')
- `.structure`: 28x Excluded (Unsupported Extension: '.structure')
- `.tokens`: 28x Excluded (Unsupported Extension: '.tokens')
- `.error`: 13x Excluded (Unsupported Extension: '.error')
- `.detect`: 9x Excluded (Unsupported Extension: '.detect')
- `.skip-ext`: 7x Excluded (Unsupported Extension: '.skip-ext')
- `.empty`: 7x Excluded (Unsupported Extension: '.empty')
- `.events`: 6x Excluded (Unsupported Extension: '.events')
- `.recursive`: 5x Excluded (Unsupported Extension: '.recursive')
- `.unicode`: 3x Excluded (Unsupported Extension: '.unicode')
- `.cfg`: 2x Excluded (Unsupported Extension: '.cfg')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 96.0 | 39.4 | 35.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 90.0 | 63.4 | 67.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 14.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 88.9 | 39.9 | 42.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 35.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 94.2 | 4.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 81.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 100 | 18 | 8 | `pyyaml-6.0.3/lib/yaml/constructor.py` |
| cleanup | 5 | 4 | 0 | `pyyaml-6.0.3/lib/yaml/__init__.py` |
| guards | 393 | 34 | 21 | `pyyaml-6.0.3/lib/yaml/constructor.py` |
| danger | 433 | 41 | 17 | `pyyaml-6.0.3/yaml/_yaml.pyx` |
| concurrency | 32 | 7 | 1 | `pyyaml-6.0.3/examples/pygments-lexer/yaml.py` |
| connectivity | 646 | 44 | 34 | `pyyaml-6.0.3/lib/yaml/scanner.py` |
| io | 151 | 28 | 6 | `pyyaml-6.0.3/tests/legacy_tests/test_appliance.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 6 | 3 | 0 | `pyyaml-6.0.3/tests/legacy_tests/test_constructor.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 11 | 3 | 0 | `pyyaml-6.0.3/lib/yaml/resolver.py` |
| events | 43 | 10 | 2 | `pyyaml-6.0.3/examples/pygments-lexer/yaml.py` |
| tests | 111 | 22 | 7 | `pyyaml-6.0.3/tests/legacy_tests/test_yaml_ext.py` |
| docs | 53 | 7 | 2 | `pyyaml-6.0.3/lib/yaml/__init__.py` |
| debt | 140 | 27 | 8 | `pyyaml-6.0.3/tests/legacy_tests/test_schema.py` |
| mutation | 4484 | 48 | 171 | `pyyaml-6.0.3/yaml/_yaml.pyx` |
| dead_code | 86 | 14 | 5 | `pyyaml-6.0.3/yaml/_yaml.pyx` |
| credential | 0 | 0 | 0 | - |
| threat | 2 | 2 | 0 | `pyyaml-6.0.3/lib/yaml/emitter.py` |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5294**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pyyaml-6.0.3/tests/legacy_tests/test_appliance.py` (Hits: 34)
- `pyyaml-6.0.3/tests/legacy_tests/test_yaml_ext.py` (Hits: 19)
- `pyyaml-6.0.3/tests/legacy_tests/test_input_output.py` (Hits: 13)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **test_appliance.py** (`pyyaml-6.0.3/tests/legacy_tests/test_appliance.py`) — 22 inbound connections
2. **error.py** (`pyyaml-6.0.3/lib/yaml/error.py`) — 10 inbound connections
3. **nodes.py** (`pyyaml-6.0.3/lib/yaml/nodes.py`) — 6 inbound connections
4. **events.py** (`pyyaml-6.0.3/lib/yaml/events.py`) — 5 inbound connections
5. **resolver.py** (`pyyaml-6.0.3/lib/yaml/resolver.py`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **setup.py** (`pyyaml-6.0.3/setup.py`) — 19 outbound dependencies
2. **test_yaml.py** (`pyyaml-6.0.3/tests/legacy_tests/test_yaml.py`) — 17 outbound dependencies
3. **test_yaml_ext.py** (`pyyaml-6.0.3/tests/legacy_tests/test_yaml_ext.py`) — 14 outbound dependencies
4. **constructor.py** (`pyyaml-6.0.3/lib/yaml/constructor.py`) — 9 outbound dependencies
5. **__init__.py** (`pyyaml-6.0.3/lib/yaml/__init__.py`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_object_to_event` **(Many-Argument Workhorses)** (@ `pyyaml-6.0.3/yaml/_yaml.pyx`) -> Impact: **145.1** | LOC: 182
- `_serialize_node` **(Many-Argument Workhorses)** (@ `pyyaml-6.0.3/yaml/_yaml.pyx`) -> Impact: **109.3** | LOC: 128
- `analyze_scalar` **(Many-Argument Workhorses)** (@ `pyyaml-6.0.3/lib/yaml/emitter.py`) -> Impact: **92.8** | LOC: 159
  * *Intent:* # Empty scalar is a special case. if not scalar: return ScalarAnalysis(scalar=scalar, empty=True, multiline=False, allow_flow_plain=False, allow_block...
- `_event_to_object` **(Compute Cores)** (@ `pyyaml-6.0.3/yaml/_yaml.pyx`) -> Impact: **77.1** | LOC: 122
- `parse_node` **(Many-Argument Workhorses)** (@ `pyyaml-6.0.3/lib/yaml/parser.py`) -> Impact: **75.0** | LOC: 100
- `_token_to_object` **(Compute Cores)** (@ `pyyaml-6.0.3/yaml/_yaml.pyx`) -> Impact: **63.5** | LOC: 93
- `write_single_quoted` **(Many-Argument Workhorses)** (@ `pyyaml-6.0.3/lib/yaml/emitter.py`) -> Impact: **60.6** | LOC: 53
  * *Intent:* # Scalar streams.
- `write_double_quoted` **(Many-Argument Workhorses)** (@ `pyyaml-6.0.3/lib/yaml/emitter.py`) -> Impact: **54.6** | LOC: 53
- `write_plain` **(Many-Argument Workhorses)** (@ `pyyaml-6.0.3/lib/yaml/emitter.py`) -> Impact: **52.9** | LOC: 58
- `add_path_resolver` **(Many-Argument Workhorses)** (@ `pyyaml-6.0.3/lib/yaml/resolver.py`) -> Impact: **49.6** | LOC: 52
  * *Intent:* # Note: `add_path_resolver` is experimental. The API could be changed. # `new_path` is a pattern that is matched against the path from the # root to t...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pyyaml-6.0.3/lib/yaml` | 17 | 6888.72 | 58.1% | 30.9% |
| `pyyaml-6.0.3/tests/legacy_tests` | 24 | 2580.62 | 28.67% | 0.0% |
| `pyyaml-6.0.3/yaml` | 4 | 2021.16 | 23.25% | 2.79% |
| `pyyaml-6.0.3/examples/pygments-lexer` | 2 | 449.66 | 23.4% | 0.0% |
| `pyyaml-6.0.3` | 5 | 319.46 | 9.76% | 37.35% |
| `pyyaml-6.0.3/examples/yaml-highlight` | 1 | 190.28 | 77.4% | 0.0% |
| `pyyaml-6.0.3/packaging` | 1 | 41.02 | 85.81% | 0.0% |
| `pyyaml-6.0.3/lib/_yaml` | 1 | 20.36 | 21.08% | 18.24% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `pyyaml-6.0.3/lib/yaml/__init__.py` -> **99.9998%** Exposure
- `pyyaml-6.0.3/Makefile` -> **99.9925%** Exposure
- `pyyaml-6.0.3/lib/yaml/loader.py` -> **99.9447%** Exposure
- `pyyaml-6.0.3/lib/yaml/tokens.py` -> **99.9083%** Exposure
- `pyyaml-6.0.3/lib/yaml/dumper.py` -> **99.9027%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `pyyaml-6.0.3/lib/yaml/composer.py` -> **100.0%** Exposure
- `pyyaml-6.0.3/lib/yaml/constructor.py` -> **100.0%** Exposure
- `pyyaml-6.0.3/lib/yaml/emitter.py` -> **100.0%** Exposure
- `pyyaml-6.0.3/lib/yaml/error.py` -> **100.0%** Exposure
- `pyyaml-6.0.3/lib/yaml/events.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pyyaml-6.0.3/lib/yaml/__init__.py` -> **20** Orphaned Functions | **0** Duplicates
- `pyyaml-6.0.3/tests/legacy_tests/test_constructor.py` -> **0** Orphaned Functions | **9** Duplicates
- `pyyaml-6.0.3/tests/legacy_tests/conftest.py` -> **5** Orphaned Functions | **2** Duplicates
- `pyyaml-6.0.3/Makefile` -> **6** Orphaned Functions | **0** Duplicates
- `pyyaml-6.0.3/setup.py` -> **5** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `179` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `pyyaml-6.0.3/yaml/_yaml.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.695)
- **Top Global Matches:** file_cluster_4: 5.695, file_cluster_6: 9.583, file_cluster_12: 11.883
- **Magnitude:** 1976.68 | **LOC:** 1398 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 15.099; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.0%), Guard Balance (formerly Safety Score) (88.1%), Connectivity (formerly Api Exposure) (56.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_object_to_event` **(Many-Argument Workhorses)** (Impact: 145.1)
  * `_serialize_node` **(Many-Argument Workhorses)** (Impact: 109.3)
  * `_event_to_object` **(Compute Cores)** (Impact: 77.1)
  * `_token_to_object` **(Compute Cores)** (Impact: 63.5)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 48.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 365 instances
* *State Mutation (weighted view):* 1173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 160`, `args: 43`, `func_start: 43`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 443`, `dead_code: 23`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 21`, `import: 1`
* *Defense:* `safety: 5`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.035613
  * `Imports (Out-Degree: 0):` yaml
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/lib/yaml/emitter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.544)
- **Top Global Matches:** file_cluster_6: 5.544, file_cluster_4: 11.7, file_cluster_8: 13.342
- **Magnitude:** 1852.76 | **LOC:** 1138 | **CtrlFlow:** 42.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 12.772; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.6%), Complexity Load (formerly Cognitive Load) (84.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `analyze_scalar` **(Many-Argument Workhorses)** (Impact: 92.8)
    * *Intent:* # Empty scalar is a special case. if not scalar: return ScalarAnalysis(scalar=scalar, empty=True, mu...
  * `write_single_quoted` **(Many-Argument Workhorses)** (Impact: 60.6)
    * *Intent:* # Scalar streams.
  * `write_double_quoted` **(Many-Argument Workhorses)** (Impact: 54.6)
  * `write_plain` **(Many-Argument Workhorses)** (Impact: 52.9)
  * `write_folded` **(Compute Cores)** (Impact: 49.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 287 instances
* *State Mutation (weighted view):* 914
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 407`, `structural_boundaries: 103`, `args: 60`, `func_start: 60`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 340`
* *Architecture:* `api: 62`, `import: 2`
* *Defense:* `safety: 35`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.772
  * `Choke Point (Betweenness):` 0.000262 | `Ripple Effect (Closeness):` 0.024691
  * `Imports (Out-Degree: 2):` .error, .events
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/lib/yaml/scanner.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.759)
- **Top Global Matches:** file_cluster_4: 6.759, file_cluster_12: 9.397, file_cluster_15: 10.811
- **Magnitude:** 1456.26 | **LOC:** 1436 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 14.493; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.9%)
- **Documentation Coverage:** 99.2958% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetch_more_tokens` **(Compute Cores)** (Impact: 49.1)
    * *Intent:* # Eat whitespaces and comments until we reach the next token. self.scan_to_next_token() # Remove obs...
  * `scan_flow_scalar_non_spaces` **(Many-Argument Workhorses)** (Impact: 46.1)
    * *Intent:* # See the specification for details. chunks = [] while True: length = 0 while self.peek(length) not ...
  * `scan_block_scalar` **(Many-Argument Workhorses)** (Impact: 38.4)
    * *Intent:* # See the specification for details. if style == '>': folded = True else: folded = False chunks = []...
  * `scan_plain_spaces` **(Many-Argument Workhorses)** (Impact: 31.8)
    * *Intent:* # See the specification for details. # The specification is really confusing about tabs in plain sca...
  * `scan_block_scalar_indicators` **(Compute Cores)** (Impact: 29.7)
    * *Intent:* # See the specification for details. chomping = None increment = None ch = self.peek() if ch in '+-'...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 206 instances
* *State Mutation (weighted view):* 688
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 301`, `structural_boundaries: 162`, `args: 72`, `func_start: 72`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 276`, `dead_code: 10`, `planned_debt: 2`
* *Architecture:* `api: 74`, `import: 2`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.493
  * `Choke Point (Betweenness):` 0.000233 | `Ripple Effect (Closeness):` 0.041667
  * `Imports (Out-Degree: 2):` .error, .tokens
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/lib/yaml/constructor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.824)
- **Top Global Matches:** file_cluster_12: 7.824, file_cluster_7: 9.192, file_cluster_4: 10.179
- **Magnitude:** 865.7 | **LOC:** 749 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 20.321; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (78.7%), Complexity Load (formerly Cognitive Load) (77.9%)
- **Documentation Coverage:** 98.2301% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `construct_object` **(Many-Argument Workhorses)** (Impact: 46.5)
  * `flatten_mapping` **(Defensive Guards)** (Impact: 31.1)
  * `set_python_instance_state` **(Defensive Guards)** (Impact: 27.7)
  * `make_python_instance` **(Defensive Guards)** (Impact: 26.2)
  * `find_python_name` **(Defensive Guards)** (Impact: 25.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 374
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 131`, `args: 51`, `func_start: 51`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 146`
* *Architecture:* `io: 4`, `api: 58`, `import: 5`
* *Defense:* `safety: 42`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.321
  * `Choke Point (Betweenness):` 0.00198 | `Ripple Effect (Closeness):` 0.083333
  * `Imports (Out-Degree: 2):` .error, .nodes, base64, binascii, collections.abc, datetime, re, sys...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/lib/yaml/parser.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.768)
- **Top Global Matches:** file_cluster_12: 6.768, file_cluster_4: 8.216, file_cluster_15: 8.432
- **Magnitude:** 734.74 | **LOC:** 590 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 11.953; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_node` **(Many-Argument Workhorses)** (Impact: 75.0)
  * `parse_flow_mapping_key` **(Compute Cores)** (Impact: 20.4)
  * `process_directives` **(Compute Cores)** (Impact: 17.1)
  * `parse_flow_sequence_entry` **(Compute Cores)** (Impact: 16.8)
  * `check_event` **(Defensive Guards)** (Impact: 12.7)
    * *Intent:* # Check the type of the next event. if self.current_event is None: if self.state: self.current_event...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 131 instances
* *State Mutation (weighted view):* 445
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 95`, `args: 31`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 183`, `dead_code: 1`
* *Architecture:* `api: 34`, `import: 4`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.953
  * `Choke Point (Betweenness):` 0.000408 | `Ripple Effect (Closeness):` 0.024691
  * `Imports (Out-Degree: 4):` .error, .events, .scanner, .tokens
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/lib/yaml/representer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.489)
- **Top Global Matches:** file_cluster_12: 7.489, file_cluster_7: 8.481, file_cluster_5: 9.89
- **Magnitude:** 512.66 | **LOC:** 390 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 15.231; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.0%), Guard Balance (formerly Safety Score) (85.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `represent_object` **(Defensive Guards)** (Impact: 44.6)
    * *Intent:* # We use __reduce__ API to save the data. data.__reduce__ returns # a tuple of length 2-5: # (functi...
  * `represent_mapping` **(Defensive Guards)** (Impact: 28.2)
  * `represent_data` **(Compute Cores)** (Impact: 24.1)
  * `represent_sequence` **(Many-Argument Workhorses)** (Impact: 18.7)
  * `represent_float` **(Compute Cores)** (Impact: 16.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 79 instances
* *State Mutation (weighted view):* 254
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 75`, `args: 29`, `func_start: 29`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 96`, `dead_code: 8`
* *Architecture:* `api: 34`, `import: 3`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.231
  * `Choke Point (Betweenness):` 0.000379 | `Ripple Effect (Closeness):` 0.041667
  * `Imports (Out-Degree: 2):` .error, .nodes, base64, collections, copyreg, datetime, types
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/canonical.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.816)
- **Top Global Matches:** file_cluster_12: 6.816, file_cluster_15: 7.739, file_cluster_4: 8.014
- **Magnitude:** 433.98 | **LOC:** 362 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 20.857; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (79.0%), Connectivity (formerly Api Exposure) (71.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (37.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `scan` **(Compute Cores)** (Impact: 27.6)
  * `scan_scalar` **(Compute Cores)** (Impact: 17.5)
  * `parse_node` **(Compute Cores)** (Impact: 15.1)
    * *Intent:* # node: ALIAS | ANCHOR? TAG? (SCALAR|sequence|mapping)
  * `check_token` **(Defensive Guards)** (Impact: 10.9)
  * `check_event` **(Defensive Guards)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 59`, `args: 30`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 85`
* *Architecture:* `api: 31`, `import: 1`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.857
  * `Choke Point (Betweenness):` 0.015374 | `Ripple Effect (Closeness):` 0.062378
  * `Imports (Out-Degree: 3):` yaml, yaml.composer, yaml.constructor, yaml.resolver
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/examples/pygments-lexer/yaml.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.977)
- **Top Global Matches:** file_cluster_9: 8.977, file_cluster_12: 10.235, file_cluster_7: 11.771
- **Magnitude:** 430.12 | **LOC:** 432 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 10.314; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (82.8%), Guard Balance (formerly Safety Score) (76.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (42.2%)
- **Documentation Coverage:** 55.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `callback` **(Compute Cores)** (Impact: 26.9)
  * `save_indent` **(Compute Cores)** (Impact: 23.6)
    * *Intent:* """Save a possible indentation level."""
  * `callback` **(Compute Cores)** (Impact: 22.6)
  * `callback` **(Compute Cores)** (Impact: 20.8)
  * `parse_block_scalar_empty_line` **(Compute Cores)** (Impact: 19.9)
    * *Intent:* """Process an empty line in a block scalar."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 145
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 38`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 53`
* *Architecture:* `api: 21`, `import: 2`
* *Defense:* `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pygments.lexer, pygments.token
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyyaml-6.0.3/tests/legacy_tests/test_constructor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.441)
- **Top Global Matches:** file_cluster_12: 6.441, file_cluster_15: 8.885, file_cluster_7: 9.257
- **Magnitude:** 330.16 | **LOC:** 305 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 18.333; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (73.2%), Guard Balance (formerly Safety Score) (70.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (47.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_make_objects` **(C Struct Operations)** (Impact: 25.9)
  * `_serialize_value` **(Stateful Encapsulated Methods)** (Impact: 12.2)
  * `test_constructor_types` **(Defensive Guards)** (Impact: 11.4)
  * `test_subclass_blacklist_types` **(Defensive Guards)** (Impact: 5.7)
  * `__eq__` **(Defensive Guards)** (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 153`, `args: 51`, `func_start: 51`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 75`, `duplicate_logic: 9`
* *Architecture:* `io: 5`, `api: 36`, `import: 7`
* *Defense:* `safety: 15`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.333
  * `Choke Point (Betweenness):` 0.002446 | `Ripple Effect (Closeness):` 0.075617
  * `Imports (Out-Degree: 2):` datetime, pprint, signal, sys, test_appliance, test_constructor, yaml, yaml.tokens
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/lib/yaml/resolver.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.597)
- **Top Global Matches:** file_cluster_8: 10.597, file_cluster_6: 15.389, file_cluster_4: 23.233
- **Magnitude:** 293.56 | **LOC:** 228 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 22.779; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.0%), Complexity Load (formerly Cognitive Load) (62.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_path_resolver` **(Many-Argument Workhorses)** (Impact: 49.6)
    * *Intent:* # Note: `add_path_resolver` is experimental. The API could be changed. # `new_path` is a pattern tha...
  * `check_resolver_prefix` **(Defensive Guards)** (Impact: 43.4)
  * `resolve` **(Compute Cores)** (Impact: 32.5)
  * `descend_resolver` **(Compute Cores)** (Impact: 23.1)
  * `add_implicit_resolver` **(Many-Argument Workhorses)** (Impact: 11.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 32`, `args: 7`, `func_start: 7`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 44`
* *Architecture:* `api: 11`, `import: 3`
* *Defense:* `safety: 9`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.779
  * `Choke Point (Betweenness):` 0.002184 | `Ripple Effect (Closeness):` 0.094837
  * `Imports (Out-Degree: 2):` .error, .nodes, re
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_yaml_ext.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.704)
- **Top Global Matches:** file_cluster_12: 6.704, file_cluster_15: 7.568, file_cluster_16: 8.456
- **Magnitude:** 292.84 | **LOC:** 295 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **14**; blast radius 18.863; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (65.0%), Connectivity (formerly Api Exposure) (57.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (46.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_compare_emitters` **(Stateful Encapsulated Methods)** (Impact: 22.3)
  * `_compare_scanners` **(Stateful Encapsulated Methods)** (Impact: 13.2)
  * `wrap_ext` **(Defensive Guards)** (Impact: 12.0)
  * `_compare_parsers` **(Stateful Encapsulated Methods)** (Impact: 10.9)
  * `test_large_file` **(Type Conversions)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 100`, `args: 29`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 100`
* *Architecture:* `io: 19`, `api: 24`, `import: 5`
* *Defense:* `safety: 30`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.863
  * `Choke Point (Betweenness):` 0.009434 | `Ripple Effect (Closeness):` 0.041667
  * `Imports (Out-Degree: 7):` _yaml, os, pprint, sys, tempfile, test_appliance, test_constructor, test_errors...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/setup.py` (PYTHON | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.503)
- **Top Global Matches:** file_cluster_12: 6.503, file_cluster_7: 8.315, file_cluster_5: 9.751
- **Magnitude:** 292.48 | **LOC:** 360 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 10.314; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (86.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.3%)
- **Documentation Coverage:** 70.918% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 12.1)
  * `finalize_options` **(Compute Cores)** (Impact: 11.1)
  * `run` **(Defensive Guards)** (Impact: 11.0)
  * `get_source_files` **(Compute Cores)** (Impact: 10.6)
  * `__init__` **(Defensive Guards)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 176
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 65`, `args: 13`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 70`, `fragile_debt: 2`, `unreferenced_by_name: 5`
* *Architecture:* `io: 9`, `api: 16`, `import: 12`
* *Defense:* `safety: 18`, `doc: 2`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Cython.Distutils, Cython.Distutils.extension, Cython.Distutils.old_build_ext, _pyyaml_pep517, distutils, distutils.errors, json, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyyaml-6.0.3/lib/yaml/__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.832)
- **Top Global Matches:** file_cluster_12: 5.832, file_cluster_7: 7.953, file_cluster_15: 9.056
- **Magnitude:** 262.46 | **LOC:** 391 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 10.314; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.1%)
- **Documentation Coverage:** 19.2982% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dump_all` **(Many-Argument Workhorses)** (Impact: 26.3)
  * `serialize_all` **(Many-Argument Workhorses)** (Impact: 23.9)
  * `__init__` **(Defensive Guards)** (Impact: 13.9)
  * `emit` **(Many-Argument Workhorses)** (Impact: 13.0)
  * `add_implicit_resolver` **(Many-Argument Workhorses)** (Impact: 8.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 65`, `args: 29`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 28`, `fragile_debt: 1`, `unreferenced_by_name: 20`
* *Architecture:* `io: 2`, `api: 30`, `import: 8`
* *Defense:* `safety: 21`, `doc: 29`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` .cyaml, .dumper, .error, .events, .loader, .nodes, .tokens, io
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyyaml-6.0.3/tests/legacy_tests/test_appliance.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.983)
- **Top Global Matches:** file_cluster_8: 10.983, file_cluster_6: 19.473, file_cluster_3: 21.5
- **Magnitude:** 240.98 | **LOC:** 149 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **7**; blast radius 168.608; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (84.0%), Connectivity (formerly Api Exposure) (63.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (42.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `display` **(Compute Cores)** (Impact: 29.7)
  * `run` **(Compute Cores)** (Impact: 29.2)
  * `execute` **(Defensive Guards)** (Impact: 17.2)
  * `parse_arguments` **(Compute Cores)** (Impact: 12.4)
  * `find_test_functions` **(Defensive Guards)** (Impact: 10.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 22`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 43`
* *Architecture:* `io: 34`, `api: 6`, `import: 1`
* *Defense:* `safety: 6`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 168.608
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.408179
  * `Imports (Out-Degree: 0):` os, os.path, pathlib, pprint, sys, traceback, types
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/lib/yaml/reader.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.096)
- **Top Global Matches:** file_cluster_15: 6.096, file_cluster_9: 7.609, file_cluster_16: 8.168
- **Magnitude:** 235.12 | **LOC:** 186 | **CtrlFlow:** 26.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 16.738; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update` **(Defensive Guards)** (Impact: 17.1)
  * `forward` **(Compute Cores)** (Impact: 12.8)
  * `determine_encoding` **(Defensive Guards)** (Impact: 12.0)
  * `check_printable` **(Compute Cores)** (Impact: 10.7)
  * `__init__` **(Defensive Guards)** (Impact: 8.3)
    * *Intent:* # Reader: # - determines the data encoding and converts it to a unicode string, # - checks if charac...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 26`, `args: 11`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 54`, `fragile_debt: 1`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.738
  * `Choke Point (Betweenness):` 0.001805 | `Ripple Effect (Closeness):` 0.056713
  * `Imports (Out-Degree: 1):` .error, codecs, re
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_structure.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.082)
- **Top Global Matches:** file_cluster_12: 7.082, file_cluster_16: 8.918, file_cluster_15: 9.322
- **Magnitude:** 193.94 | **LOC:** 200 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 13.548; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (44.7%), Connectivity (formerly Api Exposure) (43.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_compare_events` **(Stateful Encapsulated Methods)** (Impact: 18.6)
  * `_convert_structure` **(Stateful Encapsulated Methods)** (Impact: 18.4)
  * `test_structure` **(Defensive Guards)** (Impact: 11.2)
  * `_compare_nodes` **(Stateful Encapsulated Methods)** (Impact: 11.0)
  * `test_composer` **(Defensive Guards)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 22 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 68`, `args: 18`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 39`, `duplicate_logic: 4`
* *Architecture:* `io: 10`, `api: 13`, `import: 3`
* *Defense:* `safety: 27`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.548
  * `Choke Point (Betweenness):` 0.009783 | `Ripple Effect (Closeness):` 0.060606
  * `Imports (Out-Degree: 2):` canonical, pprint, test_appliance, yaml
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/examples/yaml-highlight/yaml_hl.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.17)
- **Top Global Matches:** file_cluster_8: 9.17, file_cluster_6: 10.676, file_cluster_4: 18.632
- **Magnitude:** 190.28 | **LOC:** 115 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 10.314; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (90.0%), Complexity Load (formerly Cognitive Load) (77.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (5.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `highlight` **(Compute Cores)** (Impact: 25.0)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 22.2)
  * `__init__` **(Compute Cores)** (Impact: 9.2)
  * `__setstate__` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 9`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 43`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 3`, `import: 1`
* *Defense:* `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` codecs, optparse, os.path, sys, yaml
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyyaml-6.0.3/lib/yaml/composer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.512)
- **Top Global Matches:** file_cluster_12: 6.512, file_cluster_7: 6.959, file_cluster_5: 9.047
- **Magnitude:** 170.84 | **LOC:** 140 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 17.863; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compose_node` **(Compute Cores)** (Impact: 17.2)
  * `compose_mapping_node` **(Compute Cores)** (Impact: 9.8)
  * `compose_sequence_node` **(Compute Cores)** (Impact: 9.5)
  * `compose_scalar_node` **(Compute Cores)** (Impact: 7.4)
  * `get_single_node` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* # Drop the STREAM-START event. self.get_event() # Compose a document if the stream is not empty. doc...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 27`, `args: 9`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 38`, `dead_code: 1`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.863
  * `Choke Point (Betweenness):` 0.005125 | `Ripple Effect (Closeness):` 0.072282
  * `Imports (Out-Degree: 3):` .error, .events, .nodes
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/conftest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.141)
- **Top Global Matches:** file_cluster_12: 7.141, file_cluster_7: 9.029, file_cluster_5: 9.976
- **Magnitude:** 145.44 | **LOC:** 133 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 10.314; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (72.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (44.0%), Connectivity (formerly Api Exposure) (7.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 18.6)
  * `collect` **(Compute Cores)** (Impact: 16.7)
  * `pytest_ignore_collect` **(Compute Cores)** (Impact: 10.7)
  * `pytest_pycollect_makeitem` **(Compute Cores)** (Impact: 8.9)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 36`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 24`, `duplicate_logic: 2`, `unreferenced_by_name: 5`
* *Architecture:* `io: 4`, `api: 10`, `import: 6`
* *Defense:* `safety: 3`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` os, pathlib, pytest, test_appliance, warnings, yaml
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyyaml-6.0.3/tests/legacy_tests/test_input_output.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.155)
- **Top Global Matches:** file_cluster_9: 7.155, file_cluster_15: 9.475, file_cluster_16: 9.923
- **Magnitude:** 145.24 | **LOC:** 142 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 11.258; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (41.1%), Complexity Load (formerly Cognitive Load) (33.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_unicode_output` **(Defensive Guards)** (Impact: 17.2)
  * `test_unicode_transfer` **(Defensive Guards)** (Impact: 13.1)
  * `test_unicode_input_errors` **(Defensive Guards)** (Impact: 11.5)
  * `test_unicode_input` **(Defensive Guards)** (Impact: 6.1)
  * `test_file_output` **(Defensive Guards)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 47`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 37`
* *Architecture:* `io: 13`, `api: 5`, `import: 3`
* *Defense:* `safety: 27`, `test: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.258
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` codecs, io, os, os.path, tempfile, test_appliance, yaml
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_schema.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.303)
- **Top Global Matches:** file_cluster_6: 8.303, file_cluster_4: 12.006, file_cluster_8: 16.294
- **Magnitude:** 138.08 | **LOC:** 153 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 11.258; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (67.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (37.8%), Connectivity (formerly Api Exposure) (33.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_implicit_resolver` **(Many-Argument Workhorses)** (Impact: 46.6)
    * *Intent:* # The tests/data/yaml11.schema file is copied from # https://github.com/perlpunk/yaml-test-schema/bl...
  * `check_float` **(Compute Cores)** (Impact: 16.4)
  * `check_bool` **(Compute Cores)** (Impact: 9.1)
  * `check_int` **(Type Conversions)** (Impact: 3.8)
  * `check_str` **(Parameter Forwarders)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 35`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 17`, `dead_code: 1`
* *Architecture:* `io: 4`, `api: 5`, `import: 5`
* *Defense:* `safety: 3`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.258
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.037037
  * `Imports (Out-Degree: 1):` math, pprint, sys, test_appliance, yaml
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_emitter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.844)
- **Top Global Matches:** file_cluster_12: 8.844, file_cluster_9: 10.02, file_cluster_16: 11.145
- **Magnitude:** 135.1 | **LOC:** 105 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 17.016; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (68.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (43.6%), Complexity Load (formerly Cognitive Load) (39.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_emitter_styles` **(Defensive Guards)** (Impact: 19.2)
  * `construct_event` **(Defensive Guards)** (Impact: 13.0)
  * `_compare_events` **(Stateful Encapsulated Methods)** (Impact: 11.0)
  * `test_emitter_on_canonical` **(Type Conversions)** (Impact: 5.7)
  * `test_emitter_on_data` **(Type Conversions)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 24`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 24`
* *Architecture:* `io: 4`, `api: 6`, `import: 2`
* *Defense:* `safety: 13`, `test: 7`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.016
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.064815
  * `Imports (Out-Degree: 1):` test_appliance, yaml
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/lib/yaml/serializer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.371)
- **Top Global Matches:** file_cluster_12: 8.371, file_cluster_7: 8.372, file_cluster_5: 10.128
- **Magnitude:** 115.4 | **LOC:** 112 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 15.231; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.6%), Complexity Load (formerly Cognitive Load) (70.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `serialize_node` **(Many-Argument Workhorses)** (Impact: 19.5)
  * `anchor_node` **(Defensive Guards)** (Impact: 14.5)
  * `open` **(Compute Cores)** (Impact: 6.1)
  * `serialize` **(Compute Cores)** (Impact: 5.8)
    * *Intent:* #def __del__(self): # self.close()
  * `close` **(Compute Cores)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 17`, `args: 7`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 26`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 10`, `import: 3`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.231
  * `Choke Point (Betweenness):` 0.000903 | `Ripple Effect (Closeness):` 0.041667
  * `Imports (Out-Degree: 3):` .error, .events, .nodes
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/lib/yaml/error.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.337)
- **Top Global Matches:** file_cluster_12: 7.337, file_cluster_7: 9.225, file_cluster_15: 9.674
- **Magnitude:** 104.2 | **LOC:** 76 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); blast radius 74.09; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.8%), Complexity Load (formerly Cognitive Load) (75.2%), Connectivity (formerly Api Exposure) (61.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_snippet` **(Compute Cores)** (Impact: 17.1)
  * `__str__` **(Type Conversions)** (Impact: 16.4)
  * `__init__` **(Parameter Forwarders)** (Impact: 3.2)
  * `__str__` **(Parameter Forwarders)** (Impact: 3.2)
  * `__init__` **(Parameter Forwarders)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 15`, `args: 5`, `func_start: 5`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 27`
* *Architecture:* `api: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 74.09
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.192084
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/lib/yaml/tokens.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.294)
- **Top Global Matches:** file_cluster_15: 5.294, file_cluster_11: 7.419, file_cluster_2: 7.512
- **Magnitude:** 97.98 | **LOC:** 105 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); blast radius 28.058; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Complexity Load (formerly Cognitive Load) (90.5%), Connectivity (formerly Api Exposure) (88.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__repr__` **(Compute Cores)** (Impact: 6.0)
  * `__init__` **(Parameter Forwarders)** (Impact: 2.9)
  * `__init__` **(Parameter Forwarders)** (Impact: 2.7)
  * `__init__` **(Parameter Forwarders)** (Impact: 2.5)
  * `__init__` **(Parameter Forwarders)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 30`, `args: 8`, `func_start: 8`, `class_start: 21`
* *Risk/State:* `state_mutation: 45`, `dead_code: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 22`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.106667
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `pyyaml-6.0.3/lib/yaml/serializer.py` (PYTHON) | Magnitude: 115.4 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 89, state_mutation: 26, branch: 21, structural_boundaries: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `pyyaml-6.0.3/tests/legacy_tests/test_dump_load.py` (PYTHON) | Magnitude: 16.08 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 10, test: 6, safety: 5
- `pyyaml-6.0.3/tests/legacy_tests/test_sort_keys.py` (PYTHON) | Magnitude: 19.5 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 12, state_mutation: 7, core_var_decl: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `pyyaml-6.0.3/lib/yaml/composer.py` -> **Severity: 0.513** (Bridge: 0.0051 * Flux: 100.0%)
- `pyyaml-6.0.3/lib/yaml/resolver.py` -> **Severity: 0.218** (Bridge: 0.0022 * Flux: 100.0%)
- `pyyaml-6.0.3/lib/yaml/constructor.py` -> **Severity: 0.198** (Bridge: 0.002 * Flux: 100.0%)
- `pyyaml-6.0.3/lib/yaml/reader.py` -> **Severity: 0.18** (Bridge: 0.0018 * Flux: 100.0%)
- `pyyaml-6.0.3/lib/yaml/serializer.py` -> **Severity: 0.09** (Bridge: 0.0009 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pyyaml-6.0.3/tests/legacy_tests/test_appliance.py` -> **Severity: 34.299** (Embedded: 0.4082 * Error Risk: 84.0289%)
- `pyyaml-6.0.3/lib/yaml/error.py` -> **Severity: 15.515** (Embedded: 0.1921 * Error Risk: 80.7725%)
- `pyyaml-6.0.3/lib/yaml/events.py` -> **Severity: 8.92** (Embedded: 0.1115 * Error Risk: 80.0%)
- `pyyaml-6.0.3/lib/yaml/tokens.py` -> **Severity: 7.861** (Embedded: 0.1067 * Error Risk: 73.6975%)
- `pyyaml-6.0.3/lib/yaml/nodes.py` -> **Severity: 7.745** (Embedded: 0.1224 * Error Risk: 63.2477%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pyyaml-6.0.3/tests/legacy_tests/test_appliance.py` -> **Severity: 16860.8** (Blast Radius: 168.608 * Doc Risk: 100.0%)
- `pyyaml-6.0.3/lib/yaml/error.py` -> **Severity: 7409.0** (Blast Radius: 74.09 * Doc Risk: 100.0%)
- `pyyaml-6.0.3/lib/yaml/nodes.py` -> **Severity: 4573.4** (Blast Radius: 45.734 * Doc Risk: 100.0%)
- `pyyaml-6.0.3/lib/yaml/events.py` -> **Severity: 2891.2** (Blast Radius: 28.912 * Doc Risk: 100.0%)
- `pyyaml-6.0.3/lib/yaml/tokens.py` -> **Severity: 2805.8** (Blast Radius: 28.058 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 107 literal sites + 5 sites through wrappers = 112

- `_fail` (function, debug_prints, primitive): 5 call sites in 1 files -- `pyyaml-6.0.3/tests/legacy_tests/test_schema.py`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2169 call pairs -- scoped 33.1%, unique 0.0%, ambiguous 13.0%, external 54.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 2169 | 33.1% | 0.0% | 13.0% | 54.0% |

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
