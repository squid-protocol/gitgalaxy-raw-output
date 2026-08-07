# ARCHITECTURAL_BRIEF: Dancer2
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/Dancer2` |
| **Timestamp** | `2026-08-07T03:51:30.731564+00:00` |
| **Scan Duration** | `0.45s` |
| **Git Branch** | `main` |
| **Git Commit** | `25176c5b860493b4a6dcda5bc12ecbefa67df716` |
| **Git Remote** | `https://github.com/PerlDancer/Dancer2.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3 malicious artifacts.

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
| Total Artifacts | 438 |
| Analyzed Artifacts (Scanned) | 226 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 212 |
| Total LOC | 10813 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 51.6% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.375 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 179 | 10365 | 79.2% |
| YAML | 23 | 100 | 10.2% |
| HTML | 7 | 84 | 3.1% |
| MARKDOWN | 5 | 0 | 2.2% |
| PLAINTEXT | 4 | 0 | 1.8% |
| CSS | 4 | 239 | 1.8% |
| SQLITE | 2 | 14 | 0.9% |
| DOCKERFILE | 1 | 6 | 0.4% |
| JSON | 1 | 5 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.867`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 88 | 38.9% |
| file_cluster_0 | 78 | 34.5% |
| file_cluster_8 | 50 | 22.1% |
| file_cluster_17 | 1 | 0.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 4.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 212*

**Composition by Extension & Reason:**
- `.pm`: 111x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tt`: 25x Excluded (Unsupported Extension: '.tt')
- `.t`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable), 1x Unresolved Ambiguity (Tier 4 Fallback failed Ecosystem Consensus)
- `.pod`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.psgi`: 2x Excluded (Unsupported Extension: '.psgi')
- `.fcgi`: 2x Excluded (Unsupported Extension: '.fcgi')
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.jpg`: 2x Excluded (Explicitly Denied Extension: '.jpg')
- `.db`: 1x Excluded (Unsupported Extension: '.db'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pl`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rc`: 2x Excluded (Unsupported Extension: '.rc')
- `.ini`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.skip`: 1x Excluded (Unsupported Extension: '.SKIP')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 85.2 | 30.8 | 24.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 95.6 | 52.7 | 66.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 2.3 | 0.2 | 0.0 | 0.0 |
| API Exposure | 0.0 | 9.3 | 1.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 42.3 | 0.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 67.8 | 98.3 | 0.0 |
| Commented Logic Exposure | 0.0 | 14.6 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 86.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.4 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 38.0 | 3.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 52.2 | 55.2 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 97.9 | 0.5 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `t/request_upload.t` (Hits: 5)
- `t/file_utils.t` (Hits: 3)
- `share/skel/default/public/404.html` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **content.t** (`t/dsl/content.t`) — 3 inbound connections
2. **TestPlugin.pm** (`t/issues/gh-1449/TestPlugin.pm`) — 1 inbound connections
3. **AUTHORS** (`AUTHORS`) — 0 inbound connections
4. **Changes** (`Changes`) — 0 inbound connections
5. **file.txt** (`t/public/file.txt`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **error.t** (`t/error.t`) — 17 outbound dependencies
2. **plugin_syntax.t** (`t/plugin_syntax.t`) — 14 outbound dependencies
3. **hooks.t** (`t/hooks.t`) — 13 outbound dependencies
4. **serializer_mutable_custom.t** (`t/serializer_mutable_custom.t`) — 12 outbound dependencies
5. **perf.pl** (`tools/perf.pl`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `all_tests` (@ `t/cookie.t`) -> Impact: **45.5** | LOC: 171
- `run_test` (@ `t/request_upload.t`) -> Impact: **39.4** | LOC: 167
- `run_test` (@ `t/request.t`) -> Impact: **34.5** | LOC: 111
- `test_app` (@ `t/dsl/uri_for_route.t`) -> Impact: **32.4** | LOC: 128
- `generate_id` (@ `t/session_bad_client_cookie.t`) -> Impact: **11.1** | LOC: 102
- `_normalize` (@ `t/plugin_syntax.t`) -> Impact: **7.1** | LOC: 7
- `hexe` (@ `t/file_utils.t`) -> Impact: **6.8** | LOC: 52
- `check_app` (@ `tools/perf.pl`) -> Impact: **5.8** | LOC: 12
- `write_file` (@ `t/file_utils.t`) -> Impact: **5.6** | LOC: 8
- `run_tests` (@ `t/auto_page.t`) -> Impact: **5.5** | LOC: 70

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `t` | 83 | 3104.1 | 39.64% | 3.18% |
| `t/dsl` | 24 | 824.02 | 34.62% | 7.01% |
| `t/issues` | 19 | 457.42 | 38.46% | 4.94% |
| `t/plugin2` | 13 | 259.78 | 32.15% | 0.0% |
| `t/scope_problems` | 5 | 122.12 | 39.44% | 0.0% |
| `share/skel/tutorial/t` | 4 | 74.84 | 17.14% | 0.0% |
| `__monolith__` | 7 | 59.94 | 0.0% | 0.0% |
| `share/skel/default/public` | 3 | 54.92 | 7.51% | 0.0% |
| `share/skel/tutorial/public` | 3 | 54.92 | 7.51% | 0.0% |
| `t/config/environments` | 4 | 47.8 | 5.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `share/skel/tutorial/db/entries.sql` -> **100.0%** Exposure
- `share/skel/tutorial/db/users.sql` -> **100.0%** Exposure
- `t/dsl/extend.t` -> **98.6851%** Exposure
- `t/roles/hook.t` -> **96.7987%** Exposure
- `t/issues/gh-797.t` -> **93.8921%** Exposure
### Highest State Flux (Mutation/Volatility)
- `t/deserialize.t` -> **100.0%** Exposure
- `t/disp_named_capture.t` -> **100.0%** Exposure
- `t/dsl/any.t` -> **100.0%** Exposure
- `t/dsl/splat.t` -> **100.0%** Exposure
- `t/forward_hmv_params.t` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `t/roles/hook.t` -> **2** Orphaned Functions | **0** Duplicates
- `share/skel/tutorial/db/users.sql` -> **2** Orphaned Functions | **0** Duplicates
- `t/config_reader.t` -> **1** Orphaned Functions | **0** Duplicates
- `t/dsl/extend.t` -> **1** Orphaned Functions | **0** Duplicates
- `t/dsl/send_as.t` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`share/docker/Dockerfile`** -> AI Confidence: **98.84%**
2. **`share/skel/tutorial/db/entries.sql`** -> AI Confidence: **98.84%**
3. **`share/skel/tutorial/db/users.sql`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `t/error.t` -> **97.8667%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1255` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `t/issues/gh-797.t` (PERL) -> Cumulative Risk: **490.78**
- **Archetype:** `file_cluster_13` (Distance: 11.515 IQR)
- **Magnitude:** 32.86 | **LOC:** 57 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9997%), Tech Debt (93.8921%), Safety Score (75.2927%)

