# ARCHITECTURAL_BRIEF: catalyst-runtime
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/perl-catalyst/catalyst-runtime.git` |
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
| Total Artifacts | 493 |
| Analyzed Artifacts (Scanned) | 213 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 280 |
| Total LOC | 13096 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 43.2% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8333 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 209 | 12943 | 98.1% |
| PLAINTEXT | 2 | 0 | 0.9% |
| M4 | 1 | 27 | 0.5% |
| JSON | 1 | 126 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 211 | 99.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 0.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 280*

**Composition by Extension & Reason:**
- `.pm`: 254x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pod`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.t`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rc`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mkdn`: 1x Excluded (Unsupported Extension: '.mkdn')
- `.include`: 1x Excluded (Unsupported Extension: '.include')
- `.gif`: 1x Excluded (Explicitly Denied Extension: '.gif')
- `.pl`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 87.6 | 14.8 | 10.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 92.6 | 36.0 | 49.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 12.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.5 | 0.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 12.1 | 2.8 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 33.9 | 17.4 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 20.9 | 0.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 51.7 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 46.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 229 | 65 | 3 | `t/aggregate/unit_core_script_server.t` |
| cleanup | 33 | 18 | 0 | `t/unit_utils_load_class.t` |
| guards | 490 | 203 | 3 | `t/arg_constraints.t` |
| danger | 194 | 77 | 2 | `t/aggregate/live_engine_request_uploads.t` |
| concurrency | 29 | 9 | 0 | `t/live_fork.t` |
| connectivity | 460 | 107 | 6 | `t/arg_constraints.t` |
| io | 35 | 16 | 0 | `t/optional_lighttpd-fastcgi-non-root.t` |
| crypto | 0 | 0 | 0 | - |
| ipc | 24 | 7 | 0 | `t/live_fork.t` |
| time | 16 | 6 | 0 | `t/optional_http-server-restart.t` |
| serialization | 0 | 0 | 0 | - |
| regex | 220 | 74 | 3 | `t/aggregate/live_engine_request_uri.t` |
| events | 30 | 15 | 0 | `t/aggregate/unit_core_setup.t` |
| tests | 2076 | 203 | 22 | `t/aggregate/live_component_controller_action_chained.t` |
| docs | 5 | 5 | 0 | `script/catalyst.pl` |
| debt | 99 | 40 | 1 | `t/aggregate/unit_core_mvc.t` |
| mutation | 923 | 189 | 10 | `Makefile.PL` |
| dead_code | 52 | 27 | 1 | `t/arg_constraints.t` |
| credential | 0 | 0 | 0 | - |
| threat | 160 | 76 | 2 | `t/aggregate/live_component_controller_action_action.t` |
| ml_ai | 135 | 21 | 0 | `t/aggregate/unit_core_setup.t` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `t/optional_lighttpd-fastcgi-non-root.t` (Hits: 6)
- `t/optional_lighttpd-fastcgi.t` (Hits: 6)
- `t/aggregate/unit_core_script_run_options.t` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **utf8.txt** (`t/utf8.txt`) — 11 inbound connections
2. **Changes** (`Changes`) — 0 inbound connections
3. **Makefile.PL** (`Makefile.PL`) — 0 inbound connections
4. **catalyst.pl** (`script/catalyst.pl`) — 0 inbound connections
5. **01use.t** (`t/01use.t`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **arg_constraints.t** (`t/arg_constraints.t`) — 18 outbound dependencies
2. **utf_incoming.t** (`t/utf_incoming.t`) — 17 outbound dependencies
3. **live_engine_request_uploads.t** (`t/aggregate/live_engine_request_uploads.t`) — 15 outbound dependencies
4. **live_component_controller_action_chained.t** (`t/aggregate/live_component_controller_action_chained.t`) — 14 outbound dependencies
5. **psgi-log.t** (`t/psgi-log.t`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `run_tests` (@ `t/aggregate/live_component_controller_action_chained.t`) -> Impact: **279.4** | LOC: 1147
- `run_tests` (@ `t/aggregate/live_component_controller_action_visit.t`) -> Impact: **62.0** | LOC: 259
- `run_tests` (@ `t/aggregate/live_component_controller_action_go.t`) -> Impact: **57.1** | LOC: 242
- `run_tests` (@ `t/aggregate/live_component_controller_action_auto.t`) -> Impact: **40.0** | LOC: 160
- `run_tests` (@ `t/aggregate/live_component_controller_action_action.t`) -> Impact: **37.1** | LOC: 242
- `run_tests` (@ `t/aggregate/live_component_controller_action_forward.t`) -> Impact: **36.7** | LOC: 234
- `run_tests` (@ `t/aggregate/live_component_controller_action_local.t`) -> Impact: **28.3** | LOC: 126
- `run_test_for` (@ `t/aggregate/live_component_controller_args.t`) -> Impact: **26.2** | LOC: 43
- `run_tests` (@ `t/aggregate/live_component_controller_action_default.t`) -> Impact: **22.6** | LOC: 71
- `run_tests` (@ `t/aggregate/live_component_controller_action_path.t`) -> Impact: **21.9** | LOC: 138

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `t/aggregate` | 118 | 2625.24 | 13.14% | 6.72% |
| `t` | 85 | 2331.46 | 16.76% | 21.59% |
| `__monolith__` | 2 | 136.56 | 16.83% | 0.0% |
| `xt/author` | 5 | 100.78 | 19.12% | 3.22% |
| `script` | 1 | 17.36 | 13.21% | 0.0% |
| `t/conf` | 1 | 15.54 | 0.0% | 0.0% |
| `t/something` | 1 | 10.52 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `t/unit_core_methodattributes_method_metaclass_on_subclasses.t` -> **100.0%** Exposure
- `t/class_traits.t` -> **99.9999%** Exposure
- `t/dead_load_bad_args.t` -> **99.9998%** Exposure
- `t/aggregate/unit_core_plugin.t` -> **99.929%** Exposure
- `t/set_allowed_method.t` -> **99.3307%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `t/aggregate/live_component_controller_args.t` -> **100.0%** Exposure
- `t/aggregate/live_engine_request_uri.t` -> **99.9914%** Exposure
- `Makefile.PL` -> **99.9809%** Exposure
- `t/unicode-exception-return-value.t` -> **99.9661%** Exposure
- `t/class_traits_CAR_bug.t` -> **99.9411%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `t/arg_constraints.t` -> **7** Orphaned Functions | **0** Duplicates
- `t/class_traits.t` -> **1** Orphaned Functions | **4** Duplicates
- `t/http_exceptions.t` -> **4** Orphaned Functions | **0** Duplicates
- `t/http_exceptions_backcompat.t` -> **3** Orphaned Functions | **0** Duplicates
- `t/set_allowed_method.t` -> **3** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `1510` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `xt/author/http-server.t` (PERL) -> Cumulative Risk: **586.57**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 40.74 | **LOC:** 101 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9962%), State Flux (99.1542%)
- **Heaviest Functions:** `prove` (Impact: 9.3), `wait_port_timeout` (Impact: 2.1)

### 2. `t/class_traits.t` (PERL) -> Cumulative Risk: **563.71**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 33.02 | **LOC:** 99 | **CtrlFlow:** 4.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9999%), State Flux (99.866%)
- **Heaviest Functions:** `root` (Impact: 2.0), `a` (Impact: 1.1), `b` (Impact: 1.1)

### 3. `t/class_traits_CAR_bug.t` (PERL) -> Cumulative Risk: **528.91**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 27.62 | **LOC:** 86 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9411%), Cognitive Load (86.5945%)
- **Heaviest Functions:** `root` (Impact: 2.0), `a` (Impact: 1.1), `b` (Impact: 1.1)

### 4. `t/unicode-exception-return-value.t` (PERL) -> Cumulative Risk: **494.73**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 36.64 | **LOC:** 97 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9661%), Tech Debt (74.4868%)
- **Heaviest Functions:** `main` (Impact: 10.7), `handle_unicode_encoding_exception` (Impact: 2.4)

### 5. `t/aggregate/live_component_controller_args.t` (PERL) -> Cumulative Risk: **478.15**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 58.48 | **LOC:** 97 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (86.97%)
- **Heaviest Functions:** `run_test_for` (Impact: 26.2), `run_tests` (Impact: 2.1)

### 6. `t/useless_set_headers.t` (PERL) -> Cumulative Risk: **476.68**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 27.02 | **LOC:** 68 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.2014%), Tech Debt (73.1059%)
- **Heaviest Functions:** `get_header_ok` (Impact: 3.7), `set_header_nok` (Impact: 3.7), `warn` (Impact: 1.5)

### 7. `t/forward_instances.t` (PERL) -> Cumulative Risk: **475.89**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 29.94 | **LOC:** 67 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (95.2574%), State Flux (91.6827%)
- **Heaviest Functions:** `custom` (Impact: 4.2), `test_forward` (Impact: 3.7), `test_custom` (Impact: 3.7)

### 8. `t/unicode-exception-bug.t` (PERL) -> Cumulative Risk: **473.55**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 25.9 | **LOC:** 77 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.6851%), State Flux (77.493%)
- **Heaviest Functions:** `main` (Impact: 6.2), `as_psgi` (Impact: 2.5), `new` (Impact: 2.4)

### 9. `t/accept_context_regression.t` (PERL) -> Cumulative Risk: **467.42**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 16.5 | **LOC:** 43 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (91.6827%), Tech Debt (73.1059%)
- **Heaviest Functions:** `test_model` (Impact: 3.7), `ACCEPT_CONTEXT` (Impact: 2.2)

### 10. `t/bad_warnings.t` (PERL) -> Cumulative Risk: **466.62**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 35.58 | **LOC:** 72 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (95.2574%), State Flux (83.2018%)
- **Heaviest Functions:** `test` (Impact: 3.7), `infinity` (Impact: 3.7), `midpoint` (Impact: 3.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `t/aggregate/live_component_controller_action_chained.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 308.6 | **LOC:** 1176 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.2379%), Tech Debt (15.8869%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 279.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 183`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 6`, `fragile_debt: 2`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 4`, `test: 174`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Args, Benchmark, Catalyst::Test, FindBin, Test::More, URI, URI::QueryParam, args...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/arg_constraints.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 219.22 | **LOC:** 597 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.2912%), Tech Debt (32.2429%)
**Top Internal Functions/Classes:**
  * `user` (Impact: 8.2)
  * `user_object` (Impact: 8.2)
    * *Intent:* # Tests using this are current skipped pending coercion rethink
  * `default` (Impact: 8.2)
  * `tuple` (Impact: 4.7)
  * `slurpy_tuple` (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 175`, `args: 17`, `func_start: 46`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 8`, `unreferenced_by_name: 7`
* *Architecture:* `api: 47`, `import: 33`
* *Defense:* `safety: 27`, `doc: 1`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Catalyst, Catalyst::Test, HTTP::Request::Common, Moose, Moose::Role, MooseX::MethodAttributes, MooseX::MethodAttributes::Role, MyApp::Types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/utf_incoming.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 138.12 | **LOC:** 567 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.0891%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `stream_body_fh2` (Impact: 9.1)
    * *Intent:* # If you pull the file contents into a var, NOW you need to specify the # IO encoding on the FH. Ult...
  * `stream_body_fh` (Impact: 7.3)
    * *Intent:* # Stream a file with utf8 chars directly, you don't need to decode
  * `argend` (Impact: 4.8)
  * `file_upload` (Impact: 4.4)
  * `file_upload_utf8_param` (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 141`, `args: 23`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `state_mutation: 1`, `dead_code: 1`
* *Architecture:* `io: 2`, `api: 25`, `import: 17`
* *Defense:* `safety: 3`, `test: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Catalyst, Catalyst::Test, Compress::Zlib, Data::Dumper, Encode, File::Spec, HTTP::Message::PSGI, HTTP::Request::Common...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/psgi_utils.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 115.04 | **LOC:** 442 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.6381%), Tech Debt (15.0627%)
**Top Internal Functions/Classes:**
  * `get_env` (Impact: 9.3)
  * `filehandle` (Impact: 8.3)
  * `mounted` (Impact: 6.3)
  * `streaming_body` (Impact: 4.5)
  * `streaming_body_with_charset` (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 121`, `args: 19`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 21`, `import: 13`
* *Defense:* `safety: 2`, `test: 35`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Catalyst, Catalyst::Test, Catalyst::Utils, Encode, Plack::Request, Test::More, base, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/next-action.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 108.56 | **LOC:** 172 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.206%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `a` (Impact: 6.3)
  * `b` (Impact: 6.3)
  * `root` (Impact: 5.6)
  * `d` (Impact: 5.6)
  * `root` (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 81`, `args: 12`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 13`
* *Architecture:* `api: 15`, `import: 14`
* *Defense:* `safety: 6`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst, Catalyst::Test, Data::Dumper, Test::More, base, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_visit.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 85.86 | **LOC:** 292 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.9792%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 62.0)
  * `_begin` (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 38`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 1`, `import: 8`
* *Defense:* `safety: 4`, `test: 55`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Benchmark, Catalyst::Test, FindBin, Test::More, lib, namespace, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_go.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 80.62 | **LOC:** 276 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.7469%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 57.1)
  * `_begin` (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 38`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 4`, `test: 55`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Benchmark, Catalyst, Catalyst::Test, FindBin, Test::More, lib, namespace, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile.PL` (PERL | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 72.94 | **LOC:** 224 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.6682%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 18`
* *Architecture:* `import: 4`
* *Defense:* `safety: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ExtUtils::MakeMaker, of, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Changes` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 63.62 | **LOC:** 3181 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/unit_core_component_loading.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 63.12 | **LOC:** 246 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.3082%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `write_component_file` (Impact: 6.5)
  * `make_component_file` (Impact: 6.4)
  * `COMPONENT` (Impact: 3.3)
  * `COMPONENT` (Impact: 3.1)
  * `COMPONENT` (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 67`, `args: 8`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 12`
* *Architecture:* `io: 2`, `api: 11`, `import: 17`
* *Defense:* `safety: 2`, `test: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst, File::Path, File::Spec, MRO::Compat, Test::More, base, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_args.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 58.48 | **LOC:** 97 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.97%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_test_for` (Impact: 26.2)
  * `run_tests` (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 9 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 17`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 2`, `test: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Benchmark, Catalyst::Test, FindBin, Test::More, URI::Escape, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_engine_request_uri.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 57.72 | **LOC:** 178 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.2466%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 34`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 14`
* *Architecture:* `import: 12`
* *Defense:* `safety: 2`, `test: 76`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Request, Catalyst::Test, FindBin, Test::More, TestApp::RequestBaseBug, c, lib, semi...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dispatch_on_scheme.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 52.54 | **LOC:** 124 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.2577%), Tech Debt (58.2988%)
**Top Internal Functions/Classes:**
  * `is_http` (Impact: 3.7)
  * `is_https` (Impact: 3.7)
  * `is_http_chain` (Impact: 3.7)
  * `is_https_chain` (Impact: 3.7)
  * `uri_for1` (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 36`, `args: 8`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 12`, `import: 7`
* *Defense:* `safety: 2`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst, Catalyst::Test, HTTP::Request::Common, Test::More, base, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dead_recursive_chained_attributes.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 49.64 | **LOC:** 42 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.5201%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 13`, `func_start: 4`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 6`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Test, Test::More, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/state.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 48.78 | **LOC:** 91 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.6174%), Tech Debt (94.9539%)
**Top Internal Functions/Classes:**
  * `two` (Impact: 4.4)
  * `auto` (Impact: 3.9)
  * `end` (Impact: 3.9)
  * `begin` (Impact: 3.7)
  * `base` (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 48`, `args: 9`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `safety: 2`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst, Catalyst::Test, HTTP::Request::Common, Test::More, base, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/http_exceptions.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 48.38 | **LOC:** 147 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.3704%), Tech Debt (88.7685%)
**Top Internal Functions/Classes:**
  * `from_psgi_app` (Impact: 3.8)
  * `from_catalyst` (Impact: 3.7)
  * `classic_error` (Impact: 3.7)
  * `just_die` (Impact: 3.7)
  * `end` (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 60`, `args: 15`, `func_start: 13`, `class_start: 4`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 14`, `import: 9`
* *Defense:* `safety: 2`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst, HTTP::Message::PSGI, HTTP::Request::Common, Plack::Test, Plack::Util, Test::More, base, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_forward.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 48.18 | **LOC:** 258 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.7136%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 36.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 29`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `safety: 2`, `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Benchmark, Catalyst::Test, FindBin, Test::More, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_auto.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 46.86 | **LOC:** 192 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.2738%), Tech Debt (28.362%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 40.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 39`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`, `fragile_debt: 1`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `safety: 2`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Benchmark, Catalyst::Test, FindBin, Test::More, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_action.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 46.0 | **LOC:** 269 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.4026%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 37.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 27`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 2`, `test: 67`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Benchmark, Catalyst::Action, Catalyst::Test, FindBin, Test::More, lib, strict, utf8...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/unit_stats.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 45.32 | **LOC:** 167 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.411%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 29`, `args: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 28`, `dead_code: 1`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, Time::HiRes, Tree::Simple, end, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/http_exceptions_backcompat.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 44.32 | **LOC:** 139 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.8933%), Tech Debt (77.0807%)
**Top Internal Functions/Classes:**
  * `from_psgi_app` (Impact: 3.8)
  * `from_catalyst` (Impact: 3.7)
  * `classic_error` (Impact: 3.7)
  * `just_die` (Impact: 3.7)
  * `as_psgi` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 59`, `args: 15`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `state_mutation: 1`, `dead_code: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 13`, `import: 9`
* *Defense:* `safety: 2`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst, HTTP::Message::PSGI, HTTP::Request::Common, Plack::Test, Plack::Util, Test::More, base, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/query_constraints.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 44.3 | **LOC:** 178 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.238%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `default` (Impact: 8.2)
  * `user` (Impact: 4.2)
  * `user_slurps` (Impact: 4.2)
  * `string_types` (Impact: 2.0)
  * `as_ref` (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *Amplified Sql Injection:* 8 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 51`, `args: 3`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `api: 9`, `import: 17`
* *Defense:* `safety: 4`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Catalyst, Catalyst::Test, HTTP::Request::Common, Moose, MooseX::MethodAttributes, MyApp::Types, Test::More, Type::Library...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/relative_root_action_for_bug.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 44.28 | **LOC:** 94 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.2426%), Tech Debt (55.8327%)
**Top Internal Functions/Classes:**
  * `default` (Impact: 5.4)
  * `author` (Impact: 4.3)
  * `story` (Impact: 3.8)
  * `top` (Impact: 3.7)
  * `root` (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 29`, `args: 7`, `func_start: 7`, `class_start: 4`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 1`
* *Architecture:* `api: 7`, `import: 11`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst, Catalyst::Test, Moose, MooseX::MethodAttributes, Test::More, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/unit_core_script_server.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 42.9 | **LOC:** 215 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.6486%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testOption` (Impact: 6.4)
  * `testBackgroundOptionWithFork` (Impact: 2.5)
  * `_build_testapp` (Impact: 2.5)
  * `testRestart` (Impact: 2.2)
  * `opthash` (Impact: 1.6)
    * *Intent:* # Returns the hash expected when no flags are passed
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 66`, `args: 4`, `func_start: 6`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 5`, `concurrency: 4`, `import: 13`
* *Defense:* `safety: 12`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Script::Server, Cwd, File::Temp, FindBin, MooseX::Daemonize, Plack::Handler::Starman, Test::More, Try::Tiny...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/http-server.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 40.74 | **LOC:** 101 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.6015%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `prove` (Impact: 9.3)
  * `wait_port_timeout` (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 36`, `args: 3`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 4`
* *Architecture:* `api: 2`, `concurrency: 4`, `import: 14`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Path, FindBin, MakeTestApp, Net::EmptyPort, Plack::Builder, TAP::Harness, Test::More, Test::TCP...
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

- `t/abort-chain-1.t` -> **Severity: 449.7** (Blast Radius: 4.497 * Doc Risk: 100.0%)
- `t/abort-chain-2.t` -> **Severity: 449.7** (Blast Radius: 4.497 * Doc Risk: 100.0%)
- `t/abort-chain-3.t` -> **Severity: 449.7** (Blast Radius: 4.497 * Doc Risk: 100.0%)
- `t/accept_context_regression.t` -> **Severity: 449.7** (Blast Radius: 4.497 * Doc Risk: 100.0%)
- `t/aggregate/c3_appclass_bug.t` -> **Severity: 449.7** (Blast Radius: 4.497 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
