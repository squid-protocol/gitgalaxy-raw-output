# ARCHITECTURAL_BRIEF: asm
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/0xAX/asm.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 36 analyzed artifact(s), 388 LOC.
- **Load-bearing artifact:** `content/asm_2.md` -- 3 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `content/asm_2.md` -- pulls in 9 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `float/dot_product.asm` at magnitude 50.94 (structural weight, not risk).
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
| Total Artifacts | 63 |
| Analyzed Artifacts (Scanned) | 36 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 27 |
| Total LOC | 388 |
| Volatility Index | 0.111 |
| % Scanned of codebase = | 57.1% |
| Dominant Lang | ASSEMBLY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.426 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1865 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.2941 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 2 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| MARKDOWN | 18 | 0 | 50.0% |
| MAKEFILE | 8 | 42 | 22.2% |
| ASSEMBLY | 7 | 319 | 19.4% |
| C | 2 | 27 | 5.6% |
| PLAINTEXT | 1 | 0 | 2.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo`
> **Architectural Drift Z-Score:** `4.136`
> **Composition Archetype:** `Small Flat Repo` (z +4.14; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 75%, Parameter Forwarders Files 17%, Declarative / Non-Code 3%, Large Core Modules 3%, Large Core Modules (3) 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 17 | 47.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 19 | 52.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 27*

**Composition by Extension & Reason:**
- `.svg`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 7x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 19.8 | 3.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 94.4 | 19.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 97.1 | 42.5 | 62.2 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 2.6 | 2.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 2.4 | 5.6 | 4.5 | 5.6 | 5.6 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 91.7 | 10.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 79.0 | 21.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.0 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 18.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 93.2 | 100.0 | 96.5 | 94.8 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 17 | 6 | 2 | `float/dot_product.asm` |
| cleanup | 6 | 3 | 0 | `casm/casm1/Makefile` |
| guards | 24 | 4 | 1 | `float/dot_product.asm` |
| danger | 6 | 3 | 0 | `float/dot_product.asm` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 26 | 17 | 2 | `casm/casm1/Makefile` |
| io | 22 | 6 | 2 | `float/dot_product.asm` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 2 | 1 | 0 | `float/dot_product.asm` |
| tests | 0 | 0 | 0 | - |
| docs | 0 | 0 | 0 | - |
| debt | 4 | 3 | 0 | `casm/casm3/casm.c` |
| mutation | 12 | 5 | 2 | `float/dot_product.asm` |
| dead_code | 43 | 9 | 4 | `float/dot_product.asm` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `float/dot_product.asm` (Hits: 10)
- `stack/stack.asm` (Hits: 4)
- `strings/reverse.asm` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **asm_2.md** (`content/asm_2.md`) — 3 inbound connections
2. **CODE_OF_CONDUCT.md** (`CODE_OF_CONDUCT.md`) — 2 inbound connections
3. **asm_1.md** (`content/asm_1.md`) — 2 inbound connections
4. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 1 inbound connections
5. **CONTRIBUTORS.md** (`CONTRIBUTORS.md`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **asm_2.md** (`content/asm_2.md`) — 9 outbound dependencies
2. **asm_3.md** (`content/asm_3.md`) — 5 outbound dependencies
3. **README.md** (`README.md`) — 3 outbound dependencies
4. **README.md** (`casm/README.md`) — 3 outbound dependencies
5. **asm_6.md** (`content/asm_6.md`) — 3 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_calculate_dot_product` **(Compute Cores)** (@ `float/dot_product.asm`) -> Impact: **7.5** | LOC: 29
  * *Intent:* ;; Prepare to calculate the dot product of the two vectors.
- `_parse_first_float_vector` **(Many-Argument Workhorses)** (@ `float/dot_product.asm`) -> Impact: **6.6** | LOC: 35
  * *Intent:* ;; Parse the floating-point values from the input buffer.
- `_parse_second_float_vector` **(Many-Argument Workhorses)** (@ `float/dot_product.asm`) -> Impact: **6.6** | LOC: 35
  * *Intent:* ;; Parse the floating-point values from the input buffer.