### 2. `t/forward_test_tcp.t` (PERL) -> Cumulative Risk: **487.49**
- **Archetype:** `file_cluster_0` (Distance: 11.741 IQR)
- **Magnitude:** 55.2 | **LOC:** 81 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (87.9875%)

### 3. `t/forward_hmv_params.t` (PERL) -> Cumulative Risk: **485.39**
- **Archetype:** `file_cluster_0` (Distance: 11.887 IQR)
- **Magnitude:** 40.88 | **LOC:** 58 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (84.2034%)

### 4. `t/error.t` (PERL) -> Cumulative Risk: **474.59**
- **Archetype:** `file_cluster_0` (Distance: 10.968 IQR)
- **Magnitude:** 70.86 | **LOC:** 320 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7829%), Secrets Risk (97.8667%), Safety Score (59.7957%)
- **Heaviest Functions:** `throw` (Impact: 5.5), `MyApp::Censor::censor` (Impact: 3.3), `new` (Impact: 1.1)

### 5. `t/dsl/send_as.t` (PERL) -> Cumulative Risk: **467.54**
- **Archetype:** `file_cluster_0` (Distance: 10.794 IQR)
- **Magnitude:** 49.22 | **LOC:** 167 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9925%), Documentation (83.5227%), Safety Score (75.4087%)
- **Heaviest Functions:** `TO_JSON` (Impact: 1.6)

### 6. `t/disp_named_capture.t` (PERL) -> Cumulative Risk: **463.22**
- **Archetype:** `file_cluster_13` (Distance: 12.851 IQR)
- **Magnitude:** 35.48 | **LOC:** 32 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (90.8121%), Documentation (88.5534%)

### 7. `t/session_engines.t` (PERL) -> Cumulative Risk: **458.43**
- **Archetype:** `file_cluster_13` (Distance: 11.825 IQR)
- **Magnitude:** 71.8 | **LOC:** 117 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (88.4655%), Documentation (86.5195%)

