# ARCHITECTURAL_BRIEF: keystone
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/keystone-engine/keystone.git` |
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
- **Scope:** 149 analyzed artifact(s), 4951 LOC.
- **Load-bearing artifact:** `include/keystone/keystone.h` -- 42 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `bindings/masm/KSExample_x86/KSExample_x86.Inc` -- pulls in 17 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `kstool/kstool.cpp` at magnitude 319.58 (structural weight, not risk).
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
| Total Artifacts | 1095 |
| Analyzed Artifacts (Scanned) | 149 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 946 |
| Total LOC | 4951 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 13.6% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6013 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5155 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8748 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 47 | 2104 | 31.5% |
| PLAINTEXT | 20 | 0 | 13.4% |
| MARKDOWN | 14 | 0 | 9.4% |
| SHELL | 10 | 250 | 6.7% |
| MAKEFILE | 8 | 140 | 5.4% |
| BATCH | 6 | 58 | 4.0% |
| RUBY | 6 | 66 | 4.0% |
| CSHARP | 5 | 311 | 3.4% |
| RUST | 5 | 344 | 3.4% |
| GO | 4 | 169 | 2.7% |
| HASKELL | 4 | 140 | 2.7% |
| CPP | 4 | 403 | 2.7% |
| PYTHON | 4 | 410 | 2.7% |
| YAML | 2 | 127 | 1.3% |
| ASSEMBLY | 2 | 271 | 1.3% |
| XML | 2 | 0 | 1.3% |
| POWERSHELL | 2 | 94 | 1.3% |
| PHP | 2 | 5 | 1.3% |
| M4 | 1 | 20 | 0.7% |
| APEX | 1 | 39 | 0.7% |

## 4.1 SOURCE ENCODINGS
> 2 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 142 |
| utf-8 | bom | 5 |
| cp1252 | cp1252-fallback | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 39%, Declarative / Non-Code 22%, Many-Argument Workhorses Files 21%, Large Core Modules 6%, Encapsulated Accessors Files 2%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 115 | 77.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 34 | 22.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 946*

**Composition by Extension & Reason:**
- `.h`: 248x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cpp`: 157x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 99x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 76x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 437 LOC)
- `no_extension`: 29x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 19x Unsupported Format (.undeterminable), 10x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.inc`: 53x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 106, Signals: 0)
- `.c`: 45x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.java`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cmake`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.def`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.go`: 10x Excluded (Machine-Generated Source Code Signature: 10 LOC), 1x Excluded (Machine-Generated Source Code Signature: 112 LOC)
- `.md`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rb`: 10x Excluded (Machine-Generated Source Code Signature: 7 LOC), 1x Excluded (Machine-Generated Source Code Signature: 97 LOC)
- `.cs`: 8x Excluded (Machine-Generated Source Code Signature: 10 LOC), 1x Excluded (Machine-Generated Source Code Signature: 107 LOC), 1x Excluded (Machine-Generated Source Code Signature: 95 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 92.3 | 21.2 | 3.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 83.4 | 29.8 | 49.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 20.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.6 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 89.9 | 7.5 | 3.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 44.1 | 0.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 39.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 49.4 | 50.2 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 87 | 37 | 2 | `bindings/csharp/Keystone.Net/Engine.cs` |
| cleanup | 46 | 37 | 1 | `suite/fuzz/onefile.c` |
| guards | 332 | 54 | 5 | `bindings/rust/keystone-sys/src/keystone_const.rs` |
| danger | 183 | 45 | 4 | `bindings/csharp/Keystone.Net/Engine.cs` |
| concurrency | 2 | 1 | 0 | `bindings/csharp/Keystone.Net/Engine.cs` |
| connectivity | 212 | 64 | 3 | `include/keystone/keystone.h` |
| io | 111 | 38 | 1 | `suite/fuzz/gentargets.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 0 | 0 | 0 | - |
| regex | 46 | 1 | 0 | `suite/fuzz/gentargets.sh` |
| events | 5 | 3 | 0 | `bindings/csharp/Keystone.Net.Tests/Tests.cs` |
| tests | 20 | 6 | 0 | `bindings/rust/tests/keystone.rs` |
| docs | 241 | 12 | 0 | `bindings/csharp/Keystone.Net/Engine.cs` |
| debt | 395 | 46 | 7 | `kstool/kstool.cpp` |
| mutation | 935 | 81 | 12 | `kstool/kstool.cpp` |
| dead_code | 110 | 50 | 1 | `bindings/csharp/Keystone.Net/NativeInterop.cs` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `suite/fuzz/gentargets.sh` (Hits: 46)
- `bindings/Makefile` (Hits: 15)
- `bindings/ruby/keystone_gem/keystone.gemspec` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **keystone.h** (`include/keystone/keystone.h`) — 42 inbound connections
2. **Engine.cs** (`bindings/csharp/Keystone.Net/Engine.cs`) — 2 inbound connections
3. **keystone.go** (`bindings/go/keystone/keystone.go`) — 2 inbound connections
4. **lib.rs** (`bindings/rust/keystone-sys/src/lib.rs`) — 2 inbound connections
5. **getopt.h** (`kstool/getopt.h`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **KSExample_x86.Inc** (`bindings/masm/KSExample_x86/KSExample_x86.Inc`) — 17 outbound dependencies
2. **lib.rs** (`bindings/rust/keystone-sys/src/lib.rs`) — 16 outbound dependencies
3. **keystone.h** (`include/keystone/keystone.h`) — 14 outbound dependencies
4. **KSExample_x64.Inc** (`bindings/masm/KSExample_x64/KSExample_x64.Inc`) — 10 outbound dependencies
5. **kstool.cpp** (`kstool/kstool.cpp`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `main` **(Many-Argument Workhorses)** (@ `kstool/kstool.cpp`) -> Impact: **134.5** | LOC: 265
- `getopt` **(Many-Argument Workhorses)** (@ `kstool/getopt.cpp`) -> Impact: **46.8** | LOC: 56
  * *Intent:* int opterr = 1, /* if error message should be printed */ optind = 1, /* index into parent argv vector */ optopt, /* character checked for validity */ ...
- `Get-KeystoneAssembly` **(I/O & Config Routines)** (@ `bindings/powershell/Keystone/Keystone.psm1`) -> Impact: **24.0** | LOC: 313
- `usage` **(Compute Cores)** (@ `kstool/kstool.cpp`) -> Impact: **19.2** | LOC: 73
  * *Intent:* #include <errno.h> #include <limits.h> #if !defined(WIN32) && !defined(WIN64) && !defined(_WIN32) && !defined(_WIN64) #include <unistd.h> #else #endif...
- `runTest` **(Many-Argument Workhorses)** (@ `suite/test_xedparse.py`) -> Impact: **18.6** | LOC: 29
- `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (@ `suite/fuzz/fuzz_asm_arm64_arm.c`) -> Impact: **18.5** | LOC: 59
- `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (@ `suite/fuzz/fuzz_asm_arm_arm.c`) -> Impact: **18.5** | LOC: 59
- `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (@ `suite/fuzz/fuzz_asm_arm_armbe.c`) -> Impact: **18.5** | LOC: 59
- `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (@ `suite/fuzz/fuzz_asm_arm_armv8be.c`) -> Impact: **18.5** | LOC: 59
- `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (@ `suite/fuzz/fuzz_asm_arm_thumb.c`) -> Impact: **18.5** | LOC: 59

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `suite/fuzz` | 30 | 1070.68 | 57.34% | 35.24% |
| `kstool` | 6 | 456.64 | 27.81% | 1.72% |
| `include/keystone` | 11 | 210.44 | 0.0% | 0.0% |
| `suite` | 9 | 210.12 | 12.93% | 0.0% |
| `bindings/csharp/Keystone.Net` | 4 | 190.58 | 7.81% | 45.29% |
| `bindings/vb6` | 7 | 132.34 | 2.83% | 14.29% |
| `__monolith__` | 18 | 113.08 | 3.44% | 4.19% |
| `bindings/powershell/Keystone` | 2 | 105.38 | 16.21% | 10.51% |
| `bindings/go/keystone` | 3 | 92.94 | 25.91% | 98.5% |
| `samples` | 5 | 72.5 | 5.53% | 3.59% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `bindings/csharp/Keystone.Net/NativeInterop.cs` -> **100.0%** Exposure
- `bindings/vb6/vbKeystone.cpp` -> **100.0%** Exposure
- `bindings/go/keystone/keystone-binding.go` -> **99.999%** Exposure
- `bindings/go/keystone/keystone.go` -> **99.999%** Exposure
- `bindings/rust/keystone-sys/src/lib.rs` -> **99.9988%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `bindings/powershell/Keystone/Keystone.psm1` -> **100.0%** Exposure
- `bindings/ruby/keystone_gem/keystone.gemspec` -> **100.0%** Exposure
- `kstool/getopt.cpp` -> **100.0%** Exposure
- `kstool/kstool.cpp` -> **100.0%** Exposure
- `make-common.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `bindings/csharp/Keystone.Net/NativeInterop.cs` -> **9** Orphaned Functions | **0** Duplicates
- `bindings/vb6/vbKeystone.cpp` -> **9** Orphaned Functions | **0** Duplicates
- `bindings/rust/keystone-sys/src/lib.rs` -> **8** Orphaned Functions | **0** Duplicates
- `bindings/go/keystone/keystone-binding.go` -> **7** Orphaned Functions | **0** Duplicates
- `bindings/go/keystone/keystone.go` -> **7** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `238` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `kstool/kstool.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.647)
- **Top Global Matches:** file_cluster_3: 6.647, file_cluster_8: 20.981, file_cluster_6: 33.89
- **Magnitude:** 319.58 | **LOC:** 360 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 2.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.6%), Guard Balance (formerly Safety Score) (73.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 134.5)
  * `usage` **(Compute Cores)** (Impact: 19.2)
    * *Intent:* #include <errno.h> #include <limits.h> #if !defined(WIN32) && !defined(WIN64) && !defined(_WIN32) &&...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 10`, `args: 55`, `func_start: 2`
