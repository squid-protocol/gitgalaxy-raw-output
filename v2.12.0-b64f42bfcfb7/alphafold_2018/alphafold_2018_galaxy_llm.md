# ARCHITECTURAL_BRIEF: alphafold_2018
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/google-deepmind/deepmind-research.git` |
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
- **Scope:** 21 analyzed artifact(s), 1771 LOC.
- **Load-bearing artifact:** `alphafold_casp13/config_dict.py` -- 1 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `README.md` -- pulls in 65 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `alphafold_casp13/contacts_network.py` at magnitude 406.16 (structural weight, not risk).
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
| Total Artifacts | 148 |
| Analyzed Artifacts (Scanned) | 21 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 127 |
| Total LOC | 1771 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 14.2% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 14 | 1678 | 66.7% |
| MARKDOWN | 3 | 0 | 14.3% |
| PLAINTEXT | 2 | 0 | 9.5% |
| YAML | 1 | 31 | 4.8% |
| SHELL | 1 | 62 | 4.8% |

## 4.1 SOURCE ENCODINGS
All 21 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Micro Repo (<30 files)`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Micro Repo (<30 files)` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 33%, Large Core Modules (3) 19%, Many-Argument Workhorses Files 19%, Large Core Modules (2) 10%, Parameter Forwarders Files 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 16 | 76.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 23.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 127*

**Composition by Extension & Reason:**
- `.ipynb`: 37x Excluded (Unsupported Extension: '.ipynb')
- `.py`: 19x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.png`: 18x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 5x Excluded (Unsupported Extension: '.data-00000-of-00001'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.npz`: 6x Excluded (Unsupported Extension: '.npz')
- `.index`: 5x Excluded (Unsupported Extension: '.index')
- `.dat`: 5x Excluded (Unsupported Extension: '.dat')
- `.sh`: 5x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.obj`: 4x Excluded (Explicitly Denied Extension: '.obj')
- `.txt`: 2x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Lexical Monotony: High structural repetition detected in 29427 LOC)
- `.gif`: 3x Excluded (Explicitly Denied Extension: '.gif')
- `.bazel`: 2x Excluded (Unsupported Extension: '.bazel')
- `.pickle`: 2x Excluded (Unsupported Extension: '.pickle')
- `.tfrecords`: 2x Excluded (Unsupported Extension: '.tfrecords')
- `.p`: 2x Excluded (Unsupported Extension: '.p')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 60.3 | 33.0 | 42.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 87.7 | 61.2 | 66.8 | 50.7 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 38.7 | 24.3 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 31.5 | 2.5 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 7.9 | 4.2 | 5.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 99.3 | 6.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 84.6 | 100.0 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 50.0 | 25.8 | 22.5 | 50.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 39 | 8 | 8 | `alphafold_casp13/contacts_dataset.py` |
| cleanup | 0 | 0 | 0 | - |
| guards | 75 | 9 | 9 | `alphafold_casp13/contacts_network.py` |
| danger | 37 | 8 | 5 | `alphafold_casp13/contacts_dataset.py` |
| concurrency | 5 | 1 | 0 | `alphafold_casp13/run_eval.sh` |
| connectivity | 54 | 13 | 6 | `alphafold_casp13/contacts_dataset.py` |
| io | 23 | 6 | 5 | `alphafold_casp13/paste_contact_maps.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 7 | 2 | 0 | `alphafold_casp13/contacts.py` |
| serialization | 1 | 1 | 0 | `alphafold_casp13/parsers.py` |
| regex | 0 | 0 | 0 | - |
| events | 44 | 7 | 8 | `alphafold_casp13/contacts.py` |
| tests | 32 | 1 | 0 | `alphafold_casp13/contacts.py` |
| docs | 64 | 13 | 7 | `alphafold_casp13/contacts_network.py` |
| debt | 10 | 2 | 0 | `alphafold_casp13/run_eval.sh` |
| mutation | 1147 | 15 | 150 | `alphafold_casp13/contacts_network.py` |
| dead_code | 29 | 10 | 4 | `alphafold_casp13/config_dict.py` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
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
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **config_dict.py** (`alphafold_casp13/config_dict.py`) — 1 inbound connections
2. **.travis.yml** (`.travis.yml`) — 0 inbound connections
3. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 inbound connections
4. **README.md** (`README.md`) — 0 inbound connections
5. **README.md** (`alphafold_casp13/README.md`) — 0 inbound connections

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
- `__init__` **(Stateful Encapsulated Methods)** (@ `alphafold_casp13/contacts_network.py`) -> Impact: **28.1** | LOC: 61
- `make_sep_res_layer` **(Many-Argument Workhorses)** (@ `alphafold_casp13/two_dim_resnet.py`) -> Impact: **28.0** | LOC: 95

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `alphafold_casp13` | 17 | 1938.88 | 31.06% | 31.63% |
| `__monolith__` | 4 | 17.42 | 0.0% | 20.44% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `alphafold_casp13/config_dict.py` -> **99.9925%** Exposure
- `alphafold_casp13/secstruct.py` -> **99.593%** Exposure
- `alphafold_casp13/distogram_io.py` -> **99.3614%** Exposure
- `.travis.yml` -> **81.7574%** Exposure
- `alphafold_casp13/asa_output.py` -> **81.7574%** Exposure
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

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `alphafold_casp13/contacts_network.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.301)
- **Top Global Matches:** file_cluster_12: 7.301, file_cluster_16: 8.377, file_cluster_15: 8.859
- **Magnitude:** 406.16 | **LOC:** 491 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 45.767; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.5%), Complexity Load (formerly Cognitive Load) (44.4%)
- **Documentation Coverage:** 20.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compute_outputs` **(Many-Argument Workhorses)** (Impact: 49.9)
  * `_build_2d_embedding` **(Many-Argument Workhorses)** (Impact: 38.5)
  * `_output_from_pre_logits` **(Many-Argument Workhorses)** (Impact: 33.8)
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 28.1)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` absl, alphafold_casp13, sonnet, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/contacts_dataset.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 11.201)
- **Top Global Matches:** file_cluster_6: 11.201, file_cluster_4: 12.836, file_cluster_12: 16.828
- **Magnitude:** 288.88 | **LOC:** 364 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 45.767; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (41.9%)
- **Documentation Coverage:** 15.3846% of unit weight undocumented
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` collections, enum, json, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/contacts.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 5.928)
- **Top Global Matches:** file_cluster_9: 5.928, file_cluster_15: 10.607, file_cluster_16: 10.847
- **Magnitude:** 288.84 | **LOC:** 394 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 45.767; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (70.6%), Complexity Load (formerly Cognitive Load) (49.6%), Connectivity (formerly Api Exposure) (4.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` absl, alphafold_casp13, collections, numpy, os, six, sonnet, tensorflow...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/contacts_experiment.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.477)
- **Top Global Matches:** file_cluster_16: 6.477, file_cluster_15: 7.202, file_cluster_9: 9.004
- **Magnitude:** 195.3 | **LOC:** 233 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 45.767; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.1%), Complexity Load (formerly Cognitive Load) (45.9%)
- **Documentation Coverage:** 38.4615% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Stateful Encapsulated Methods)** (Impact: 22.6)
  * `_build_evaluation_graph` **(Many-Argument Workhorses)** (Impact: 21.9)
    * *Intent:* """Constructs the graph in pieces so it can be fed."""
  * `get_one_example` **(Defensive Guards)** (Impact: 12.1)
    * *Intent:* """Pull one example off the queue so we can feed it for evaluation."""
  * `_get_feature_normalization` **(Encapsulated Accessors)** (Impact: 5.4)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` absl, alphafold_casp13, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/two_dim_resnet.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.34)
- **Top Global Matches:** file_cluster_9: 6.34, file_cluster_16: 12.289, file_cluster_15: 12.344
- **Magnitude:** 160.18 | **LOC:** 202 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 45.767; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.1%), Complexity Load (formerly Cognitive Load) (47.6%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` absl, alphafold_casp13, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/paste_contact_maps.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.295)
- **Top Global Matches:** file_cluster_12: 8.295, file_cluster_9: 8.934, file_cluster_15: 9.551
- **Magnitude:** 133.12 | **LOC:** 201 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 45.767; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.2%), Complexity Load (formerly Cognitive Load) (43.7%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `paste_distance_histograms` **(Many-Argument Workhorses)** (Impact: 32.3)
  * `generate_domains` **(Many-Argument Workhorses)** (Impact: 14.4)
    * *Intent:* """Take fasta files and generate a domain definition for data generation."""
  * `get_weights` **(Type Conversions)** (Impact: 5.1)
    * *Intent:* """Fetch all the weights from a TFRecord."""
  * `main` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 30`, `args: 5`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 33`
* *Architecture:* `io: 7`, `api: 4`, `import: 9`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` absl, alphafold_casp13, numpy, os, six, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/ensemble_contact_maps.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.264)
- **Top Global Matches:** file_cluster_9: 7.264, file_cluster_12: 12.412, file_cluster_15: 13.197
- **Magnitude:** 110.68 | **LOC:** 125 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 45.767; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (73.8%), Complexity Load (formerly Cognitive Load) (47.7%), Connectivity (formerly Api Exposure) (5.7%)
- **Documentation Coverage:** 16.6667% of unit weight undocumented
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` absl, alphafold_casp13, os, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/two_dim_convnet.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.213)
- **Top Global Matches:** file_cluster_15: 5.213, file_cluster_2: 7.606, file_cluster_16: 7.9
- **Magnitude:** 96.0 | **LOC:** 138 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 45.767; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.4%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_conv_layer` **(Many-Argument Workhorses)** (Impact: 19.8)
  * `make_conv_sep2d_layer` **(Many-Argument Workhorses)** (Impact: 16.6)
  * `conv2d` **(Compute Cores)** (Impact: 7.3)
  * `batch_norm_layer` **(Parameter Forwarders)** (Impact: 5.0)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` absl, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/secstruct.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.514)
