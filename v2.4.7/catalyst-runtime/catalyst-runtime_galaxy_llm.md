# ARCHITECTURAL_BRIEF: catalyst-runtime
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/catalyst-runtime` |
| **Timestamp** | `2026-08-07T03:51:41.264174+00:00` |
| **Scan Duration** | `0.49s` |
| **Git Branch** | `master` |
| **Git Commit** | `1d40b8ea5a7f4a4ae99af921b914f04e7c9a21c3` |
| **Git Remote** | `https://github.com/perl-catalyst/catalyst-runtime.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1 malicious artifacts.

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
| Total Artifacts | 493 |
| Analyzed Artifacts (Scanned) | 213 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 280 |
| Total LOC | 13088 |
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
| PERL | 209 | 12935 | 98.1% |
| PLAINTEXT | 2 | 0 | 0.9% |
| M4 | 1 | 27 | 0.5% |
| JSON | 1 | 126 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.889`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_0 | 108 | 50.7% |
| file_cluster_13 | 86 | 40.4% |
| file_cluster_8 | 15 | 7.0% |
| file_cluster_4 | 2 | 0.9% |

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

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.6 | 47.7 | 50.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 60.2 | 70.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 15.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 2.5 | 0.1 | 0.0 | 0.0 |
| API Exposure | 0.0 | 7.1 | 0.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 77.2 | 99.7 | 0.0 |
| Commented Logic Exposure | 0.0 | 20.9 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 6.3 | 93.9 | 43.1 | 42.7 | 54.3 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `t/optional_lighttpd-fastcgi-non-root.t` (Hits: 9)
- `t/optional_lighttpd-fastcgi.t` (Hits: 9)
- `t/optional_http-server-restart.t` (Hits: 5)

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

- `run_tests` (@ `t/aggregate/live_component_controller_action_chained.t`) -> Impact: **404.0** | LOC: 1149
- `streaming_body_with_charset` (@ `t/psgi_utils.t`) -> Impact: **94.9** | LOC: 374
- `uri_for` (@ `t/utf_incoming.t`) -> Impact: **92.2** | LOC: 527
- `run_tests` (@ `t/aggregate/live_component_controller_action_visit.t`) -> Impact: **64.0** | LOC: 259
- `run_tests` (@ `t/aggregate/live_component_controller_action_go.t`) -> Impact: **59.1** | LOC: 242
- `make_component_file` (@ `t/aggregate/unit_core_component_loading.t`) -> Impact: **53.5** | LOC: 189
- `run_tests` (@ `t/aggregate/live_component_controller_action_auto.t`) -> Impact: **40.0** | LOC: 160
- `run_tests` (@ `t/aggregate/live_component_controller_action_action.t`) -> Impact: **37.2** | LOC: 244
- `run_tests` (@ `t/aggregate/live_component_controller_action_forward.t`) -> Impact: **36.7** | LOC: 234
- `run_tests` (@ `t/aggregate/live_component_controller_action_local.t`) -> Impact: **27.3** | LOC: 126

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `t` | 85 | 7433.18 | 45.83% | 25.0% |
| `t/aggregate` | 118 | 5013.22 | 50.07% | 9.0% |
| `xt/author` | 5 | 170.78 | 40.45% | 4.25% |
| `__monolith__` | 2 | 115.52 | 10.51% | 0.0% |
| `script` | 1 | 32.36 | 17.79% | 0.0% |
| `t/conf` | 1 | 15.54 | 9.46% | 0.0% |
| `t/something` | 1 | 10.52 | 5.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `t/aggregate/unit_controller_namespace.t` -> **100.0%** Exposure
- `t/aggregate/unit_metaclass_compat_non_moose_controller.t` -> **100.0%** Exposure
- `t/class_traits.t` -> **100.0%** Exposure
- `t/dead_load_bad_args.t` -> **100.0%** Exposure
- `t/dead_load_multiple_chained_attributes.t` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `t/aggregate/live_component_controller_action_auto.t` -> **100.0%** Exposure
- `t/aggregate/live_component_controller_action_chained.t` -> **100.0%** Exposure
- `t/aggregate/live_component_controller_action_default.t` -> **100.0%** Exposure
- `t/aggregate/live_component_controller_action_index.t` -> **100.0%** Exposure
- `t/aggregate/live_component_controller_args.t` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `t/next-action.t` -> **0** Orphaned Functions | **7** Duplicates
- `t/class_traits.t` -> **1** Orphaned Functions | **4** Duplicates
- `t/http_exceptions.t` -> **3** Orphaned Functions | **2** Duplicates
- `t/http_exceptions_backcompat.t` -> **3** Orphaned Functions | **2** Duplicates
- `t/dead_recursive_chained_attributes.t` -> **0** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`t/conf/extra.conf.in`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1510` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `t/unit_core_methodattributes_method_metaclass_on_subclasses.t` (PERL) -> Cumulative Risk: **536.7**
- **Archetype:** `file_cluster_0` (Distance: 12.457 IQR)
- **Magnitude:** 20.7 | **LOC:** 31 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (92.2728%)
- **Heaviest Functions:** `test` (Impact: 1.1), `test` (Impact: 1.1)

