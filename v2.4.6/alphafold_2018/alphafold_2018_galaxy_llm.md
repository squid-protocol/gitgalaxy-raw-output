# ARCHITECTURAL_BRIEF: alphafold_2018
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/alphafold_2018` |
| **Timestamp** | `2026-08-03T19:23:59.884659+00:00` |
| **Scan Duration** | `0.25s` |
| **Git Branch** | `master` |
| **Git Commit** | `f5de0ede8430809180254ee957abf36ed62579ef` |
| **Git Remote** | `https://github.com/google-deepmind/deepmind-research.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 28 malicious artifacts.

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
| Total Artifacts | 208 |
| Analyzed Artifacts (Scanned) | 33 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 175 |
| Total LOC | 1751 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 15.9% |
| Dominant Lang | BINARY_THREAT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 14 | 1676 | 42.4% |
| BINARY_THREAT | 13 | 13 | 39.4% |
| MARKDOWN | 3 | 0 | 9.1% |
| PLAINTEXT | 2 | 0 | 6.1% |
| SHELL | 1 | 62 | 3.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.573`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unknown | 13 | 39.4% |
| file_cluster_8 | 11 | 33.3% |
| file_cluster_13 | 3 | 9.1% |
| file_cluster_12 | 1 | 3.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 15.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 175*

**Composition by Extension & Reason:**
- `.py`: 53x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 13x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.ipynb`: 35x Excluded (Unsupported Extension: '.ipynb'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 18x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 5x Excluded (Unsupported Extension: '.data-00000-of-00001'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.npz`: 6x Excluded (Unsupported Extension: '.npz')
- `.sh`: 5x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.index`: 5x Excluded (Unsupported Extension: '.index')
- `.dat`: 5x Excluded (Unsupported Extension: '.dat')
- `.obj`: 4x Excluded (Explicitly Denied Extension: '.obj')
- `.gif`: 3x Excluded (Explicitly Denied Extension: '.gif')
- `.txt`: 1x Excluded (Lexical Monotony: High structural repetition detected in 29427 LOC), 1x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.bazel`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.bazel')
- `.pickle`: 2x Excluded (Unsupported Extension: '.pickle')
- `.tfrecords`: 2x Excluded (Unsupported Extension: '.tfrecords')
- `.p`: 2x Excluded (Unsupported Extension: '.p')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 9.9 | 4.6 | 0.0 |
| Error & Exception Exposure | 0.0 | 69.9 | 8.0 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 22.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 26.2 | 1.0 | 0.0 |
| API Exposure | 0.0 | 7.9 | 1.7 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 99.5 | 3.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 24.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 49.3 | 40.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 91.6 | 10.0 | 4.8 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 34.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 28.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `alphafold_casp13/paste_contact_maps.py` (Hits: 7)
- `alphafold_casp13/contacts.py` (Hits: 5)
- `alphafold_casp13/ensemble_contact_maps.py` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 inbound connections
2. **README.md** (`README.md`) — 0 inbound connections
3. **README.md** (`alphafold_casp13/README.md`) — 0 inbound connections
4. **__init__.py** (`__init__.py`) — 0 inbound connections
5. **asa_output.py** (`alphafold_casp13/asa_output.py`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **contacts.py** (`alphafold_casp13/contacts.py`) — 9 outbound dependencies
2. **paste_contact_maps.py** (`alphafold_casp13/paste_contact_maps.py`) — 6 outbound dependencies
3. **contacts_dataset.py** (`alphafold_casp13/contacts_dataset.py`) — 4 outbound dependencies
4. **contacts_network.py** (`alphafold_casp13/contacts_network.py`) — 4 outbound dependencies
5. **distogram_io.py** (`alphafold_casp13/distogram_io.py`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_concatenate_2d` (@ `alphafold_casp13/contacts_network.py`) -> Impact: **600.5** | LOC: 249
- `ensemble_distance_histograms` (@ `alphafold_casp13/ensemble_contact_maps.py`) -> Impact: **256.2** | LOC: 85
- `compute_one_prediction` (@ `alphafold_casp13/contacts.py`) -> Impact: **233.2** | LOC: 220
- `make_sep_res_layer` (@ `alphafold_casp13/two_dim_resnet.py`) -> Impact: **195.0** | LOC: 182
- `_build` (@ `alphafold_casp13/contacts_network.py`) -> Impact: **145.6** | LOC: 95
- `normalize_from_stats_file` (@ `alphafold_casp13/contacts_dataset.py`) -> Impact: **130.7** | LOC: 109
  * *Intent:* # Reshape the tensors according to the sequence length and num alignments. for k, v in parsed_features.items(): new_shape = shape(feature_name=k, num_...
- `weight_variable` (@ `alphafold_casp13/two_dim_convnet.py`) -> Impact: **124.7** | LOC: 70
- `__init__` (@ `alphafold_casp13/contacts_network.py`) -> Impact: **107.7** | LOC: 62
- `batch_norm_layer` (@ `alphafold_casp13/two_dim_convnet.py`) -> Impact: **96.4** | LOC: 50
- `get_weights` (@ `alphafold_casp13/paste_contact_maps.py`) -> Impact: **84.4** | LOC: 112

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `_concatenate_2d` (@ `alphafold_casp13/contacts_network.py`) -> **O(2^N) [Recursive]**
- `weight_variable` (@ `alphafold_casp13/two_dim_convnet.py`) -> **O(2^N) [Recursive]**
- `ensemble_distance_histograms` (@ `alphafold_casp13/ensemble_contact_maps.py`) -> **O(2^N) [Recursive]**
- `batch_norm_layer` (@ `alphafold_casp13/two_dim_convnet.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `alphafold_casp13/contacts_network.py`) -> **O(2^N) [Recursive]**
- `__init__` (@ `alphafold_casp13/config_dict.py`) -> **O(2^N) [Recursive]**
- `make_sep_res_layer` (@ `alphafold_casp13/two_dim_resnet.py`) -> **O(2^N) [Recursive]**
- `__setitem__` (@ `alphafold_casp13/config_dict.py`) -> **O(2^N) [Recursive]**
- `__delitem__` (@ `alphafold_casp13/config_dict.py`) -> **O(2^N) [Recursive]**
- `compute_one_prediction` (@ `alphafold_casp13/contacts.py`) -> **O(N^6)**

### Highest Data Gravity (Database Complexity)
- `_build_evaluation_graph` (@ `alphafold_casp13/contacts_experiment.py`) -> DB Complexity: **30**
- `__init__` (@ `alphafold_casp13/contacts_network.py`) -> DB Complexity: **25**
- `get_weights` (@ `alphafold_casp13/paste_contact_maps.py`) -> DB Complexity: **21**
- `ensemble_distance_histograms` (@ `alphafold_casp13/ensemble_contact_maps.py`) -> DB Complexity: **16**
- `evaluate` (@ `alphafold_casp13/contacts.py`) -> DB Complexity: **15**
  * *Intent:* """Main evaluation loop."""
- `__init__` (@ `alphafold_casp13/contacts_experiment.py`) -> DB Complexity: **14**
  * *Intent:* """Builds the TensorFlow graph."""
- `normalize_from_stats_file` (@ `alphafold_casp13/contacts_dataset.py`) -> DB Complexity: **7**
  * *Intent:* # Reshape the tensors according to the sequence length and num alignments. for k, v in parsed_features.items(): new_shape = shape(feature_name=k, num_...
- `make_layer_new` (@ `alphafold_casp13/secstruct.py`) -> DB Complexity: **6**
- `_build` (@ `alphafold_casp13/contacts_network.py`) -> DB Complexity: **3**
- `save_torsions` (@ `alphafold_casp13/distogram_io.py`) -> DB Complexity: **3**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `alphafold_casp13` | 17 | 2827.84 | 16.02% | 37.62% |
| `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21` | 3 | 1500.0 | 0.0% | 0.0% |
| `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21m` | 3 | 1500.0 | 0.0% | 0.0% |
| `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21mc` | 3 | 1500.0 | 0.0% | 0.0% |
| `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21mu` | 3 | 1500.0 | 0.0% | 0.0% |
| `catch_carry` | 1 | 500.0 | 0.0% | 0.0% |
| `__monolith__` | 3 | 13.5 | 1.67% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `alphafold_casp13/asa_output.py` -> **100.0%** Exposure
- `alphafold_casp13/config_dict.py` -> **99.9998%** Exposure
- `alphafold_casp13/distogram_io.py` -> **99.7504%** Exposure
- `alphafold_casp13/parsers.py` -> **96.3358%** Exposure
- `alphafold_casp13/secstruct.py` -> **96.0144%** Exposure
### Highest State Flux (Mutation/Volatility)
- `alphafold_casp13/contacts_experiment.py` -> **100.0%** Exposure
- `alphafold_casp13/run_eval.sh` -> **99.3286%** Exposure
- `alphafold_casp13/asa_output.py` -> **99.3259%** Exposure
- `alphafold_casp13/secstruct.py` -> **98.3433%** Exposure
- `alphafold_casp13/contacts_network.py` -> **96.6823%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `alphafold_casp13/config_dict.py` -> **5** Orphaned Functions | **0** Duplicates
- `alphafold_casp13/distogram_io.py` -> **4** Orphaned Functions | **0** Duplicates
- `alphafold_casp13/asa_output.py` -> **2** Orphaned Functions | **0** Duplicates
- `alphafold_casp13/contacts_dataset.py` -> **2** Orphaned Functions | **0** Duplicates
- `alphafold_casp13/contacts_network.py` -> **2** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`alphafold_casp13/contacts.py`** -> AI Confidence: **99.24%**
2. **`alphafold_casp13/run_eval.sh`** -> AI Confidence: **99.17%**
3. **`alphafold_casp13/two_dim_resnet.py`** -> AI Confidence: **99.09%**
4. **`alphafold_casp13/contacts_dataset.py`** -> AI Confidence: **99.06%**
5. **`alphafold_casp13/contacts_network.py`** -> AI Confidence: **99.06%**
6. **`alphafold_casp13/parsers.py`** -> AI Confidence: **99.06%**
7. **`alphafold_casp13/two_dim_convnet.py`** -> AI Confidence: **99.06%**
8. **`alphafold_casp13/paste_contact_maps.py`** -> AI Confidence: **99.03%**
9. **`alphafold_casp13/contacts_experiment.py`** -> AI Confidence: **99.0%**
10. **`alphafold_casp13/ensemble_contact_maps.py`** -> AI Confidence: **98.96%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `alphafold_casp13/contacts.py` -> **100.0%** Exposure
- `alphafold_casp13/contacts_dataset.py` -> **100.0%** Exposure
- `alphafold_casp13/contacts_experiment.py` -> **100.0%** Exposure
- `alphafold_casp13/contacts_network.py` -> **100.0%** Exposure
- `alphafold_casp13/ensemble_contact_maps.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `alphafold_casp13/contacts.py` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `alphafold_casp13/contacts.py` -> **100.0%** Exposure
- `alphafold_casp13/contacts_dataset.py` -> **100.0%** Exposure
- `alphafold_casp13/contacts_experiment.py` -> **100.0%** Exposure
- `alphafold_casp13/contacts_network.py` -> **100.0%** Exposure
- `alphafold_casp13/ensemble_contact_maps.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `48` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `alphafold_casp13/contacts_dataset.py` (PYTHON) -> Cumulative Risk: **590.01**
- **Archetype:** `file_cluster_8` (Distance: 10.038 IQR)
- **Magnitude:** 250.36 | **LOC:** 364 | **CtrlFlow:** 64.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (89.9174%)
- **Heaviest Functions:** `normalize_from_stats_file` (Impact: 130.7), `dim` (Impact: 75.2), `shape` (Impact: 8.6)

### 2. `alphafold_casp13/contacts_experiment.py` (PYTHON) -> Cumulative Risk: **588.5**
- **Archetype:** `file_cluster_8` (Distance: 12.06 IQR)
- **Magnitude:** 245.0 | **LOC:** 233 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_build_evaluation_graph` (Impact: 77.8), `__init__` (Impact: 54.1), `_get_feature_normalization` (Impact: 10.6)

### 3. `alphafold_casp13/contacts_network.py` (PYTHON) -> Cumulative Risk: **553.42**
- **Archetype:** `file_cluster_8` (Distance: 10.248 IQR)
- **Magnitude:** 923.96 | **LOC:** 491 | **CtrlFlow:** 59.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (96.6823%)
- **Heaviest Functions:** `_concatenate_2d` (Impact: 600.5), `_build` (Impact: 145.6), `__init__` (Impact: 107.7)

### 4. `alphafold_casp13/secstruct.py` (PYTHON) -> Cumulative Risk: **537.89**
- **Archetype:** `file_cluster_13` (Distance: 10.717 IQR)
- **Magnitude:** 31.88 | **LOC:** 93 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (98.3433%)
- **Heaviest Functions:** `make_layer_new` (Impact: 11.3), `make_q3_matrices` (Impact: 5.8), `__init__` (Impact: 1.9)

### 5. `alphafold_casp13/run_eval.sh` (SHELL) -> Cumulative Risk: **522.26**
- **Archetype:** `file_cluster_12` (Distance: 11.039 IQR)
- **Magnitude:** 34.24 | **LOC:** 104 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Concurrency (99.5016%), State Flux (99.3286%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 9.0), `__global_context__` (Impact: 4.0)

### 6. `alphafold_casp13/contacts.py` (PYTHON) -> Cumulative Risk: **502.71**
- **Archetype:** `file_cluster_8` (Distance: 8.566 IQR)
- **Magnitude:** 317.44 | **LOC:** 394 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `compute_one_prediction` (Impact: 233.2), `evaluate` (Impact: 74.2)

### 7. `alphafold_casp13/two_dim_convnet.py` (PYTHON) -> Cumulative Risk: **483.93**
- **Archetype:** `file_cluster_8` (Distance: 7.86 IQR)
- **Magnitude:** 229.1 | **LOC:** 138 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (91.5665%)
- **Heaviest Functions:** `weight_variable` (Impact: 124.7), `batch_norm_layer` (Impact: 96.4)

### 8. `alphafold_casp13/paste_contact_maps.py` (PYTHON) -> Cumulative Risk: **453.01**
- **Archetype:** `file_cluster_8` (Distance: 9.223 IQR)
- **Magnitude:** 113.42 | **LOC:** 201 | **CtrlFlow:** 40.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Verification (80.0%)
- **Heaviest Functions:** `get_weights` (Impact: 84.4), `generate_domains` (Impact: 14.4), `main` (Impact: 2.2)

### 9. `alphafold_casp13/ensemble_contact_maps.py` (PYTHON) -> Cumulative Risk: **436.2**
- **Archetype:** `file_cluster_13` (Distance: 9.65 IQR)
- **Magnitude:** 263.98 | **LOC:** 125 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Verification (80.0%)
- **Heaviest Functions:** `ensemble_distance_histograms` (Impact: 256.2)

### 10. `alphafold_casp13/parsers.py` (PYTHON) -> Cumulative Risk: **381.54**
- **Archetype:** `file_cluster_8` (Distance: 9.062 IQR)
- **Magnitude:** 49.92 | **LOC:** 67 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9579%), Tech Debt (96.3358%), Safety Score (49.2308%)
- **Heaviest Functions:** `distance_histogram_dict` (Impact: 43.7), `parse_distance_histogram_dict` (Impact: 3.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `alphafold_casp13/contacts_network.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.248 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.283 IQR)
- **Top Global Matches:** file_cluster_8: 10.248, file_cluster_7: 10.588, file_cluster_13: 10.665
- **Magnitude:** 923.96 | **LOC:** 491 | **CtrlFlow:** 59.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (11.0412%), Tech Debt (13.9356%)
**Top Internal Functions/Classes:**
  * `_concatenate_2d` (Impact: 600.5 | O(2^N) | DB: 2)
  * `_build` (Impact: 145.6 | O(N^6) | DB: 3)
  * `__init__` (Impact: 107.7 | O(2^N) | DB: 25)
  * `quant_threshold` (Impact: 2.9 | O(N^2))
  * `call_on_tuple` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 33`, `args: 16`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 52`, `orphaned_logic: 2`
* *Architecture:* `api: 6`, `import: 7`
* *Defense:* `safety: 1`, `doc: 22`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sonnet, tensorflow, absl, alphafold_casp13
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `catch_carry/mocap_data.h5` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21/saved_model.pb` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21/smart_module.pb` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21/tfhub_module.pb` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21m/saved_model.pb` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21m/smart_module.pb` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21m/tfhub_module.pb` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21mc/saved_model.pb` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21mc/smart_module.pb` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21mc/tfhub_module.pb` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21mu/saved_model.pb` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21mu/smart_module.pb` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21mu/tfhub_module.pb` (BINARY_THREAT | Tier 0 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/contacts.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.566 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.606 IQR)
- **Top Global Matches:** file_cluster_8: 8.566, file_cluster_13: 9.176, file_cluster_7: 9.224
- **Magnitude:** 317.44 | **LOC:** 394 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (5.5347%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `compute_one_prediction` (Impact: 233.2 | O(N^6))
  * `evaluate` (Impact: 74.2 | O(N^6) | DB: 15)
    * *Intent:* """Main evaluation loop."""
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 46`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`
* *Architecture:* `io: 5`, `api: 4`, `import: 14`
* *Defense:* `safety: 8`, `doc: 10`, `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` six, sonnet, collections, alphafold_casp13, os, numpy, absl, tensorflow...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/ensemble_contact_maps.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.65 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.601 IQR)
- **Top Global Matches:** file_cluster_13: 9.65, file_cluster_8: 9.736, file_cluster_17: 9.882
- **Magnitude:** 263.98 | **LOC:** 125 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (8.0441%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ensemble_distance_histograms` (Impact: 256.2 | O(2^N) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 29`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `io: 5`, `api: 3`, `import: 7`
* *Defense:* `safety: 5`, `doc: 6`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` os, tensorflow, absl, alphafold_casp13
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/contacts_dataset.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.038 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.425 IQR)
- **Top Global Matches:** file_cluster_8: 10.038, file_cluster_7: 10.326, file_cluster_13: 10.381
- **Magnitude:** 250.36 | **LOC:** 364 | **CtrlFlow:** 64.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (12.627%), Tech Debt (23.6817%)
**Top Internal Functions/Classes:**
  * `normalize_from_stats_file` (Impact: 130.7 | O(N^3) | DB: 7)
    * *Intent:* # Reshape the tensors according to the sequence length and num alignments. for k, v in parsed_featur...
  * `dim` (Impact: 75.2 | O(N^5))
  * `shape` (Impact: 8.6 | O(N^1))
  * `create_tf_dataset` (Impact: 4.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 25`, `args: 8`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 21`, `orphaned_logic: 2`
* *Architecture:* `api: 7`, `import: 4`
* *Defense:* `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tensorflow, collections, json, enum
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/contacts_experiment.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.06 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.183 IQR)
- **Top Global Matches:** file_cluster_8: 12.06, file_cluster_13: 12.165, file_cluster_7: 12.357
- **Magnitude:** 245.0 | **LOC:** 233 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (34.3438%), Tech Debt (15.8869%)
**Top Internal Functions/Classes:**
  * `_build_evaluation_graph` (Impact: 77.8 | O(N^4) | DB: 30)
  * `__init__` (Impact: 54.1 | O(N^4) | DB: 14)
    * *Intent:* """Builds the TensorFlow graph."""
  * `_get_feature_normalization` (Impact: 10.6 | O(N^3))
  * `_int_ph` (Impact: 2.1 | O(N^1))
  * `model` (Impact: 1.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 26`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 90`, `orphaned_logic: 1`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `safety: 5`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tensorflow, absl, alphafold_casp13
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/two_dim_convnet.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.86 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.735 IQR)
- **Top Global Matches:** file_cluster_8: 7.86, file_cluster_7: 8.387, file_cluster_1: 8.642
- **Magnitude:** 229.1 | **LOC:** 138 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.474%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `weight_variable` (Impact: 124.7 | O(2^N))
  * `batch_norm_layer` (Impact: 96.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 17`, `args: 6`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tensorflow, absl
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/two_dim_resnet.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.489 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 2.889 IQR)
- **Top Global Matches:** file_cluster_8: 7.489, file_cluster_7: 8.204, file_cluster_1: 8.425
- **Magnitude:** 200.18 | **LOC:** 202 | **CtrlFlow:** 57.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.8186%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `make_sep_res_layer` (Impact: 195.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 11`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tensorflow, absl, alphafold_casp13
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/paste_contact_maps.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.223 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.508 IQR)
- **Top Global Matches:** file_cluster_8: 9.223, file_cluster_13: 9.236, file_cluster_7: 9.667
- **Magnitude:** 113.42 | **LOC:** 201 | **CtrlFlow:** 40.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (6.4542%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_weights` (Impact: 84.4 | O(N^6) | DB: 21)
  * `generate_domains` (Impact: 14.4 | O(N^1) | DB: 2)
  * `main` (Impact: 2.2 | O(N^1))
    * *Intent:* # Compute the contact map and save it as an RR file. contact_probs = distogram_io.contact_map_from_d...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 28`, `args: 5`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`
* *Architecture:* `io: 7`, `api: 4`, `import: 9`
* *Defense:* `safety: 1`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` six, alphafold_casp13, os, numpy, absl, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/config_dict.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.215 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.404 IQR)
- **Top Global Matches:** file_cluster_8: 11.215, file_cluster_13: 11.363, file_cluster_12: 11.401
- **Magnitude:** 60.3 | **LOC:** 63 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (46.7967%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 30.4 | O(2^N))
  * `_add` (Impact: 6.2 | O(N^1))
  * `__setitem__` (Impact: 4.2 | O(2^N) | DB: 1)
  * `__getattr__` (Impact: 3.7 | O(N^1))
  * `__delitem__` (Impact: 3.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 16`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 4`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` json
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/distogram_io.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.451 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.552 IQR)
- **Top Global Matches:** file_cluster_8: 11.451, file_cluster_13: 11.493, file_cluster_7: 11.77
- **Magnitude:** 52.76 | **LOC:** 98 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (4.7879%), Tech Debt (99.7504%)
**Top Internal Functions/Classes:**
  * `save_rr_file` (Impact: 25.1 | O(N^4))
  * `save_distance_histogram_from_dict` (Impact: 7.6 | O(N^1))
  * `contact_map_from_distogram` (Impact: 5.8 | O(N^2))
  * `save_torsions` (Impact: 4.8 | O(N^1) | DB: 3)
  * `save_distance_histogram` (Impact: 3.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 25`, `args: 5`, `func_start: 5`
* *Risk/State:* `orphaned_logic: 4`
* *Architecture:* `io: 1`, `api: 5`, `import: 4`
* *Defense:* `safety: 8`, `doc: 14`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tensorflow, os, numpy, six.moves.cPickle
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/parsers.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.062 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.002 IQR)
- **Top Global Matches:** file_cluster_8: 9.062, file_cluster_13: 9.235, file_cluster_7: 9.406
- **Magnitude:** 49.92 | **LOC:** 67 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (15.012%), Tech Debt (96.3358%)
**Top Internal Functions/Classes:**
  * `distance_histogram_dict` (Impact: 43.7 | O(N^6) | DB: 2)
  * `parse_distance_histogram_dict` (Impact: 3.7 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 8`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tensorflow, pickle
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/test_domains.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 36.42 | **LOC:** 1821 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `alphafold_casp13/run_eval.sh` (SHELL) | Magnitude: 34.24 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 44, indent_spaces: 36, state_mutation: 11, concurrency: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `alphafold_casp13/ensemble_contact_maps.py` (PYTHON) | Magnitude: 263.98 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 29, branch: 22, import: 7
- `alphafold_casp13/asa_output.py` (PYTHON) | Magnitude: 9.12 | Delta: **0.184 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 6, doc: 6, args: 2
- `alphafold_casp13/secstruct.py` (PYTHON) | Magnitude: 31.88 | Delta: **0.267 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 16, doc: 10, state_mutation: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `alphafold_casp13/paste_contact_maps.py` (PYTHON) | Magnitude: 113.42 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 28, branch: 19, telemetry: 10
- `alphafold_casp13/distogram_io.py` (PYTHON) | Magnitude: 52.76 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 25, doc: 14, branch: 8
- `alphafold_casp13/contacts_experiment.py` (PYTHON) | Magnitude: 245.0 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 173, state_mutation: 90, encapsulation: 77, structural_boundaries: 26
- `alphafold_casp13/config_dict.py` (PYTHON) | Magnitude: 60.3 | Delta: **0.148 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 16, encapsulation: 16, args: 9
- `alphafold_casp13/parsers.py` (PYTHON) | Magnitude: 49.92 | Delta: **0.173 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 8, branch: 7, doc: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `alphafold_casp13/two_dim_convnet.py` -> **Severity: 2774.74** (Blast Radius: 30.303 * Doc Risk: 91.5665%)
- `alphafold_casp13/contacts_network.py` -> **Severity: 1190.669** (Blast Radius: 30.303 * Doc Risk: 39.2921%)
- `alphafold_casp13/contacts_experiment.py` -> **Severity: 599.66** (Blast Radius: 30.303 * Doc Risk: 19.7888%)
- `alphafold_casp13/ensemble_contact_maps.py` -> **Severity: 380.948** (Blast Radius: 30.303 * Doc Risk: 12.5713%)
- `alphafold_casp13/config_dict.py` -> **Severity: 361.221** (Blast Radius: 30.303 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
