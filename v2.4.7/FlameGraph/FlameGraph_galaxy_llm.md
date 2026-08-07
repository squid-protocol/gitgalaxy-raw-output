# ARCHITECTURAL_BRIEF: FlameGraph
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/FlameGraph` |
| **Timestamp** | `2026-08-07T03:51:32.722652+00:00` |
| **Scan Duration** | `0.29s` |
| **Git Branch** | `master` |
| **Git Commit** | `41fee1f99f9276008b7cd112fca19dc3ea84ac32` |
| **Git Remote** | `https://github.com/brendangregg/FlameGraph.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2 malicious artifacts.

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
| Total Artifacts | 161 |
| Analyzed Artifacts (Scanned) | 36 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 125 |
| Total LOC | 2117 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 22.4% |
| Dominant Lang | PERL |

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
| PERL | 22 | 1979 | 61.1% |
| XML | 9 | 0 | 25.0% |
| MARKDOWN | 3 | 0 | 8.3% |
| SHELL | 1 | 65 | 2.8% |
| PYTHON | 1 | 73 | 2.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.019`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 25 | 69.4% |
| file_cluster_0 | 6 | 16.7% |
| file_cluster_17 | 1 | 2.8% |
| file_cluster_13 | 1 | 2.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 8.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 125*

**Composition by Extension & Reason:**
- `.txt`: 92x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 41914 LOC exceeds safe regex boundaries)
- `.svg`: 1x Excluded (Static Asset Blob without Intent: 1256 LOC), 1x Excluded (Massive Static Asset Blob: 2520 LOC), 1x Excluded (Massive Static Asset Blob: 3556 LOC)
- `.pl`: 1x Excluded (Machine-Generated Source Code Signature: 151 LOC), 1x Excluded (Machine-Generated Source Code Signature: 146 LOC), 1x Excluded (Machine-Generated Source Code Signature: 177 LOC)
- `.awk`: 3x Excluded (Unsupported Extension: '.awk')
- `.d`: 2x Excluded (Unsupported Extension: '.d')
- `.sh`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 1x Excluded (Machine-Generated Source Code Signature: 14469 LOC)
- `.gz`: 1x Excluded (Explicitly Denied Extension: '.gz')
- `.php`: 1x Excluded (Machine-Generated Source Code Signature: 198 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 95.8 | 65.9 | 84.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 70.7 | 96.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 9.6 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 11.2 | 2.3 | 0.2 |
| API Exposure | 0.0 | 7.3 | 0.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 72.7 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 23.8 | 1.5 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 74.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 12.1 | 8.9 | 11.9 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `flamegraph.pl` (Hits: 12)
- `difffolded.pl` (Hits: 6)
- `aix-perf.pl` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **README.md** (`README.md`) — 0 inbound connections
2. **README** (`demos/README`) — 0 inbound connections
3. **README** (`dev/README`) — 0 inbound connections
4. **aix-perf.pl** (`aix-perf.pl`) — 0 inbound connections
5. **hcstackcollapse.pl** (`dev/hcstackcollapse.pl`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **flamegraph.pl** (`flamegraph.pl`) — 9 outbound dependencies
2. **range-perf.pl** (`range-perf.pl`) — 4 outbound dependencies
3. **hotcoldgraph.pl** (`dev/hotcoldgraph.pl`) — 3 outbound dependencies
4. **stackcollapse-elfutils.pl** (`stackcollapse-elfutils.pl`) — 3 outbound dependencies
5. **hcstackcollapse.pl** (`dev/hcstackcollapse.pl`) — 2 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `sum_namehash` (@ `flamegraph.pl`) -> Impact: **238.6** | LOC: 387
- `reset_search` (@ `flamegraph.pl`) -> Impact: **50.3** | LOC: 106
- `header` (@ `flamegraph.pl`) -> Impact: **42.7** | LOC: 14
- `save_stack` (@ `stackcollapse-chrome-tracing.py`) -> Impact: **30.4** | LOC: 54
- `zoom` (@ `flamegraph.pl`) -> Impact: **30.1** | LOC: 37
- `group_start` (@ `flamegraph.pl`) -> Impact: **28.5** | LOC: 51
- `Anonymous_Block` (@ `jmaps`) -> Impact: **25.7** | LOC: 34
- `zoom` (@ `flamegraph.pl`) -> Impact: **25.0** | LOC: 49
- `header` (@ `dev/hotcoldgraph.pl`) -> Impact: **20.4** | LOC: 8
- `flow` (@ `dev/hotcoldgraph.pl`) -> Impact: **17.9** | LOC: 15

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 22 | 2821.54 | 83.98% | 14.42% |
| `dev` | 4 | 337.44 | 70.21% | 0.0% |
| `demos` | 10 | 95.68 | 4.5% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `jmaps` -> **100.0%** Exposure
- `stackcollapse-vsprof.pl` -> **99.9908%** Exposure
- `flamegraph.pl` -> **78.2244%** Exposure
- `stackcollapse-chrome-tracing.py` -> **39.0501%** Exposure
### Highest State Flux (Mutation/Volatility)
- `aix-perf.pl` -> **100.0%** Exposure
- `dev/hcstackcollapse.pl` -> **100.0%** Exposure
- `dev/hotcoldgraph.pl` -> **100.0%** Exposure
- `dev/thcstackcollapse.pl` -> **100.0%** Exposure
- `difffolded.pl` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `flamegraph.pl` -> **0** Orphaned Functions | **8** Duplicates
- `jmaps` -> **1** Orphaned Functions | **7** Duplicates
- `stackcollapse-vsprof.pl` -> **0** Orphaned Functions | **2** Duplicates
- `stackcollapse-chrome-tracing.py` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`jmaps`** -> AI Confidence: **99.29%**
2. **`stackcollapse-chrome-tracing.py`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `50` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `jmaps` (SHELL) -> Cumulative Risk: **581.27**
- **Archetype:** `file_cluster_8` (Distance: 12.98 IQR)
- **Magnitude:** 122.4 | **LOC:** 105 | **CtrlFlow:** 90.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.9887%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 25.7), `Anonymous_Block` (Impact: 9.4), `Anonymous_Block` (Impact: 8.2)

### 2. `flamegraph.pl` (PERL) -> Cumulative Risk: **570.97**
- **Archetype:** `file_cluster_8` (Distance: 13.937 IQR)
- **Magnitude:** 1660.94 | **LOC:** 1304 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.2323%), Cognitive Load (95.819%)
- **Heaviest Functions:** `sum_namehash` (Impact: 238.6), `reset_search` (Impact: 50.3), `header` (Impact: 42.7)

### 3. `stackcollapse-vsprof.pl` (PERL) -> Cumulative Risk: **506.32**
- **Archetype:** `file_cluster_0` (Distance: 14.633 IQR)
- **Magnitude:** 69.86 | **LOC:** 99 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9908%), Safety Score (99.051%)
- **Heaviest Functions:** `print_stack_trace` (Impact: 3.6), `massage_function_names` (Impact: 2.1), `parse_integer` (Impact: 2.1)

### 4. `stackcollapse-chrome-tracing.py` (PYTHON) -> Cumulative Risk: **504.81**
- **Archetype:** `file_cluster_8` (Distance: 10.588 IQR)
- **Magnitude:** 78.96 | **LOC:** 145 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9706%), Safety Score (84.469%), Cognitive Load (82.0971%)
- **Heaviest Functions:** `save_stack` (Impact: 30.4), `get_trace_events` (Impact: 9.2), `load_events` (Impact: 5.7)

### 5. `dev/hotcoldgraph.pl` (PERL) -> Cumulative Risk: **483.75**
- **Archetype:** `file_cluster_8` (Distance: 12.97 IQR)
- **Magnitude:** 266.12 | **LOC:** 268 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.5484%), Cognitive Load (93.2764%)
- **Heaviest Functions:** `header` (Impact: 20.4), `flow` (Impact: 17.9), `stringTTF` (Impact: 16.9)

### 6. `stackcollapse-vtune.pl` (PERL) -> Cumulative Risk: **419.53**
- **Archetype:** `file_cluster_0` (Distance: 17.264 IQR)
- **Magnitude:** 75.74 | **LOC:** 98 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.5504%), Cognitive Load (81.9581%)

### 7. `difffolded.pl` (PERL) -> Cumulative Risk: **412.09**
- **Archetype:** `file_cluster_0` (Distance: 13.44 IQR)
- **Magnitude:** 44.66 | **LOC:** 116 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.8172%), Cognitive Load (91.2106%)
- **Heaviest Functions:** `usage` (Impact: 4.6)

### 8. `dev/hcstackcollapse.pl` (PERL) -> Cumulative Risk: **406.27**
- **Archetype:** `file_cluster_8` (Distance: 12.928 IQR)
- **Magnitude:** 35.76 | **LOC:** 88 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.9792%), Cognitive Load (93.7864%)
- **Heaviest Functions:** `remember_stack` (Impact: 2.2)

### 9. `dev/thcstackcollapse.pl` (PERL) -> Cumulative Risk: **405.66**
- **Archetype:** `file_cluster_8` (Distance: 12.933 IQR)
- **Magnitude:** 34.56 | **LOC:** 90 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.5725%), Cognitive Load (93.7864%)
- **Heaviest Functions:** `remember_stack` (Impact: 3.0)

### 10. `pkgsplit-perf.pl` (PERL) -> Cumulative Risk: **405.53**
- **Archetype:** `file_cluster_8` (Distance: 12.813 IQR)
- **Magnitude:** 57.7 | **LOC:** 87 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.4072%), Cognitive Load (92.9%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `flamegraph.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.937 IQR)
- **Top Global Matches:** file_cluster_8: 13.937, file_cluster_0: 13.98, file_cluster_17: 14.043
- **Magnitude:** 1660.94 | **LOC:** 1304 | **CtrlFlow:** 55.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.819%), Tech Debt (78.2244%)
**Top Internal Functions/Classes:**
  * `sum_namehash` (Impact: 238.6)
  * `reset_search` (Impact: 50.3)
  * `header` (Impact: 42.7)
  * `zoom` (Impact: 30.1)
  * `group_start` (Impact: 28.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 374`, `structural_boundaries: 305`, `args: 42`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 1`, `state_mutation: 1055`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 3`, `duplicate_logic: 8`
* *Architecture:* `io: 12`, `import: 3`
* *Defense:* `safety: 6`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` consistent, Getopt::Long, this, my, strict, open, GET, common...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/hotcoldgraph.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.97 IQR)
- **Top Global Matches:** file_cluster_8: 12.97, file_cluster_13: 13.338, file_cluster_17: 13.369
- **Magnitude:** 266.12 | **LOC:** 268 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.2764%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `header` (Impact: 20.4)
  * `flow` (Impact: 17.9)
  * `stringTTF` (Impact: 16.9)
  * `filledRectangle` (Impact: 8.9)
  * `color` (Impact: 5.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 83`, `args: 12`, `func_start: 12`
* *Risk/State:* `state_mutation: 180`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, meaning, this
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `jmaps` (SHELL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.98 IQR)
- **Top Global Matches:** file_cluster_8: 12.98, file_cluster_11: 13.094, file_cluster_17: 13.109
- **Magnitude:** 122.4 | **LOC:** 105 | **CtrlFlow:** 90.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.3658%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 25.7)
  * `Anonymous_Block` (Impact: 9.4)
  * `Anonymous_Block` (Impact: 8.2)
  * `Anonymous_Block` (Impact: 8.2)
  * `Anonymous_Block` (Impact: 7.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 6`, `args: 1`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 3`, `state_mutation: 48`, `duplicate_logic: 7`, `orphaned_logic: 1`
* *Architecture:* `io: 2`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-aix.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.055 IQR)
- **Top Global Matches:** file_cluster_8: 13.055, file_cluster_13: 13.275, file_cluster_17: 13.559
- **Magnitude:** 90.98 | **LOC:** 62 | **CtrlFlow:** 65.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.6533%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 8`
* *Risk/State:* `state_mutation: 75`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-chrome-tracing.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.588 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.298 IQR)
- **Top Global Matches:** file_cluster_8: 10.588, file_cluster_13: 10.8, file_cluster_7: 11.134
- **Magnitude:** 78.96 | **LOC:** 145 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.0971%), Tech Debt (39.0501%)
**Top Internal Functions/Classes:**
  * `save_stack` (Impact: 30.4)
  * `get_trace_events` (Impact: 9.2)
  * `load_events` (Impact: 5.7)
  * `__init__` (Impact: 2.5)
  * `cantor_pairing` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 16`, `args: 8`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 19`, `orphaned_logic: 1`