### 2. `xt/author/http-server.t` (PERL) -> Cumulative Risk: **523.81**
- **Archetype:** `file_cluster_4` (Distance: 12.451 IQR)
- **Magnitude:** 77.74 | **LOC:** 101 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.6359%)
- **Heaviest Functions:** `prove` (Impact: 14.3), `wait_port_timeout` (Impact: 2.1)

### 3. `t/aggregate/unit_core_ctx_attr.t` (PERL) -> Cumulative Risk: **514.04**
- **Archetype:** `file_cluster_13` (Distance: 12.125 IQR)
- **Magnitude:** 27.52 | **LOC:** 32 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9993%), Cognitive Load (79.9731%)

### 4. `t/aggregate/psgi_file.t` (PERL) -> Cumulative Risk: **513.77**
- **Archetype:** `file_cluster_0` (Distance: 14.726 IQR)
- **Magnitude:** 33.76 | **LOC:** 54 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9973%), Concurrency (99.7574%), Cognitive Load (88.6213%)

### 5. `t/optional_threads.t` (PERL) -> Cumulative Risk: **510.81**
- **Archetype:** `file_cluster_0` (Distance: 11.341 IQR)
- **Magnitude:** 35.92 | **LOC:** 55 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9899%), Concurrency (99.8144%), Cognitive Load (94.4069%)

### 6. `t/http_method.t` (PERL) -> Cumulative Risk: **493.13**
- **Archetype:** `file_cluster_0` (Distance: 11.533 IQR)
- **Magnitude:** 51.06 | **LOC:** 94 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (93.4547%), Safety Score (83.7174%)
- **Heaviest Functions:** `Catalyst::Response::format` (Impact: 13.9), `show` (Impact: 3.9), `post_user` (Impact: 3.8)

### 7. `t/aggregate/live_priorities.t` (PERL) -> Cumulative Risk: **492.55**
- **Archetype:** `file_cluster_13` (Distance: 12.521 IQR)
- **Magnitude:** 48.88 | **LOC:** 72 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (93.6192%), Cognitive Load (86.0348%)

### 8. `t/next-action.t` (PERL) -> Cumulative Risk: **486.98**
- **Archetype:** `file_cluster_0` (Distance: 11.974 IQR)
- **Magnitude:** 129.56 | **LOC:** 172 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9975%), Safety Score (87.4136%)
- **Heaviest Functions:** `a` (Impact: 6.3), `b` (Impact: 6.3), `root` (Impact: 5.6)

### 9. `t/forward_instances.t` (PERL) -> Cumulative Risk: **486.19**
- **Archetype:** `file_cluster_0` (Distance: 11.26 IQR)
- **Magnitude:** 30.94 | **LOC:** 67 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.97%), Tech Debt (98.8049%), Safety Score (76.0464%)
- **Heaviest Functions:** `custom` (Impact: 4.2), `test_forward` (Impact: 3.7), `test_custom` (Impact: 3.7)

