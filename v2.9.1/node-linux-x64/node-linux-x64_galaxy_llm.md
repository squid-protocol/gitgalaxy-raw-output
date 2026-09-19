# ARCHITECTURAL_BRIEF: node-linux-x64
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 463 analyzed artifact(s), 84048 LOC.
- **Load-bearing artifact:** `package/include/node/openssl/macros.h` -- 225 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/include/node/v8.h` -- pulls in 44 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/include/node/node_api.h` at magnitude 1164.5 (structural weight, not risk).
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
| Total Artifacts | 2734 |
| Analyzed Artifacts (Scanned) | 463 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2271 |
| Total LOC | 84048 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 16.9% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7969 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3073 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 18.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3757 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 46 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 407 | 76418 | 87.9% |
| OBJECTIVE-C | 51 | 6770 | 11.0% |
| MARKDOWN | 2 | 0 | 0.4% |
| PYTHON | 2 | 860 | 0.4% |
| PLAINTEXT | 1 | 0 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `4.745`
> **Composition Archetype:** `Hub-Coupled App` (z +4.75; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 65%, Encapsulated Accessors Files 15%, Data / Markup / Trivial 8%, Parameter Forwarders Files 4%, Large Core Modules (3) 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 460 | 99.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 0.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2271*

**Composition by Extension & Reason:**
- `.h`: 114x Excluded (Machine-Generated Source Code Signature: 132 LOC), 58x Excluded (Machine-Generated Source Code Signature: 48 LOC), 58x Excluded (Machine-Generated Source Code Signature: 126 LOC)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected), 1x Unsupported Format (.undeterminable)
- `.gypi`: 1x Excluded (Machine-Generated Source Code Signature: 534 LOC)
- `.1`: 1x Excluded (Lexical Monotony: High structural repetition detected in 2333 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 83.8 | 26.8 | 22.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.3 | 34.3 | 36.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.6 | 4.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 3.7 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 33.4 | 18.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 95.0 | 1.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 11.1 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 22.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 19627 | 305 | 118 | `package/include/node/openssl/evp.h` |
| cleanup | 0 | 0 | 0 | - |
| guards | 16148 | 327 | 102 | `package/include/node/openssl/evp.h` |
| danger | 2331 | 197 | 29 | `package/include/node/cppgc/internal/write-barrier.h` |
| concurrency | 16 | 7 | 0 | `package/include/node/cppgc/internal/atomic-entry-flag.h` |
| connectivity | 10379 | 304 | 58 | `package/include/node/openssl/evp.h` |
| io | 7 | 3 | 0 | `package/share/doc/node/lldb_commands.py` |
| crypto | 0 | 0 | 0 | - |
| ipc | 19 | 3 | 0 | `package/include/node/uv.h` |
| time | 4 | 1 | 0 | `package/include/node/openssl/params.h` |
| serialization | 0 | 0 | 0 | - |
| regex | 2 | 1 | 0 | `package/share/doc/node/lldb_commands.py` |
| events | 130 | 23 | 0 | `package/include/node/v8-isolate.h` |
| tests | 0 | 0 | 0 | - |
| docs | 1746 | 83 | 7 | `package/include/node/v8-isolate.h` |
| debt | 169 | 94 | 1 | `package/include/node/v8-internal.h` |
| mutation | 2693 | 89 | 11 | `package/include/node/v8-internal.h` |
| dead_code | 91 | 21 | 0 | `package/share/doc/node/lldb_commands.py` |
| credential | 0 | 0 | 0 | - |
| threat | 8231 | 208 | 65 | `package/include/node/openssl/pem.h` |
| ml_ai | 163 | 9 | 0 | `package/include/node/v8-function-callback.h` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **3.4**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/share/doc/node/lldb_commands.py` (Hits: 4)
- `package/include/node/v8-function.h` (Hits: 2)
- `package/include/node/v8-object.h` (Hits: 1)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **macros.h** (`package/include/node/openssl/macros.h`) — 225 inbound connections
2. **e_os2.h** (`package/include/node/openssl/e_os2.h`) — 131 inbound connections
3. **bio.h** (`package/include/node/openssl/bio.h`) — 126 inbound connections
4. **opensslconf.h** (`package/include/node/openssl/opensslconf.h`) — 91 inbound connections
5. **types.h** (`package/include/node/openssl/types.h`) — 81 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **v8.h** (`package/include/node/v8.h`) — 44 outbound dependencies
2. **CHANGELOG.md** (`package/CHANGELOG.md`) — 25 outbound dependencies
3. **unix.h** (`package/include/node/uv/unix.h`) — 23 outbound dependencies
4. **v8-isolate.h** (`package/include/node/v8-isolate.h`) — 21 outbound dependencies
5. **asn1_no-asm.h** (`package/include/node/openssl/asn1_no-asm.h`) — 20 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `bta` **(Compute Cores)** (@ `package/share/doc/node/lldb_commands.py`) -> Impact: **29.3** | LOC: 31
  * *Intent:* """Print stack trace with assertion scopes"""
- `TypeCheckLocal` **(Generic / Templated Code)** (@ `package/include/node/v8-local-handle.h`) -> Impact: **23.4** | LOC: 16
  * *Intent:* #ifdef V8_ENABLE_CHECKS
- `ptr_arg_cmd` **(Many-Argument Workhorses)** (@ `package/share/doc/node/lldb_commands.py`) -> Impact: **19.6** | LOC: 21
- `GetNameFor` **(Stateful Encapsulated Methods)** (@ `package/include/node/cppgc/internal/name-trait.h`) -> Impact: **11.9** | LOC: 31
- `WriteBarrier` **(Compute Cores)** (@ `package/include/node/cppgc/internal/pointer-policies.h`) -> Impact: **11.9** | LOC: 15
- `ReadExternalPointerField` **(Many-Argument Workhorses)** (@ `package/include/node/v8-internal.h`) -> Impact: **11.4** | LOC: 28
- `jlh` **(Compute Cores)** (@ `package/share/doc/node/lldb_commands.py`) -> Impact: **11.2** | LOC: 24
  * *Intent:* """Print v8::(Maybe)?Local value"""
- `AssignUnsafe` **(Compute Cores)** (@ `package/include/node/cppgc/cross-thread-persistent.h`) -> Impact: **11.2** | LOC: 27
- `ReadCppHeapPointerField` **(Many-Argument Workhorses)** (@ `package/include/node/v8-sandbox.h`) -> Impact: **11.1** | LOC: 43
- `no_arg_cmd` **(Compute Cores)** (@ `package/share/doc/node/lldb_commands.py`) -> Impact: **10.8** | LOC: 16

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/include/node/openssl` | 166 | 5935.72 | 11.24% | 1.0% |
| `package/include/node` | 65 | 3836.24 | 3.85% | 10.63% |
| `package/include/node/cppgc` | 26 | 830.87 | 4.19% | 14.72% |
| `package/include/node/uv` | 13 | 426.28 | 9.49% | 2.41% |
| `package/include/node/cppgc/internal` | 15 | 409.8 | 11.28% | 6.54% |
| `package/share/doc/node` | 1 | 341.24 | 45.13% | 99.58% |
| `package/include/node/openssl/archs/BSD-x86/asm/include/openssl` | 3 | 167.66 | 56.92% | 3.26% |
| `package/include/node/openssl/archs/BSD-x86/asm_avx2/include/openssl` | 3 | 167.66 | 56.92% | 3.26% |
| `package/include/node/openssl/archs/BSD-x86/no-asm/include/openssl` | 3 | 167.66 | 56.92% | 3.26% |
| `package/include/node/openssl/archs/BSD-x86_64/asm/include/openssl` | 3 | 167.66 | 56.92% | 3.26% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/share/doc/node/lldb_commands.py` -> **99.5811%** Exposure
- `package/include/node/node_object_wrap.h` -> **98.2394%** Exposure
- `package/include/node/v8-maybe.h` -> **95.7395%** Exposure
- `package/include/node/cppgc/heap-consistency.h` -> **93.9237%** Exposure
- `package/include/node/cppgc/process-heap-statistics.h` -> **92.4142%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/share/doc/node/lldb_commands.py` -> **100.0%** Exposure
- `package/include/node/openssl/byteorder.h` -> **100.0%** Exposure
- `package/include/node/uv/tree.h` -> **99.9981%** Exposure
- `package/include/node/node_object_wrap.h` -> **79.7076%** Exposure
- `package/include/node/cppgc/custom-space.h` -> **40.1312%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/share/doc/node/lldb_commands.py` -> **16** Orphaned Functions | **0** Duplicates
- `package/include/node/openssl/byteorder.h` -> **12** Orphaned Functions | **0** Duplicates
- `package/include/node/v8-profiler.h` -> **12** Orphaned Functions | **0** Duplicates
- `package/include/node/cppgc/heap-consistency.h` -> **5** Orphaned Functions | **0** Duplicates
- `package/include/node/cppgc/internal/pointer-policies.h` -> **0** Orphaned Functions | **4** Duplicates

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
- **Unknown Dependencies:** `1966` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/include/node/node_api.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 1164.5 | **LOC:** 266 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.498; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (73.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (8.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 26`, `args: 40`, `func_start: 1`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 36`, `import: 2`
* *Defense:* `safety: 11`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.498
  * `Choke Point (Betweenness):` 2.8e-05 | `Ripple Effect (Closeness):` 0.002861
  * `Imports (Out-Degree: 2):` js_native_api.h, node_api_types.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/include/node/openssl/evp.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 893.08 | **LOC:** 2256 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **12**; blast radius 0.948; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (6.9%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 443`, `args: 855`, `class_start: 9`
* *Risk/State:* None
* *Architecture:* `api: 840`, `import: 12`
* *Defense:* `safety: 142`, `immutability_locks: 889`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.948
  * `Choke Point (Betweenness):` 0.000524 | `Ripple Effect (Closeness):` 0.013734
  * `Imports (Out-Degree: 9):` bio.h, core.h, core_dispatch.h, evperr.h, macros.h, objects.h, opensslconf.h, params.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `package/include/node/uv.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 506.16 | **LOC:** 1991 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.401; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (41.8%), Connectivity (formerly Api Exposure) (16.1%), Debt Markers (formerly Tech Debt) (9.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `uv_tty_set_mode` **(Parameter Forwarders)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 368`, `args: 450`, `func_start: 1`, `class_start: 130`
* *Risk/State:* `state_mutation: 17`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 459`, `import: 8`
* *Defense:* `safety: 50`, `immutability_locks: 135`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.401
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` math.h, stddef.h, stdint.h, stdio.h, errno.h, unix.h, version.h, win.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/share/doc/node/lldb_commands.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 341.24 | **LOC:** 327 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.401; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.6%), Guard Balance (formerly Safety Score) (98.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 41.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bta` **(Compute Cores)** (Impact: 29.3)
    * *Intent:* """Print stack trace with assertion scopes"""
  * `ptr_arg_cmd` **(Many-Argument Workhorses)** (Impact: 19.6)
  * `jlh` **(Compute Cores)** (Impact: 11.2)
    * *Intent:* """Print v8::(Maybe)?Local value"""
  * `no_arg_cmd` **(Compute Cores)** (Impact: 10.8)
  * `jca` **(Type Conversions)** (Impact: 10.5)
    * *Intent:* """Print a v8 Code object assembly code from an internal code address"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 61`, `args: 28`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 65`, `dead_code: 1`, `unreferenced_by_name: 16`
* *Architecture:* `io: 4`, `api: 27`, `import: 5`
* *Defense:* `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.401
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, lldb, os, re, shlex
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/include/node/v8-internal.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 275.2 | **LOC:** 1821 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **13**; blast radius 6.56; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (37.9%), Debt Markers (formerly Tech Debt) (25.6%)
- **Documentation Coverage:** 97.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ReadExternalPointerField` **(Many-Argument Workhorses)** (Impact: 11.4)
  * `GetRoot` **(Compute Cores)** (Impact: 9.5)
  * `ExternalPointerCanBeEmpty` **(Compute Cores)** (Impact: 6.0)
    * *Intent:* // When an external poiner field can contain the null external pointer handle, // the type checking ...
  * `EqualHandles` **(Parameter Forwarders)** (Impact: 5.4)
  * `SlotAsValue` **(Defensive Guards)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 221`, `args: 89`, `func_start: 69`, `class_start: 13`
* *Risk/State:* `state_mutation: 30`, `dead_code: 5`, `planned_debt: 12`, `duplicate_logic: 2`
* *Architecture:* `api: 50`, `concurrency: 1`, `import: 13`
* *Defense:* `safety: 70`, `doc: 4`, `immutability_locks: 324`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.56
  * `Choke Point (Betweenness):` 0.000198 | `Ripple Effect (Closeness):` 0.060774
  * `Imports (Out-Degree: 2):` atomic, compare, concepts, iterator, limits, memory, optional, stddef.h...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `package/include/node/openssl/byteorder.h` (OBJECTIVE-C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 238.52 | **LOC:** 340 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.401; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.4%), Debt Markers (formerly Tech Debt) (86.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OPENSSL_load_u64_le` **(Compute Cores)** (Impact: 4.7)
  * `OPENSSL_load_u64_be` **(Compute Cores)** (Impact: 4.7)
  * `OPENSSL_store_u64_le` **(Compute Cores)** (Impact: 4.5)
  * `OPENSSL_store_u64_be` **(Compute Cores)** (Impact: 4.5)
  * `OPENSSL_load_u32_le` **(Compute Cores)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 24`, `args: 12`, `func_start: 12`
* *Risk/State:* `state_mutation: 68`, `unreferenced_by_name: 12`
* *Architecture:* `import: 7`
* *Defense:* `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.401
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` endian.h, OSByteOrder.h, e_os2.h, stdlib.h, string.h, endian.h, types.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/include/node/openssl/ec.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 228.98 | **LOC:** 1570 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 1.111; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (92.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (31.4%), Complexity Load (formerly Cognitive Load) (2.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 64`, `args: 216`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1`
* *Architecture:* `api: 203`, `import: 10`
* *Defense:* `safety: 25`, `doc: 157`, `immutability_locks: 259`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.111
  * `Choke Point (Betweenness):` 0.000223 | `Ripple Effect (Closeness):` 0.006438
  * `Imports (Out-Degree: 7):` asn1.h, bn.h, ecerr.h, macros.h, opensslconf.h, params.h, symhacks.h, types.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/include/node/openssl/bn.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 223.68 | **LOC:** 589 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **7**; blast radius 1.202; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (6.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 49`, `args: 204`
* *Risk/State:* None
* *Architecture:* `api: 201`, `import: 7`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 230`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.202
  * `Choke Point (Betweenness):` 0.0003 | `Ripple Effect (Closeness):` 0.018297
  * `Imports (Out-Degree: 5):` bnerr.h, crypto.h, e_os2.h, macros.h, opensslconf.h, types.h, stdio.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `package/include/node/openssl/ts.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 183.16 | **LOC:** 522 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.401; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (16.3%), Debt Markers (formerly Tech Debt) (13.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 44`, `args: 179`, `class_start: 9`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* `api: 162`, `import: 16`
* *Defense:* `immutability_locks: 84`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.401
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` asn1.h, bio.h, buffer.h, dh.h, dsa.h, ess.h, evp.h, macros.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/include/node/uv/tree.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 176.12 | **LOC:** 522 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 0.608; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.6%), Complexity Load (formerly Cognitive Load) (78.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 83`, `args: 46`, `class_start: 20`
* *Risk/State:* `state_mutation: 65`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.608
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002861
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/include/node/openssl/engine.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 162.74 | **LOC:** 842 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.401; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (18.7%), Connectivity (formerly Api Exposure) (14.7%), Complexity Load (formerly Cognitive Load) (7.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 94`, `args: 161`, `class_start: 3`
* *Risk/State:* `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `api: 140`, `import: 14`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.401
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` bn.h, dh.h, dsa.h, ec.h, engineerr.h, err.h, macros.h, opensslconf.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/include/node/openssl/rsa.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 162.22 | **LOC:** 615 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 0.454; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (93.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 25`, `args: 158`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 138`, `import: 10`
* *Defense:* `safety: 3`, `immutability_locks: 162`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.454
  * `Choke Point (Betweenness):` 2.7e-05 | `Ripple Effect (Closeness):` 0.004292
  * `Imports (Out-Degree: 8):` asn1.h, bio.h, bn.h, crypto.h, macros.h, opensslconf.h, rsaerr.h, safestack.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/include/node/v8-platform.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 160.66 | **LOC:** 1444 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **9**; blast radius 1.285; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (64.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (43.3%)
- **Documentation Coverage:** 22.7273% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AddTraceEventWithTimestamp` **(Many-Argument Workhorses)** (Impact: 4.2)
  * `AddTraceEvent` **(Many-Argument Workhorses)** (Impact: 4.1)
    * *Intent:* /** * Adds a trace event to the platform tracing system. These function calls are * usually the resu...
  * `PostDelayedTaskOnWorkerThread` **(Parameter Forwarders)** (Impact: 2.6)
    * *Intent:* /** * Schedules a task to be invoked on a worker thread after |delay_in_seconds| * expires. * Embedd...
  * `AllocatePages` **(Defensive Guards)** (Impact: 2.4)
    * *Intent:* /** * Allocates memory in range with the given alignment and permission. In * addition to AllocatePa...
  * `ResizeAllocationAt` **(Defensive Guards)** (Impact: 2.4)
    * *Intent:* /** * Resizes the previously allocated memory at the given address. Returns true * if the allocation...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 164`, `args: 68`, `func_start: 50`, `class_start: 5`
* *Risk/State:* `state_mutation: 9`, `planned_debt: 7`, `fragile_debt: 4`
* *Architecture:* `api: 38`, `import: 9`
* *Defense:* `safety: 49`, `doc: 124`, `immutability_locks: 59`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.285
  * `Choke Point (Betweenness):` 0.000128 | `Ripple Effect (Closeness):` 0.029164
  * `Imports (Out-Degree: 2):` math.h, memory, optional, stddef.h, stdint.h, stdlib.h, string, v8-source-location.h...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `package/include/node/js_native_api.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 157.26 | **LOC:** 625 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.613; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (86.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (10.8%), Complexity Load (formerly Cognitive Load) (4.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 51`, `args: 128`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* `api: 132`, `import: 3`
* *Defense:* `safety: 38`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.613
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.003219
  * `Imports (Out-Degree: 1):` js_native_api_types.h, stdbool.h, stddef.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/include/node/openssl/types.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 144.64 | **LOC:** 249 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **81** in-repo importer(s); it depends on **4**; blast radius 13.874; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (4.3%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 248`, `args: 3`, `class_start: 122`
* *Risk/State:* None
* *Architecture:* `api: 126`, `import: 4`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.874
  * `Choke Point (Betweenness):` 0.002894 | `Ripple Effect (Closeness):` 0.231697
  * `Imports (Out-Degree: 3):` limits.h, e_os2.h, macros.h, safestack.h
  * `Imported By (In-Degree: 81):` (Excluded from Brief to save tokens)

### `package/include/node/node.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 143.36 | **LOC:** 1678 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.571; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (59.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.6%), Debt Markers (formerly Tech Debt) (9.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NODE_SET_METHOD` **(Parameter Forwarders)** (Impact: 2.7)
    * *Intent:* // Used to be a macro, hence the uppercase name.
  * `NODE_SET_METHOD` **(Parameter Forwarders)** (Impact: 2.6)
    * *Intent:* // Used to be a macro, hence the uppercase name.
  * `NODE_SET_PROTOTYPE_METHOD` **(Parameter Forwarders)** (Impact: 2.6)
    * *Intent:* #define NODE_SET_METHOD node::NODE_SET_METHOD // Used to be a macro, hence the uppercase name. // No...
  * `NODE_V8_UNIXTIME` **(Parameter Forwarders)** (Impact: 1.6)
  * `RemoveEnvironmentCleanupHook` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 179`, `args: 93`, `func_start: 5`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `api: 83`, `import: 12`
* *Defense:* `safety: 40`, `immutability_locks: 112`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.571
  * `Choke Point (Betweenness):` 9.2e-05 | `Ripple Effect (Closeness):` 0.002146
  * `Imports (Out-Degree: 5):` cassert, cstdint, functional, memory, node_api.h, node_version.h, optional, ostream...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/include/node/cppgc/visitor.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 141.16 | **LOC:** 534 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 0.594; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (32.9%), Debt Markers (formerly Tech Debt) (30.5%)
- **Documentation Coverage:** 51.1628% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TraceMultiple` **(Defensive Guards)** (Impact: 9.6)
  * `VisitMultipleCompressedMember` **(Defensive Guards)** (Impact: 6.8)
    * *Intent:* #if defined(CPPGC_POINTER_COMPRESSION)
  * `VisitMultipleUncompressedMember` **(Defensive Guards)** (Impact: 6.7)
  * `TraceEphemeron` **(Compute Cores)** (Impact: 6.2)
  * `TraceEphemeron` **(Defensive Guards)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 88`, `args: 45`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `duplicate_logic: 2`
* *Architecture:* `api: 7`, `import: 13`
* *Defense:* `safety: 27`, `doc: 17`, `immutability_locks: 84`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.594
  * `Choke Point (Betweenness):` 0.00021 | `Ripple Effect (Closeness):` 0.006438
  * `Imports (Out-Degree: 12):` custom-space.h, garbage-collected.h, logging.h, member-storage.h, pointer-policies.h, liveness-broker.h, macros.h, member.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/include/node/zlib.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 133.86 | **LOC:** 1968 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.401; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (62.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (25.8%), Complexity Load (formerly Cognitive Load) (16.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 24`, `args: 83`, `class_start: 6`
* *Risk/State:* `state_mutation: 9`, `dead_code: 3`
* *Architecture:* `api: 85`, `import: 1`
* *Defense:* `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.401
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` zconf.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/include/node/v8-local-handle.h` (OBJECTIVE-C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 124.02 | **LOC:** 885 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **34** in-repo importer(s); it depends on **5**; blast radius 4.856; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.5%), Connectivity (formerly Api Exposure) (58.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TypeCheckLocal` **(Generic / Templated Code)** (Impact: 23.4)
    * *Intent:* #ifdef V8_ENABLE_CHECKS
  * `LocalBase` **(I/O & Config Routines)** (Impact: 2.3)
  * `LocalVector` **(Generic / Templated Code)** (Impact: 2.3)
  * `LocalBase` **(Generic / Templated Code)** (Impact: 2.2)
  * `insert` **(Parameter Forwarders)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 79`, `args: 36`, `func_start: 60`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 13`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 9`, `import: 5`
* *Defense:* `doc: 22`, `immutability_locks: 64`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.856
  * `Choke Point (Betweenness):` 0.000324 | `Ripple Effect (Closeness):` 0.076304
  * `Imports (Out-Degree: 2):` stddef.h, type_traits, v8-handle-base.h, v8-internal.h, vector
  * `Imported By (In-Degree: 34):` (Excluded from Brief to save tokens)

### `package/include/node/openssl/store.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 108.94 | **LOC:** 371 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.401; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (15.2%), Dead Code Surface (formerly Dead Code) (7.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 44`, `args: 75`, `class_start: 3`
* *Risk/State:* `dead_code: 2`
* *Architecture:* `api: 90`, `import: 5`
* *Defense:* `safety: 2`, `immutability_locks: 79`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.401
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` macros.h, pem.h, storeerr.h, types.h, stdarg.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/include/node/openssl/dh.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 108.86 | **LOC:** 334 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 0.497; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (98.9%), Guard Balance (formerly Safety Score) (54.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 26`, `args: 113`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* `api: 89`, `import: 10`
* *Defense:* `safety: 4`, `immutability_locks: 69`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.497
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.006438
  * `Imports (Out-Degree: 7):` asn1.h, bio.h, bn.h, dherr.h, e_os2.h, macros.h, opensslconf.h, types.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/include/node/openssl/dsa.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 98.0 | **LOC:** 274 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 0.454; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (95.2%), Guard Balance (formerly Safety Score) (55.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 25`, `args: 89`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `api: 79`, `import: 12`
* *Defense:* `safety: 1`, `immutability_locks: 84`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.454
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.004292
  * `Imports (Out-Degree: 9):` asn1.h, bio.h, bn.h, crypto.h, dh.h, dsaerr.h, e_os2.h, macros.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/include/node/openssl/pem.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 93.32 | **LOC:** 549 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.515; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (76.7%), Guard Balance (formerly Safety Score) (56.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (47.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 53`, `args: 85`
* *Risk/State:* `safety_bypasses: 6`
* *Architecture:* `api: 69`, `import: 9`
* *Defense:* `doc: 7`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.515
  * `Choke Point (Betweenness):` 0.000102 | `Ripple Effect (Closeness):` 0.002146
  * `Imports (Out-Degree: 7):` bio.h, e_os2.h, evp.h, macros.h, pemerr.h, safestack.h, symhacks.h, x509.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/include/node/cppgc/member.h` (OBJECTIVE-C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 88.58 | **LOC:** 670 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 0.616; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (40.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BasicMember` **(I/O & Config Routines)** (Impact: 2.3)
  * `BasicMember` **(I/O & Config Routines)** (Impact: 2.3)
  * `BasicMember` **(I/O & Config Routines)** (Impact: 2.2)
    * *Intent:* // Move ctor.
  * `SetRawStorageAtomic` **(Generic / Templated Code)** (Impact: 1.6)
  * `CheckPointer` **(Generic / Templated Code)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 53`, `args: 4`, `func_start: 49`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 7`
* *Architecture:* `api: 7`, `import: 9`
* *Defense:* `doc: 5`, `immutability_locks: 64`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.616
  * `Choke Point (Betweenness):` 0.000132 | `Ripple Effect (Closeness):` 0.009559
  * `Imports (Out-Degree: 6):` atomic, api-constants.h, member-storage.h, pointer-policies.h, sentinel-pointer.h, type-traits.h, cstddef, type_traits...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/include/node/cppgc/macros.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 85.28 | **LOC:** 57 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 1.056; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (41.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 10`, `args: 4`, `func_start: 1`
* *Risk/State:* None
* *Architecture:* `import: 2`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.056
  * `Choke Point (Betweenness):` 0.000217 | `Ripple Effect (Closeness):` 0.02838
  * `Imports (Out-Degree: 1):` compiler-specific.h, cstddef
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/include/node/cppgc/platform.h` -> **Severity: 0.005** (Bridge: 0.0004 * Flux: 11.9203%)
- `package/include/node/cppgc/internal/gc-info.h` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 11.5103%)
- `package/include/node/cppgc/internal/logging.h` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 16.7982%)
- `package/include/node/v8-primitive.h` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 8.917%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/include/node/openssl/macros.h` -> **Severity: 25.736** (Embedded: 0.4746 * Error Risk: 54.2238%)
- `package/include/node/v8config.h` -> **Severity: 8.285** (Embedded: 0.1607 * Error Risk: 51.5459%)
- `package/include/node/v8-local-handle.h` -> **Severity: 4.995** (Embedded: 0.0763 * Error Risk: 65.4664%)
- `package/include/node/v8-internal.h` -> **Severity: 2.303** (Embedded: 0.0608 * Error Risk: 37.9019%)
- `package/include/node/v8-handle-base.h` -> **Severity: 2.141** (Embedded: 0.0433 * Error Risk: 49.4828%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/include/node/v8-internal.h` -> **Severity: 637.257** (Blast Radius: 6.56 * Doc Risk: 97.1429%)
- `package/include/node/v8-local-handle.h` -> **Severity: 404.667** (Blast Radius: 4.856 * Doc Risk: 83.3333%)
- `package/include/node/v8-handle-base.h` -> **Severity: 246.5** (Blast Radius: 2.465 * Doc Risk: 100.0%)
- `package/include/node/v8-data.h` -> **Severity: 110.6** (Blast Radius: 1.106 * Doc Risk: 100.0%)
- `package/include/node/v8-source-location.h` -> **Severity: 103.2** (Blast Radius: 2.064 * Doc Risk: 50.0%)

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
