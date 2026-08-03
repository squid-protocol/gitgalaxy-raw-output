# ARCHITECTURAL_BRIEF: FlameGraph
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/FlameGraph` |
| **Timestamp** | `2026-08-03T19:29:25.918615+00:00` |
| **Scan Duration** | `0.35s` |
| **Git Branch** | `master` |
| **Git Commit** | `41fee1f99f9276008b7cd112fca19dc3ea84ac32` |
| **Git Remote** | `https://github.com/brendangregg/FlameGraph.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2 malicious artifacts.

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
| Cognitive Load Exposure | 5.0 | 99.3 | 66.7 | 86.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 63.2 | 83.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 8.1 | 0.0 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 11.2 | 2.3 | 0.2 |
| API Exposure | 0.0 | 7.3 | 0.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 72.7 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 23.8 | 1.5 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 74.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 94.9 | 11.4 | 11.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 6.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 18.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 12.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `sum_namehash` (@ `flamegraph.pl`) -> Impact: **723.6** | LOC: 387
- `save_stack` (@ `stackcollapse-chrome-tracing.py`) -> Impact: **169.0** | LOC: 54
- `reset_search` (@ `flamegraph.pl`) -> Impact: **95.4** | LOC: 106
- `header` (@ `flamegraph.pl`) -> Impact: **42.7** | LOC: 14
- `zoom_child` (@ `flamegraph.pl`) -> Impact: **28.9** | LOC: 18
- `group_start` (@ `flamegraph.pl`) -> Impact: **28.5** | LOC: 51
- `Anonymous_Block` (@ `jmaps`) -> Impact: **25.7** | LOC: 34
- `zoom` (@ `flamegraph.pl`) -> Impact: **25.0** | LOC: 49
- `get_trace_events` (@ `stackcollapse-chrome-tracing.py`) -> Impact: **22.2** | LOC: 11
- `zoom_parent` (@ `flamegraph.pl`) -> Impact: **21.5** | LOC: 15

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `save_stack` (@ `stackcollapse-chrome-tracing.py`) -> **O(2^N) [Recursive]**
- `sum_namehash` (@ `flamegraph.pl`) -> **O(2^N) [Recursive]**
- `svg` (@ `dev/hotcoldgraph.pl`) -> **O(2^N) [Recursive]**
- `reset_search` (@ `flamegraph.pl`) -> **O(2^N) [Recursive]**
- `zoom_child` (@ `flamegraph.pl`) -> **O(2^N) [Recursive]**
- `zoom_parent` (@ `flamegraph.pl`) -> **O(2^N) [Recursive]**
- `zoom_reset` (@ `flamegraph.pl`) -> **O(2^N) [Recursive]**
  * *Intent:* // zoom
- `find_group` (@ `flamegraph.pl`) -> **O(2^N) [Recursive]**
- `init` (@ `flamegraph.pl`) -> **O(N^4)**
- `get_trace_events` (@ `stackcollapse-chrome-tracing.py`) -> **O(N^4)**