* *Architecture:* `api: 7`, `import: 2`
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` json, argparse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-vtune.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 17.264 IQR)
- **Top Global Matches:** file_cluster_0: 17.264, file_cluster_9: 17.339, file_cluster_17: 17.392
- **Magnitude:** 75.74 | **LOC:** 98 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.9581%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 13`
* *Risk/State:* `state_mutation: 60`, `dead_code: 2`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.402 IQR)
- **Top Global Matches:** file_cluster_8: 13.402, file_cluster_13: 13.529, file_cluster_17: 13.814
- **Magnitude:** 71.72 | **LOC:** 110 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.5326%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `remember_stack` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 14`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 69`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, this
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-vsprof.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.633 IQR)
- **Top Global Matches:** file_cluster_0: 14.633, file_cluster_13: 14.761, file_cluster_17: 14.762
- **Magnitude:** 69.86 | **LOC:** 99 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.8977%), Tech Debt (99.9908%)
**Top Internal Functions/Classes:**
  * `print_stack_trace` (Impact: 3.6)
  * `massage_function_names` (Impact: 2.1)
  * `parse_integer` (Impact: 2.1)
  * `print_stack_trace` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 24`, `args: 1`, `func_start: 6`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 59`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-vtune-mc.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.469 IQR)
- **Top Global Matches:** file_cluster_0: 12.469, file_cluster_13: 12.65, file_cluster_17: 12.683
- **Magnitude:** 66.58 | **LOC:** 104 | **CtrlFlow:** 64.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.454%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `usage` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 17`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 60`
* *Architecture:* `io: 1`, `import: 2`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, Getopt::Long
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.906 IQR)
- **Top Global Matches:** file_cluster_0: 12.906, file_cluster_13: 13.059, file_cluster_8: 13.159
- **Magnitude:** 59.38 | **LOC:** 63 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.4256%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `wanted` (Impact: 6.8)
  * `usage` (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 11`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 47`
* *Architecture:* `import: 2`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, File::Find
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkgsplit-perf.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.813 IQR)
- **Top Global Matches:** file_cluster_8: 12.813, file_cluster_13: 12.917, file_cluster_0: 12.975
- **Magnitude:** 57.7 | **LOC:** 87 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.9%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 6`
* *Risk/State:* `state_mutation: 42`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, the
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `range-perf.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.495 IQR)
- **Top Global Matches:** file_cluster_13: 12.495, file_cluster_8: 12.63, file_cluster_0: 12.764
- **Magnitude:** 57.48 | **LOC:** 138 | **CtrlFlow:** 57.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.6445%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `usage` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 14`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 54`
* *Architecture:* `io: 1`, `import: 3`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` raw, strict, POSIX, Getopt::Long
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-elfutils.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.066 IQR)
- **Top Global Matches:** file_cluster_8: 12.066, file_cluster_13: 12.168, file_cluster_0: 12.396
- **Magnitude:** 56.84 | **LOC:** 99 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.1391%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `add_current` (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 12`, `func_start: 1`
* *Risk/State:* `state_mutation: 51`
* *Architecture:* `io: 1`, `import: 2`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, Getopt::Long, this
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-gdb.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.975 IQR)
- **Top Global Matches:** file_cluster_8: 11.975, file_cluster_13: 12.155, file_cluster_17: 12.518
- **Magnitude:** 45.66 | **LOC:** 73 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.5139%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 7`
* *Risk/State:* `state_mutation: 30`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, this
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `aix-perf.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.965 IQR)
- **Top Global Matches:** file_cluster_17: 12.965, file_cluster_0: 13.015, file_cluster_13: 13.053
- **Magnitude:** 45.52 | **LOC:** 32 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.9512%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 9`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 30`
* *Architecture:* `io: 3`, `import: 1`
* *Defense:* `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `difffolded.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.44 IQR)
- **Top Global Matches:** file_cluster_0: 13.44, file_cluster_13: 13.687, file_cluster_11: 13.79
- **Magnitude:** 44.66 | **LOC:** 116 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.2106%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `usage` (Impact: 4.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 13`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 39`, `dead_code: 1`
* *Architecture:* `io: 6`, `import: 2`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, Getopt::Std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-java-exceptions.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.052 IQR)
- **Top Global Matches:** file_cluster_0: 12.052, file_cluster_13: 12.058, file_cluster_8: 12.095
- **Magnitude:** 40.2 | **LOC:** 73 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.4078%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `usage` (Impact: 4.4)
  * `remember_stack` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 16`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* `io: 1`, `import: 2`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, Getopt::Long
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-bpftrace.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.436 IQR)
- **Top Global Matches:** file_cluster_8: 12.436, file_cluster_13: 12.533, file_cluster_17: 12.92
- **Magnitude:** 39.52 | **LOC:** 73 | **CtrlFlow:** 81.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.099%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 3`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-faulthandler.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.836 IQR)
- **Top Global Matches:** file_cluster_8: 11.836, file_cluster_13: 11.982, file_cluster_17: 12.376
- **Magnitude:** 36.56 | **LOC:** 62 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.4999%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 5`
* *Risk/State:* `state_mutation: 21`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, this
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/hcstackcollapse.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.928 IQR)
- **Top Global Matches:** file_cluster_8: 12.928, file_cluster_13: 12.982, file_cluster_17: 13.328
- **Magnitude:** 35.76 | **LOC:** 88 | **CtrlFlow:** 60.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.7864%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `remember_stack` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, this
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/thcstackcollapse.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.933 IQR)
- **Top Global Matches:** file_cluster_8: 12.933, file_cluster_13: 12.983, file_cluster_17: 13.33
- **Magnitude:** 34.56 | **LOC:** 90 | **CtrlFlow:** 67.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.7864%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `remember_stack` (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 9`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 31`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, this
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-instruments.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.31 IQR)
- **Top Global Matches:** file_cluster_8: 12.31, file_cluster_13: 12.313, file_cluster_0: 12.361
- **Magnitude:** 33.44 | **LOC:** 35 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0797%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 6`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `io: 2`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-stap.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.978 IQR)
- **Top Global Matches:** file_cluster_8: 12.978, file_cluster_13: 13.021, file_cluster_17: 13.38
- **Magnitude:** 32.42 | **LOC:** 85 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.1401%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `remember_stack` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 7`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 30`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, this
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-recursive.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.967 IQR)
- **Top Global Matches:** file_cluster_8: 10.967, file_cluster_7: 11.583, file_cluster_13: 11.722
- **Magnitude:** 30.44 | **LOC:** 61 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.8294%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 7`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `io: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` this
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `demos/cpu-grep.svg` (XML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 10.52 | **LOC:** 136 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `stackcollapse-java-exceptions.pl` (PERL) | Magnitude: 40.2 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 33, indent_tabs: 19, structural_boundaries: 16, branch: 14
- `stackcollapse-vtune.pl` (PERL) | Magnitude: 75.74 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 60, indent_tabs: 18, structural_boundaries: 13, encapsulation: 12
- `stackcollapse-vsprof.pl` (PERL) | Magnitude: 69.86 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 59, indent_spaces: 26, structural_boundaries: 24, branch: 15
- `files.pl` (PERL) | Magnitude: 59.38 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 47, indent_tabs: 27, branch: 12, structural_boundaries: 11
- `stackcollapse-vtune-mc.pl` (PERL) | Magnitude: 66.58 | Delta: **0.181 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 60, indent_tabs: 34, branch: 31, structural_boundaries: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `range-perf.pl` (PERL) | Magnitude: 57.48 | Delta: **0.135 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 54, indent_tabs: 26, branch: 19, structural_boundaries: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `aix-perf.pl` (PERL) | Magnitude: 45.52 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 30, indent_tabs: 11, branch: 10, structural_boundaries: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `stackcollapse-instruments.pl` (PERL) | Magnitude: 33.44 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 18, indent_tabs: 16, branch: 6, structural_boundaries: 6
- `flamegraph.pl` (PERL) | Magnitude: 1660.94 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 1055, indent_tabs: 869, branch: 374, structural_boundaries: 305
- `stackcollapse-stap.pl` (PERL) | Magnitude: 32.42 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 30, indent_tabs: 16, branch: 11, regex_execution: 8
- `dev/thcstackcollapse.pl` (PERL) | Magnitude: 34.56 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 31, branch: 19, indent_tabs: 16, structural_boundaries: 9
- `dev/hcstackcollapse.pl` (PERL) | Magnitude: 35.76 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 33, indent_tabs: 16, branch: 14, structural_boundaries: 9

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `dev/hcstackcollapse.pl` -> **Severity: 337.247** (Blast Radius: 27.778 * Doc Risk: 12.1408%)
- `aix-perf.pl` -> **Severity: 331.122** (Blast Radius: 27.778 * Doc Risk: 11.9203%)
- `dev/hotcoldgraph.pl` -> **Severity: 331.122** (Blast Radius: 27.778 * Doc Risk: 11.9203%)
- `dev/thcstackcollapse.pl` -> **Severity: 331.122** (Blast Radius: 27.778 * Doc Risk: 11.9203%)
- `difffolded.pl` -> **Severity: 331.122** (Blast Radius: 27.778 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
