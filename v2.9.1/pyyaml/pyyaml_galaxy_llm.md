# ARCHITECTURAL_BRIEF: pyyaml
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 36 analyzed artifact(s), 4448 LOC.
- **Load-bearing artifact:** `pyyaml-6.0.3/examples/pygments-lexer/yaml.py` -- 21 in-repo importer(s) depend on it. Changes here propagate furthest.
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
| Total Artifacts | 616 |
| Analyzed Artifacts (Scanned) | 36 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 580 |
| Total LOC | 4448 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 5.8% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1595 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6743 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.582 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 30 | 4177 | 83.3% |
| PLAINTEXT | 2 | 0 | 5.6% |
| MAKEFILE | 1 | 36 | 2.8% |
| MARKDOWN | 1 | 0 | 2.8% |
| YAML | 1 | 227 | 2.8% |
| C | 1 | 8 | 2.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `1.468`
> **Composition Archetype:** `Small Flat Repo (2)` (z +1.47; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 33%, Parameter Forwarders Files 17%, Data / Markup / Trivial 14%, Declarative / Non-Code 11%, Large Core Modules (3) 11%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 33 | 91.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 8.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 580*

**Composition by Extension & Reason:**
- `.data`: 133x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 69x Excluded (Unsupported Extension: '.data')
- `no_extension`: 82x Excluded (Unsupported Extension: '.loader-error'), 16x Excluded (Unsupported Extension: '.emitter-error'), 6x Excluded (Unsupported Extension: '.dumper-error')
- `.canonical`: 86x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Unsupported Extension: '.canonical')
- `.code`: 55x Excluded (Unsupported Extension: '.code')
- `.structure`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tokens`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.error`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.detect`: 9x Excluded (Unsupported Extension: '.detect')
- `.skip-ext`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Unsupported Extension: '.skip-ext')
- `.empty`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.empty')
- `.events`: 6x Excluded (Unsupported Extension: '.events')
- `.recursive`: 5x Excluded (Unsupported Extension: '.recursive')
- `.unicode`: 3x Excluded (Unsupported Extension: '.unicode')
- `.cfg`: 2x Excluded (Unsupported Extension: '.cfg')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 93.0 | 31.7 | 32.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 72.1 | 79.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 82.4 | 30.3 | 32.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 21.0 | 1.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 78.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 58 | 12 | 8 | `pyyaml-6.0.3/tests/legacy_tests/test_structure.py` |
| cleanup | 3 | 3 | 0 | `pyyaml-6.0.3/Makefile` |
| guards | 251 | 24 | 20 | `pyyaml-6.0.3/tests/legacy_tests/test_yaml_ext.py` |
| danger | 194 | 25 | 12 | `pyyaml-6.0.3/yaml/_yaml.pyx` |
| concurrency | 14 | 4 | 1 | `pyyaml-6.0.3/examples/pygments-lexer/yaml.py` |
| connectivity | 242 | 27 | 21 | `pyyaml-6.0.3/tests/legacy_tests/test_constructor.py` |
| io | 142 | 24 | 10 | `pyyaml-6.0.3/tests/legacy_tests/test_appliance.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 3 | 1 | 0 | `pyyaml-6.0.3/tests/legacy_tests/test_constructor.py` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 30 | 7 | 2 | `pyyaml-6.0.3/examples/pygments-lexer/yaml.py` |
| tests | 111 | 22 | 10 | `pyyaml-6.0.3/tests/legacy_tests/test_yaml_ext.py` |
| docs | 16 | 3 | 0 | `pyyaml-6.0.3/examples/pygments-lexer/yaml.py` |
| debt | 126 | 19 | 10 | `pyyaml-6.0.3/tests/legacy_tests/test_schema.py` |
| mutation | 2094 | 29 | 130 | `pyyaml-6.0.3/yaml/_yaml.pyx` |
| dead_code | 46 | 6 | 5 | `pyyaml-6.0.3/yaml/_yaml.pyx` |
| credential | 0 | 0 | 0 | - |
| threat | 35 | 9 | 4 | `pyyaml-6.0.3/tests/legacy_tests/test_constructor.py` |
| ml_ai | 1 | 1 | 0 | `pyyaml-6.0.3/setup.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.9**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pyyaml-6.0.3/tests/legacy_tests/test_appliance.py` (Hits: 34)
- `pyyaml-6.0.3/tests/legacy_tests/test_yaml_ext.py` (Hits: 19)
- `pyyaml-6.0.3/tests/legacy_tests/test_input_output.py` (Hits: 13)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **yaml.py** (`pyyaml-6.0.3/examples/pygments-lexer/yaml.py`) — 21 inbound connections
2. **test_appliance.py** (`pyyaml-6.0.3/tests/legacy_tests/test_appliance.py`) — 21 inbound connections
3. **test_constructor.py** (`pyyaml-6.0.3/tests/legacy_tests/test_constructor.py`) — 3 inbound connections
4. **canonical.py** (`pyyaml-6.0.3/tests/legacy_tests/canonical.py`) — 2 inbound connections
5. **test_emitter.py** (`pyyaml-6.0.3/tests/legacy_tests/test_emitter.py`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **setup.py** (`pyyaml-6.0.3/setup.py`) — 19 outbound dependencies
2. **test_yaml.py** (`pyyaml-6.0.3/tests/legacy_tests/test_yaml.py`) — 17 outbound dependencies
3. **test_yaml_ext.py** (`pyyaml-6.0.3/tests/legacy_tests/test_yaml_ext.py`) — 14 outbound dependencies
4. **test_constructor.py** (`pyyaml-6.0.3/tests/legacy_tests/test_constructor.py`) — 8 outbound dependencies
5. **test_appliance.py** (`pyyaml-6.0.3/tests/legacy_tests/test_appliance.py`) — 7 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_object_to_event` **(Many-Argument Workhorses)** (@ `pyyaml-6.0.3/yaml/_yaml.pyx`) -> Impact: **145.1** | LOC: 182
- `_serialize_node` **(Many-Argument Workhorses)** (@ `pyyaml-6.0.3/yaml/_yaml.pyx`) -> Impact: **109.3** | LOC: 128
- `_event_to_object` **(Compute Cores)** (@ `pyyaml-6.0.3/yaml/_yaml.pyx`) -> Impact: **77.1** | LOC: 122
- `_token_to_object` **(Compute Cores)** (@ `pyyaml-6.0.3/yaml/_yaml.pyx`) -> Impact: **63.5** | LOC: 93
- `__init__` **(Many-Argument Workhorses)** (@ `pyyaml-6.0.3/yaml/_yaml.pyx`) -> Impact: **48.8** | LOC: 38
- `test_implicit_resolver` **(Many-Argument Workhorses)** (@ `pyyaml-6.0.3/tests/legacy_tests/test_schema.py`) -> Impact: **46.6** | LOC: 93
  * *Intent:* # The tests/data/yaml11.schema file is copied from # https://github.com/perlpunk/yaml-test-schema/blob/master/data/schema-yaml11.yaml
- `_compose_node` **(Many-Argument Workhorses)** (@ `pyyaml-6.0.3/yaml/_yaml.pyx`) -> Impact: **30.1** | LOC: 41
- `display` **(Compute Cores)** (@ `pyyaml-6.0.3/tests/legacy_tests/test_appliance.py`) -> Impact: **29.7** | LOC: 39
- `run` **(Compute Cores)** (@ `pyyaml-6.0.3/tests/legacy_tests/test_appliance.py`) -> Impact: **29.2** | LOC: 29
- `scan` **(Compute Cores)** (@ `pyyaml-6.0.3/tests/legacy_tests/canonical.py`) -> Impact: **27.6** | LOC: 43

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `pyyaml-6.0.3/tests/legacy_tests` | 23 | 2558.46 | 29.56% | 0.0% |
| `pyyaml-6.0.3/yaml` | 4 | 2021.16 | 26.48% | 2.89% |
| `pyyaml-6.0.3/examples/pygments-lexer` | 2 | 449.66 | 23.4% | 0.0% |
| `pyyaml-6.0.3` | 5 | 319.46 | 9.76% | 37.92% |
| `pyyaml-6.0.3/examples/yaml-highlight` | 1 | 190.28 | 77.4% | 0.0% |
| `pyyaml-6.0.3/packaging` | 1 | 41.02 | 85.81% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `pyyaml-6.0.3/Makefile` -> **99.9983%** Exposure
- `pyyaml-6.0.3/setup.py` -> **89.5975%** Exposure
- `pyyaml-6.0.3/yaml/_yaml.pyx` -> **11.573%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `pyyaml-6.0.3/setup.py` -> **100.0%** Exposure
- `pyyaml-6.0.3/yaml/_yaml.pyx` -> **100.0%** Exposure
- `pyyaml-6.0.3/packaging/_pyyaml_pep517.py` -> **99.9994%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pyyaml-6.0.3/tests/legacy_tests/test_constructor.py` -> **0** Orphaned Functions | **9** Duplicates
- `pyyaml-6.0.3/tests/legacy_tests/conftest.py` -> **5** Orphaned Functions | **2** Duplicates
- `pyyaml-6.0.3/Makefile` -> **6** Orphaned Functions | **0** Duplicates
- `pyyaml-6.0.3/setup.py` -> **5** Orphaned Functions | **0** Duplicates
- `pyyaml-6.0.3/tests/legacy_tests/test_structure.py` -> **0** Orphaned Functions | **4** Duplicates

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
- **Unknown Dependencies:** `152` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `pyyaml-6.0.3/yaml/_yaml.pyx` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1976.68 | **LOC:** 1398 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 16.289; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Complexity Load (formerly Cognitive Load) (93.0%), Connectivity (formerly Api Exposure) (52.0%)
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
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 443`, `dead_code: 26`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 21`, `import: 1`
* *Defense:* `safety: 5`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.289
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` yaml
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyyaml-6.0.3/tests/legacy_tests/canonical.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 433.98 | **LOC:** 362 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 27.089; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (98.3%), Connectivity (formerly Api Exposure) (71.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (37.3%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.089
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0875
  * `Imports (Out-Degree: 1):` yaml, yaml.composer, yaml.constructor, yaml.resolver
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/examples/pygments-lexer/yaml.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 430.12 | **LOC:** 432 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **2**; blast radius 193.933; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (97.3%), Connectivity (formerly Api Exposure) (82.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (42.2%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 193.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.609524
  * `Imports (Out-Degree: 0):` pygments.lexer, pygments.token
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_constructor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 330.16 | **LOC:** 305 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 25.683; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (93.4%), Connectivity (formerly Api Exposure) (73.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (47.6%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.683
  * `Choke Point (Betweenness):` 5.6e-05 | `Ripple Effect (Closeness):` 0.102857
  * `Imports (Out-Degree: 2):` datetime, pprint, signal, sys, test_appliance, test_constructor, yaml, yaml.tokens
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_yaml_ext.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 292.84 | **LOC:** 295 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **14**; blast radius 28.144; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (87.5%), Connectivity (formerly Api Exposure) (57.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (46.8%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.144
  * `Choke Point (Betweenness):` 0.011485 | `Ripple Effect (Closeness):` 0.064286
  * `Imports (Out-Degree: 7):` _yaml, os, pprint, sys, tempfile, test_appliance, test_constructor, test_errors...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/setup.py` (PYTHON | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 292.48 | **LOC:** 360 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 16.289; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.3%), Debt Markers (formerly Tech Debt) (89.6%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 70`, `dead_code: 2`, `fragile_debt: 2`, `unreferenced_by_name: 5`
* *Architecture:* `io: 9`, `api: 16`, `import: 12`
* *Defense:* `safety: 18`, `doc: 2`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.289
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Cython.Distutils, Cython.Distutils.extension, Cython.Distutils.old_build_ext, _pyyaml_pep517, distutils, distutils.errors, json, os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyyaml-6.0.3/tests/legacy_tests/test_appliance.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 240.98 | **LOC:** 149 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **7**; blast radius 165.948; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.4%), Connectivity (formerly Api Exposure) (62.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (42.1%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 165.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.601242
  * `Imports (Out-Degree: 0):` os, os.path, pathlib, pprint, sys, traceback, types
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_structure.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 193.94 | **LOC:** 200 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 20.767; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (72.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (44.7%), Connectivity (formerly Api Exposure) (43.8%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.767
  * `Choke Point (Betweenness):` 0.003277 | `Ripple Effect (Closeness):` 0.079365
  * `Imports (Out-Degree: 3):` canonical, pprint, test_appliance, yaml
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/examples/yaml-highlight/yaml_hl.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 190.28 | **LOC:** 115 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 16.289; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.9%), Complexity Load (formerly Cognitive Load) (77.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (5.8%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.289
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` codecs, optparse, os.path, sys, yaml
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyyaml-6.0.3/tests/legacy_tests/conftest.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 145.44 | **LOC:** 133 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 16.289; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (95.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (44.0%), Connectivity (formerly Api Exposure) (7.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.289
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` os, pathlib, pytest, test_appliance, warnings, yaml
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyyaml-6.0.3/tests/legacy_tests/test_input_output.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 145.24 | **LOC:** 142 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 17.35; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (73.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (41.1%), Complexity Load (formerly Cognitive Load) (33.7%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.35
  * `Choke Point (Betweenness):` 5.6e-05 | `Ripple Effect (Closeness):` 0.042857
  * `Imports (Out-Degree: 2):` codecs, io, os, os.path, tempfile, test_appliance, yaml
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_schema.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 138.08 | **LOC:** 153 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 17.35; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (91.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (37.8%), Connectivity (formerly Api Exposure) (33.8%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.35
  * `Choke Point (Betweenness):` 5.6e-05 | `Ripple Effect (Closeness):` 0.042857
  * `Imports (Out-Degree: 2):` math, pprint, sys, test_appliance, yaml
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_emitter.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 135.1 | **LOC:** 105 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 23.234; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (92.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (43.6%), Complexity Load (formerly Cognitive Load) (39.2%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.234
  * `Choke Point (Betweenness):` 5.6e-05 | `Ripple Effect (Closeness):` 0.085714
  * `Imports (Out-Degree: 2):` test_appliance, yaml
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_resolver.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 95.08 | **LOC:** 99 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 20.767; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (87.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (33.9%), Complexity Load (formerly Cognitive Load) (33.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_convert_node` **(Stateful Encapsulated Methods)** (Impact: 9.1)
  * `test_implicit_resolver` **(Defensive Guards)** (Impact: 8.9)
  * `test_path_resolver_dumper` **(Defensive Guards)** (Impact: 8.7)
  * `test_path_resolver_loader` **(Defensive Guards)** (Impact: 6.7)
  * `_make_path_loader_and_dumper` **(C Struct Operations)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 34`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 21`
* *Architecture:* `io: 6`, `api: 5`, `import: 3`
* *Defense:* `safety: 15`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.767
  * `Choke Point (Betweenness):` 5.6e-05 | `Ripple Effect (Closeness):` 0.079365
  * `Imports (Out-Degree: 2):` pprint, test_appliance, yaml
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_errors.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 55.46 | **LOC:** 72 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 20.767; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (50.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.5%), Complexity Load (formerly Cognitive Load) (32.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_dumper_error` **(Defensive Guards)** (Impact: 5.8)
  * `test_emitter_error` **(Defensive Guards)** (Impact: 5.7)
  * `test_loader_error` **(Defensive Guards)** (Impact: 5.6)
  * `test_loader_error_string` **(Defensive Guards)** (Impact: 5.6)
  * `test_loader_error_single` **(Defensive Guards)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 7 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 25`, `args: 5`, `func_start: 5`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 7`
* *Architecture:* `io: 5`, `api: 5`, `import: 4`
* *Defense:* `safety: 10`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.767
  * `Choke Point (Betweenness):` 0.001737 | `Ripple Effect (Closeness):` 0.079365
  * `Imports (Out-Degree: 3):` io, test_appliance, test_emitter, yaml
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_canonical.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 51.38 | **LOC:** 44 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 17.35; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (84.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (40.1%), Complexity Load (formerly Cognitive Load) (31.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_canonical_error` **(Defensive Guards)** (Impact: 6.5)
  * `test_canonical_scanner` **(Defensive Guards)** (Impact: 5.6)
  * `test_canonical_parser` **(Defensive Guards)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 14`, `args: 3`, `func_start: 3`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `io: 3`, `api: 3`, `import: 2`
* *Defense:* `safety: 4`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.35
  * `Choke Point (Betweenness):` 0.001036 | `Ripple Effect (Closeness):` 0.042857
  * `Imports (Out-Degree: 3):` canonical, test_appliance, yaml
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_multi_constructor.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 44.58 | **LOC:** 66 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 17.35; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (96.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (40.4%), Complexity Load (formerly Cognitive Load) (29.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_multi_constructor` **(Defensive Guards)** (Impact: 7.3)
  * `myconstructor2` **(Defensive Guards)** (Impact: 4.7)
  * `myconstructor1` **(Parameter Forwarders)** (Impact: 2.1)
  * `_load_code` **(Encapsulated Accessors)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 22`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 11`
* *Architecture:* `io: 2`, `api: 5`, `import: 4`
* *Defense:* `safety: 4`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.35
  * `Choke Point (Betweenness):` 5.6e-05 | `Ripple Effect (Closeness):` 0.042857
  * `Imports (Out-Degree: 2):` pprint, sys, test_appliance, yaml
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_tokens.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 42.36 | **LOC:** 81 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 20.767; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (72.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (32.3%), Connectivity (formerly Api Exposure) (20.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_tokens` **(Defensive Guards)** (Impact: 10.8)
  * `test_scanner` **(Defensive Guards)** (Impact: 8.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 13`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 8`
* *Architecture:* `io: 3`, `api: 2`, `import: 3`
* *Defense:* `safety: 7`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 20.767
  * `Choke Point (Betweenness):` 5.6e-05 | `Ripple Effect (Closeness):` 0.079365
  * `Imports (Out-Degree: 2):` pprint, test_appliance, yaml
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/packaging/_pyyaml_pep517.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 41.02 | **LOC:** 52 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 23.211; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.7%), Complexity Load (formerly Cognitive Load) (85.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_expose_config_settings` **(Stateful Encapsulated Methods)** (Impact: 6.7)
  * `_bridge_build_meta` **(Encapsulated Accessors)** (Impact: 3.6)
  * `__exit__` **(Parameter Forwarders)** (Impact: 2.3)
  * `__init__` **(Encapsulated Accessors)** (Impact: 1.8)
  * `__enter__` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 20`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 8`
* *Architecture:* `io: 1`, `api: 5`, `import: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.211
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.028571
  * `Imports (Out-Degree: 0):` contextlib, functools, inspect, setuptools, sys
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_mark.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 37.06 | **LOC:** 34 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 17.35; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (79.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (30.9%), Connectivity (formerly Api Exposure) (20.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_marks` **(Defensive Guards)** (Impact: 11.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 10`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 5`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.35
  * `Choke Point (Betweenness):` 5.6e-05 | `Ripple Effect (Closeness):` 0.042857
  * `Imports (Out-Degree: 2):` test_appliance, yaml
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_recursive.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 35.42 | **LOC:** 53 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 17.35; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.5%), Connectivity (formerly Api Exposure) (59.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (34.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_recursive` **(Defensive Guards)** (Impact: 4.5)
  * `__init__` **(Parameter Forwarders)** (Impact: 2.1)
  * `__setstate__` **(Parameter Forwarders)** (Impact: 1.8)
  * `__repr__` **(Defensive Guards)** (Impact: 1.7)
  * `__getstate__` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 15`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 12`
* *Architecture:* `io: 1`, `api: 7`, `import: 2`
* *Defense:* `safety: 5`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.35
  * `Choke Point (Betweenness):` 5.6e-05 | `Ripple Effect (Closeness):` 0.042857
  * `Imports (Out-Degree: 2):` test_appliance, yaml
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_representer.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 30.78 | **LOC:** 45 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 17.35; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (73.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (27.5%), Connectivity (formerly Api Exposure) (20.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_representer_types` **(Defensive Guards)** (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 10`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`
* *Architecture:* `io: 1`, `api: 1`, `import: 4`
* *Defense:* `safety: 5`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.35
  * `Choke Point (Betweenness):` 5.6e-05 | `Ripple Effect (Closeness):` 0.042857
  * `Imports (Out-Degree: 3):` pprint, test_appliance, test_constructor, yaml
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_reader.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 24.04 | **LOC:** 39 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 17.35; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (62.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (12.7%), Connectivity (formerly Api Exposure) (10.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_run_reader` **(Stateful Encapsulated Methods)** (Impact: 7.4)
  * `test_stream_error` **(Defensive Guards)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 16`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `io: 4`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.35
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.042857
  * `Imports (Out-Degree: 1):` test_appliance, yaml.reader
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_build_ext.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 22.16 | **LOC:** 12 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 16.289; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (73.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (8.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 2`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.289
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` distutils.util, os, sys, test_appliance, test_yaml_ext
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyyaml-6.0.3/yaml/_yaml.pxd` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 19.8 | **LOC:** 259 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.289
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pyyaml-6.0.3/tests/legacy_tests/test_appliance.py` -> **Severity: 59.771** (Embedded: 0.6012 * Error Risk: 99.413%)
- `pyyaml-6.0.3/examples/pygments-lexer/yaml.py` -> **Severity: 59.305** (Embedded: 0.6095 * Error Risk: 97.2973%)
- `pyyaml-6.0.3/tests/legacy_tests/test_constructor.py` -> **Severity: 9.607** (Embedded: 0.1029 * Error Risk: 93.4022%)
- `pyyaml-6.0.3/tests/legacy_tests/canonical.py` -> **Severity: 8.6** (Embedded: 0.0875 * Error Risk: 98.2853%)
- `pyyaml-6.0.3/tests/legacy_tests/test_emitter.py` -> **Severity: 7.958** (Embedded: 0.0857 * Error Risk: 92.8484%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pyyaml-6.0.3/tests/legacy_tests/test_appliance.py` -> **Severity: 16594.8** (Blast Radius: 165.948 * Doc Risk: 100.0%)
- `pyyaml-6.0.3/examples/pygments-lexer/yaml.py` -> **Severity: 10774.064** (Blast Radius: 193.933 * Doc Risk: 55.5556%)
- `pyyaml-6.0.3/tests/legacy_tests/test_yaml_ext.py` -> **Severity: 2814.4** (Blast Radius: 28.144 * Doc Risk: 100.0%)
- `pyyaml-6.0.3/tests/legacy_tests/canonical.py` -> **Severity: 2708.9** (Blast Radius: 27.089 * Doc Risk: 100.0%)
- `pyyaml-6.0.3/tests/legacy_tests/test_constructor.py` -> **Severity: 2568.3** (Blast Radius: 25.683 * Doc Risk: 100.0%)

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