### Highest Data Gravity (Database Complexity)
- `sum_namehash` (@ `flamegraph.pl`) -> DB Complexity: **159**
- `reset_search` (@ `flamegraph.pl`) -> DB Complexity: **28**
- `usage` (@ `flamegraph.pl`) -> DB Complexity: **21**
- `zoom` (@ `flamegraph.pl`) -> DB Complexity: **20**
- `group_start` (@ `flamegraph.pl`) -> DB Complexity: **16**
- `namehash` (@ `flamegraph.pl`) -> DB Complexity: **13**
- `usage` (@ `files.pl`) -> DB Complexity: **9**
- `color` (@ `dev/hotcoldgraph.pl`) -> DB Complexity: **8**
- `flow` (@ `dev/hotcoldgraph.pl`) -> DB Complexity: **7**
- `update_text` (@ `flamegraph.pl`) -> DB Complexity: **7**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 22 | 3522.24 | 86.04% | 12.2% |
| `dev` | 4 | 335.04 | 65.88% | 0.0% |
| `demos` | 10 | 95.68 | 4.5% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `jmaps` -> **100.0%** Exposure
- `stackcollapse-vsprof.pl` -> **99.9908%** Exposure
- `stackcollapse-chrome-tracing.py` -> **39.0501%** Exposure
- `flamegraph.pl` -> **29.307%** Exposure
### Highest State Flux (Mutation/Volatility)
- `aix-perf.pl` -> **100.0%** Exposure
- `dev/hcstackcollapse.pl` -> **100.0%** Exposure
- `dev/hotcoldgraph.pl` -> **100.0%** Exposure
- `dev/thcstackcollapse.pl` -> **100.0%** Exposure
- `difffolded.pl` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `jmaps` -> **1** Orphaned Functions | **7** Duplicates
- `flamegraph.pl` -> **0** Orphaned Functions | **2** Duplicates
- `stackcollapse-vsprof.pl` -> **0** Orphaned Functions | **2** Duplicates
- `stackcollapse-chrome-tracing.py` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`jmaps`** -> AI Confidence: **99.29%**
2. **`stackcollapse-chrome-tracing.py`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `aix-perf.pl` -> **100.0%** Exposure
- `flamegraph.pl` -> **100.0%** Exposure
- `stackcollapse-chrome-tracing.py` -> **100.0%** Exposure
- `stackcollapse-vtune-mc.pl` -> **99.9931%** Exposure
- `range-perf.pl` -> **99.1879%** Exposure
### Weaponizable Injection Vectors
- `aix-perf.pl` -> **100.0%** Exposure
- `range-perf.pl` -> **100.0%** Exposure
- `stackcollapse-vtune-mc.pl` -> **100.0%** Exposure
- `stackcollapse-vtune.pl` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `flamegraph.pl` -> **100.0%** Exposure
- `stackcollapse-chrome-tracing.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `50` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `stackcollapse-chrome-tracing.py` (PYTHON) -> Cumulative Risk: **760.74**
- **Archetype:** `file_cluster_8` (Distance: 10.588 IQR)
- **Magnitude:** 235.16 | **LOC:** 145 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9706%)
- **Heaviest Functions:** `save_stack` (Impact: 169.0), `get_trace_events` (Impact: 22.2), `load_events` (Impact: 8.3)

### 2. `flamegraph.pl` (PERL) -> Cumulative Risk: **721.13**
- **Archetype:** `file_cluster_8` (Distance: 13.971 IQR)
- **Magnitude:** 2197.44 | **LOC:** 1304 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `sum_namehash` (Impact: 723.6), `reset_search` (Impact: 95.4), `header` (Impact: 42.7)

### 3. `aix-perf.pl` (PERL) -> Cumulative Risk: **613.11**
- **Archetype:** `file_cluster_17` (Distance: 12.975 IQR)
- **Magnitude:** 45.52 | **LOC:** 32 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)

### 4. `stackcollapse-vtune.pl` (PERL) -> Cumulative Risk: **611.86**
- **Archetype:** `file_cluster_0` (Distance: 17.264 IQR)
- **Magnitude:** 75.74 | **LOC:** 98 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Injection Surface (100.0%), Safety Score (98.5826%)

### 5. `stackcollapse-vtune-mc.pl` (PERL) -> Cumulative Risk: **608.03**
- **Archetype:** `file_cluster_0` (Distance: 12.474 IQR)
- **Magnitude:** 66.58 | **LOC:** 104 | **CtrlFlow:** 67.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Injection Surface (100.0%), Logic Bomb (99.9931%)
- **Heaviest Functions:** `usage` (Impact: 5.5)

### 6. `range-perf.pl` (PERL) -> Cumulative Risk: **602.01**
- **Archetype:** `file_cluster_13` (Distance: 12.508 IQR)
- **Magnitude:** 57.48 | **LOC:** 138 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Injection Surface (100.0%), Logic Bomb (99.1879%)
- **Heaviest Functions:** `usage` (Impact: 2.5)

### 7. `jmaps` (SHELL) -> Cumulative Risk: **582.12**
- **Archetype:** `file_cluster_8` (Distance: 12.982 IQR)
- **Magnitude:** 122.4 | **LOC:** 105 | **CtrlFlow:** 89.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.9896%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 25.7), `Anonymous_Block` (Impact: 9.4), `Anonymous_Block` (Impact: 8.2)

### 8. `stackcollapse-vsprof.pl` (PERL) -> Cumulative Risk: **508.41**
- **Archetype:** `file_cluster_0` (Distance: 14.655 IQR)
- **Magnitude:** 69.86 | **LOC:** 99 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9908%), Safety Score (96.1953%)
- **Heaviest Functions:** `print_stack_trace` (Impact: 3.6), `massage_function_names` (Impact: 2.1), `parse_integer` (Impact: 2.1)

### 9. `dev/hotcoldgraph.pl` (PERL) -> Cumulative Risk: **461.17**
- **Archetype:** `file_cluster_8` (Distance: 12.992 IQR)
- **Magnitude:** 263.72 | **LOC:** 268 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (93.3132%), Verification (80.0%)
- **Heaviest Functions:** `header` (Impact: 20.4), `flow` (Impact: 17.9), `stringTTF` (Impact: 16.9)

### 10. `files.pl` (PERL) -> Cumulative Risk: **404.62**
- **Archetype:** `file_cluster_0` (Distance: 12.973 IQR)
- **Magnitude:** 67.38 | **LOC:** 63 | **CtrlFlow:** 71.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.172%), Cognitive Load (94.8294%)
- **Heaviest Functions:** `wanted` (Impact: 14.8), `usage` (Impact: 4.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `flamegraph.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.971 IQR)
- **Top Global Matches:** file_cluster_8: 13.971, file_cluster_0: 14.017, file_cluster_17: 14.084
- **Magnitude:** 2197.44 | **LOC:** 1304 | **CtrlFlow:** 57.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 159
- **Risk Profile:** Cognitive Load (96.2968%), Tech Debt (29.307%)
**Top Internal Functions/Classes:**
  * `sum_namehash` (Impact: 723.6 | O(2^N) | DB: 159)
  * `reset_search` (Impact: 95.4 | O(2^N) | DB: 28)
  * `header` (Impact: 42.7 | O(N^1) | DB: 6)
  * `zoom_child` (Impact: 28.9 | O(2^N) | DB: 1)
  * `group_start` (Impact: 28.5 | O(N^1) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 387`, `structural_boundaries: 286`, `args: 42`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 1`, `state_mutation: 1059`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 12`, `import: 3`
* *Defense:* `safety: 6`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, this, common, open, consistent, meaning, GET, my...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/hotcoldgraph.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.992 IQR)
- **Top Global Matches:** file_cluster_8: 12.992, file_cluster_13: 13.362, file_cluster_17: 13.396
- **Magnitude:** 263.72 | **LOC:** 268 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (75.936%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `header` (Impact: 20.4 | O(N^1))
  * `flow` (Impact: 17.9 | O(N^1) | DB: 7)
  * `stringTTF` (Impact: 16.9 | O(N^1) | DB: 2)
  * `filledRectangle` (Impact: 8.9 | O(N^1) | DB: 5)
  * `color` (Impact: 5.0 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 74`, `args: 12`, `func_start: 12`
* *Risk/State:* `state_mutation: 180`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` meaning, strict, this
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-chrome-tracing.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.588 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.298 IQR)
- **Top Global Matches:** file_cluster_8: 10.588, file_cluster_13: 10.8, file_cluster_7: 11.134
- **Magnitude:** 235.16 | **LOC:** 145 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (82.0971%), Tech Debt (39.0501%)
**Top Internal Functions/Classes:**
  * `save_stack` (Impact: 169.0 | O(2^N) | DB: 4)
  * `get_trace_events` (Impact: 22.2 | O(N^4) | DB: 1)
  * `load_events` (Impact: 8.3 | O(N^2))
  * `__init__` (Impact: 3.6 | O(N^2) | DB: 4)
  * `get_stop_timestamp` (Impact: 2.7 | O(N^2))
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

### `jmaps` (SHELL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.982 IQR)
- **Top Global Matches:** file_cluster_8: 12.982, file_cluster_11: 13.087, file_cluster_17: 13.103
- **Magnitude:** 122.4 | **LOC:** 105 | **CtrlFlow:** 89.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (90.2064%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 25.7 | O(N^1) | DB: 6)
  * `Anonymous_Block` (Impact: 9.4 | O(N^1))
  * `Anonymous_Block` (Impact: 8.2 | O(N^1) | DB: 2)
  * `Anonymous_Block` (Impact: 8.2 | O(N^1) | DB: 2)
  * `Anonymous_Block` (Impact: 7.2 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 7`, `args: 1`
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
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

### `stackcollapse-vtune.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 17.264 IQR)
- **Top Global Matches:** file_cluster_0: 17.264, file_cluster_9: 17.339, file_cluster_17: 17.392
- **Magnitude:** 75.74 | **LOC:** 98 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Global Archetype:** `file_cluster_8` (Drift: 13.418 IQR)
- **Top Global Matches:** file_cluster_8: 13.418, file_cluster_13: 13.543, file_cluster_17: 13.831
- **Magnitude:** 71.72 | **LOC:** 110 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (91.2253%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `remember_stack` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 13`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 69`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, this
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-vsprof.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.655 IQR)
- **Top Global Matches:** file_cluster_0: 14.655, file_cluster_13: 14.783, file_cluster_17: 14.793
- **Magnitude:** 69.86 | **LOC:** 99 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (86.8389%), Tech Debt (99.9908%)
**Top Internal Functions/Classes:**
  * `print_stack_trace` (Impact: 3.6 | O(N^1) | DB: 4)
  * `massage_function_names` (Impact: 2.1 | O(N^1) | DB: 1)
  * `parse_integer` (Impact: 2.1 | O(N^1) | DB: 1)
  * `print_stack_trace` (Impact: 2.0 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 18`, `args: 1`, `func_start: 6`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 59`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `files.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.973 IQR)
- **Top Global Matches:** file_cluster_0: 12.973, file_cluster_13: 13.122, file_cluster_8: 13.247
- **Magnitude:** 67.38 | **LOC:** 63 | **CtrlFlow:** 71.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (94.8294%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `wanted` (Impact: 14.8 | O(N^1) | DB: 6)
  * `usage` (Impact: 4.7 | O(N^1) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 9`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 47`
* *Architecture:* `import: 2`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, File::Find
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-vtune-mc.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.474 IQR)
- **Top Global Matches:** file_cluster_0: 12.474, file_cluster_13: 12.655, file_cluster_17: 12.689
- **Magnitude:** 66.58 | **LOC:** 104 | **CtrlFlow:** 67.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (95.7349%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `usage` (Impact: 5.5 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 16`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 60`
* *Architecture:* `io: 1`, `import: 2`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, Getopt::Long
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `pkgsplit-perf.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.813 IQR)
- **Top Global Matches:** file_cluster_8: 12.813, file_cluster_13: 12.917, file_cluster_0: 12.975
- **Magnitude:** 57.7 | **LOC:** 87 | **CtrlFlow:** 82.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (92.9%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 6`
* *Risk/State:* `state_mutation: 42`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` the, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `range-perf.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.508 IQR)
- **Top Global Matches:** file_cluster_13: 12.508, file_cluster_8: 12.644, file_cluster_0: 12.777
- **Magnitude:** 57.48 | **LOC:** 138 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (92.626%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `usage` (Impact: 2.5 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 13`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 54`
* *Architecture:* `io: 1`, `import: 3`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, Getopt::Long, raw, POSIX
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-elfutils.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.087 IQR)
- **Top Global Matches:** file_cluster_8: 12.087, file_cluster_13: 12.188, file_cluster_0: 12.415
- **Magnitude:** 56.84 | **LOC:** 99 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (81.3617%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `add_current` (Impact: 4.7 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 11`, `func_start: 1`
* *Risk/State:* `state_mutation: 51`
* *Architecture:* `io: 1`, `import: 2`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, this, Getopt::Long
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-gdb.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.975 IQR)
- **Top Global Matches:** file_cluster_8: 11.975, file_cluster_13: 12.155, file_cluster_17: 12.518
- **Magnitude:** 45.66 | **LOC:** 73 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Global Archetype:** `file_cluster_17` (Drift: 12.975 IQR)
- **Top Global Matches:** file_cluster_17: 12.975, file_cluster_0: 13.025, file_cluster_13: 13.064
- **Magnitude:** 45.52 | **LOC:** 32 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (99.2776%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 9`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 30`
* *Architecture:* `io: 3`, `import: 1`
* *Defense:* `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Getopt::Std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `difffolded.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.451 IQR)
- **Top Global Matches:** file_cluster_0: 13.451, file_cluster_13: 13.698, file_cluster_11: 13.798
- **Magnitude:** 44.66 | **LOC:** 116 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (94.0179%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `usage` (Impact: 4.6 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 12`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 39`, `dead_code: 1`
* *Architecture:* `io: 6`, `import: 2`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, Getopt::Std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stackcollapse-java-exceptions.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.074 IQR)
- **Top Global Matches:** file_cluster_0: 12.074, file_cluster_13: 12.081, file_cluster_8: 12.118
- **Magnitude:** 40.2 | **LOC:** 73 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (86.6072%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `usage` (Impact: 4.4 | O(N^1) | DB: 2)
  * `remember_stack` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 14`, `args: 1`, `func_start: 2`
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Global Archetype:** `file_cluster_8` (Drift: 12.933 IQR)
- **Top Global Matches:** file_cluster_8: 12.933, file_cluster_13: 12.988, file_cluster_17: 13.338
- **Magnitude:** 35.76 | **LOC:** 88 | **CtrlFlow:** 63.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (93.7864%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `remember_stack` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 8`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 27.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, this
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/thcstackcollapse.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.937 IQR)
- **Top Global Matches:** file_cluster_8: 12.937, file_cluster_13: 12.989, file_cluster_17: 13.34
- **Magnitude:** 34.56 | **LOC:** 90 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (93.7864%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `remember_stack` (Impact: 3.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 8`, `args: 1`, `func_start: 1`
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Global Archetype:** `file_cluster_8` (Drift: 12.982 IQR)
- **Top Global Matches:** file_cluster_8: 12.982, file_cluster_13: 13.027, file_cluster_17: 13.391
- **Magnitude:** 32.42 | **LOC:** 85 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (92.1401%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `remember_stack` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 6`, `args: 1`, `func_start: 1`
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- `stackcollapse-java-exceptions.pl` (PERL) | Magnitude: 40.2 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 33, indent_tabs: 19, branch: 16, structural_boundaries: 14
- `stackcollapse-vtune.pl` (PERL) | Magnitude: 75.74 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 60, indent_tabs: 18, structural_boundaries: 13, encapsulation: 12
- `stackcollapse-vsprof.pl` (PERL) | Magnitude: 69.86 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 59, indent_spaces: 26, structural_boundaries: 18, branch: 15
- `files.pl` (PERL) | Magnitude: 67.38 | Delta: **0.149 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 47, indent_tabs: 27, branch: 22, structural_boundaries: 9
- `stackcollapse-vtune-mc.pl` (PERL) | Magnitude: 66.58 | Delta: **0.181 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 60, indent_tabs: 34, branch: 33, structural_boundaries: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `range-perf.pl` (PERL) | Magnitude: 57.48 | Delta: **0.136 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 54, indent_tabs: 26, branch: 21, structural_boundaries: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `aix-perf.pl` (PERL) | Magnitude: 45.52 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 30, branch: 12, indent_tabs: 11, structural_boundaries: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `stackcollapse-instruments.pl` (PERL) | Magnitude: 33.44 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 18, indent_tabs: 16, branch: 6, structural_boundaries: 6
- `stackcollapse-stap.pl` (PERL) | Magnitude: 32.42 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 30, indent_tabs: 16, branch: 11, regex_execution: 8
- `flamegraph.pl` (PERL) | Magnitude: 2197.44 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 1059, indent_tabs: 869, branch: 387, structural_boundaries: 286
- `dev/thcstackcollapse.pl` (PERL) | Magnitude: 34.56 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 31, branch: 19, indent_tabs: 16, structural_boundaries: 8
- `dev/hcstackcollapse.pl` (PERL) | Magnitude: 35.76 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 33, indent_tabs: 16, branch: 14, structural_boundaries: 8

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `stackcollapse-chrome-tracing.py` -> **Severity: 2636.729** (Blast Radius: 27.778 * Doc Risk: 94.9215%)
- `flamegraph.pl` -> **Severity: 350.833** (Blast Radius: 27.778 * Doc Risk: 12.6299%)
- `dev/hcstackcollapse.pl` -> **Severity: 341.681** (Blast Radius: 27.778 * Doc Risk: 12.3004%)
- `aix-perf.pl` -> **Severity: 331.122** (Blast Radius: 27.778 * Doc Risk: 11.9203%)
- `dev/hotcoldgraph.pl` -> **Severity: 331.122** (Blast Radius: 27.778 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