### 10. `t/aggregate/unit_core_script_server.t` (PERL) -> Cumulative Risk: **485.0**
- **Archetype:** `file_cluster_0` (Distance: 12.837 IQR)
- **Magnitude:** 129.48 | **LOC:** 215 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.8985%), Cognitive Load (89.3773%)
- **Heaviest Functions:** `testBackgroundOptionWithFork` (Impact: 15.1), `testOption` (Impact: 9.9), `_build_testapp` (Impact: 6.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `t/arg_constraints.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.397 IQR)
- **Top Global Matches:** file_cluster_0: 12.397, file_cluster_13: 12.656, file_cluster_8: 12.863
- **Magnitude:** 4463.26 | **LOC:** 597 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.0627%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 174`, `args: 17`, `func_start: 46`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 160`
* *Architecture:* `api: 1`, `import: 33`
* *Defense:* `safety: 27`, `doc: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Moose::Role, MooseX::MethodAttributes, utf8, base, HTTP::Request::Common, Catalyst, Test::More, Type::Utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_chained.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.255 IQR)
- **Top Global Matches:** file_cluster_0: 12.255, file_cluster_8: 12.912, file_cluster_13: 13.115
- **Magnitude:** 823.2 | **LOC:** 1176 | **CtrlFlow:** 46.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.6277%), Tech Debt (16.7293%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 404.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 183`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 403`, `planned_debt: 6`, `fragile_debt: 2`
* *Architecture:* `import: 10`
* *Defense:* `safety: 4`, `test: 174`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Benchmark, Test::More, Catalyst::Test, FindBin, args, URI::QueryParam, warnings, Args...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_args.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.662 IQR)
- **Top Global Matches:** file_cluster_13: 12.662, file_cluster_0: 12.82, file_cluster_8: 13.03
- **Magnitude:** 412.09 | **LOC:** 97 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.3548%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 17`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 42`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Benchmark, URI::Escape, Test::More, Catalyst::Test, FindBin, warnings, lib, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/args0_bug.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 16.493 IQR)
- **Top Global Matches:** file_cluster_0: 16.493, file_cluster_13: 16.538, file_cluster_11: 16.892
- **Magnitude:** 241.94 | **LOC:** 66 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.9594%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `chain_base` (Impact: 2.0)
  * `chained_one_args_0` (Impact: 2.0)
  * `chained_one_args_1` (Impact: 2.0)
  * `chained_one_args_2` (Impact: 2.0)
  * `chained_zero_args_0` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 18`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 227`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `doc: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MooseX::MethodAttributes, Test::More, Catalyst::Test, Moose, warnings, strict, Catalyst
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/utf_incoming.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.972 IQR)
- **Top Global Matches:** file_cluster_0: 10.972, file_cluster_8: 11.375, file_cluster_13: 11.399
- **Magnitude:** 213.32 | **LOC:** 567 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.0458%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `uri_for` (Impact: 92.2)
  * `heart` (Impact: 3.8)
  * `hat` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 140`, `args: 23`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `state_mutation: 104`, `dead_code: 1`
* *Architecture:* `io: 3`, `api: 1`, `import: 17`
* *Defense:* `safety: 3`, `test: 30`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Compress::Zlib, File::Spec, Scalar::Util, utf8, base, HTTP::Request::Common, Catalyst, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/psgi_utils.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.4 IQR)
- **Top Global Matches:** file_cluster_0: 10.4, file_cluster_8: 10.42, file_cluster_13: 10.605
- **Magnitude:** 196.44 | **LOC:** 442 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.3473%), Tech Debt (32.0974%)
**Top Internal Functions/Classes:**
  * `streaming_body_with_charset` (Impact: 94.9)
  * `filehandle` (Impact: 8.3)
  * `name_args` (Impact: 4.3)
  * `direct` (Impact: 4.2)
  * `streaming_body` (Impact: 4.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 121`, `args: 19`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `state_mutation: 63`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 2`, `import: 13`
* *Defense:* `safety: 2`, `test: 35`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` base, utf8, Test::More, Encode, Catalyst::Test, Catalyst::Utils, warnings, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_visit.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.165 IQR)
- **Top Global Matches:** file_cluster_0: 11.165, file_cluster_8: 11.739, file_cluster_13: 11.833
- **Magnitude:** 149.86 | **LOC:** 292 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.2492%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 64.0)
  * `_begin` (Impact: 1.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 38`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 79`
* *Architecture:* `import: 8`
* *Defense:* `safety: 4`, `test: 55`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Benchmark, Test::More, Catalyst::Test, FindBin, warnings, lib, namespace, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_go.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.275 IQR)
- **Top Global Matches:** file_cluster_0: 11.275, file_cluster_8: 11.815, file_cluster_13: 11.853
- **Magnitude:** 144.62 | **LOC:** 276 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.4167%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 59.1)
  * `_begin` (Impact: 1.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 38`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 79`
* *Architecture:* `import: 9`
* *Defense:* `safety: 4`, `test: 55`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Benchmark, Test::More, Catalyst::Test, FindBin, warnings, lib, namespace, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/unit_core_component_loading.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.086 IQR)
- **Top Global Matches:** file_cluster_0: 11.086, file_cluster_13: 11.516, file_cluster_8: 11.804
- **Magnitude:** 132.02 | **LOC:** 246 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.1515%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `make_component_file` (Impact: 53.5)
  * `write_component_file` (Impact: 6.5)
  * `COMPONENT` (Impact: 3.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 62`, `args: 6`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 61`
* *Architecture:* `io: 3`, `api: 4`, `import: 14`
* *Defense:* `safety: 2`, `test: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Spec, File::Path, base, Test::More, warnings, MRO::Compat, strict, Catalyst
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/next-action.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.974 IQR)
- **Top Global Matches:** file_cluster_0: 11.974, file_cluster_13: 12.152, file_cluster_8: 12.509
- **Magnitude:** 129.56 | **LOC:** 172 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.9168%), Tech Debt (99.9975%)
**Top Internal Functions/Classes:**
  * `a` (Impact: 6.3)
  * `b` (Impact: 6.3)
  * `root` (Impact: 5.6)
  * `d` (Impact: 5.6)
  * `root` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 81`, `args: 12`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 68`, `duplicate_logic: 7`
