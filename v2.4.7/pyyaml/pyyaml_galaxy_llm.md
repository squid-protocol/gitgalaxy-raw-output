# ARCHITECTURAL_BRIEF: pyyaml
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/pypi_top_200/pyyaml` |
| **Timestamp** | `2026-08-07T05:25:47.993304+00:00` |
| **Scan Duration** | `0.45s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 30 malicious artifacts.

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
| Total Artifacts | 616 |
| Analyzed Artifacts (Scanned) | 34 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 582 |
| Total LOC | 4345 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 5.5% |
| Dominant Lang | PYTHON |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1652 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6695 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.0199 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PYTHON | 29 | 4083 | 85.3% |
| PLAINTEXT | 2 | 0 | 5.9% |
| MAKEFILE | 1 | 36 | 2.9% |
| MARKDOWN | 1 | 0 | 2.9% |
| YAML | 1 | 226 | 2.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.447`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 25 | 73.5% |
| file_cluster_13 | 6 | 17.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 8.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 582*

**Composition by Extension & Reason:**
- `.data`: 133x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 69x Excluded (Unsupported Extension: '.data')
- `no_extension`: 81x Excluded (Unsupported Extension: '.loader-error'), 16x Excluded (Unsupported Extension: '.emitter-error'), 6x Excluded (Unsupported Extension: '.dumper-error')
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
- `.py`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 78.7 | 17.4 | 9.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 38.7 | 36.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 6.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 2.7 | 0.0 | 0.0 |
| API Exposure | 0.0 | 10.0 | 3.2 | 2.8 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 97.9 | 7.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 21.0 | 1.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.6 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 97.0 | 7.5 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `pyyaml-6.0.3/tests/legacy_tests/test_appliance.py` (Hits: 40)
- `pyyaml-6.0.3/tests/legacy_tests/test_yaml_ext.py` (Hits: 20)
- `pyyaml-6.0.3/setup.py` (Hits: 15)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **yaml.py** (`pyyaml-6.0.3/examples/pygments-lexer/yaml.py`) — 20 inbound connections
2. **test_appliance.py** (`pyyaml-6.0.3/tests/legacy_tests/test_appliance.py`) — 20 inbound connections
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

- `__str__` (@ `pyyaml-6.0.3/yaml/_yaml.pyx`) -> Impact: **649.4** | LOC: 1313
- `scan` (@ `pyyaml-6.0.3/tests/legacy_tests/canonical.py`) -> Impact: **87.6** | LOC: 159
- `execute` (@ `pyyaml-6.0.3/tests/legacy_tests/test_appliance.py`) -> Impact: **84.8** | LOC: 95
- `__init__` (@ `pyyaml-6.0.3/examples/yaml-highlight/yaml_hl.py`) -> Impact: **79.3** | LOC: 104
- `__init__` (@ `pyyaml-6.0.3/setup.py`) -> Impact: **71.9** | LOC: 81
- `test_c_version` (@ `pyyaml-6.0.3/tests/legacy_tests/test_yaml_ext.py`) -> Impact: **68.1** | LOC: 115
- `test_implicit_resolver` (@ `pyyaml-6.0.3/tests/legacy_tests/test_schema.py`) -> Impact: **52.6** | LOC: 93
  * *Intent:* # The tests/data/yaml11.schema file is copied from # https://github.com/perlpunk/yaml-test-schema/blob/master/data/schema-yaml11.yaml
- `_serialize_value` (@ `pyyaml-6.0.3/tests/legacy_tests/test_constructor.py`) -> Impact: **41.5** | LOC: 67
- `test_emitter_on_canonical` (@ `pyyaml-6.0.3/tests/legacy_tests/test_emitter.py`) -> Impact: **39.9** | LOC: 71
- `_make_objects` (@ `pyyaml-6.0.3/tests/legacy_tests/test_constructor.py`) -> Impact: **38.6** | LOC: 217

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `pyyaml-6.0.3/tests/legacy_tests` | 22 | 2040.45 | 12.97% | 0.0% |
| `pyyaml-6.0.3/yaml` | 3 | 917.08 | 21.04% | 0.0% |
| `pyyaml-6.0.3/examples/pygments-lexer` | 2 | 343.84 | 8.22% | 0.0% |
| `pyyaml-6.0.3` | 5 | 223.44 | 5.55% | 39.57% |
| `pyyaml-6.0.3/examples/yaml-highlight` | 1 | 129.38 | 78.71% | 0.0% |
| `pyyaml-6.0.3/packaging` | 1 | 29.82 | 67.74% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `pyyaml-6.0.3/Makefile` -> **100.0%** Exposure
- `pyyaml-6.0.3/setup.py` -> **97.8515%** Exposure
### Highest State Flux (Mutation/Volatility)
- `pyyaml-6.0.3/yaml/_yaml.pyx` -> **97.9488%** Exposure
- `pyyaml-6.0.3/setup.py` -> **96.8759%** Exposure
- `pyyaml-6.0.3/packaging/_pyyaml_pep517.py` -> **27.0976%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `pyyaml-6.0.3/tests/legacy_tests/test_constructor.py` -> **0** Orphaned Functions | **37** Duplicates
- `pyyaml-6.0.3/examples/pygments-lexer/yaml.py` -> **0** Orphaned Functions | **8** Duplicates
- `pyyaml-6.0.3/Makefile` -> **6** Orphaned Functions | **0** Duplicates
- `pyyaml-6.0.3/tests/legacy_tests/test_structure.py` -> **0** Orphaned Functions | **6** Duplicates
- `pyyaml-6.0.3/setup.py` -> **3** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`pyyaml-6.0.3/tests/legacy_tests/test_appliance.py`** -> AI Confidence: **99.33%**
2. **`pyyaml-6.0.3/setup.py`** -> AI Confidence: **99.31%**
3. **`pyyaml-6.0.3/tests/legacy_tests/test_input_output.py`** -> AI Confidence: **99.25%**
4. **`pyyaml-6.0.3/examples/yaml-highlight/yaml_hl.py`** -> AI Confidence: **99.23%**
5. **`pyyaml-6.0.3/tests/legacy_tests/test_yaml_ext.py`** -> AI Confidence: **99.08%**
6. **`pyyaml-6.0.3/tests/legacy_tests/test_schema.py`** -> AI Confidence: **99.05%**
7. **`pyyaml-6.0.3/tests/legacy_tests/test_canonical.py`** -> AI Confidence: **99.01%**
8. **`pyyaml-6.0.3/tests/legacy_tests/test_tokens.py`** -> AI Confidence: **99.01%**
9. **`pyyaml-6.0.3/tests/legacy_tests/test_yaml.py`** -> AI Confidence: **99.01%**
10. **`pyyaml-6.0.3/examples/pygments-lexer/yaml.py`** -> AI Confidence: **98.98%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `145` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `pyyaml-6.0.3/setup.py` (PYTHON) -> Cumulative Risk: **559.73**
- **Archetype:** `file_cluster_13` (Distance: 11.653 IQR)
- **Magnitude:** 196.76 | **LOC:** 360 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (97.8515%), State Flux (96.8759%), Verification (80.0%)
- **Heaviest Functions:** `__init__` (Impact: 71.9), `build_extensions` (Impact: 28.9), `ext_status` (Impact: 11.1)

### 2. `pyyaml-6.0.3/yaml/_yaml.pyx` (PYTHON) -> Cumulative Risk: **417.3**
- **Archetype:** `file_cluster_8` (Distance: 13.083 IQR)
- **Magnitude:** 886.76 | **LOC:** 1398 | **CtrlFlow:** 67.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (97.9488%), Safety Score (67.5896%), Cognitive Load (58.1193%)
- **Heaviest Functions:** `__str__` (Impact: 649.4), `__init__` (Impact: 3.2), `get_version_string` (Impact: 1.9)

### 3. `pyyaml-6.0.3/packaging/_pyyaml_pep517.py` (PYTHON) -> Cumulative Risk: **415.58**
- **Archetype:** `file_cluster_13` (Distance: 9.006 IQR)
- **Magnitude:** 29.82 | **LOC:** 52 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (97.0408%), Safety Score (68.3648%), Cognitive Load (67.7419%)
- **Heaviest Functions:** `_expose_config_settings` (Impact: 8.7), `_bridge_build_meta` (Impact: 5.8), `__exit__` (Impact: 2.3)

### 4. `pyyaml-6.0.3/Makefile` (MAKEFILE) -> Cumulative Risk: **323.06**
- **Archetype:** `file_cluster_8` (Distance: 7.019 IQR)
- **Magnitude:** 19.02 | **LOC:** 52 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (56.0013%), Stability (50.0%)
- **Heaviest Functions:** `dist` (Impact: 1.2), `build` (Impact: 1.1), `buildext` (Impact: 1.1)

### 5. `pyyaml-6.0.3/examples/yaml-highlight/yaml_hl.py` (PYTHON) -> Cumulative Risk: **318.49**
- **Archetype:** `file_cluster_8` (Distance: 11.121 IQR)
- **Magnitude:** 129.38 | **LOC:** 115 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (88.3148%), Cognitive Load (78.7127%), Stability (50.0%)
- **Heaviest Functions:** `__init__` (Impact: 79.3)

### 6. `pyyaml-6.0.3/tests/legacy_tests/canonical.py` (PYTHON) -> Cumulative Risk: **285.25**
- **Archetype:** `file_cluster_8` (Distance: 11.584 IQR)
- **Magnitude:** 345.98 | **LOC:** 362 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (80.3867%), Stability (50.0%), Cognitive Load (44.8393%)
- **Heaviest Functions:** `scan` (Impact: 87.6), `parse_node` (Impact: 18.3), `check_token` (Impact: 10.9)

### 7. `pyyaml-6.0.3/tests/legacy_tests/test_appliance.py` (PYTHON) -> Cumulative Risk: **265.01**
- **Archetype:** `file_cluster_8` (Distance: 11.381 IQR)
- **Magnitude:** 164.68 | **LOC:** 149 | **CtrlFlow:** 72.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (74.7421%), Stability (50.0%), Cognitive Load (35.0924%)
- **Heaviest Functions:** `execute` (Impact: 84.8), `parse_arguments` (Impact: 15.0), `find_test_functions` (Impact: 12.7)

### 8. `pyyaml-6.0.3/tests/legacy_tests/test_yaml.py` (PYTHON) -> Cumulative Risk: **254.03**
- **Archetype:** `file_cluster_13` (Distance: 6.642 IQR)
- **Magnitude:** 15.38 | **LOC:** 24 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (99.7527%), Stability (50.0%), Cognitive Load (4.2806%)

### 9. `pyyaml-6.0.3/tests/legacy_tests/test_constructor.py` (PYTHON) -> Cumulative Risk: **253.8**
- **Archetype:** `file_cluster_8` (Distance: 11.594 IQR)
- **Magnitude:** 282.36 | **LOC:** 305 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (65.0492%), Stability (50.0%), Cognitive Load (34.7315%)
- **Heaviest Functions:** `_serialize_value` (Impact: 41.5), `_make_objects` (Impact: 38.6), `__eq__` (Impact: 5.4)

### 10. `pyyaml-6.0.3/tests/legacy_tests/test_multi_constructor.py` (PYTHON) -> Cumulative Risk: **239.8**
- **Archetype:** `file_cluster_8` (Distance: 9.665 IQR)
- **Magnitude:** 29.88 | **LOC:** 66 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (80.0%), Stability (50.0%), Cognitive Load (5.0613%)
- **Heaviest Functions:** `test_multi_constructor` (Impact: 11.3), `myconstructor2` (Impact: 8.7), `myconstructor1` (Impact: 2.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `pyyaml-6.0.3/yaml/_yaml.pyx` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.083 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.881 IQR)
- **Top Global Matches:** file_cluster_8: 13.083, file_cluster_0: 13.204, file_cluster_9: 13.244
- **Magnitude:** 886.76 | **LOC:** 1398 | **CtrlFlow:** 67.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.1193%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__str__` (Impact: 649.4)
  * `__init__` (Impact: 3.2)
  * `get_version_string` (Impact: 1.9)
  * `get_version` (Impact: 1.9)
  * `get_snippet` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 336`, `structural_boundaries: 160`, `args: 29`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 181`, `dead_code: 26`
