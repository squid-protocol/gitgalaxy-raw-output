# ARCHITECTURAL_BRIEF: jedi
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_python/jedi` |
| **Timestamp** | `2026-08-07T04:00:23.300639+00:00` |
| **Scan Duration** | `0.52s` |
| **Git Branch** | `master` |
| **Git Commit** | `76c1e03f07b351c07b54609df12615dfb9379a9a` |
| **Git Remote** | `https://github.com/davidhalter/jedi.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 93 malicious artifacts.

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
| Total Artifacts | 387 |
| Analyzed Artifacts (Scanned) | 99 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 288 |
| Total LOC | 13890 |
| Volatility Index | 0.03 |
| % Scanned of codebase = | 25.6% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2516 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1415 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 35.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2351 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 89 | 13854 | 89.9% |
| PLAINTEXT | 4 | 0 | 4.0% |
| MARKDOWN | 2 | 0 | 2.0% |
| SHELL | 2 | 34 | 2.0% |
| BINARY_THREAT | 2 | 2 | 2.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.973`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 63 | 63.6% |
| file_cluster_8 | 23 | 23.2% |
| file_cluster_0 | 2 | 2.0% |
| Unknown | 2 | 2.0% |
| file_cluster_17 | 1 | 1.0% |
| file_cluster_16 | 1 | 1.0% |
| file_cluster_7 | 1 | 1.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 6.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 288*

**Composition by Extension & Reason:**
- `.py`: 225x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 47 LOC), 1x Excluded (Machine-Generated Source Code Signature: 609 LOC)
- `.rst`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.rst')
- `.pyi`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.png`: 4x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cfg`: 1x Excluded (Unsupported Extension: '.cfg'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.egg-link`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 2x Excluded (Explicitly Denied Extension: '.zip')
- `.css`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.so`: 1x Excluded (Explicitly Denied Extension: '.so')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.0 | 21.3 | 15.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 45.0 | 50.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 37.5 | 13.2 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 42.2 | 80.0 | 80.0 |
| API Exposure | 0.0 | 11.5 | 3.5 | 3.2 | 0.0 |
| Concurrency Exposure | 0.0 | 28.8 | 1.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 43.1 | 32.4 | 0.0 |
| Commented Logic Exposure | 0.0 | 21.9 | 1.7 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 90.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.3 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 9.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 56.0 | 61.4 | 100.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `jedi/api/environment.py` (Hits: 38)
- `jedi/__main__.py` (Hits: 15)
- `jedi/inference/compiled/subprocess/__init__.py` (Hits: 14)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **base_value.py** (`jedi/inference/base_value.py`) — 38 inbound connections
2. **names.py** (`jedi/inference/names.py`) — 25 inbound connections
3. **cache.py** (`jedi/inference/cache.py`) — 22 inbound connections
4. **typing.py** (`jedi/inference/gradual/typing.py`) — 22 inbound connections
5. **helpers.py** (`jedi/inference/helpers.py`) — 20 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **imports.py** (`jedi/inference/imports.py`) — 31 outbound dependencies
2. **__init__.py** (`jedi/api/__init__.py`) — 28 outbound dependencies
3. **klass.py** (`jedi/inference/value/klass.py`) — 25 outbound dependencies
4. **completion.py** (`jedi/api/completion.py`) — 22 outbound dependencies
5. **names.py** (`jedi/inference/names.py`) — 21 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `infer_node` (@ `jedi/inference/syntax_tree.py`) -> Impact: **493.7** | LOC: 798
- `get_stack_at_position` (@ `jedi/api/helpers.py`) -> Impact: **271.0** | LOC: 322
- `__repr__` (@ `jedi/inference/compiled/access.py`) -> Impact: **168.9** | LOC: 364
- `__repr__` (@ `jedi/api/__init__.py`) -> Impact: **168.5** | LOC: 390
- `iterate_argument_clinic` (@ `jedi/inference/arguments.py`) -> Impact: **144.7** | LOC: 254
- `_extract_string_while_in_string` (@ `jedi/api/completion.py`) -> Impact: **143.5** | LOC: 168
- `get_type_hint` (@ `jedi/inference/value/function.py`) -> Impact: **129.1** | LOC: 331
- `infer_import` (@ `jedi/inference/imports.py`) -> Impact: **127.4** | LOC: 297
- `_complete_python` (@ `jedi/api/completion.py`) -> Impact: **108.1** | LOC: 187
- `description` (@ `jedi/api/classes.py`) -> Impact: **102.6** | LOC: 286

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `jedi/inference` | 25 | 4505.2 | 27.62% | 41.3% |
| `jedi/api` | 13 | 2335.58 | 16.74% | 20.1% |
| `jedi/inference/value` | 8 | 1401.04 | 15.25% | 63.87% |
| `jedi/inference/gradual` | 10 | 1365.06 | 20.35% | 57.94% |
| `test/examples/sample_venvs/pth_directory` | 2 | 1000.0 | 0.0% | 0.0% |
| `jedi/inference/compiled` | 5 | 924.08 | 36.62% | 44.72% |
| `jedi` | 10 | 645.38 | 17.07% | 29.06% |
| `jedi/api/refactoring` | 2 | 481.66 | 16.11% | 28.8% |
| `jedi/inference/compiled/subprocess` | 3 | 389.16 | 30.41% | 7.91% |
| `jedi/plugins` | 4 | 265.94 | 13.63% | 49.97% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `scripts/profiled_pytest.sh` -> **100.0%** Exposure
- `jedi/api/interpreter.py` -> **100.0%** Exposure
- `jedi/file_io.py` -> **100.0%** Exposure
- `jedi/inference/base_value.py` -> **100.0%** Exposure
- `jedi/inference/cache.py` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `deploy-master.sh` -> **100.0%** Exposure
- `jedi/inference/compiled/subprocess/__main__.py` -> **99.995%** Exposure
- `jedi/inference/utils.py` -> **99.9928%** Exposure
- `jedi/inference/lazy_value.py` -> **99.9249%** Exposure
- `jedi/inference/gradual/type_var.py` -> **99.9201%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `jedi/inference/names.py` -> **0** Orphaned Functions | **54** Duplicates
- `jedi/inference/value/iterable.py` -> **0** Orphaned Functions | **34** Duplicates
- `jedi/inference/base_value.py` -> **0** Orphaned Functions | **20** Duplicates
- `jedi/inference/gradual/typing.py` -> **0** Orphaned Functions | **20** Duplicates
- `jedi/inference/compiled/value.py` -> **0** Orphaned Functions | **17** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`jedi/__main__.py`** -> AI Confidence: **99.31%**
2. **`jedi/api/completion.py`** -> AI Confidence: **99.31%**
3. **`jedi/api/helpers.py`** -> AI Confidence: **99.31%**
4. **`jedi/api/refactoring/extract.py`** -> AI Confidence: **99.31%**
5. **`jedi/inference/docstrings.py`** -> AI Confidence: **99.31%**
6. **`jedi/inference/gradual/conversion.py`** -> AI Confidence: **99.31%**
7. **`jedi/inference/gradual/typeshed.py`** -> AI Confidence: **99.31%**
8. **`jedi/inference/imports.py`** -> AI Confidence: **99.31%**
9. **`jedi/inference/param.py`** -> AI Confidence: **99.31%**
10. **`jedi/inference/references.py`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `746` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `jedi/inference/names.py` (PYTHON) -> Cumulative Risk: **656.61**
- **Archetype:** `file_cluster_13` (Distance: 10.499 IQR)
- **Magnitude:** 471.18 | **LOC:** 674 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Verification (80.0%)
- **Heaviest Functions:** `goto` (Impact: 55.4), `get_kind` (Impact: 22.1), `assignment_indexes` (Impact: 17.0)

### 2. `jedi/inference/filters.py` (PYTHON) -> Cumulative Risk: **647.26**
- **Archetype:** `file_cluster_13` (Distance: 11.664 IQR)
- **Magnitude:** 220.0 | **LOC:** 371 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.5532%)
- **Heaviest Functions:** `__repr__` (Impact: 42.7), `__repr__` (Impact: 18.8), `_get_definition_names` (Impact: 16.9)

### 3. `jedi/inference/gradual/type_var.py` (PYTHON) -> Cumulative Risk: **611.47**
- **Archetype:** `file_cluster_13` (Distance: 11.095 IQR)
- **Magnitude:** 124.54 | **LOC:** 128 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9588%), State Flux (99.9201%), Documentation (98.4984%)
- **Heaviest Functions:** `__init__` (Impact: 26.2), `py__call__` (Impact: 19.2), `define_generics` (Impact: 7.4)

### 4. `jedi/inference/value/klass.py` (PYTHON) -> Cumulative Risk: **607.43**
- **Archetype:** `file_cluster_13` (Distance: 10.658 IQR)
- **Magnitude:** 387.7 | **LOC:** 695 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.8651%), Churn (82.04%)
- **Heaviest Functions:** `py__mro__` (Impact: 73.0), `get_metaclass_filters` (Impact: 25.1), `is_typeddict` (Impact: 17.0)

### 5. `jedi/inference/signature.py` (PYTHON) -> Cumulative Risk: **575.93**
- **Archetype:** `file_cluster_0` (Distance: 9.795 IQR)
- **Magnitude:** 125.88 | **LOC:** 153 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (97.6224%), Verification (80.0%)
- **Heaviest Functions:** `to_string` (Impact: 16.9), `param_strings` (Impact: 14.9), `matches_signature` (Impact: 14.8)

### 6. `jedi/inference/gradual/base.py` (PYTHON) -> Cumulative Risk: **567.15**
- **Archetype:** `file_cluster_13` (Distance: 10.639 IQR)
- **Magnitude:** 220.96 | **LOC:** 435 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9999%), Documentation (91.754%), State Flux (90.9153%)
- **Heaviest Functions:** `get_type_hint` (Impact: 47.9), `__repr__` (Impact: 33.4), `py__stop_iteration_returns` (Impact: 9.2)

### 7. `jedi/inference/value/iterable.py` (PYTHON) -> Cumulative Risk: **559.29**
- **Archetype:** `file_cluster_0` (Distance: 11.174 IQR)
- **Magnitude:** 406.62 | **LOC:** 648 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (92.7207%), Documentation (92.5815%)
- **Heaviest Functions:** `get_tree_entries` (Impact: 33.4), `__repr__` (Impact: 30.9), `__repr__` (Impact: 30.3)

### 8. `jedi/inference/analysis.py` (PYTHON) -> Cumulative Risk: **551.02**
- **Archetype:** `file_cluster_13` (Distance: 12.195 IQR)
- **Magnitude:** 144.9 | **LOC:** 214 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.7711%), Tech Debt (98.2014%), Verification (80.0%)
- **Heaviest Functions:** `add_attribute_error` (Impact: 72.9), `_check_for_setattr` (Impact: 11.3), `__str__` (Impact: 6.1)

### 9. `jedi/inference/star_args.py` (PYTHON) -> Cumulative Risk: **535.72**
- **Archetype:** `file_cluster_13` (Distance: 9.844 IQR)
- **Magnitude:** 168.86 | **LOC:** 218 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.7711%), Verification (80.0%), Safety Score (76.6017%)
- **Heaviest Functions:** `process_params` (Impact: 83.5), `_remove_given_params` (Impact: 16.4), `_iter_nodes_for_param` (Impact: 15.5)

### 10. `deploy-master.sh` (SHELL) -> Cumulative Risk: **533.12**
- **Archetype:** `file_cluster_17` (Distance: 14.6 IQR)
- **Magnitude:** 39.26 | **LOC:** 54 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.8916%), Cognitive Load (99.0108%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 10.4), `__global_context__` (Impact: 7.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `jedi/inference/syntax_tree.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.049 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.937 IQR)
- **Top Global Matches:** file_cluster_8: 10.049, file_cluster_13: 10.104, file_cluster_7: 10.373
- **Magnitude:** 545.18 | **LOC:** 906 | **CtrlFlow:** 53.6% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (18.5116%), Tech Debt (12.9371%)
**Top Internal Functions/Classes:**
  * `infer_node` (Impact: 493.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 230`, `args: 28`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 18`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `api: 14`, `concurrency: 6`, `import: 25`
* *Defense:* `safety: 27`, `doc: 21`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.917
  * `Choke Point (Betweenness):` 0.018301 | `Ripple Effect (Closeness):` 0.281255
  * `Imports (Out-Degree: 11):` jedi.inference.value, jedi.inference.cache, parso.python, jedi.inference.helpers, itertools, jedi.inference, __future__, jedi.inference.context...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `test/examples/sample_venvs/pth_directory/foo.pth` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.74%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.204294
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `test/examples/sample_venvs/pth_directory/import_smth.pth` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jedi/api/completion.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.983 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.61 IQR)
- **Top Global Matches:** file_cluster_13: 9.983, file_cluster_8: 10.041, file_cluster_7: 10.365
- **Magnitude:** 487.8 | **LOC:** 697 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.7486%), Tech Debt (9.1123%)
**Top Internal Functions/Classes:**
  * `_extract_string_while_in_string` (Impact: 143.5)
  * `_complete_python` (Impact: 108.1)
  * `_complete_trailer` (Impact: 53.8)
  * `filter_names` (Impact: 35.4)
  * `complete` (Impact: 21.4)
    * *Intent:* # Return list of completions in this order: # - Beginning with what user is typing # - Public (alpha...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 162`, `args: 31`, `func_start: 29`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 29`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 15`, `import: 24`