- **Top Global Matches:** file_cluster_15: 6.514, file_cluster_11: 6.644, file_cluster_16: 7.346
- **Magnitude:** 61.78 | **LOC:** 93 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 45.767; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.6%), Guard Balance (formerly Safety Score) (72.5%), Complexity Load (formerly Cognitive Load) (29.9%)
- **Documentation Coverage:** 27.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `save_secstructs` **(Many-Argument Workhorses)** (Impact: 11.9)
  * `make_q3_matrices` **(Interface Declarations)** (Impact: 3.5)
    * *Intent:* """Generate mapping matrices for secstruct Q8:Q3 equivalence classes."""
  * `make_layer_new` **(Parameter Forwarders)** (Impact: 2.1)
    * *Intent:* """Make the layer."""
  * `__init__` **(Encapsulated Accessors)** (Impact: 1.9)
  * `get_q8_probs` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 18`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 17`, `unreferenced_by_name: 4`
* *Architecture:* `io: 2`, `api: 5`, `import: 4`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` absl, numpy, os, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/distogram_io.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.26)
- **Top Global Matches:** file_cluster_15: 7.26, file_cluster_2: 8.105, file_cluster_11: 8.328
- **Magnitude:** 48.06 | **LOC:** 98 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 45.767; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.4%), Guard Balance (formerly Safety Score) (51.1%), Complexity Load (formerly Cognitive Load) (28.1%)
- **Documentation Coverage:** 20.0% of unit weight undocumented
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` numpy, os, six.moves.cPickle, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/config_dict.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.593)
- **Top Global Matches:** file_cluster_15: 6.593, file_cluster_16: 7.924, file_cluster_11: 8.02
- **Magnitude:** 40.5 | **LOC:** 63 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 84.668; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (96.1%), Complexity Load (formerly Cognitive Load) (53.3%), Guard Balance (formerly Safety Score) (49.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__init__` **(Defensive Guards)** (Impact: 10.4)
  * `_add` **(Stateful Encapsulated Methods)** (Impact: 6.2)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 84.668
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.05
  * `Imports (Out-Degree: 0):` json
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `alphafold_casp13/test_domains.txt` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 36.42 | **LOC:** 1821 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/run_eval.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.819)
- **Top Global Matches:** file_cluster_2: 3.819, file_cluster_17: 5.572, file_cluster_13: 6.349
- **Magnitude:** 31.94 | **LOC:** 104 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 45.767; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.3%), Mutation Surface (formerly State Flux) (99.1%), Complexity Load (formerly Cognitive Load) (60.3%), Guard Balance (formerly Safety Score) (55.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 9
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 6`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `concurrency: 4`, `import: 1`
* *Defense:* `safety: 1`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` activate
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/parsers.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.399)
- **Top Global Matches:** file_cluster_15: 7.399, file_cluster_9: 7.626, file_cluster_16: 9.155
- **Magnitude:** 22.04 | **LOC:** 67 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 45.767; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (59.5%), Debt Markers (formerly Tech Debt) (37.8%), Complexity Load (formerly Cognitive Load) (8.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `distance_histogram_dict` **(Compute Cores)** (Impact: 11.9)
    * *Intent:* """Parses distance histogram dict pickle. Distance histograms are stored as pickles of dicts. Write ...
  * `parse_distance_histogram_dict` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* """Parses distance histogram piclkle from filepath."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 9`, `args: 2`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` pickle, tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `__init__.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 14 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/asa_output.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.65)