### 8. `t/request_upload.t` (PERL) -> Cumulative Risk: **453.67**
- **Archetype:** `file_cluster_0` (Distance: 12.472 IQR)
- **Magnitude:** 161.64 | **LOC:** 210 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.5867%), Cognitive Load (72.7512%)
- **Heaviest Functions:** `run_test` (Impact: 39.4), `test_path` (Impact: 1.9)

### 9. `t/session_bad_client_cookie.t` (PERL) -> Cumulative Risk: **452.59**
- **Archetype:** `file_cluster_0` (Distance: 11.347 IQR)
- **Magnitude:** 47.8 | **LOC:** 121 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Safety Score (80.3089%), Cognitive Load (61.5523%)
- **Heaviest Functions:** `generate_id` (Impact: 11.1)

### 10. `t/template_default_tokens.t` (PERL) -> Cumulative Risk: **449.83**
- **Archetype:** `file_cluster_13` (Distance: 11.975 IQR)
- **Magnitude:** 32.82 | **LOC:** 54 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Documentation (85.986%), Safety Score (79.0488%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `t/request_upload.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.472 IQR)
- **Top Global Matches:** file_cluster_0: 12.472, file_cluster_13: 12.833, file_cluster_11: 13.145
- **Magnitude:** 161.64 | **LOC:** 210 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (72.7512%), Tech Debt (23.9997%)
**Top Internal Functions/Classes:**
  * `run_test` (Impact: 39.4)
  * `test_path` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 43`, `args: 1`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 117`, `orphaned_logic: 1`
* *Architecture:* `io: 5`, `import: 13`
* *Defense:* `safety: 3`, `test: 8`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Encode, Carp, strict, warnings, File::Temp, Test::More, Test::Fatal, Dancer2::Core::Request...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/request.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.844 IQR)
- **Top Global Matches:** file_cluster_0: 10.844, file_cluster_8: 11.191, file_cluster_13: 11.382
- **Magnitude:** 99.1 | **LOC:** 274 | **CtrlFlow:** 58.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (52.8231%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run_test` (Impact: 34.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 39`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 60`
* *Architecture:* `import: 6`
* *Defense:* `safety: 2`, `test: 25`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, warnings, Dancer2::Core::App, Test::More, Dancer2::Core::Request
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dispatcher.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.433 IQR)
- **Top Global Matches:** file_cluster_0: 11.433, file_cluster_8: 11.455, file_cluster_13: 11.535
- **Magnitude:** 98.98 | **LOC:** 247 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (58.4605%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 56`, `args: 5`
* *Risk/State:* `state_mutation: 80`
* *Architecture:* `import: 11`
* *Defense:* `safety: 3`, `test: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2::Core::Hook, Carp, strict, Dancer2, Dancer2::Core::Route, warnings, Dancer2::Core::Response, Dancer2::Core::App...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/deserialize.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.616 IQR)
- **Top Global Matches:** file_cluster_0: 11.616, file_cluster_13: 11.813, file_cluster_8: 11.99
- **Magnitude:** 98.3 | **LOC:** 229 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.1596%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 66`, `args: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 77`
* *Architecture:* `api: 3`, `import: 12`
* *Defense:* `safety: 2`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Encode, strict, Dancer2, warnings, utf8, JSON::MaybeXS, HTTP::Request::Common, Dancer2::Logger::Capture...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dsl/uri_for_route.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.045 IQR)
- **Top Global Matches:** file_cluster_0: 11.045, file_cluster_8: 11.352, file_cluster_13: 11.363
- **Magnitude:** 97.2 | **LOC:** 247 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.1587%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_app` (Impact: 32.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 45`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 57`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 6`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Plack::Builder, strict, Dancer2, warnings, JSON::MaybeXS, HTTP::Request::Common, Plack::Test, Test::More
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/hooks.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.315 IQR)
- **Top Global Matches:** file_cluster_0: 11.315, file_cluster_13: 11.51, file_cluster_8: 11.75
- **Magnitude:** 86.46 | **LOC:** 352 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (32.49%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `my_after` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 113`, `args: 8`, `func_start: 1`, `class_start: 9`
* *Risk/State:* `state_mutation: 67`
* *Architecture:* `api: 13`, `import: 21`
* *Defense:* `safety: 3`, `test: 34`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` content, Capture::Tiny, strict, Template, Dancer2, warnings, JSON::MaybeXS, Sub::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dsl/parameters.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 9.859 IQR)
- **Top Global Matches:** file_cluster_0: 9.859, file_cluster_8: 10.03, file_cluster_13: 10.295
- **Magnitude:** 81.62 | **LOC:** 393 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.8235%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 73`, `class_start: 7`
* *Risk/State:* `state_mutation: 51`
* *Architecture:* `api: 9`, `import: 14`
* *Defense:* `safety: 2`, `test: 53`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Encode, strict, Dancer2, utf8, warnings, critic, HTTP::Request::Common, Plack::Test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/cookie.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.474 IQR)
- **Top Global Matches:** file_cluster_0: 10.474, file_cluster_8: 10.613, file_cluster_13: 10.654
- **Magnitude:** 80.96 | **LOC:** 211 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.8815%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `all_tests` (Impact: 45.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 31`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 32`
* *Architecture:* `import: 10`
* *Defense:* `safety: 2`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, warnings, Dancer2::Core::Cookie, domain, Test::More, Test::Fatal, Dancer2::Core::Request, cookie
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/multiapp_template_hooks.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.503 IQR)
- **Top Global Matches:** file_cluster_0: 11.503, file_cluster_13: 11.585, file_cluster_8: 11.605
- **Magnitude:** 80.9 | **LOC:** 206 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (59.5369%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 43`, `args: 6`, `class_start: 2`
* *Risk/State:* `state_mutation: 60`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 2`, `test: 17`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, Dancer2, hooks, routes, warnings, HTTP::Request::Common, Plack::Test, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/session_lifecycle.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.667 IQR)
- **Top Global Matches:** file_cluster_8: 10.667, file_cluster_13: 10.749, file_cluster_0: 10.883
- **Magnitude:** 77.36 | **LOC:** 228 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.843%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 67`, `class_start: 1`
* *Risk/State:* `state_mutation: 53`
* *Architecture:* `api: 6`, `import: 9`
* *Defense:* `safety: 2`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, HTTP::Cookies, Dancer2, warnings, HTTP::Request::Common, lib, new, Plack::Test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/issues/gh-1564.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.796 IQR)
- **Top Global Matches:** file_cluster_13: 11.796, file_cluster_0: 11.909, file_cluster_8: 11.953
- **Magnitude:** 74.92 | **LOC:** 114 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.1355%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 42`, `args: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 51`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `safety: 2`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Plack::Builder, strict, Dancer2, warnings, HTTP::Request::Common, Plack::Test, Test::More
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/session_forward.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.002 IQR)
- **Top Global Matches:** file_cluster_0: 11.002, file_cluster_13: 11.457, file_cluster_11: 11.645
- **Magnitude:** 72.92 | **LOC:** 196 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.119%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 52`, `class_start: 3`
* *Risk/State:* `state_mutation: 47`, `dead_code: 1`
* *Architecture:* `api: 8`, `import: 9`
* *Defense:* `safety: 2`, `test: 13`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, HTTP::Cookies, Dancer2, warnings, HTTP::Request::Common, Plack::Test, Test::More
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/session_engines.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.825 IQR)
- **Top Global Matches:** file_cluster_13: 11.825, file_cluster_0: 11.913, file_cluster_8: 12.101
- **Magnitude:** 71.8 | **LOC:** 117 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (72.6667%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 44`, `args: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 51`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 2`, `test: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, HTTP::Cookies, Dancer2, warnings, YAML, HTTP::Request::Common, Plack::Test, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/error.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.968 IQR)
- **Top Global Matches:** file_cluster_0: 10.968, file_cluster_13: 11.184, file_cluster_8: 11.347
- **Magnitude:** 70.86 | **LOC:** 320 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.7408%), Tech Debt (17.1636%)
**Top Internal Functions/Classes:**
  * `throw` (Impact: 5.5)
  * `MyApp::Censor::censor` (Impact: 3.3)
  * `new` (Impact: 1.1)
  * `as_str` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 105`, `args: 4`, `func_start: 4`, `class_start: 6`
* *Risk/State:* `state_mutation: 50`, `orphaned_logic: 1`
* *Architecture:* `api: 5`, `import: 21`
* *Defense:* `safety: 5`, `test: 36`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` errors, Dancer2::Core::Error, overload, strict, Dancer2, warnings, Dancer2::Core::Response, JSON::MaybeXS...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dsl/delayed.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.708 IQR)
- **Top Global Matches:** file_cluster_0: 10.708, file_cluster_13: 10.939, file_cluster_11: 11.082
- **Magnitude:** 65.22 | **LOC:** 189 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.9708%), Tech Debt (38.193%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 58`, `args: 3`, `class_start: 6`
* *Risk/State:* `state_mutation: 37`, `planned_debt: 4`
* *Architecture:* `api: 7`, `concurrency: 3`, `import: 13`
* *Defense:* `safety: 3`, `test: 30`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, Dancer2, warnings, critic, HTTP::Request::Common, Plack::Test, Test::More, AnyEvent
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/template.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.69 IQR)
- **Top Global Matches:** file_cluster_0: 10.69, file_cluster_13: 10.819, file_cluster_8: 11.11
- **Magnitude:** 61.24 | **LOC:** 221 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (21.8983%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 59`, `args: 5`, `class_start: 4`
* *Risk/State:* `state_mutation: 32`
* *Architecture:* `api: 11`, `import: 13`
* *Defense:* `safety: 3`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2::Core::Hook, strict, Template, Dancer2, warnings, HTTP::Request::Common, lib, Plack::Test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/redirect.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.86 IQR)
- **Top Global Matches:** file_cluster_13: 10.86, file_cluster_8: 10.937, file_cluster_0: 11.015
- **Magnitude:** 58.18 | **LOC:** 141 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.312%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 33`, `args: 2`, `class_start: 2`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* `api: 8`, `import: 8`
* *Defense:* `safety: 2`, `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, Dancer2, warnings, HTTP::Request::Common, Plack::Test, Test::More, Ref::Util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/serializer_mutable.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.562 IQR)
- **Top Global Matches:** file_cluster_0: 11.562, file_cluster_13: 11.627, file_cluster_8: 11.939
- **Magnitude:** 57.8 | **LOC:** 118 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.3962%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 39`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* `safety: 2`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Encode, strict, Dancer2, warnings, JSON::MaybeXS, YAML, HTTP::Request::Common, Plack::Test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/forward_test_tcp.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.741 IQR)
- **Top Global Matches:** file_cluster_0: 11.741, file_cluster_13: 11.796, file_cluster_11: 12.145
- **Magnitude:** 55.2 | **LOC:** 81 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (70.4052%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 21`, `args: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 31`
* *Architecture:* `api: 8`, `import: 7`
* *Defense:* `safety: 2`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, Dancer2, warnings, HTTP::Request::Common, Plack::Test, Test::More, Ref::Util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dsl/send_file.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.344 IQR)
- **Top Global Matches:** file_cluster_13: 10.344, file_cluster_0: 10.442, file_cluster_8: 10.519
- **Magnitude:** 54.52 | **LOC:** 161 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (25.6643%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 57`, `args: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `io: 1`, `api: 10`, `import: 14`
* *Defense:* `safety: 2`, `test: 37`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Encode, strict, Dancer2, utf8, warnings, streaming, HTTP::Request::Common, Plack::Test...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/session_hooks_no_change_id.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.834 IQR)
- **Top Global Matches:** file_cluster_0: 10.834, file_cluster_8: 10.835, file_cluster_13: 10.891
- **Magnitude:** 54.0 | **LOC:** 196 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.4217%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 62`, `args: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 32`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 2`, `test: 12`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, HTTP::Cookies, Dancer2, warnings, HTTP::Request::Common, lib, Plack::Test, Test::More
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/session_hooks.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.812 IQR)
- **Top Global Matches:** file_cluster_0: 10.812, file_cluster_8: 10.813, file_cluster_13: 10.906
- **Magnitude:** 53.98 | **LOC:** 191 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.6932%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 61`, `args: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 32`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `safety: 2`, `test: 12`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, HTTP::Cookies, Dancer2, warnings, HTTP::Request::Common, Plack::Test, Test::More
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/app.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 9.923 IQR)
- **Top Global Matches:** file_cluster_0: 9.923, file_cluster_8: 10.137, file_cluster_13: 10.199
- **Magnitude:** 50.6 | **LOC:** 285 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (16.4367%), Tech Debt (14.9423%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 77`
* *Risk/State:* `state_mutation: 31`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `import: 9`
* *Defense:* `safety: 3`, `test: 10`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2::Core::Hook, strict, Dancer2, warnings, Dancer2::Core::App, Test::More, Test::Fatal, Dancer2::Core::Dispatcher...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dsl/send_as.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.794 IQR)
- **Top Global Matches:** file_cluster_0: 10.794, file_cluster_13: 10.955, file_cluster_8: 10.986
- **Magnitude:** 49.22 | **LOC:** 167 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (46.7603%), Tech Debt (31.3794%)
**Top Internal Functions/Classes:**
  * `TO_JSON` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 45`, `args: 1`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `state_mutation: 38`, `orphaned_logic: 1`
* *Architecture:* `api: 7`, `import: 8`
* *Defense:* `safety: 2`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, Moo, Dancer2, warnings, HTTP::Request::Common, Plack::Test, Test::More, defined
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/session_object.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.525 IQR)
- **Top Global Matches:** file_cluster_0: 13.525, file_cluster_13: 13.54, file_cluster_11: 13.992
- **Magnitude:** 48.76 | **LOC:** 51 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (77.9569%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 22`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* `import: 10`
* *Defense:* `safety: 4`, `test: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dups, Crypt::URandom, duplicate, Dancer2::Core::Session, strict, Math::Random::ISAAC::XS, warnings, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `t/serializer.t` (PERL) | Magnitude: 23.68 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 15, decorators: 9, import: 8
- `t/session_hooks.t` (PERL) | Magnitude: 53.98 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 115, structural_boundaries: 61, pointers: 44, state_mutation: 32
- `t/session_hooks_no_change_id.t` (PERL) | Magnitude: 54.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 115, structural_boundaries: 62, pointers: 44, state_mutation: 32
- `t/dsl/to_app.t` (PERL) | Magnitude: 23.5 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 17, indent_spaces: 16, decorators: 8, import: 7
- `t/dsl/mime.t` (PERL) | Magnitude: 19.56 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 13, test: 7, decorators: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/issues/gh-723.t` (PERL) | Magnitude: 24.92 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 22, test: 11, decorators: 8
- `t/plugin2/no-config.t` (PERL) | Magnitude: 15.48 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 9, decorators: 6, import: 6
- `t/disp_named_capture.t` (PERL) | Magnitude: 35.48 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 18, structural_boundaries: 15, indent_spaces: 8, decorators: 6
- `t/charset_server.t` (PERL) | Magnitude: 27.86 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 18, decorators: 9, import: 9
- `t/no_default_middleware.t` (PERL) | Magnitude: 25.92 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 23, decorators: 13, import: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `t/dsl/any.t` (PERL) | Magnitude: 41.82 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 33, indent_spaces: 29, state_mutation: 25, encapsulation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `t/config_settings.t` (PERL) | Magnitude: 15.34 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: test: 10, branch: 5, structural_boundaries: 4, import: 4
- `t/app/t1/bin/app.psgi` (PERL) | Magnitude: 12.08 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, import: 2, ssr_boundaries: 1
- `t/app/t_config_file_extended/bin/app.psgi` (PERL) | Magnitude: 12.08 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, import: 2, ssr_boundaries: 1
- `t/named_routes.t` (PERL) | Magnitude: 25.34 | Delta: **0.071 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 26, test: 17, closures: 12
- `t/plugin_register.t` (PERL) | Magnitude: 15.92 | Delta: **0.08 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 21, test: 10, import: 10

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `t/request_upload.t` -> **Sawyer X** (100.0% isolated ownership) | Magnitude: 161.64
- `t/request.t` -> **Sawyer X** (100.0% isolated ownership) | Magnitude: 99.1
- `t/dispatcher.t` -> **Sawyer X** (100.0% isolated ownership) | Magnitude: 98.98
- `t/cookie.t` -> **Sawyer X** (100.0% isolated ownership) | Magnitude: 80.96
- `t/multiapp_template_hooks.t` -> **Sawyer X** (100.0% isolated ownership) | Magnitude: 80.9

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `t/dsl/content.t` -> **Severity: 0.907** (Embedded: 0.0133 * Error Risk: 68.3381%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `t/dsl/content.t` -> **Severity: 869.258** (Blast Radius: 15.408 * Doc Risk: 56.416%)
- `t/issues/gh-1449/TestPlugin.pm` -> **Severity: 588.866** (Blast Radius: 8.03 * Doc Risk: 73.3333%)
- `t/caller.t` -> **Severity: 434.0** (Blast Radius: 4.34 * Doc Risk: 100.0%)
- `t/dsl/halt_with_param.t` -> **Severity: 434.0** (Blast Radius: 4.34 * Doc Risk: 100.0%)
- `t/dsl/send_file.t` -> **Severity: 434.0** (Blast Radius: 4.34 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