* *Architecture:* `api: 3`, `import: 14`
* *Defense:* `safety: 6`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` base, Test::More, Catalyst::Test, Data::Dumper, warnings, strict, Catalyst
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/unit_core_script_server.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.837 IQR)
- **Top Global Matches:** file_cluster_0: 12.837, file_cluster_4: 12.927, file_cluster_13: 12.939
- **Magnitude:** 129.48 | **LOC:** 215 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.3773%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testBackgroundOptionWithFork` (Impact: 15.1)
  * `testOption` (Impact: 9.9)
  * `_build_testapp` (Impact: 6.0)
  * `testRestart` (Impact: 2.2)
  * `opthash` (Impact: 1.6)
    * *Intent:* # Returns the hash expected when no flags are passed
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 66`, `args: 5`, `func_start: 6`
* *Risk/State:* `state_mutation: 71`
* *Architecture:* `concurrency: 19`, `import: 13`
* *Defense:* `safety: 12`, `test: 9`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Script::Server, File::Temp, Cwd, Test::More, Try::Tiny, opts, Plack::Handler::Starman, MooseX::Daemonize...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_engine_request_uri.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.702 IQR)
- **Top Global Matches:** file_cluster_13: 12.702, file_cluster_0: 12.791, file_cluster_8: 12.869
- **Magnitude:** 128.72 | **LOC:** 178 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.4472%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 34`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 111`
* *Architecture:* `import: 12`
* *Defense:* `safety: 2`, `test: 76`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Request, semi, Test::More, c, Catalyst::Test, FindBin, warnings, lib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_auto.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.482 IQR)
- **Top Global Matches:** file_cluster_0: 11.482, file_cluster_13: 12.166, file_cluster_8: 12.244
- **Magnitude:** 114.86 | **LOC:** 192 | **CtrlFlow:** 47.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.8809%), Tech Debt (35.9641%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 40.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 39`, `func_start: 1`
* *Risk/State:* `state_mutation: 72`, `fragile_debt: 1`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Benchmark, Test::More, Catalyst::Test, FindBin, warnings, lib, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_engine_request_uploads.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.052 IQR)
- **Top Global Matches:** file_cluster_0: 11.052, file_cluster_8: 11.253, file_cluster_13: 11.308
- **Magnitude:** 109.5 | **LOC:** 412 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.456%), Tech Debt (23.2846%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 70`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 88`, `fragile_debt: 2`
* *Architecture:* `import: 20`
* *Defense:* `safety: 2`, `test: 71`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Request, Scalar::Util, HTTP::Body::OctetStream, HTTP::Request::Common, Test::More, HTTP::Headers::Util, way, HTTP::Headers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_forward.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.67 IQR)
- **Top Global Matches:** file_cluster_0: 10.67, file_cluster_8: 11.124, file_cluster_13: 11.345
- **Magnitude:** 96.18 | **LOC:** 258 | **CtrlFlow:** 49.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 36.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 29`, `func_start: 1`
* *Risk/State:* `state_mutation: 55`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Benchmark, Test::More, Catalyst::Test, FindBin, warnings, lib, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_engine_request_parameters.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.88 IQR)
- **Top Global Matches:** file_cluster_0: 11.88, file_cluster_13: 12.123, file_cluster_8: 12.212
- **Magnitude:** 86.82 | **LOC:** 171 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.187%), Tech Debt (36.5947%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 40`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 69`, `fragile_debt: 1`
* *Architecture:* `import: 9`
* *Defense:* `safety: 2`, `test: 53`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Catalyst::Request, HTTP::Request::Common, Test::More, HTTP::Headers, Catalyst::Test, FindBin, warnings, lib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/unit_core_engine_fixenv-lighttpd.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.146 IQR)
- **Top Global Matches:** file_cluster_8: 9.146, file_cluster_13: 9.311, file_cluster_0: 9.803
- **Magnitude:** 86.49 | **LOC:** 56 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.0824%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 14`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `import: 4`
* *Defense:* `safety: 2`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, warnings, Catalyst
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/query_constraints.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.567 IQR)
- **Top Global Matches:** file_cluster_0: 12.567, file_cluster_13: 12.602, file_cluster_11: 12.974
- **Magnitude:** 85.9 | **LOC:** 178 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.6119%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `default` (Impact: 8.2)
  * `chain` (Impact: 2.0)
  * `big` (Impact: 2.0)
  * `small` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 50`, `args: 3`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 69`