- **Top Global Matches:** file_cluster_15: 5.65, file_cluster_11: 6.773, file_cluster_2: 6.874
- **Magnitude:** 9.22 | **LOC:** 34 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 45.767; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (81.8%), Guard Balance (formerly Safety Score) (51.7%), Mutation Surface (formerly State Flux) (50.0%), Connectivity (formerly Api Exposure) (5.6%)
- **Documentation Coverage:** 16.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compute_asa_output` **(Parameter Forwarders)** (Impact: 2.2)
    * *Intent:* """Just compute the logits and outputs given activations."""
  * `__init__` **(Parameter Forwarders)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 1`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tensorflow
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 8.76 | **LOC:** 438 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.travis.yml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.593)
- **Top Global Matches:** file_cluster_2: 5.593, file_cluster_17: 7.424, file_cluster_15: 7.677
- **Magnitude:** 3.92 | **LOC:** 37 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (81.8%), Guard Balance (formerly Safety Score) (50.7%), Mutation Surface (formerly State Flux) (16.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `before_script` **(I/O & Config Routines)** (Impact: 1.2)
  * `script` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 1`, `planned_debt: 4`
* *Architecture:* `io: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.98 | **LOC:** 99 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **65**; blast radius 45.767; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PrediNet, adversarial_robustness, affordances_theory, alphafold_casp13, avae, bigbigan, box_arrangement, byol...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CONTRIBUTING.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 25 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `alphafold_casp13/requirements.txt` (PLAINTEXT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 1.0 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 45.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `alphafold_casp13/secstruct.py` (PYTHON) | Magnitude: 61.78 | Delta: **0.13** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 18, state_mutation: 17, core_var_decl: 15

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `alphafold_casp13/config_dict.py` -> **Severity: 2.45** (Embedded: 0.05 * Error Risk: 49.0001%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `alphafold_casp13/config_dict.py` -> **Severity: 4233.4** (Blast Radius: 84.668 * Doc Risk: 50.0%)
- `alphafold_casp13/contacts.py` -> **Severity: 2288.35** (Blast Radius: 45.767 * Doc Risk: 50.0%)
- `alphafold_casp13/two_dim_resnet.py` -> **Severity: 2288.35** (Blast Radius: 45.767 * Doc Risk: 50.0%)
- `alphafold_casp13/contacts_experiment.py` -> **Severity: 1760.267** (Blast Radius: 45.767 * Doc Risk: 38.4615%)
- `alphafold_casp13/two_dim_convnet.py` -> **Severity: 1525.565** (Blast Radius: 45.767 * Doc Risk: 33.3333%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 381 call pairs -- scoped 10.2%, unique 0.0%, ambiguous 1.6%, external 88.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| python | 376 | 10.4% | 0.0% | 1.6% | 88.0% |
| shell | 5 | 0.0% | 0.0% | 0.0% | 100.0% |

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