- `.loop` **(Compute Cores)** (@ `casm/casm3/casm.asm`) -> Impact: **6.1** | LOC: 9
- `_loop` **(Many-Argument Workhorses)** (@ `float/dot_product.asm`) -> Impact: **5.8** | LOC: 18
  * *Intent:* ;; Calculate the the dot product in the loop.
- `_start` **(Parameter Forwarders)** (@ `stack/stack.asm`) -> Impact: **5.2** | LOC: 34
  * *Intent:* ;; Entry point
- `__repeat` **(Parameter Forwarders)** (@ `stack/stack.asm`) -> Impact: **4.9** | LOC: 18
- `reverseStringAndPrint` **(Parameter Forwarders)** (@ `strings/reverse.asm`) -> Impact: **4.8** | LOC: 15
  * *Intent:* ;; Calculate the length of the input string and prepare to reverse it.
- `int_to_str` **(Parameter Forwarders)** (@ `stack/stack.asm`) -> Impact: **4.5** | LOC: 20
  * *Intent:* ;; Convert the sum to a string and print it to the standard output.
- `reverseString` **(Parameter Forwarders)** (@ `strings/reverse.asm`) -> Impact: **4.2** | LOC: 15
  * *Intent:* ;; Reverse the string and store it in the output buffer.

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Parameter Forwarders**: thin, many-argument glue that forwards to other code

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `content` | 7 | 61.36 | 0.0% | 0.0% |
| `float` | 3 | 56.24 | 2.03% | 25.31% |
| `stack` | 3 | 38.58 | 3.36% | 27.52% |
| `strings` | 3 | 31.14 | 6.59% | 27.25% |
| `casm/casm3` | 3 | 23.16 | 4.8% | 53.1% |
| `sum` | 3 | 15.0 | 1.75% | 32.36% |
| `hello` | 3 | 9.46 | 0.0% | 27.25% |
| `__monolith__` | 6 | 8.66 | 0.0% | 0.0% |
| `casm/casm1` | 2 | 8.26 | 0.0% | 40.88% |
| `casm/casm2` | 2 | 6.82 | 0.0% | 31.12% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `casm/casm3/casm.asm` -> **97.0688%** Exposure
- `sum/sum.asm` -> **97.0688%** Exposure
- `stack/stack.asm` -> **82.5498%** Exposure
- `casm/casm1/casm.asm` -> **81.7574%** Exposure
- `hello/hello.asm` -> **81.7574%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `strings/reverse.asm` -> **91.6827%** Exposure
- `casm/casm3/casm.asm` -> **50.0%** Exposure
- `stack/stack.asm` -> **37.5637%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `float/dot_product.asm` -> **4** Orphaned Functions | **0** Duplicates
- `casm/casm3/casm.asm` -> **2** Orphaned Functions | **0** Duplicates
- `stack/stack.asm` -> **2** Orphaned Functions | **0** Duplicates
- `sum/sum.asm` -> **2** Orphaned Functions | **0** Duplicates
- `casm/casm1/casm.asm` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `9` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `float/dot_product.asm` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 50.94 | **LOC:** 333 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Debt Markers (formerly Tech Debt) (75.9%), Guard Balance (formerly Safety Score) (73.0%), Dead Code Surface (formerly Dead Code) (49.3%)
- **Documentation Coverage:** 93.242% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_calculate_dot_product` **(Compute Cores)** (Impact: 7.5)
    * *Intent:* ;; Prepare to calculate the dot product of the two vectors.
  * `_parse_first_float_vector` **(Many-Argument Workhorses)** (Impact: 6.6)
    * *Intent:* ;; Parse the floating-point values from the input buffer.
  * `_parse_second_float_vector` **(Many-Argument Workhorses)** (Impact: 6.6)
    * *Intent:* ;; Parse the floating-point values from the input buffer.
  * `_loop` **(Many-Argument Workhorses)** (Impact: 5.8)
    * *Intent:* ;; Calculate the the dot product in the loop.
  * `_read_first_float_vector` **(Parameter Forwarders)** (Impact: 4.1)
    * *Intent:* ;; Read the first input string with floating-point values
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 69`, `args: 67`, `func_start: 11`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 2`, `dead_code: 11`, `unreferenced_by_name: 4`
* *Architecture:* `io: 10`, `api: 1`
* *Defense:* `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stack/stack.asm` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 33.28 | **LOC:** 164 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (87.2%), Debt Markers (formerly Tech Debt) (82.5%), Dead Code Surface (formerly Dead Code) (57.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.1%)
- **Documentation Coverage:** 94.342% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_start` **(Parameter Forwarders)** (Impact: 5.2)
    * *Intent:* ;; Entry point
  * `__repeat` **(Parameter Forwarders)** (Impact: 4.9)
  * `int_to_str` **(Parameter Forwarders)** (Impact: 4.5)
    * *Intent:* ;; Convert the sum to a string and print it to the standard output.
  * `printResult` **(Parameter Forwarders)** (Impact: 3.7)
    * *Intent:* ;; Print the result to the standard output.
  * `argcError` **(Parameter Forwarders)** (Impact: 2.6)
    * *Intent:* ;; Print the error message if not enough command-line arguments.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 46`, `args: 30`, `func_start: 8`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 2`, `dead_code: 6`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 1`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `strings/reverse.asm` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 25.84 | **LOC:** 104 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (94.4%), Mutation Surface (formerly State Flux) (91.7%), Debt Markers (formerly Tech Debt) (81.8%), Dead Code Surface (formerly Dead Code) (79.0%)
- **Documentation Coverage:** 94.342% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `reverseStringAndPrint` **(Parameter Forwarders)** (Impact: 4.8)
    * *Intent:* ;; Calculate the length of the input string and prepare to reverse it.
  * `reverseString` **(Parameter Forwarders)** (Impact: 4.2)
    * *Intent:* ;; Reverse the string and store it in the output buffer.
  * `printResult` **(Parameter Forwarders)** (Impact: 3.4)
    * *Intent:* ;; Print the reversed string to the standard output.
  * `_start` **(Parameter Forwarders)** (Impact: 2.5)
    * *Intent:* ;; Entry point of the program.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 21`, `args: 18`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 3`, `dead_code: 5`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 1`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `content/asm_3.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 12.78 | **LOC:** 639 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 31.314; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.038095
  * `Imports (Out-Degree: 1):` asm_2.md, asm-3-args-on-stack.svg, asm-3-stack-of__double-1.svg, asm-3-stack-of__double-2.svg, asm_2.md
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `casm/casm3/casm.asm` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 12.62 | **LOC:** 23 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.1%), Guard Balance (formerly Safety Score) (72.0%), Mutation Surface (formerly State Flux) (50.0%), Complexity Load (formerly Cognitive Load) (9.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `.loop` **(Compute Cores)** (Impact: 6.1)
  * `my_strlen` **(I/O & Config Routines)** (Impact: 1.2)
    * *Intent:* ;; Function that returns the length of the string passed in the first argument
  * `.done` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 3`, `args: 1`, `func_start: 3`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `content/asm_6.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 11.94 | **LOC:** 597 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 29.471; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 29.471
  * `Choke Point (Betweenness):` 0.001681 | `Ripple Effect (Closeness):` 0.028571
  * `Imports (Out-Degree: 3):` asm_2.md, asm_3.md, asm_4.md
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `content/asm_2.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 10.08 | **LOC:** 504 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 64.438; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 64.438
  * `Choke Point (Betweenness):` 0.001681 | `Ripple Effect (Closeness):` 0.085714
  * `Imports (Out-Degree: 1):` newscombinator-screenshot.png, rax.svg, reddit-screenshot.png, stack-before-call.svg, stack-during-call.svg, stack-preserve-bp.svg, stack.svg, asm_1.md...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `sum/sum.asm` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 9.7 | **LOC:** 54 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (97.1%), Dead Code Surface (formerly Dead Code) (58.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.1%), Complexity Load (formerly Cognitive Load) (5.3%)