* *Architecture:* `io: 1`, `api: 24`, `import: 1`
* *Defense:* `safety: 11`, `test: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.795
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` yaml
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyyaml-6.0.3/tests/legacy_tests/canonical.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.584 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 3.187 IQR)
- **Top Global Matches:** file_cluster_8: 11.584, file_cluster_13: 12.038, file_cluster_7: 12.099
- **Magnitude:** 345.98 | **LOC:** 362 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.8393%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `scan` (Impact: 87.6)
  * `parse_node` (Impact: 18.3)
    * *Intent:* # node: ALIAS | ANCHOR? TAG? (SCALAR|sequence|mapping)
  * `check_token` (Impact: 10.9)
  * `check_event` (Impact: 10.9)
  * `parse_stream` (Impact: 7.4)
    * *Intent:* # stream: STREAM-START document* STREAM-END
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 59`, `args: 30`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 100`, `duplicate_logic: 3`
* *Architecture:* `api: 36`, `import: 1`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.93
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.090074
  * `Imports (Out-Degree: 1):` yaml, yaml.composer, yaml.resolver, yaml.constructor
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/examples/pygments-lexer/yaml.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.14 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.095 IQR)
- **Top Global Matches:** file_cluster_8: 10.14, file_cluster_7: 10.175, file_cluster_13: 10.5
- **Magnitude:** 324.32 | **LOC:** 432 | **CtrlFlow:** 61.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.191%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `callback` (Impact: 26.9)
  * `save_indent` (Impact: 23.6)
  * `callback` (Impact: 22.6)
  * `callback` (Impact: 20.8)
  * `parse_block_scalar_empty_line` (Impact: 19.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 38`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 28`, `duplicate_logic: 8`
* *Architecture:* `api: 20`, `import: 2`
* *Defense:* `doc: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 192.821
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.598416
  * `Imports (Out-Degree: 0):` pygments.token, pygments.lexer
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_tokens.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.01%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.629 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.215 IQR)
- **Top Global Matches:** file_cluster_8: 10.629, file_cluster_13: 10.677, file_cluster_0: 11.168
- **Magnitude:** 312.69 | **LOC:** 81 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.3805%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 10`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`
* *Architecture:* `io: 3`, `api: 2`, `import: 3`
* *Defense:* `safety: 7`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.413
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.081699
  * `Imports (Out-Degree: 2):` yaml, pprint, test_appliance
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_constructor.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.594 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.296 IQR)
- **Top Global Matches:** file_cluster_8: 11.594, file_cluster_13: 11.648, file_cluster_0: 11.952
- **Magnitude:** 282.36 | **LOC:** 305 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.7315%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_serialize_value` (Impact: 41.5)
  * `_make_objects` (Impact: 38.6)
  * `__eq__` (Impact: 5.4)
  * `__eq__` (Impact: 5.4)
  * `__eq__` (Impact: 5.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 150`, `args: 51`, `func_start: 51`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 43`, `duplicate_logic: 37`
* *Architecture:* `io: 5`, `api: 36`, `import: 7`
* *Defense:* `safety: 16`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.481
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.105882
  * `Imports (Out-Degree: 2):` test_appliance, sys, yaml.tokens, datetime, signal, test_constructor, yaml, pprint
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/setup.py` (PYTHON | Tier 1 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.653 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.446 IQR)
- **Top Global Matches:** file_cluster_13: 11.653, file_cluster_0: 11.9, file_cluster_8: 11.982
- **Magnitude:** 196.76 | **LOC:** 360 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.1689%), Tech Debt (97.8515%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 71.9)
  * `build_extensions` (Impact: 28.9)
  * `ext_status` (Impact: 11.1)
  * `has_ext_modules` (Impact: 9.1)
  * `__init__` (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 64`, `args: 13`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 39`, `dead_code: 2`, `fragile_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `io: 15`, `api: 16`, `import: 12`
* *Defense:* `safety: 22`, `doc: 4`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.795
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` setuptools.command.build_ext, os.path, Cython.Distutils, sys, setuptools, wheel.bdist_wheel, distutils, _pyyaml_pep517...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyyaml-6.0.3/tests/legacy_tests/test_yaml_ext.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.073 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.133 IQR)
- **Top Global Matches:** file_cluster_8: 11.073, file_cluster_13: 11.351, file_cluster_0: 11.574
- **Magnitude:** 184.74 | **LOC:** 295 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.3598%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_c_version` (Impact: 68.1)
  * `wrap_ext_function` (Impact: 20.8)
  * `test_large_file` (Impact: 9.3)
  * `test_c_emitter` (Impact: 6.2)
  * `wrapper` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 89`, `args: 29`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 9`
* *Architecture:* `io: 20`, `api: 25`, `import: 5`
* *Defense:* `safety: 36`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 29.018
  * `Choke Point (Betweenness):` 0.012181 | `Ripple Effect (Closeness):` 0.066176
  * `Imports (Out-Degree: 7):` tempfile, test_appliance, test_resolver, sys, os, test_errors, test_tokens, test_constructor...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_structure.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.294 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.429 IQR)
- **Top Global Matches:** file_cluster_8: 11.294, file_cluster_13: 11.598, file_cluster_0: 11.761
- **Magnitude:** 166.04 | **LOC:** 200 | **CtrlFlow:** 48.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.2454%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_convert_structure` (Impact: 22.2)
  * `test_structure` (Impact: 19.2)
  * `_compare_events` (Impact: 18.6)
  * `test_composer` (Impact: 14.8)
  * `test_parser` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 58`, `args: 18`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 11`, `duplicate_logic: 6`
* *Architecture:* `io: 10`, `api: 13`, `import: 3`
* *Defense:* `safety: 27`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.413
  * `Choke Point (Betweenness):` 0.003476 | `Ripple Effect (Closeness):` 0.081699
  * `Imports (Out-Degree: 3):` yaml, pprint, canonical, test_appliance
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_appliance.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.33%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.381 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.457 IQR)
- **Top Global Matches:** file_cluster_8: 11.381, file_cluster_13: 11.65, file_cluster_0: 11.69
- **Magnitude:** 164.68 | **LOC:** 149 | **CtrlFlow:** 72.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.0924%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `execute` (Impact: 84.8)
  * `parse_arguments` (Impact: 15.0)
  * `find_test_functions` (Impact: 12.7)
  * `find_test_filenames` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 21`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 36`
* *Architecture:* `io: 40`, `api: 6`, `import: 1`
* *Defense:* `safety: 8`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 163.967
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.589572
  * `Imports (Out-Degree: 0):` os.path, sys, traceback, pathlib, os, pprint, types
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/examples/yaml-highlight/yaml_hl.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.121 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.062 IQR)
- **Top Global Matches:** file_cluster_8: 11.121, file_cluster_13: 11.466, file_cluster_17: 11.59
- **Magnitude:** 129.38 | **LOC:** 115 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.7127%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__init__` (Impact: 79.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 9`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 45`
* *Architecture:* `io: 6`, `api: 3`, `import: 1`
* *Defense:* `safety: 1`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.795
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` os.path, sys, yaml, codecs, optparse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyyaml-6.0.3/tests/legacy_tests/test_schema.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.05%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.419 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.079 IQR)
- **Top Global Matches:** file_cluster_8: 9.419, file_cluster_13: 9.717, file_cluster_7: 10.122
- **Magnitude:** 95.08 | **LOC:** 153 | **CtrlFlow:** 53.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.6603%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_implicit_resolver` (Impact: 52.6)
    * *Intent:* # The tests/data/yaml11.schema file is copied from # https://github.com/perlpunk/yaml-test-schema/bl...
  * `check_float` (Impact: 16.4)
  * `check_bool` (Impact: 9.1)
  * `check_int` (Impact: 3.8)
  * `check_str` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 33`, `args: 6`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `dead_code: 1`
* *Architecture:* `io: 4`, `api: 5`, `import: 5`
* *Defense:* `safety: 4`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.889
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.044118
  * `Imports (Out-Degree: 2):` test_appliance, sys, yaml, math, pprint
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_input_output.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.528 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.802 IQR)
- **Top Global Matches:** file_cluster_8: 10.528, file_cluster_13: 11.044, file_cluster_7: 11.276
- **Magnitude:** 84.54 | **LOC:** 142 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.2668%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_unicode_output` (Impact: 20.7)
  * `test_file_output` (Impact: 16.9)
  * `test_unicode_input_errors` (Impact: 16.7)
  * `test_unicode_transfer` (Impact: 14.9)
  * `test_unicode_input` (Impact: 7.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 38`, `args: 5`, `func_start: 5`
* *Risk/State:* None
* *Architecture:* `io: 13`, `api: 5`, `import: 3`
* *Defense:* `safety: 27`, `test: 23`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.889
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.044118
  * `Imports (Out-Degree: 2):` tempfile, os.path, test_appliance, os, io, yaml, codecs
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_resolver.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.91%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.221 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.46 IQR)
- **Top Global Matches:** file_cluster_8: 11.221, file_cluster_13: 11.322, file_cluster_0: 11.651
- **Magnitude:** 71.68 | **LOC:** 99 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.5317%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_implicit_resolver` (Impact: 16.9)
  * `test_path_resolver_loader` (Impact: 14.7)
  * `test_path_resolver_dumper` (Impact: 12.7)
  * `_convert_node` (Impact: 11.0)
  * `_make_path_loader_and_dumper` (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 28`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 7`
* *Architecture:* `io: 6`, `api: 5`, `import: 3`
* *Defense:* `safety: 15`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.413
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.081699
  * `Imports (Out-Degree: 2):` yaml, pprint, test_appliance
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_emitter.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.769 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.876 IQR)
- **Top Global Matches:** file_cluster_8: 10.769, file_cluster_13: 11.036, file_cluster_0: 11.339
- **Magnitude:** 68.2 | **LOC:** 105 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.7726%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_emitter_on_canonical` (Impact: 39.9)
  * `_compare_events` (Impact: 11.0)
  * `test_emitter_on_data` (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 20`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`
* *Architecture:* `io: 4`, `api: 6`, `import: 2`
* *Defense:* `safety: 14`, `test: 13`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.956
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.088235
  * `Imports (Out-Degree: 2):` yaml, test_appliance
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_errors.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.694 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.998 IQR)
- **Top Global Matches:** file_cluster_8: 10.694, file_cluster_13: 10.881, file_cluster_7: 11.4
- **Magnitude:** 48.76 | **LOC:** 72 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.7818%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_loader_error_single` (Impact: 16.7)
  * `test_loader_error` (Impact: 16.6)
  * `test_dumper_error` (Impact: 9.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 20`, `args: 5`, `func_start: 5`
* *Risk/State:* None
* *Architecture:* `io: 5`, `api: 5`, `import: 4`
* *Defense:* `safety: 10`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.413
  * `Choke Point (Betweenness):` 0.001842 | `Ripple Effect (Closeness):` 0.081699
  * `Imports (Out-Degree: 3):` yaml, test_emitter, test_appliance, io
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_recursive.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.75%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.764 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.67 IQR)
- **Top Global Matches:** file_cluster_8: 10.764, file_cluster_13: 10.845, file_cluster_0: 11.3
- **Magnitude:** 30.02 | **LOC:** 53 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.0936%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_recursive` (Impact: 9.7)
  * `__repr__` (Impact: 3.8)
  * `__init__` (Impact: 2.1)
  * `__getstate__` (Impact: 1.8)
  * `__setstate__` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 14`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 1`, `api: 7`, `import: 2`
* *Defense:* `safety: 5`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.889
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.044118
  * `Imports (Out-Degree: 2):` yaml, test_appliance
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_multi_constructor.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.76%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.665 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.637 IQR)
- **Top Global Matches:** file_cluster_8: 9.665, file_cluster_13: 9.806, file_cluster_0: 10.373
- **Magnitude:** 29.88 | **LOC:** 66 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0613%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_multi_constructor` (Impact: 11.3)
  * `myconstructor2` (Impact: 8.7)
  * `myconstructor1` (Impact: 2.1)
  * `_load_code` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 20`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`
* *Architecture:* `io: 2`, `api: 5`, `import: 4`
* *Defense:* `safety: 6`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.889
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.044118
  * `Imports (Out-Degree: 2):` yaml, pprint, test_appliance, sys
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/packaging/_pyyaml_pep517.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.006 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.723 IQR)
- **Top Global Matches:** file_cluster_13: 9.006, file_cluster_8: 9.456, file_cluster_0: 9.601
- **Magnitude:** 29.82 | **LOC:** 52 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.7419%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_expose_config_settings` (Impact: 8.7)
  * `_bridge_build_meta` (Impact: 5.8)
  * `__exit__` (Impact: 2.3)
  * `__init__` (Impact: 1.8)
  * `__enter__` (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 19`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`
* *Architecture:* `io: 1`, `api: 6`, `import: 6`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.029412
  * `Imports (Out-Degree: 0):` inspect, sys, setuptools, contextlib, functools
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_canonical.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 99.01%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.883 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 5.969 IQR)
- **Top Global Matches:** file_cluster_8: 9.883, file_cluster_13: 10.227, file_cluster_7: 10.656
- **Magnitude:** 28.78 | **LOC:** 44 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.3427%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_canonical_error` (Impact: 10.5)
  * `test_canonical_scanner` (Impact: 7.3)
  * `test_canonical_parser` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 11`, `args: 3`, `func_start: 3`
* *Risk/State:* None
* *Architecture:* `io: 3`, `api: 3`, `import: 2`
* *Defense:* `safety: 4`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.889
  * `Choke Point (Betweenness):` 0.001099 | `Ripple Effect (Closeness):` 0.044118
  * `Imports (Out-Degree: 3):` yaml, test_appliance, canonical
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_reader.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.969 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 5.689 IQR)
- **Top Global Matches:** file_cluster_8: 8.969, file_cluster_13: 9.325, file_cluster_7: 9.804
- **Magnitude:** 25.54 | **LOC:** 39 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.135%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_stream_error` (Impact: 14.7)
  * `_run_reader` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 12`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `io: 4`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.889
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.044118
  * `Imports (Out-Degree: 1):` test_appliance, yaml.reader
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/tests/legacy_tests/test_representer.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.237 IQR)
- **Local Micro-Species:** `Cluster 3: Data Pipelines & I/O Operations` (Drift: 6.296 IQR)
- **Top Global Matches:** file_cluster_8: 9.237, file_cluster_13: 9.477, file_cluster_7: 10.059
- **Magnitude:** 20.68 | **LOC:** 45 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.2819%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_representer_types` (Impact: 18.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 4`
* *Defense:* `safety: 5`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.889
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.044118
  * `Imports (Out-Degree: 3):` yaml, test_constructor, pprint, test_appliance
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `pyyaml-6.0.3/yaml/_yaml.pxd` (PYTHON | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.434 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.266 IQR)
- **Top Global Matches:** file_cluster_8: 4.434, file_cluster_7: 6.207, file_cluster_1: 6.312
- **Magnitude:** 19.8 | **LOC:** 259 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `safety: 5`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.795
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyyaml-6.0.3/examples/pygments-lexer/example.yaml` (YAML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.992 IQR)
- **Top Global Matches:** file_cluster_8: 6.992, file_cluster_7: 7.998, file_cluster_1: 8.194
- **Magnitude:** 19.52 | **LOC:** 303 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.2495%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.795
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyyaml-6.0.3/Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.019 IQR)
- **Top Global Matches:** file_cluster_8: 7.019, file_cluster_7: 8.117, file_cluster_1: 8.251
- **Magnitude:** 19.02 | **LOC:** 52 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.5892%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `dist` (Impact: 1.2)
  * `build` (Impact: 1.1)
  * `buildext` (Impact: 1.1)
  * `force` (Impact: 1.1)
  * `forceext` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `func_start: 12`
* *Risk/State:* `orphaned_logic: 6`
* *Architecture:* `api: 5`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.795
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pyyaml-6.0.3/tests/legacy_tests/test_build_ext.py` (PYTHON | Tier 1.5 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.027 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 6.732 IQR)
- **Top Global Matches:** file_cluster_13: 9.027, file_cluster_8: 9.398, file_cluster_7: 10.107
- **Magnitude:** 16.16 | **LOC:** 12 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 4`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.795
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` test_yaml_ext, test_appliance, sys, os, distutils.util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `pyyaml-6.0.3/tests/legacy_tests/test_dump_load.py` (PYTHON) | Magnitude: 10.78 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 10, test: 9, safety: 5
- `pyyaml-6.0.3/setup.py` (PYTHON) | Magnitude: 196.76 | Delta: **0.247 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 228, structural_boundaries: 64, branch: 61, state_mutation: 39
- `pyyaml-6.0.3/tests/legacy_tests/test_build_ext.py` (PYTHON) | Magnitude: 16.16 | Delta: **0.371 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 7, io: 4, structural_boundaries: 2, state_mutation: 2
- `pyyaml-6.0.3/packaging/_pyyaml_pep517.py` (PYTHON) | Magnitude: 29.82 | Delta: **0.45 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 19, encapsulation: 15, args: 6
- `pyyaml-6.0.3/tests/legacy_tests/test_yaml.py` (PYTHON) | Magnitude: 15.38 | Delta: **0.526 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 33, import: 17, safety_bypasses: 16, encapsulation: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `pyyaml-6.0.3/tests/legacy_tests/test_sort_keys.py` (PYTHON) | Magnitude: 12.5 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 10, branch: 5, test: 5
- `pyyaml-6.0.3/examples/pygments-lexer/yaml.py` (PYTHON) | Magnitude: 324.32 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 258, branch: 61, structural_boundaries: 38, state_mutation: 28
- `pyyaml-6.0.3/tests/legacy_tests/test_tokens.py` (PYTHON) | Magnitude: 312.69 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, branch: 15, structural_boundaries: 10, safety: 7
- `pyyaml-6.0.3/tests/legacy_tests/test_constructor.py` (PYTHON) | Magnitude: 282.36 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 249, structural_boundaries: 150, encapsulation: 77, args: 51
- `pyyaml-6.0.3/tests/legacy_tests/test_recursive.py` (PYTHON) | Magnitude: 30.02 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 14, api: 7, branch: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pyyaml-6.0.3/tests/legacy_tests/test_appliance.py` -> **Severity: 44.066** (Embedded: 0.5896 * Error Risk: 74.7421%)
- `pyyaml-6.0.3/examples/pygments-lexer/yaml.py` -> **Severity: 40.545** (Embedded: 0.5984 * Error Risk: 67.7537%)
- `pyyaml-6.0.3/tests/legacy_tests/canonical.py` -> **Severity: 7.241** (Embedded: 0.0901 * Error Risk: 80.3867%)
- `pyyaml-6.0.3/tests/legacy_tests/test_constructor.py` -> **Severity: 6.888** (Embedded: 0.1059 * Error Risk: 65.0492%)
- `pyyaml-6.0.3/tests/legacy_tests/test_yaml.py` -> **Severity: 3.912** (Embedded: 0.0392 * Error Risk: 99.7527%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `pyyaml-6.0.3/packaging/_pyyaml_pep517.py` -> **Severity: 2322.477** (Blast Radius: 23.933 * Doc Risk: 97.0408%)
- `pyyaml-6.0.3/Makefile` -> **Severity: 940.542** (Blast Radius: 16.795 * Doc Risk: 56.0013%)
- `pyyaml-6.0.3/setup.py` -> **Severity: 706.218** (Blast Radius: 16.795 * Doc Risk: 42.0493%)
- `pyyaml-6.0.3/yaml/_yaml.pyx` -> **Severity: 346.231** (Blast Radius: 16.795 * Doc Risk: 20.6151%)
- `pyyaml-6.0.3/yaml/_yaml.pxd` -> **Severity: 228.958** (Blast Radius: 16.795 * Doc Risk: 13.6325%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