* *Architecture:* `import: 17`
* *Defense:* `safety: 4`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` MooseX::MethodAttributes, utf8, HTTP::Request::Common, Test::More, Type::Utils, Types::Standard, Catalyst::Test, Moose...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/live_fork.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.196 IQR)
- **Top Global Matches:** file_cluster_4: 13.196, file_cluster_13: 13.665, file_cluster_0: 13.827
- **Magnitude:** 79.84 | **LOC:** 66 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.4681%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `result_ok` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 17`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `concurrency: 55`, `import: 7`
* *Defense:* `safety: 3`, `doc: 2`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, Catalyst::Test, JSON::MaybeXS, FindBin, warnings, lib, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/http-server.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.451 IQR)
- **Top Global Matches:** file_cluster_4: 12.451, file_cluster_0: 12.692, file_cluster_13: 12.715
- **Magnitude:** 77.74 | **LOC:** 101 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.6359%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `prove` (Impact: 14.3)
  * `wait_port_timeout` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 36`, `args: 3`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 36`
* *Architecture:* `concurrency: 24`, `import: 14`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Path, Try::Tiny, Test::More, Plack::Builder, Test::TCP, FindBin, TestApp, Net::EmptyPort...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_action.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.362 IQR)
- **Top Global Matches:** file_cluster_0: 10.362, file_cluster_8: 10.418, file_cluster_13: 10.697
- **Magnitude:** 76.1 | **LOC:** 269 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.9423%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 37.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 27`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 34`
* *Architecture:* `import: 9`
* *Defense:* `safety: 2`, `test: 67`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Benchmark, utf8, Test::More, Catalyst::Test, Catalyst::Action, FindBin, warnings, lib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/psgi-log.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.721 IQR)
- **Top Global Matches:** file_cluster_13: 12.721, file_cluster_0: 12.875, file_cluster_11: 13.218
- **Magnitude:** 71.66 | **LOC:** 110 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (61.9234%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 39`, `args: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 55`
* *Architecture:* `import: 16`
* *Defense:* `safety: 3`, `doc: 2`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Spec, File::Temp, HTTP::Request::Common, the, Test::More, Plack::Builder, FindBin, TestApp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_index.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.143 IQR)
- **Top Global Matches:** file_cluster_0: 12.143, file_cluster_13: 12.218, file_cluster_17: 12.538
- **Magnitude:** 67.3 | **LOC:** 99 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.9341%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_tests` (Impact: 21.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 21`, `func_start: 1`
* *Risk/State:* `state_mutation: 44`
* *Architecture:* `import: 13`
* *Defense:* `safety: 2`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Benchmark, Test::More, Catalyst::Test, FindBin, warnings, lib, strict, slash
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/http_exceptions.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.319 IQR)
- **Top Global Matches:** file_cluster_0: 11.319, file_cluster_13: 11.499, file_cluster_8: 11.655
- **Magnitude:** 64.18 | **LOC:** 147 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.8386%), Tech Debt (99.8332%)
**Top Internal Functions/Classes:**
  * `from_psgi_app` (Impact: 3.8)
  * `from_catalyst` (Impact: 3.7)
  * `classic_error` (Impact: 3.7)
  * `just_die` (Impact: 3.7)
  * `end` (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 60`, `args: 15`, `func_start: 13`, `class_start: 4`
* *Risk/State:* `state_mutation: 30`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 2`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.497
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` base, HTTP::Request::Common, Test::More, HTTP::Message::PSGI, Plack::Util, warnings, Plack::Test, strict...
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

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `t/aggregate/unit_core_action_for.t` (PERL) | Magnitude: 15.3 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: decorators: 6, indent_spaces: 6, structural_boundaries: 5, import: 5
- `t/consumes.t` (PERL) | Magnitude: 23.9 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 19, state_mutation: 13, decorators: 9
- `t/unicode-exception-return-value.t` (PERL) | Magnitude: 46.34 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, state_mutation: 34, structural_boundaries: 31, encapsulation: 18
- `t/optional_apache-cgi-rewrite.pl` (PERL) | Magnitude: 12.7 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 15, decorators: 12, import: 10
- `t/optional_apache-cgi.pl` (PERL) | Magnitude: 12.7 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 15, decorators: 12, import: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/plugin_new_method_backcompat.t` (PERL) | Magnitude: 15.34 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 12, import: 6, decorators: 5, test: 2
- `t/aggregate/unit_metaclass_compat_extend_non_moose_controller.t` (PERL) | Magnitude: 17.36 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 10, decorators: 9, import: 6
- `t/no_test_stash_bug.t` (PERL) | Magnitude: 6.46 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 9, decorators: 6, import: 6
- `t/query_keywords_and_parameters.t` (PERL) | Magnitude: 20.54 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 23, branch: 22, state_mutation: 15
- `t/live_redirect_body.t` (PERL) | Magnitude: 42.8 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 27, indent_spaces: 26, test: 19, structural_boundaries: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `xt/author/http-server.t` (PERL) | Magnitude: 77.74 | Delta: **0.241 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 36, state_mutation: 36, indent_spaces: 32, concurrency: 24
- `t/live_fork.t` (PERL) | Magnitude: 79.84 | Delta: **0.469 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 55, indent_spaces: 26, state_mutation: 22, structural_boundaries: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `t/aggregate/unit_utils_env_value.t` (PERL) | Magnitude: 15.5 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 13, decorators: 10, structural_boundaries: 5, test: 5
- `t/content_negotiation.t` (PERL) | Magnitude: 45.82 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 37, state_mutation: 29, encapsulation: 29
- `t/aggregate/unit_controller_config.t` (PERL) | Magnitude: 18.7 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: test: 17, pointers: 11, structural_boundaries: 9, indent_spaces: 9
- `t/aggregate/unit_core_merge_config_hashes.t` (PERL) | Magnitude: 18.76 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, branch: 9, structural_boundaries: 6, import: 4
- `t/aggregate/unit_core_engine-prepare_path.t` (PERL) | Magnitude: 36.6 | Delta: **0.126 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 82, branch: 34, state_mutation: 32, structural_boundaries: 23

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `t/aggregate/unit_metaclass_compat_extend_non_moose_controller.t` -> **Severity: 422.343** (Blast Radius: 4.497 * Doc Risk: 93.9166%)
- `t/aggregate/unit_controller_namespace.t` -> **Severity: 404.705** (Blast Radius: 4.497 * Doc Risk: 89.9945%)
- `t/no_test_stash_bug.t` -> **Severity: 376.155** (Blast Radius: 4.497 * Doc Risk: 83.6458%)
- `t/accept_context_regression.t` -> **Severity: 374.158** (Blast Radius: 4.497 * Doc Risk: 83.2018%)
- `t/aggregate/unit_core_component_mro.t` -> **Severity: 361.782** (Blast Radius: 4.497 * Doc Risk: 80.4496%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