* *Defense:* `safety: 10`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.208
  * `Choke Point (Betweenness):` 0.003361 | `Ripple Effect (Closeness):` 0.022959
  * `Imports (Out-Degree: 10):` re, jedi.parser_utils, jedi.inference.value, parso.python, jedi.inference.helpers, jedi.inference, jedi.inference.context, jedi.api...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jedi/api/helpers.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.317 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.354 IQR)
- **Top Global Matches:** file_cluster_13: 9.317, file_cluster_8: 9.472, file_cluster_7: 9.568
- **Magnitude:** 480.82 | **LOC:** 523 | **CtrlFlow:** 49.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.6698%), Tech Debt (13.8698%)
**Top Internal Functions/Classes:**
  * `get_stack_at_position` (Impact: 271.0)
  * `_get_code_for_stack` (Impact: 27.9)
  * `wrapper` (Impact: 22.9)
  * `get_module_names` (Impact: 21.3)
  * `validate_line_column` (Impact: 16.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 157`, `args: 32`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 8`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 32`, `import: 14`
* *Defense:* `safety: 5`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.69
  * `Choke Point (Betweenness):` 0.002435 | `Ripple Effect (Closeness):` 0.05
  * `Imports (Out-Degree: 5):` jedi.inference.helpers, re, itertools, inspect, jedi.cache, functools, jedi.parser_utils, parso.python.parser...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `jedi/inference/names.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.499 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.407 IQR)
