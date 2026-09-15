# ARCHITECTURAL_BRIEF: alphafold_2018
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/google-deepmind/deepmind-research.git` |
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
| Total Artifacts | 202 |
| Analyzed Artifacts (Scanned) | 33 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 169 |
| Total LOC | 1753 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 16.3% |
| Dominant Lang | BINARY_THREAT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | n/a (not computed) | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | n/a (not computed) | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 14 | 1678 | 42.4% |
| BINARY_THREAT | 13 | 13 | 39.4% |
| MARKDOWN | 3 | 0 | 9.1% |
| PLAINTEXT | 2 | 0 | 6.1% |
| SHELL | 1 | 62 | 3.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.008`
> **Composition Archetype:** `Small Flat Repo` (z +0.21; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 58%, Many-Argument Workhorses Files 15%, Large Core Modules 9%, Defensive Guards Files 6%, Parameter Forwarders Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 15 | 45.5% |
| Unknown | 13 | 39.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 15.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 169*

**Composition by Extension & Reason:**
- `.py`: 49x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 13x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.ipynb`: 37x Excluded (Unsupported Extension: '.ipynb')
- `.png`: 18x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 5x Excluded (Unsupported Extension: '.data-00000-of-00001'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.npz`: 6x Excluded (Unsupported Extension: '.npz')
- `.index`: 5x Excluded (Unsupported Extension: '.index')
- `.dat`: 5x Excluded (Unsupported Extension: '.dat')
- `.sh`: 5x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.obj`: 4x Excluded (Explicitly Denied Extension: '.obj')
- `.gif`: 3x Excluded (Explicitly Denied Extension: '.gif')
- `.txt`: 1x Excluded (Lexical Monotony: High structural repetition detected in 29427 LOC), 1x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.bazel`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.bazel')
- `.pickle`: 2x Excluded (Unsupported Extension: '.pickle')
- `.tfrecords`: 2x Excluded (Unsupported Extension: '.tfrecords')
- `.p`: 2x Excluded (Unsupported Extension: '.p')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 60.3 | 18.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 42.6 | 27.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 21.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.9 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 7.9 | 2.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 99.3 | 3.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 47.7 | 25.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 46.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 50.0 | 13.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 39 | 8 | 4 | `alphafold_casp13/contacts_dataset.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 75 | 9 | 8 | `alphafold_casp13/contacts_network.py` |
| danger | 37 | 8 | 3 | `alphafold_casp13/contacts_dataset.py` |
| concurrency | 5 | 1 | 0 | `alphafold_casp13/run_eval.sh` |
| connectivity | 54 | 13 | 5 | `alphafold_casp13/contacts_dataset.py` |
| io | 20 | 5 | 2 | `alphafold_casp13/paste_contact_maps.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 7 | 2 | 0 | `alphafold_casp13/contacts.py` |
| serialization | 1 | 1 | 0 | `alphafold_casp13/parsers.py` |
| regex | 0 | 0 | 0 | - |
| events | 44 | 7 | 6 | `alphafold_casp13/contacts.py` |
| tests | 32 | 1 | 0 | `alphafold_casp13/contacts.py` |
| docs | 64 | 13 | 5 | `alphafold_casp13/contacts_network.py` |
| debt | 6 | 1 | 0 | `alphafold_casp13/run_eval.sh` |
| mutation | 1131 | 14 | 134 | `alphafold_casp13/contacts_network.py` |
| dead_code | 29 | 10 | 4 | `alphafold_casp13/config_dict.py` |
| credential | 0 | 0 | 0 | - |
| threat | 7 | 3 | 0 | `alphafold_casp13/config_dict.py` |
| ml_ai | 17 | 12 | 2 | `alphafold_casp13/secstruct.py` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `alphafold_casp13/paste_contact_maps.py` (Hits: 7)
- `alphafold_casp13/contacts.py` (Hits: 5)
- `alphafold_casp13/ensemble_contact_maps.py` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
No file in this repository is imported by another file that GitGalaxy could resolve, so there is no blast-radius ranking to report. That is itself a finding: either the codebase genuinely has no internal dependency structure (a collection of scripts, documents or configuration rather than a coupled system), or its import style is one the engine does not resolve for this language. Do not infer that any file is load-bearing from this section.


### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.md** (`README.md`) — 65 outbound dependencies
2. **contacts.py** (`alphafold_casp13/contacts.py`) — 9 outbound dependencies
3. **paste_contact_maps.py** (`alphafold_casp13/paste_contact_maps.py`) — 6 outbound dependencies
4. **contacts_dataset.py** (`alphafold_casp13/contacts_dataset.py`) — 4 outbound dependencies
5. **contacts_network.py** (`alphafold_casp13/contacts_network.py`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `convert_to_legacy_proteins_dataset_format` **(Many-Argument Workhorses)** (@ `alphafold_casp13/contacts_dataset.py`) -> Impact: **50.1** | LOC: 108
- `make_two_dim_resnet` **(Many-Argument Workhorses)** (@ `alphafold_casp13/two_dim_resnet.py`) -> Impact: **50.0** | LOC: 83
- `compute_outputs` **(Many-Argument Workhorses)** (@ `alphafold_casp13/contacts_network.py`) -> Impact: **49.9** | LOC: 70
- `_build_2d_embedding` **(Many-Argument Workhorses)** (@ `alphafold_casp13/contacts_network.py`) -> Impact: **38.5** | LOC: 77
- `compute_one_prediction` **(Many-Argument Workhorses)** (@ `alphafold_casp13/contacts.py`) -> Impact: **35.0** | LOC: 117
- `_output_from_pre_logits` **(Many-Argument Workhorses)** (@ `alphafold_casp13/contacts_network.py`) -> Impact: **33.8** | LOC: 44
- `paste_distance_histograms` **(Many-Argument Workhorses)** (@ `alphafold_casp13/paste_contact_maps.py`) -> Impact: **32.3** | LOC: 107
- `compute_one_patch` **(Many-Argument Workhorses)** (@ `alphafold_casp13/contacts.py`) -> Impact: **29.2** | LOC: 80
- `__init__` **(Many-Argument Workhorses)** (@ `alphafold_casp13/contacts_network.py`) -> Impact: **28.1** | LOC: 61
- `make_sep_res_layer` **(Many-Argument Workhorses)** (@ `alphafold_casp13/two_dim_resnet.py`) -> Impact: **28.0** | LOC: 95

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `alphafold_casp13` | 17 | 1938.88 | 31.06% | 35.45% |
| `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21` | 3 | 1500.0 | 0.0% | 0.0% |
| `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21m` | 3 | 1500.0 | 0.0% | 0.0% |
| `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21mc` | 3 | 1500.0 | 0.0% | 0.0% |
| `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21mu` | 3 | 1500.0 | 0.0% | 0.0% |
| `catch_carry` | 1 | 500.0 | 0.0% | 0.0% |
| `__monolith__` | 3 | 13.5 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `alphafold_casp13/config_dict.py` -> **99.9972%** Exposure
- `alphafold_casp13/secstruct.py` -> **99.8499%** Exposure
- `alphafold_casp13/distogram_io.py` -> **99.7504%** Exposure
- `alphafold_casp13/asa_output.py` -> **92.4142%** Exposure
- `alphafold_casp13/parsers.py` -> **62.2459%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `alphafold_casp13/contacts.py` -> **100.0%** Exposure
- `alphafold_casp13/contacts_dataset.py` -> **100.0%** Exposure
- `alphafold_casp13/contacts_experiment.py` -> **100.0%** Exposure
- `alphafold_casp13/contacts_network.py` -> **100.0%** Exposure
- `alphafold_casp13/ensemble_contact_maps.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `alphafold_casp13/config_dict.py` -> **6** Orphaned Functions | **0** Duplicates
- `alphafold_casp13/contacts_network.py` -> **4** Orphaned Functions | **0** Duplicates
- `alphafold_casp13/distogram_io.py` -> **4** Orphaned Functions | **0** Duplicates
- `alphafold_casp13/secstruct.py` -> **4** Orphaned Functions | **0** Duplicates
- `alphafold_casp13/contacts_dataset.py` -> **3** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `113` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `alphafold_casp13/two_dim_resnet.py` (PYTHON) -> Cumulative Risk: **492.86**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.56)
- **Magnitude:** 160.18 | **LOC:** 202 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (93.6729%), Verification (80.0%)
- **Heaviest Functions:** `make_two_dim_resnet` (Many-Argument Workhorses, Impact: 50.0), `make_sep_res_layer` (Many-Argument Workhorses, Impact: 28.0)

### 2. `alphafold_casp13/contacts_experiment.py` (PYTHON) -> Cumulative Risk: **487.39**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.21)
- **Magnitude:** 195.3 | **LOC:** 233 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.3385%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Many-Argument Workhorses, Impact: 22.6), `_build_evaluation_graph` (Many-Argument Workhorses, Impact: 21.9), `get_one_example` (Defensive Guards, Impact: 12.1)

### 3. `alphafold_casp13/two_dim_convnet.py` (PYTHON) -> Cumulative Risk: **484.63**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.31)
- **Magnitude:** 96.0 | **LOC:** 138 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9986%), Safety Score (86.4127%), Verification (80.0%)
- **Heaviest Functions:** `make_conv_layer` (Many-Argument Workhorses, Impact: 19.8), `make_conv_sep2d_layer` (Many-Argument Workhorses, Impact: 16.6), `conv2d` (Many-Argument Workhorses, Impact: 7.3)

### 4. `alphafold_casp13/contacts_dataset.py` (PYTHON) -> Cumulative Risk: **476.82**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.14)
- **Magnitude:** 288.88 | **LOC:** 364 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.7556%), Verification (80.0%)
- **Heaviest Functions:** `convert_to_legacy_proteins_dataset_format` (Many-Argument Workhorses, Impact: 50.1), `normalize_from_stats_file` (Many-Argument Workhorses, Impact: 25.0), `dim` (Compute Cores, Impact: 14.1)

### 5. `alphafold_casp13/contacts_network.py` (PYTHON) -> Cumulative Risk: **463.69**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.85)
- **Magnitude:** 406.16 | **LOC:** 491 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.357%), Verification (80.0%)
- **Heaviest Functions:** `compute_outputs` (Many-Argument Workhorses, Impact: 49.9), `_build_2d_embedding` (Many-Argument Workhorses, Impact: 38.5), `_output_from_pre_logits` (Many-Argument Workhorses, Impact: 33.8)

### 6. `alphafold_casp13/secstruct.py` (PYTHON) -> Cumulative Risk: **463.02**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.61)
- **Magnitude:** 61.78 | **LOC:** 93 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8499%), Safety Score (96.2929%)
- **Heaviest Functions:** `save_secstructs` (Many-Argument Workhorses, Impact: 11.9), `make_q3_matrices` (Interface Declarations, Impact: 3.5), `make_layer_new` (Parameter Forwarders, Impact: 2.1)

### 7. `alphafold_casp13/config_dict.py` (PYTHON) -> Cumulative Risk: **462.56**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z +0.51)
- **Magnitude:** 40.5 | **LOC:** 63 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9972%), State Flux (96.0834%), Safety Score (55.5485%)
- **Heaviest Functions:** `__init__` (Defensive Guards, Impact: 10.4), `_add` (Defensive Guards, Impact: 6.2), `__setattr__` (Parameter Forwarders, Impact: 2.1)

### 8. `alphafold_casp13/paste_contact_maps.py` (PYTHON) -> Cumulative Risk: **451.78**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +1.01)
- **Magnitude:** 133.12 | **LOC:** 201 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.0627%), Verification (80.0%)
- **Heaviest Functions:** `paste_distance_histograms` (Many-Argument Workhorses, Impact: 32.3), `generate_domains` (Many-Argument Workhorses, Impact: 14.4), `get_weights` (Type Conversions, Impact: 5.1)

### 9. `alphafold_casp13/distogram_io.py` (PYTHON) -> Cumulative Risk: **419.41**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +1.55)
- **Magnitude:** 48.06 | **LOC:** 98 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9993%), Tech Debt (99.7504%), Safety Score (61.3079%)
- **Heaviest Functions:** `save_rr_file` (Defensive Guards, Impact: 7.9), `save_distance_histogram_from_dict` (Defensive Guards, Impact: 5.8), `save_distance_histogram` (Many-Argument Workhorses, Impact: 3.4)

### 10. `alphafold_casp13/contacts.py` (PYTHON) -> Cumulative Risk: **400.1**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.96)
- **Magnitude:** 288.84 | **LOC:** 394 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (93.7137%), Documentation (50.0%)
- **Heaviest Functions:** `compute_one_prediction` (Many-Argument Workhorses, Impact: 35.0), `compute_one_patch` (Many-Argument Workhorses, Impact: 29.2), `_run_evaluation` (Many-Argument Workhorses, Impact: 21.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `catch_carry/mocap_data.h5` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21/saved_model.pb` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21/smart_module.pb` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21/tfhub_module.pb` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21m/saved_model.pb` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21m/smart_module.pb` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21m/tfhub_module.pb` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21mc/saved_model.pb` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21mc/smart_module.pb` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21mc/tfhub_module.pb` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21mu/saved_model.pb` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21mu/smart_module.pb` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `density_functional_approximation_dm21/density_functional_approximation_dm21/checkpoints/DM21mu/tfhub_module.pb` (BINARY_THREAT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 500.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `alphafold_casp13/contacts_network.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 406.16 | **LOC:** 491 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.3522%), Tech Debt (21.8032%)
**Top Internal Functions/Classes:**
  * `compute_outputs` **(Many-Argument Workhorses)** (Impact: 49.9)
  * `_build_2d_embedding` **(Many-Argument Workhorses)** (Impact: 38.5)
  * `_output_from_pre_logits` **(Many-Argument Workhorses)** (Impact: 33.8)
  * `__init__` **(Many-Argument Workhorses)** (Impact: 28.1)
  * `_concatenate_2d` **(Many-Argument Workhorses)** (Impact: 16.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 197
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 37`, `args: 16`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 97`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`, `import: 7`
* *Defense:* `safety: 1`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` absl, alphafold_casp13, sonnet, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/contacts_dataset.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 288.88 | **LOC:** 364 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.8598%), Tech Debt (34.3407%)
**Top Internal Functions/Classes:**
  * `convert_to_legacy_proteins_dataset_format` **(Many-Argument Workhorses)** (Impact: 50.1)
  * `normalize_from_stats_file` **(Many-Argument Workhorses)** (Impact: 25.0)
  * `dim` **(Compute Cores)** (Impact: 14.1)
    * *Intent:* """Determine the type of feature. Args: feature_name: String identifier for the feature to lookup. I...
  * `shape` **(Many-Argument Workhorses)** (Impact: 9.1)
    * *Intent:* """Get the shape for the given feature name. Args: feature_name: String identifier for the feature. ...
  * `parse_tfexample` **(Compute Cores)** (Impact: 8.6)
    * *Intent:* """Read a single TF Example proto and return a subset of its features. Args: raw_data: A serialized ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 27`, `args: 8`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 60`, `unreferenced_by_name: 3`
* *Architecture:* `api: 7`, `import: 4`
* *Defense:* `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections, enum, json, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/contacts.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 288.84 | **LOC:** 394 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.6376%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `compute_one_prediction` **(Many-Argument Workhorses)** (Impact: 35.0)
  * `compute_one_patch` **(Many-Argument Workhorses)** (Impact: 29.2)
  * `_run_evaluation` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `main` **(Compute Cores)** (Impact: 9.3)
  * `evaluate` **(Many-Argument Workhorses)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 50`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 95`
* *Architecture:* `io: 5`, `api: 4`, `import: 14`
* *Defense:* `safety: 8`, `doc: 5`, `test: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` absl, alphafold_casp13, collections, numpy, os, six, sonnet, tensorflow...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/contacts_experiment.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 195.3 | **LOC:** 233 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.8917%), Tech Debt (24.7664%)
**Top Internal Functions/Classes:**
  * `__init__` **(Many-Argument Workhorses)** (Impact: 22.6)
  * `_build_evaluation_graph` **(Many-Argument Workhorses)** (Impact: 21.9)
    * *Intent:* """Constructs the graph in pieces so it can be fed."""
  * `get_one_example` **(Defensive Guards)** (Impact: 12.1)
    * *Intent:* """Pull one example off the queue so we can feed it for evaluation."""
  * `_get_feature_normalization` **(Type Conversions)** (Impact: 5.4)
  * `_int_ph` **(Encapsulated Accessors)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 27`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 58`, `unreferenced_by_name: 2`
* *Architecture:* `api: 5`, `import: 4`
* *Defense:* `safety: 5`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` absl, alphafold_casp13, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/two_dim_resnet.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 160.18 | **LOC:** 202 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.6368%), Tech Debt (17.4135%)
**Top Internal Functions/Classes:**
  * `make_two_dim_resnet` **(Many-Argument Workhorses)** (Impact: 50.0)
  * `make_sep_res_layer` **(Many-Argument Workhorses)** (Impact: 28.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 12`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 27`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` absl, alphafold_casp13, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/paste_contact_maps.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 133.12 | **LOC:** 201 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.6502%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `paste_distance_histograms` **(Many-Argument Workhorses)** (Impact: 32.3)
  * `generate_domains` **(Many-Argument Workhorses)** (Impact: 14.4)
    * *Intent:* """Take fasta files and generate a domain definition for data generation."""
  * `get_weights` **(Type Conversions)** (Impact: 5.1)
    * *Intent:* """Fetch all the weights from a TFRecord."""
  * `main` **(Interface Declarations)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 30`, `args: 5`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 33`
* *Architecture:* `io: 7`, `api: 4`, `import: 9`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` absl, alphafold_casp13, numpy, os, six, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/ensemble_contact_maps.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 110.68 | **LOC:** 125 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.7218%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ensemble_one_distance_histogram` **(Defensive Guards)** (Impact: 17.1)
    * *Intent:* """Average the given pickle_files and dump."""
  * `ensemble_distance_histograms` **(Many-Argument Workhorses)** (Impact: 15.6)
    * *Intent:* """Find all the contact maps in the first dir, then ensemble across dirs."""
  * `main` **(Defensive Guards)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 30`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 22`
* *Architecture:* `io: 5`, `api: 3`, `import: 7`
* *Defense:* `safety: 5`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` absl, alphafold_casp13, os, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/two_dim_convnet.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 96.0 | **LOC:** 138 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.9957%), Tech Debt (50.0%)
**Top Internal Functions/Classes:**
  * `make_conv_layer` **(Many-Argument Workhorses)** (Impact: 19.8)
  * `make_conv_sep2d_layer` **(Many-Argument Workhorses)** (Impact: 16.6)
  * `conv2d` **(Many-Argument Workhorses)** (Impact: 7.3)
  * `batch_norm_layer` **(Many-Argument Workhorses)** (Impact: 5.0)
    * *Intent:* """Batch norm layer."""
  * `weight_variable` **(Type Conversions)** (Impact: 3.7)
    * *Intent:* """Returns the weight variable."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 21`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 14`, `unreferenced_by_name: 2`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` absl, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/secstruct.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 61.78 | **LOC:** 93 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.9344%), Tech Debt (99.8499%)
**Top Internal Functions/Classes:**
  * `save_secstructs` **(Many-Argument Workhorses)** (Impact: 11.9)
  * `make_q3_matrices` **(Interface Declarations)** (Impact: 3.5)
    * *Intent:* """Generate mapping matrices for secstruct Q8:Q3 equivalence classes."""
  * `make_layer_new` **(Parameter Forwarders)** (Impact: 2.1)
    * *Intent:* """Make the layer."""
  * `__init__` **(Encapsulated Accessors)** (Impact: 1.9)
  * `get_q8_probs` **(Interface Declarations)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 18`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 17`, `unreferenced_by_name: 4`
* *Architecture:* `io: 2`, `api: 5`, `import: 4`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` absl, numpy, os, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/distogram_io.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 48.06 | **LOC:** 98 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.0508%), Tech Debt (99.7504%)
**Top Internal Functions/Classes:**
  * `save_rr_file` **(Defensive Guards)** (Impact: 7.9)
  * `save_distance_histogram_from_dict` **(Defensive Guards)** (Impact: 5.8)
    * *Intent:* """Save a distance histogram prediction matrix as a pickle file."""
  * `save_distance_histogram` **(Many-Argument Workhorses)** (Impact: 3.4)
  * `contact_map_from_distogram` **(Type Conversions)** (Impact: 3.4)
    * *Intent:* """Split the boundary bin."""
  * `save_torsions` **(Type Conversions)** (Impact: 2.5)
    * *Intent:* """Save Torsions to a file as pickle of a dict."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 28`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 11`, `unreferenced_by_name: 4`
* *Architecture:* `io: 1`, `api: 5`, `import: 4`
* *Defense:* `safety: 8`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` numpy, os, six.moves.cPickle, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/config_dict.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 40.5 | **LOC:** 63 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.2573%), Tech Debt (99.9972%)
**Top Internal Functions/Classes:**
  * `__init__` **(Defensive Guards)** (Impact: 10.4)
  * `_add` **(Defensive Guards)** (Impact: 6.2)
  * `__setattr__` **(Parameter Forwarders)** (Impact: 2.1)
  * `__setitem__` **(Parameter Forwarders)** (Impact: 2.1)
  * `__getattr__` **(Defensive Guards)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 16`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 6`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 30.303
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` json
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/test_domains.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 36.42 | **LOC:** 1821 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `alphafold_casp13/config_dict.py` -> **Severity: 1515.15** (Blast Radius: 30.303 * Doc Risk: 50.0%)
- `alphafold_casp13/contacts.py` -> **Severity: 1515.15** (Blast Radius: 30.303 * Doc Risk: 50.0%)
- `alphafold_casp13/two_dim_resnet.py` -> **Severity: 1515.15** (Blast Radius: 30.303 * Doc Risk: 50.0%)
- `alphafold_casp13/contacts_experiment.py` -> **Severity: 1165.499** (Blast Radius: 30.303 * Doc Risk: 38.4615%)
- `alphafold_casp13/two_dim_convnet.py` -> **Severity: 1010.099** (Blast Radius: 30.303 * Doc Risk: 33.3333%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