- **Documentation Coverage:** 93.1735% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `.correctSum` **(Parameter Forwarders)** (Impact: 2.6)
    * *Intent:* ;; Print a message that the sum is correct
  * `.compare` **(I/O & Config Routines)** (Impact: 2.4)
  * `.exit` **(Parameter Forwarders)** (Impact: 1.8)
    * *Intent:* ;; Exit procedure
  * `_start` **(Interface Declarations)** (Impact: 1.4)
    * *Intent:* ;; Entry point
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 11`, `args: 4`, `func_start: 4`
* *Risk/State:* `dead_code: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `content/asm_5.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 9.04 | **LOC:** 452 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `content/asm_4.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 6.42 | **LOC:** 321 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 31.314; role: Pure Producer (Foundation)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.038095
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `casm/casm3/casm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 6.22 | **LOC:** 16 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 22.964; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (62.2%), Connectivity (formerly Api Exposure) (5.6%), Complexity Load (formerly Cognitive Load) (5.1%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Parameter Forwarders)** (Impact: 4.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`, `args: 2`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `content/asm_1.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 5.66 | **LOC:** 283 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 84.243; role: Pure Producer (Foundation)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 84.243
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.07619
  * `Imports (Out-Degree: 0):` registers.png
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `content/asm_7.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 5.44 | **LOC:** 272 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 22.964; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` asm_1.md, asm_2.md, asm_6.md
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `casm/casm1/Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 4.32 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (5.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `all` **(I/O & Config Routines)** (Impact: 1.1)
  * `clean` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `casm/casm3/Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 4.32 | **LOC:** 8 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (5.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `all` **(I/O & Config Routines)** (Impact: 1.1)
  * `clean` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `casm/casm2/Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 4.3 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (5.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `all` **(State Mutators)** (Impact: 1.1)
  * `clean` **(I/O & Config Routines)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `float/Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 4.3 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (5.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 93.242% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `all` **(I/O & Config Routines)** (Impact: 1.1)
  * `clean` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hello/Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 4.3 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (5.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 94.834% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `all` **(I/O & Config Routines)** (Impact: 1.1)
  * `clean` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `stack/Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 4.3 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (5.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 94.342% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `all` **(I/O & Config Routines)** (Impact: 1.1)
  * `clean` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `strings/Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 4.3 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (5.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 94.342% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `all` **(I/O & Config Routines)** (Impact: 1.1)
  * `clean` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sum/Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 4.3 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (5.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 93.1735% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `all` **(I/O & Config Routines)** (Impact: 1.1)
  * `clean` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `hello/hello.asm` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 4.16 | **LOC:** 31 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (81.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.3%), Dead Code Surface (formerly Dead Code) (64.6%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 94.834% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_start` **(Parameter Forwarders)** (Impact: 2.9)
    * *Intent:* ;; Entry point
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `args: 4`, `func_start: 1`
* *Risk/State:* `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `casm/casm1/casm.asm` (ASSEMBLY | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 3.94 | **LOC:** 30 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (81.8%), Dead Code Surface (formerly Dead Code) (64.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.1%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_start` **(Parameter Forwarders)** (Impact: 2.7)
    * *Intent:* ;; Entry point
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `args: 4`, `func_start: 1`
* *Risk/State:* `dead_code: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CODE_OF_CONDUCT.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 2.58 | **LOC:** 129 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); blast radius 46.631; role: Pure Producer (Foundation)
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 46.631
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.057143
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `casm/casm2/casm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2.52 | **LOC:** 20 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 22.964; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (62.2%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 1.2)
    * *Intent:* #include <stdio.h> #include <string.h>
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 3`, `func_start: 1`
* *Risk/State:* `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 22.964
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `float/dot_product.asm` -> Churn: **100.0%** | Cog Load: 6.0812% | Debt: 75.9444%
- `hello/hello.asm` -> Churn: **68.26%** | Cog Load: 0.0% | Debt: 81.7574%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `float/dot_product.asm` -> **Alex Kuleshov** (100.0% isolated ownership) | Magnitude: 50.94

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `casm/casm1/Makefile` -> **Severity: 2296.4** (Blast Radius: 22.964 * Doc Risk: 100.0%)
- `casm/casm2/Makefile` -> **Severity: 2296.4** (Blast Radius: 22.964 * Doc Risk: 100.0%)
- `casm/casm3/Makefile` -> **Severity: 2296.4** (Blast Radius: 22.964 * Doc Risk: 100.0%)
- `casm/casm1/casm.asm` -> **Severity: 2296.4** (Blast Radius: 22.964 * Doc Risk: 100.0%)
- `casm/casm3/casm.asm` -> **Severity: 2296.4** (Blast Radius: 22.964 * Doc Risk: 100.0%)

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