- **Top Global Matches:** file_cluster_13: 10.499, file_cluster_8: 10.623, file_cluster_0: 10.73
- **Magnitude:** 471.18 | **LOC:** 674 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.7166%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `goto` (Impact: 55.4)
  * `get_kind` (Impact: 22.1)
  * `assignment_indexes` (Impact: 17.0)
  * `__repr__` (Impact: 17.0)
  * `py__doc__` (Impact: 14.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 276`, `args: 77`, `func_start: 77`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 40`, `planned_debt: 1`, `duplicate_logic: 54`
* *Architecture:* `api: 78`, `concurrency: 6`, `import: 25`
* *Defense:* `safety: 3`, `doc: 10`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 43.816
  * `Choke Point (Betweenness):` 0.072446 | `Ripple Effect (Closeness):` 0.383529
  * `Imports (Out-Degree: 15):` jedi.cache, jedi.inference.imports, nodes, jedi.parser_utils, jedi.inference.cache, jedi.inference.gradual.annotation, jedi.inference.utils, jedi.inference.helpers...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `jedi/inference/base_value.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.567 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.67 IQR)
- **Top Global Matches:** file_cluster_13: 10.567, file_cluster_8: 10.839, file_cluster_0: 10.855
- **Magnitude:** 440.4 | **LOC:** 559 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.1329%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_getitem` (Impact: 78.2)
  * `goto` (Impact: 23.7)
  * `get_type_hint` (Impact: 14.8)
  * `is_sub_class_of` (Impact: 13.2)
  * `iterate` (Impact: 10.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 241`, `args: 90`, `func_start: 90`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 16`, `planned_debt: 4`, `duplicate_logic: 20`
* *Architecture:* `api: 99`, `import: 21`
* *Defense:* `safety: 16`, `doc: 17`, `test: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 89.898
  * `Choke Point (Betweenness):` 0.044796 | `Ripple Effect (Closeness):` 0.441505
  * `Imports (Out-Degree: 10):` parso.python.tree, jedi.inference.helpers, jedi.inference.utils, itertools, jedi.inference.gradual.conversion, operator, jedi.cache, jedi.inference...
  * `Imported By (In-Degree: 38):` (Excluded from Brief to save tokens)

### `jedi/inference/value/iterable.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.174 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.034 IQR)
- **Top Global Matches:** file_cluster_0: 11.174, file_cluster_13: 11.176, file_cluster_11: 11.583
- **Magnitude:** 406.62 | **LOC:** 648 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.9803%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `get_tree_entries` (Impact: 33.4)
  * `__repr__` (Impact: 30.9)
  * `__repr__` (Impact: 30.3)
  * `__repr__` (Impact: 29.4)
  * `py__simple_getitem__` (Impact: 10.9)
    * *Intent:* """Here the index is an int/str. Raises IndexError/KeyError."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 230`, `args: 76`, `func_start: 76`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 55`, `dead_code: 3`, `planned_debt: 3`, `duplicate_logic: 34`
* *Architecture:* `api: 62`, `import: 14`
* *Defense:* `safety: 12`, `doc: 22`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.815
  * `Choke Point (Betweenness):` 0.005035 | `Ripple Effect (Closeness):` 0.251453
  * `Imports (Out-Degree: 11):` jedi.inference.gradual.base, jedi.inference.value.dynamic_arrays, jedi.inference.utils, jedi.inference.helpers, jedi.inference.lazy_value, jedi.inference, jedi.inference.filters, jedi.parser_utils...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `jedi/inference/imports.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.873 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.526 IQR)
- **Top Global Matches:** file_cluster_13: 10.873, file_cluster_0: 11.235, file_cluster_8: 11.269
- **Magnitude:** 393.78 | **LOC:** 592 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.7365%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `infer_import` (Impact: 127.4)
  * `completion_names` (Impact: 36.3)
  * `import_module` (Impact: 34.3)
  * `import_module_by_names` (Impact: 25.9)
  * `load_module_from_path` (Impact: 22.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 120`, `args: 22`, `func_start: 22`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 35`, `dead_code: 3`
* *Architecture:* `io: 8`, `api: 18`, `import: 24`
* *Defense:* `safety: 11`, `doc: 20`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.979
  * `Choke Point (Betweenness):` 0.030027 | `Ripple Effect (Closeness):` 0.281255
  * `Imports (Out-Degree: 12):` jedi.parser_utils, jedi.inference.gradual.typeshed, , jedi.inference.value, jedi.inference.cache, parso.python, for, jedi.inference.utils...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `jedi/inference/compiled/value.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.545 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.334 IQR)
- **Top Global Matches:** file_cluster_13: 10.545, file_cluster_0: 10.68, file_cluster_8: 10.778
- **Magnitude:** 393.42 | **LOC:** 627 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.3467%), Tech Debt (99.9995%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 63.9)
  * `_parse_function_doc` (Impact: 28.6)
  * `_get` (Impact: 28.1)
  * `get_param_names` (Impact: 14.7)
  * `py__call__` (Impact: 11.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 228`, `args: 82`, `func_start: 78`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 29`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 17`
* *Architecture:* `io: 1`, `api: 69`, `import: 21`
* *Defense:* `safety: 19`, `doc: 12`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.386
  * `Choke Point (Betweenness):` 0.033485 | `Ripple Effect (Closeness):` 0.336012
  * `Imports (Out-Degree: 12):` re, jedi.cache, jedi.inference.value, jedi.inference.cache, jedi.inference.utils, jedi.inference.helpers, typing, jedi.inference...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `jedi/inference/value/klass.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.658 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.786 IQR)
- **Top Global Matches:** file_cluster_13: 10.658, file_cluster_0: 10.98, file_cluster_11: 11.056
- **Magnitude:** 387.7 | **LOC:** 695 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (21.4697%), Tech Debt (99.8651%)
**Top Internal Functions/Classes:**
  * `py__mro__` (Impact: 73.0)
    * *Intent:* """ param_names = [] filter_ = cls.as_context().get_global_filter() for name in sorted(filter_.value...
  * `get_metaclass_filters` (Impact: 25.1)
  * `is_typeddict` (Impact: 17.0)
    * *Intent:* # If dataclass_transform is applied to a class, dataclass-like semantics # will be assumed for any c...
  * `get_dataclass_param_names` (Impact: 15.1)
  * `init_mode_from_new` (Impact: 15.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 200`, `args: 48`, `func_start: 47`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 28`, `dead_code: 1`, `planned_debt: 5`, `duplicate_logic: 9`
* *Architecture:* `api: 47`, `import: 29`
* *Defense:* `safety: 15`, `doc: 28`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 11.113
  * `Choke Point (Betweenness):` 0.011911 | `Ripple Effect (Closeness):` 0.241843
  * `Imports (Out-Degree: 17):` system., jedi.parser_utils, jedi.inference.value, jedi.inference.cache, jedi.inference.gradual.annotation, jedi.inference.value.function, jedi.inference.gradual.base, typing...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `jedi/api/classes.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.484 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.264 IQR)
- **Top Global Matches:** file_cluster_13: 11.484, file_cluster_0: 11.613, file_cluster_8: 11.74
- **Magnitude:** 328.1 | **LOC:** 894 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.4307%), Tech Debt (99.8167%)
**Top Internal Functions/Classes:**
  * `description` (Impact: 102.6)
  * `type` (Impact: 14.7)
    * *Intent:* """ Shows the file path of a module. e.g. ``/usr/lib/python3.9/os.py`` """
  * `docstring` (Impact: 14.7)
  * `get_definition_end_position` (Impact: 9.4)
  * `defined_names` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 199`, `args: 63`, `func_start: 58`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`, `planned_debt: 3`, `duplicate_logic: 8`
* *Architecture:* `io: 8`, `api: 54`, `import: 15`
* *Defense:* `safety: 10`, `doc: 108`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.675
  * `Choke Point (Betweenness):` 0.002371 | `Ripple Effect (Closeness):` 0.02449
  * `Imports (Out-Degree: 11):` re, jedi.cache, jedi.api.helpers, keyword, jedi.inference.utils, typing, jedi.api, json...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `jedi/api/refactoring/extract.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.955 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.26 IQR)
- **Top Global Matches:** file_cluster_8: 8.955, file_cluster_7: 9.29, file_cluster_13: 9.337
- **Magnitude:** 310.74 | **LOC:** 387 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.4499%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `extract_function` (Impact: 78.3)
  * `_find_nodes` (Impact: 36.5)
  * `_remove_unwanted_expression_nodes` (Impact: 27.6)
  * `_replace` (Impact: 25.4)
  * `extract_variable` (Impact: 17.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 86`, `args: 19`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 9`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `safety: 5`, `doc: 12`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.757
  * `Choke Point (Betweenness):` 0.000158 | `Ripple Effect (Closeness):` 0.010204
  * `Imports (Out-Degree: 3):` jedi.api.refactoring, jedi.parser_utils, jedi.api.exceptions, jedi.common, jedi, textwrap, parso
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `jedi/inference/compiled/access.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.141 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.966 IQR)
- **Top Global Matches:** file_cluster_13: 11.141, file_cluster_8: 11.239, file_cluster_12: 11.505
- **Magnitude:** 293.8 | **LOC:** 563 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (60.2312%), Tech Debt (56.9001%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 168.9)
  * `get_api_type` (Impact: 12.6)
  * `safe_getattr` (Impact: 10.9)
  * `_is_class_instance` (Impact: 9.2)
  * `load_module` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 189`, `args: 53`, `func_start: 53`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 7`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 7`, `api: 49`, `import: 16`
* *Defense:* `safety: 60`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.222
  * `Choke Point (Betweenness):` 0.006711 | `Ripple Effect (Closeness):` 0.246554
  * `Imports (Out-Degree: 2):` warnings, jedi.inference.compiled.getattr_static, typing, re, inspect, operator, builtins, structure...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `jedi/inference/context.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.833 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.421 IQR)
- **Top Global Matches:** file_cluster_13: 9.833, file_cluster_8: 10.061, file_cluster_0: 10.062
- **Magnitude:** 290.06 | **LOC:** 499 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.0891%), Tech Debt (55.0503%)
**Top Internal Functions/Classes:**
  * `goto` (Impact: 91.0)
  * `create_context` (Impact: 41.5)
  * `from_scope_node` (Impact: 41.5)
  * `_get_global_filters_for_name` (Impact: 16.9)
  * `get_global_filters` (Impact: 7.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 197`, `args: 65`, `func_start: 65`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 68`, `import: 18`
* *Defense:* `safety: 12`, `doc: 11`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.316
  * `Choke Point (Betweenness):` 0.017972 | `Ripple Effect (Closeness):` 0.283354
  * `Imports (Out-Degree: 8):` parso.python.tree, typing, jedi.inference.base_value, jedi.inference, jedi.inference.filters, contextlib, jedi.parser_utils, jedi.inference.syntax_tree...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `jedi/inference/value/function.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.598 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.376 IQR)
- **Top Global Matches:** file_cluster_13: 9.598, file_cluster_8: 9.821, file_cluster_0: 9.975
- **Magnitude:** 283.32 | **LOC:** 460 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (33.8804%), Tech Debt (12.4992%)
**Top Internal Functions/Classes:**
  * `get_type_hint` (Impact: 129.1)
  * `_find_overload_functions` (Impact: 28.0)
  * `_is_overload_decorated` (Impact: 12.8)
  * `get_qualified_names` (Impact: 9.2)
  * `param_name_to_str` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 171`, `args: 46`, `func_start: 46`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 18`, `planned_debt: 3`
* *Architecture:* `api: 49`, `import: 20`
* *Defense:* `safety: 4`, `doc: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.496
  * `Choke Point (Betweenness):` 0.009578 | `Ripple Effect (Closeness):` 0.224671
  * `Imports (Out-Degree: 13):` jedi.inference.gradual.base, jedi.inference.helpers, jedi.inference.value.instance, jedi.inference.lazy_value, jedi.inference, jedi.inference.filters, jedi.inference.gradual.generics, jedi.inference.context...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `jedi/api/__init__.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.539 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.158 IQR)
- **Top Global Matches:** file_cluster_13: 10.539, file_cluster_8: 10.788, file_cluster_7: 10.927
- **Magnitude:** 275.68 | **LOC:** 799 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.3963%), Tech Debt (14.8284%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 168.5)
  * `__init__` (Impact: 33.6)
    * *Intent:* # Jedi uses lots and lots of recursion. By setting this a little bit higher, we
  * `_get_module` (Impact: 19.4)
  * `preload_module` (Impact: 3.8)
  * `set_debug_function` (Impact: 2.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 143`, `args: 30`, `func_start: 28`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 15`, `planned_debt: 5`
* *Architecture:* `io: 3`, `api: 23`, `import: 33`
* *Defense:* `safety: 7`, `doc: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.596
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` os.path, jedi.inference.base_value, jedi.parser_utils, jedi.api.helpers, jedi.inference.value, jedi.api.refactoring.extract, sys, parso.python...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jedi/api/project.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.767 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.207 IQR)
- **Top Global Matches:** file_cluster_13: 11.767, file_cluster_0: 11.978, file_cluster_8: 12.196
- **Magnitude:** 257.62 | **LOC:** 449 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.3596%), Tech Debt (10.5488%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 43.5)
  * `_search_func` (Impact: 39.9)
  * `_get_sys_path` (Impact: 29.0)
  * `_try_to_skip_duplicates` (Impact: 12.9)
  * `wrapper` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 95`, `args: 23`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 46`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 17`, `import: 14`
* *Defense:* `safety: 16`, `doc: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.776
  * `Choke Point (Betweenness):` 0.004195 | `Ripple Effect (Closeness):` 0.020408
  * `Imports (Out-Degree: 9):` jedi.api.environment, itertools, jedi.inference.imports, jedi.inference.sys_path, jedi.file_io, jedi.api.exceptions, jedi.api.helpers, jedi...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `jedi/inference/gradual/annotation.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.805 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.81 IQR)
- **Top Global Matches:** file_cluster_8: 9.805, file_cluster_13: 9.885, file_cluster_7: 10.157
- **Magnitude:** 246.76 | **LOC:** 475 | **CtrlFlow:** 44.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.6671%), Tech Debt (10.248%)
**Top Internal Functions/Classes:**
  * `infer_return_types` (Impact: 77.9)
  * `_infer_param` (Impact: 26.5)
  * `_get_forward_reference_node` (Impact: 17.6)
  * `infer_param` (Impact: 11.1)
  * `find_unknown_type_vars` (Impact: 11.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 112`, `args: 24`, `func_start: 23`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 9`, `planned_debt: 1`
* *Architecture:* `api: 17`, `import: 13`
* *Defense:* `safety: 15`, `doc: 16`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.959
  * `Choke Point (Betweenness):` 0.006648 | `Ripple Effect (Closeness):` 0.311224
  * `Imports (Out-Degree: 7):` jedi.inference.gradual.base, jedi.inference.helpers, re, inspect, jedi.inference.gradual.generics, jedi.inference.gradual.type_var, jedi.inference.compiled, jedi.inference.param...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `jedi/inference/gradual/typeshed.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.757 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.084 IQR)