* *Risk/State:* `state_mutation: 54`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `import: 10`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` errno.h, fcntl.h, getopt.h, inttypes.h, keystone.h, limits.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/csharp/Keystone.Net/Engine.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.057)
- **Top Global Matches:** file_cluster_15: 6.057, file_cluster_11: 7.445, file_cluster_16: 7.505
- **Magnitude:** 144.28 | **LOC:** 371 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 7.886; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.1%), Concurrency Surface (formerly Concurrency) (44.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Assemble` **(Many-Argument Workhorses)** (Impact: 16.3)
    * *Intent:* /// <summary> /// Encodes the given statement(s) into the given buffer. /// </summary> /// <param na...
  * `Assemble` **(Many-Argument Workhorses)** (Impact: 10.5)
    * *Intent:* /// <summary> /// Encodes the given statement(s). /// </summary> /// <param name="toEncode">String t...
  * `Assemble` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* /// <summary> /// Encodes the given statement(s) into the given stream. /// </summary> /// <param na...
  * `SetOption` **(Type Conversions)** (Impact: 5.9)
    * *Intent:* /// <summary> /// Sets an option in the engine. /// </summary> /// <param name="type">Type of the op...
  * `ResolveSymbolInternal` **(Stateful Encapsulated Methods)** (Impact: 5.8)
    * *Intent:* /// <summary> /// Method used for symbol resolving. /// </summary> /// <param name="symbolPtr">Point...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 32`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 21`, `unreferenced_by_name: 4`