- **Top Global Matches:** file_cluster_13: 9.757, file_cluster_8: 10.003, file_cluster_6: 10.029
- **Magnitude:** 242.72 | **LOC:** 311 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.7717%), Tech Debt (48.3413%)
**Top Internal Functions/Classes:**
  * `_try_to_load_stub` (Impact: 65.5)
  * `wrapper` (Impact: 30.9)
  * `import_module_decorator` (Impact: 22.5)
  * `_get_typeshed_directories` (Impact: 21.5)
  * `_load_from_typeshed` (Impact: 21.5)
    * *Intent:* # If no stub is found, that's fine, the calling function has to deal with # it. return None def _loa...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 63`, `args: 13`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 6`, `dead_code: 1`, `planned_debt: 10`
* *Architecture:* `io: 14`, `api: 7`, `import: 12`
* *Defense:* `safety: 13`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.079
  * `Choke Point (Betweenness):` 0.005574 | `Ripple Effect (Closeness):` 0.223349
  * `Imports (Out-Degree: 6):` typing, re, jedi.inference.base_value, functools, os, jedi.file_io, jedi.parser_utils, jedi.inference.gradual.stub_value...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `jedi/parser_utils.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.655 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.806 IQR)
- **Top Global Matches:** file_cluster_13: 10.655, file_cluster_8: 10.736, file_cluster_7: 10.906
- **Magnitude:** 242.5 | **LOC:** 346 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.8075%), Tech Debt (90.6593%)
**Top Internal Functions/Classes:**
  * `get_executable_nodes` (Impact: 29.4)
    * *Intent:* """ For static analysis. """
  * `get_parent_scope` (Impact: 29.2)
  * `get_signature` (Impact: 23.2)
  * `get_following_comment_same_line` (Impact: 16.9)
    * *Intent:* """ Move the `Node` start_pos. """
  * `expr_is_dotted` (Impact: 14.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 100`, `args: 24`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 9`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 27`, `concurrency: 1`, `import: 8`
* *Defense:* `safety: 15`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 29.454
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.3375
  * `Imports (Out-Degree: 0):` re, weakref, inspect, ast, parso.cache, textwrap, parso, parso.python
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `jedi/inference/arguments.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.519 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.737 IQR)
- **Top Global Matches:** file_cluster_13: 10.519, file_cluster_0: 10.807, file_cluster_8: 10.906
- **Magnitude:** 235.88 | **LOC:** 336 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.2344%), Tech Debt (13.1787%)
**Top Internal Functions/Classes:**
  * `iterate_argument_clinic` (Impact: 144.7)
  * `_star_star_dict` (Impact: 16.4)
  * `try_iter_content` (Impact: 11.2)
    * *Intent:* """Helper method for static analysis."""
  * `repack_with_argument_clinic` (Impact: 6.1)
  * `decorator` (Impact: 5.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 105`, `args: 28`, `func_start: 28`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 17`, `planned_debt: 2`
* *Architecture:* `api: 24`, `import: 12`
* *Defense:* `safety: 14`, `doc: 9`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.21
  * `Choke Point (Betweenness):` 0.005574 | `Ripple Effect (Closeness):` 0.313797
  * `Imports (Out-Degree: 6):` jedi.inference.utils, re, itertools, jedi.inference, jedi.inference.lazy_value, jedi.inference.value.instance, jedi.inference.value, jedi...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `jedi/inference/gradual/base.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.639 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.124 IQR)