* *Architecture:* `api: 18`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 9`, `doc: 133`, `sync_locks: 1`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.886
  * `Choke Point (Betweenness):` 0.000224 | `Ripple Effect (Closeness):` 0.013333
  * `Imports (Out-Degree: 3):` System, System.Collections.Generic, System.IO, System.Runtime.InteropServices, System.Threading
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `kstool/getopt.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.853)
- **Top Global Matches:** file_cluster_1: 5.853, file_cluster_3: 48.228, file_cluster_8: 70.051
- **Magnitude:** 110.96 | **LOC:** 76 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 2.846; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.3%), Guard Balance (formerly Safety Score) (83.4%), Test Surface (formerly Verification) (2.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getopt` **(Many-Argument Workhorses)** (Impact: 46.8)
    * *Intent:* int opterr = 1, /* if error message should be printed */ optind = 1, /* index into parent argv vecto...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 10`, `args: 6`, `func_start: 1`
* *Risk/State:* `state_mutation: 21`
* *Architecture:* `import: 3`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.846
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006667
  * `Imports (Out-Degree: 1):` getopt.h, stdio.h, string.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `bindings/powershell/Keystone/Keystone.psm1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.707)
- **Top Global Matches:** file_cluster_9: 7.707, file_cluster_10: 12.989, file_cluster_16: 13.085
- **Magnitude:** 90.7 | **LOC:** 313 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.9%), Complexity Load (formerly Cognitive Load) (32.4%), Debt Markers (formerly Tech Debt) (21.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Get-KeystoneAssembly` **(I/O & Config Routines)** (Impact: 24.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 6`, `func_start: 1`
* *Risk/State:* `state_mutation: 25`, `unreferenced_by_name: 1`
* *Architecture:* None
* *Defense:* `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/vb6/CAsmResult.cls` (APEX | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.277)
- **Top Global Matches:** file_cluster_2: 3.277, file_cluster_13: 4.374, file_cluster_17: 5.221
- **Magnitude:** 81.24 | **LOC:** 48 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Guard Balance (formerly Safety Score) (56.4%), Complexity Load (formerly Cognitive Load) (19.8%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 1`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `suite/test_xedparse.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.792)
- **Top Global Matches:** file_cluster_9: 6.792, file_cluster_15: 8.594, file_cluster_2: 8.783
- **Magnitude:** 67.14 | **LOC:** 199 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.217; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.9%), Guard Balance (formerly Safety Score) (56.8%), Complexity Load (formerly Cognitive Load) (17.6%), Connectivity (formerly Api Exposure) (4.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runTest` **(Many-Argument Workhorses)** (Impact: 18.6)
  * `printTest` **(Many-Argument Workhorses)** (Impact: 12.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 13`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`
* *Architecture:* `io: 4`, `api: 2`, `import: 2`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` keystone, sys
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/rust/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.68)
- **Top Global Matches:** file_cluster_5: 6.68, file_cluster_12: 6.892, file_cluster_7: 8.598
- **Magnitude:** 56.84 | **LOC:** 169 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 5.704; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (85.5%), Guard Balance (formerly Safety Score) (51.3%), Connectivity (formerly Api Exposure) (10.8%), Complexity Load (formerly Cognitive Load) (3.6%)
- **Documentation Coverage:** 22.2222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `asm` **(Many-Argument Workhorses)** (Impact: 7.8)
    * *Intent:* /// Assemble a string given its the buffer, size, start address and number /// of instructions to be...
  * `new` **(Generic / Templated Code)** (Impact: 7.7)
    * *Intent:* /// Create new instance of Keystone engine.
  * `option` **(Compute Cores)** (Impact: 6.4)
    * *Intent:* /// Set option for Keystone engine at runtime
  * `fmt` **(Compute Cores)** (Impact: 5.5)
  * `error` **(Generic / Templated Code)** (Impact: 4.6)
    * *Intent:* /// Report the last error number when some API function fail.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 38`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `unreferenced_by_name: 5`
* *Architecture:* `api: 15`, `import: 3`
* *Defense:* `safety: 1`, `doc: 27`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.704
  * `Choke Point (Betweenness):` 0.000179 | `Ripple Effect (Closeness):` 0.008889
  * `Imports (Out-Degree: 1):` ffi::keystone_const::*, ffi::ks_handle, keystone_sys, libc, std::convert::TryInto, std::ffi::CStr, std::ffi::CString, std::fmt...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `suite/test_roundtrips.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.345)
- **Top Global Matches:** file_cluster_12: 6.345, file_cluster_15: 7.389, file_cluster_2: 7.987
- **Magnitude:** 55.3 | **LOC:** 206 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.217; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Guard Balance (formerly Safety Score) (60.3%), Complexity Load (formerly Cognitive Load) (23.6%), Connectivity (formerly Api Exposure) (4.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assemble` **(Defensive Guards)** (Impact: 5.7)
  * `disassemble` **(Parameter Forwarders)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 12`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 16`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` __future__, capstone, keystone
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `samples/sample.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.228)
- **Top Global Matches:** file_cluster_16: 7.228, file_cluster_15: 7.731, file_cluster_2: 8.669
- **Magnitude:** 54.14 | **LOC:** 161 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Guard Balance (formerly Safety Score) (52.9%), Complexity Load (formerly Cognitive Load) (27.7%), Debt Markers (formerly Tech Debt) (18.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_ks` **(Many-Argument Workhorses)** (Impact: 15.3)
    * *Intent:* // Sample code for Keystone Assembler Engine (www.keystone-enigne.org). // By Nguyen Anh Quynh, 2016...
  * `test_sym_resolver` **(I/O & Config Routines)** (Impact: 7.0)
    * *Intent:* // test symbol resolver to handle missing symbols
  * `sym_resolver` **(Stateful Encapsulated Methods)** (Impact: 4.1)
    * *Intent:* // symbol resolver callback
  * `main` **(State Mutators)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 10`, `args: 32`, `func_start: 4`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 7`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` keystone.h, stdio.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/ruby/keystone_gem/ext/keystone.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.755)
- **Top Global Matches:** file_cluster_15: 4.755, file_cluster_11: 6.229, file_cluster_16: 7.49
- **Magnitude:** 44.74 | **LOC:** 114 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.6%), Guard Balance (formerly Safety Score) (54.3%), Debt Markers (formerly Tech Debt) (24.8%), Complexity Load (formerly Cognitive Load) (21.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `m_ks_asm` **(Many-Argument Workhorses)** (Impact: 11.8)
  * `m_ks_initialize` **(Compute Cores)** (Impact: 9.0)
  * `m_ks_set_syntax` **(Parameter Forwarders)** (Impact: 2.3)
  * `Init_keystone` **(Interface Declarations)** (Impact: 1.6)
  * `m_ks_get_syntax` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 5`, `args: 15`, `func_start: 5`
* *Risk/State:* `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` keystone.h, keystone.h, ruby.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bindings/Makefile` (MAKEFILE | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.621)
- **Top Global Matches:** file_cluster_2: 7.621, file_cluster_15: 8.096, file_cluster_13: 8.634
- **Magnitude:** 42.64 | **LOC:** 92 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (56.9%), Complexity Load (formerly Cognitive Load) (9.6%), Connectivity (formerly Api Exposure) (6.1%), Test Surface (formerly Verification) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clean` **(I/O & Config Routines)** (Impact: 7.4)
  * `check` **(I/O & Config Routines)** (Impact: 6.3)
  * `all` **(I/O & Config Routines)** (Impact: 4.3)
  * `expected` **(I/O & Config Routines)** (Impact: 2.5)
  * `python` **(I/O & Config Routines)** (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 9`, `func_start: 14`
* *Risk/State:* `unreferenced_by_name: 2`
* *Architecture:* `io: 15`, `api: 3`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `suite/fuzz/fuzz_asm_arm64_arm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.671)
- **Top Global Matches:** file_cluster_9: 6.671, file_cluster_16: 12.449, file_cluster_15: 12.604
- **Magnitude:** 38.46 | **LOC:** 67 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (62.7%), Guard Balance (formerly Safety Score) (57.1%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 2`, `args: 3`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` keystone.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `suite/fuzz/fuzz_asm_arm_arm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.671)
- **Top Global Matches:** file_cluster_9: 6.671, file_cluster_16: 12.449, file_cluster_15: 12.604
- **Magnitude:** 38.46 | **LOC:** 67 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (62.7%), Guard Balance (formerly Safety Score) (57.1%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 2`, `args: 3`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` keystone.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `suite/fuzz/fuzz_asm_arm_armbe.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.671)
- **Top Global Matches:** file_cluster_9: 6.671, file_cluster_16: 12.449, file_cluster_15: 12.604
- **Magnitude:** 38.46 | **LOC:** 67 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (62.7%), Guard Balance (formerly Safety Score) (57.1%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 2`, `args: 3`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` keystone.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `suite/fuzz/fuzz_asm_arm_armv8be.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.671)
- **Top Global Matches:** file_cluster_9: 6.671, file_cluster_16: 12.449, file_cluster_15: 12.604
- **Magnitude:** 38.46 | **LOC:** 67 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (62.7%), Guard Balance (formerly Safety Score) (57.1%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 2`, `args: 3`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` keystone.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `suite/fuzz/fuzz_asm_arm_thumb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.671)
- **Top Global Matches:** file_cluster_9: 6.671, file_cluster_16: 12.449, file_cluster_15: 12.604
- **Magnitude:** 38.46 | **LOC:** 67 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (62.7%), Guard Balance (formerly Safety Score) (57.1%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 2`, `args: 3`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` keystone.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `suite/fuzz/fuzz_asm_arm_thumbbe.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.671)
- **Top Global Matches:** file_cluster_9: 6.671, file_cluster_16: 12.449, file_cluster_15: 12.604
- **Magnitude:** 38.46 | **LOC:** 67 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (62.7%), Guard Balance (formerly Safety Score) (57.1%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 2`, `args: 3`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` keystone.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `suite/fuzz/fuzz_asm_arm_thumbv8.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.671)
- **Top Global Matches:** file_cluster_9: 6.671, file_cluster_16: 12.449, file_cluster_15: 12.604
- **Magnitude:** 38.46 | **LOC:** 67 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (62.7%), Guard Balance (formerly Safety Score) (57.1%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 2`, `args: 3`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` keystone.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `suite/fuzz/fuzz_asm_arm_thumbv8be.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.671)
- **Top Global Matches:** file_cluster_9: 6.671, file_cluster_16: 12.449, file_cluster_15: 12.604
- **Magnitude:** 38.46 | **LOC:** 67 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (62.7%), Guard Balance (formerly Safety Score) (57.1%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 2`, `args: 3`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` keystone.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `suite/fuzz/fuzz_asm_armv8_arm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.671)
- **Top Global Matches:** file_cluster_9: 6.671, file_cluster_16: 12.449, file_cluster_15: 12.604
- **Magnitude:** 38.46 | **LOC:** 67 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (62.7%), Guard Balance (formerly Safety Score) (57.1%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 2`, `args: 3`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` keystone.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `suite/fuzz/fuzz_asm_evm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.671)
- **Top Global Matches:** file_cluster_9: 6.671, file_cluster_16: 12.449, file_cluster_15: 12.604
- **Magnitude:** 38.46 | **LOC:** 67 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (62.7%), Guard Balance (formerly Safety Score) (57.1%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 2`, `args: 3`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` keystone.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `suite/fuzz/fuzz_asm_hex.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.671)
- **Top Global Matches:** file_cluster_9: 6.671, file_cluster_16: 12.449, file_cluster_15: 12.604
- **Magnitude:** 38.46 | **LOC:** 67 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (62.7%), Guard Balance (formerly Safety Score) (57.1%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 2`, `args: 3`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` keystone.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `suite/fuzz/fuzz_asm_mips.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.671)
- **Top Global Matches:** file_cluster_9: 6.671, file_cluster_16: 12.449, file_cluster_15: 12.604
- **Magnitude:** 38.46 | **LOC:** 67 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (62.7%), Guard Balance (formerly Safety Score) (57.1%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 2`, `args: 3`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` keystone.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `suite/fuzz/fuzz_asm_mips64.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.671)
- **Top Global Matches:** file_cluster_9: 6.671, file_cluster_16: 12.449, file_cluster_15: 12.604
- **Magnitude:** 38.46 | **LOC:** 67 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (62.7%), Guard Balance (formerly Safety Score) (57.1%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 2`, `args: 3`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` keystone.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `suite/fuzz/fuzz_asm_mips64be.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.671)
- **Top Global Matches:** file_cluster_9: 6.671, file_cluster_16: 12.449, file_cluster_15: 12.604
- **Magnitude:** 38.46 | **LOC:** 67 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.217; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (62.7%), Guard Balance (formerly Safety Score) (57.1%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LLVMFuzzerTestOneInput` **(Many-Argument Workhorses)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 2`, `args: 3`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` keystone.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `bindings/rust/keystone-sys/src/lib.rs` (RUST) | Magnitude: 36.76 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 36, pointers: 21, structural_boundaries: 17, api: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `bindings/vb6/vbKeystone.cpp` (CPP) | Magnitude: 17.94 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: pointers: 13, macros: 11, structural_boundaries: 10, func_start: 9

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `bindings/csharp/Keystone.Net/Engine.cs` -> **Severity: 0.022** (Bridge: 0.0002 * Flux: 99.9409%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `bindings/csharp/Keystone.Net/Engine.cs` -> **Severity: 0.668** (Embedded: 0.0133 * Error Risk: 50.1005%)
- `bindings/csharp/Keystone.Net/EncodedData.cs` -> **Severity: 0.6** (Embedded: 0.012 * Error Risk: 50.0%)
- `kstool/getopt.cpp` -> **Severity: 0.556** (Embedded: 0.0067 * Error Risk: 83.4158%)
- `bindings/go/keystone/keystone-binding.go` -> **Severity: 0.457** (Embedded: 0.0089 * Error Risk: 51.4282%)
- `bindings/rust/src/lib.rs` -> **Severity: 0.456** (Embedded: 0.0089 * Error Risk: 51.3136%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `bindings/rust/keystone-sys/src/lib.rs` -> **Severity: 2945.02** (Blast Radius: 32.255 * Doc Risk: 91.3043%)
- `bindings/go/keystone/keystone.go` -> **Severity: 2157.4** (Blast Radius: 21.574 * Doc Risk: 100.0%)
- `bindings/go/keystone/keystone-binding.go` -> **Severity: 2055.7** (Blast Radius: 20.557 * Doc Risk: 100.0%)
- `bindings/csharp/Keystone.Net/NativeInterop.cs` -> **Severity: 445.2** (Blast Radius: 4.452 * Doc Risk: 100.0%)
- `bindings/rust/examples/asm.rs` -> **Severity: 410.2** (Blast Radius: 4.102 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 746 call pairs -- scoped 4.4%, unique 3.2%, ambiguous 1.9%, external 90.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 406 | 0.5% | 0.0% | 0.2% | 99.3% |
| rust | 69 | 8.7% | 0.0% | 0.0% | 91.3% |
| go | 52 | 13.5% | 25.0% | 7.7% | 53.8% |
| csharp | 51 | 17.6% | 9.8% | 15.7% | 56.9% |
| haskell | 39 | 7.7% | 12.8% | 0.0% | 79.5% |
| python | 36 | 11.1% | 0.0% | 0.0% | 88.9% |
| cpp | 32 | 3.1% | 3.1% | 0.0% | 93.8% |
| ruby | 29 | 3.4% | 0.0% | 0.0% | 96.6% |
| powershell | 18 | 0.0% | 0.0% | 0.0% | 100.0% |
| shell | 14 | 0.0% | 0.0% | 7.1% | 92.9% |

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