- **Top Global Matches:** file_cluster_13: 10.639, file_cluster_0: 10.809, file_cluster_11: 11.059
- **Magnitude:** 220.96 | **LOC:** 435 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.465%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `get_type_hint` (Impact: 47.9)
  * `__repr__` (Impact: 33.4)
  * `py__stop_iteration_returns` (Impact: 9.2)
  * `infer` (Impact: 7.4)
  * `iter_` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 158`, `args: 58`, `func_start: 58`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 33`, `dead_code: 1`, `planned_debt: 4`, `duplicate_logic: 12`
* *Architecture:* `api: 39`, `import: 13`
* *Defense:* `safety: 9`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.349
  * `Choke Point (Betweenness):` 0.006565 | `Ripple Effect (Closeness):` 0.263676
  * `Imports (Out-Degree: 10):` jedi.inference.utils, jedi.inference.gradual.generics, jedi.inference.value.klass, jedi.inference.compiled, jedi.inference.context, jedi.inference.gradual.typing, jedi.inference.names, jedi.inference.gradual.type_var...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `jedi/inference/gradual/typing.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.398 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.435 IQR)
- **Top Global Matches:** file_cluster_13: 9.398, file_cluster_8: 9.569, file_cluster_0: 9.699
- **Magnitude:** 220.38 | **LOC:** 489 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.7976%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_remap` (Impact: 26.8)
  * `__repr__` (Impact: 13.3)
  * `__repr__` (Impact: 12.9)
  * `infer_type_vars` (Impact: 11.7)
  * `infer_type_vars` (Impact: 10.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 158`, `args: 45`, `func_start: 43`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 10`, `planned_debt: 2`, `duplicate_logic: 20`
* *Architecture:* `api: 53`, `import: 16`
* *Defense:* `safety: 9`, `doc: 8`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 64.914
  * `Choke Point (Betweenness):` 0.066636 | `Ripple Effect (Closeness):` 0.358202
  * `Imports (Out-Degree: 12):` jedi.inference.gradual.base, itertools, jedi.inference.lazy_value, jedi.inference.imports, jedi.inference.filters, jedi.inference.compiled.value, jedi.inference.arguments, jedi.inference.gradual.generics...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `jedi/inference/filters.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.664 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.462 IQR)
- **Top Global Matches:** file_cluster_13: 11.664, file_cluster_17: 11.878, file_cluster_0: 11.909
- **Magnitude:** 220.0 | **LOC:** 371 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (41.4767%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `__repr__` (Impact: 42.7)
  * `__repr__` (Impact: 18.8)
  * `_get_definition_names` (Impact: 16.9)
  * `__init__` (Impact: 13.3)
  * `_filter` (Impact: 7.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 127`, `args: 48`, `func_start: 47`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 49`, `planned_debt: 1`, `duplicate_logic: 13`
* *Architecture:* `api: 31`, `import: 9`
* *Defense:* `safety: 14`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.484
  * `Choke Point (Betweenness):` 0.00159 | `Ripple Effect (Closeness):` 0.294336
  * `Imports (Out-Degree: 5):` parso.python.tree, jedi.inference.utils, typing, weakref, jedi.inference, jedi.parser_utils, jedi.inference.names, abc...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `jedi/inference/value/iterable.py` (PYTHON) | Magnitude: 406.62 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 423, structural_boundaries: 230, encapsulation: 136, branch: 92
- `jedi/inference/signature.py` (PYTHON) | Magnitude: 125.88 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 60, encapsulation: 30, branch: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `jedi/inference/analysis.py` (PYTHON) | Magnitude: 144.9 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 139, structural_boundaries: 80, branch: 42, state_mutation: 25
- `jedi/plugins/__init__.py` (PYTHON) | Magnitude: 34.94 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 29, encapsulation: 16, structural_boundaries: 14, listeners: 9
- `jedi/inference/cache.py` (PYTHON) | Magnitude: 140.48 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 34, branch: 15, api: 15
- `jedi/file_io.py` (PYTHON) | Magnitude: 61.18 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 34, api: 19, args: 14
- `jedi/api/replstartup.py` (PYTHON) | Magnitude: 12.6 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, doc: 2, import: 2, encapsulation: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `jedi/api/completion_cache.py` (PYTHON) | Magnitude: 14.54 | Delta: **0.148 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, encapsulation: 10, structural_boundaries: 8, generics: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `deploy-master.sh` (SHELL) | Magnitude: 39.26 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 21, safety_bypasses: 17, branch: 13, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `jedi/api/exceptions.py` (PYTHON) | Magnitude: 15.6 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 5, class_start: 4, encapsulation: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `jedi/inference/param.py` (PYTHON) | Magnitude: 123.84 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 159, branch: 46, structural_boundaries: 46, state_mutation: 28
- `jedi/inference/gradual/utils.py` (PYTHON) | Magnitude: 16.08 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 9, branch: 4, safety: 3
- `jedi/inference/syntax_tree.py` (PYTHON) | Magnitude: 545.18 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 613, branch: 266, structural_boundaries: 230, encapsulation: 63
- `jedi/inference/gradual/annotation.py` (PYTHON) | Magnitude: 246.76 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 267, structural_boundaries: 112, branch: 90, args: 24
- `jedi/inference/compiled/__init__.py` (PYTHON) | Magnitude: 28.78 | Delta: **0.121 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 25, args: 8, func_start: 8

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `jedi/inference/value/klass.py` -> Churn: **82.04%** | Cog Load: 21.4697% | Debt: 99.8651%
- `jedi/api/classes.py` -> Churn: **58.68%** | Cog Load: 28.4307% | Debt: 99.8167%
- `jedi/inference/context.py` -> Churn: **58.68%** | Cog Load: 19.0891% | Debt: 55.0503%
- `jedi/inference/filters.py` -> Churn: **58.68%** | Cog Load: 41.4767% | Debt: 100.0%
- `jedi/inference/names.py` -> Churn: **58.68%** | Cog Load: 48.7166% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `jedi/api/completion.py` -> **Dave Halter** (100.0% isolated ownership) | Magnitude: 487.8
- `jedi/inference/names.py` -> **Dave Halter** (100.0% isolated ownership) | Magnitude: 471.18
- `jedi/inference/imports.py` -> **Dave Halter** (100.0% isolated ownership) | Magnitude: 393.78
- `jedi/inference/value/klass.py` -> **Eric Masseran** (100.0% isolated ownership) | Magnitude: 387.7
- `jedi/api/classes.py` -> **Dave Halter** (100.0% isolated ownership) | Magnitude: 328.1

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `jedi/inference/names.py` -> **Severity: 5.285** (Bridge: 0.0724 * Flux: 72.948%)
- `jedi/inference/imports.py` -> **Severity: 2.3** (Bridge: 0.03 * Flux: 76.5908%)
- `jedi/inference/compiled/value.py` -> **Severity: 1.849** (Bridge: 0.0335 * Flux: 55.2127%)
- `jedi/inference/gradual/typing.py` -> **Severity: 1.572** (Bridge: 0.0666 * Flux: 23.589%)
- `jedi/inference/base_value.py` -> **Severity: 1.453** (Bridge: 0.0448 * Flux: 32.4464%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `jedi/cache.py` -> **Severity: 25.104** (Embedded: 0.3138 * Error Risk: 80.0%)
- `jedi/inference/lazy_value.py` -> **Severity: 23.093** (Embedded: 0.3245 * Error Risk: 71.1587%)
- `jedi/inference/names.py` -> **Severity: 23.007** (Embedded: 0.3835 * Error Risk: 59.9867%)
- `jedi/inference/utils.py` -> **Severity: 22.958** (Embedded: 0.3189 * Error Risk: 71.992%)
- `jedi/inference/base_value.py` -> **Severity: 20.771** (Embedded: 0.4415 * Error Risk: 47.0452%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `jedi/inference/base_value.py` -> **Severity: 8986.123** (Blast Radius: 89.898 * Doc Risk: 99.9591%)
- `jedi/inference/gradual/typing.py` -> **Severity: 6268.985** (Blast Radius: 64.914 * Doc Risk: 96.5737%)
- `jedi/inference/names.py` -> **Severity: 4381.6** (Blast Radius: 43.816 * Doc Risk: 100.0%)
- `jedi/inference/cache.py` -> **Severity: 3537.674** (Blast Radius: 36.886 * Doc Risk: 95.9083%)
- `jedi/inference/utils.py` -> **Severity: 3377.758** (Blast Radius: 33.794 * Doc Risk: 99.9514%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
