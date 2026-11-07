# ARCHITECTURAL_BRIEF: cosmopolitan
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/jart/cosmopolitan.git` |
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
- **Scope:** 6673 analyzed artifact(s), 352243 LOC.
- **Load-bearing artifact:** `libc/runtime/runtime.h` -- 731 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Makefile` -- pulls in 166 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `dsp/audio/cosmoaudio/miniaudio.h` at magnitude 66041.4 (structural weight, not risk).
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
| Total Artifacts | 17762 |
| Analyzed Artifacts (Scanned) | 6673 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 11089 |
| Total LOC | 352243 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 37.6% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4234 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1249 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.7005 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 290 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 3742 | 222252 | 56.1% |
| ASSEMBLY | 2541 | 26450 | 38.1% |
| CPP | 156 | 17088 | 2.3% |
| MAKEFILE | 93 | 6738 | 1.4% |
| LUA | 56 | 4844 | 0.8% |
| SHELL | 34 | 1768 | 0.5% |
| YAML | 17 | 555 | 0.3% |
| PLAINTEXT | 13 | 0 | 0.2% |
| MARKDOWN | 8 | 0 | 0.1% |
| PYTHON | 7 | 636 | 0.1% |
| HTML | 2 | 34 | 0.0% |
| OBJECTIVE-C | 1 | 71760 | 0.0% |
| SQLITE | 1 | 7 | 0.0% |
| FORTRAN | 1 | 76 | 0.0% |
| CSS | 1 | 35 | 0.0% |

## 4.1 SOURCE ENCODINGS
All 6673 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 35%, Parameter Forwarders Files 16%, Declarative / Non-Code 16%, Compute Cores Files 10%, Many-Argument Workhorses Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 6646 | 99.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 27 | 0.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 11089*

**Composition by Extension & Reason:**
- `no_extension`: 3094x Excluded (Binary Format Detected), 272x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 26x Unsupported Format (.undeterminable)
- `.c`: 2302x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1633 LOC), 1x Packed Payload Guard (Impossible Density: 3.76 hits/line)
- `.h`: 1985x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4305 LOC), 1x Excluded (Embedded Hex Payload: 1551 hex tokens in 993 LOC)
- `.py`: 1750x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.crt`: 199x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.inc`: 180x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 13973 commas in 1086 LOC), 1x Excluded (Embedded Array/Matrix Payload: 23940 commas in 1867 LOC)
- `.txt`: 172x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2622 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 34925 LOC)
- `.dectest`: 143x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cc`: 101x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cpp`: 95x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mk`: 73x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.der`: 72x Excluded (Explicitly Denied Extension: '.der')
- `.datax`: 67x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pem`: 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 14x Excluded (Unsupported Extension: '.pem')
- `.cosmo`: 41x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.cosmo')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.9 | 10.7 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.7 | 22.4 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 11.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.2 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 6.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 19.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.2 | 1.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 35.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 98.7 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 6972 | 719 | 1 | `dsp/audio/cosmoaudio/miniaudio.h` |
| cleanup | 2024 | 424 | 0 | `test/libc/intrin/mmap_test.c` |
| guards | 20224 | 2161 | 5 | `dsp/audio/cosmoaudio/miniaudio.h` |
| danger | 8056 | 1246 | 2 | `dsp/audio/cosmoaudio/miniaudio.h` |
| concurrency | 1580 | 303 | 0 | `libc/intrin/aarch64/atomics.S` |
| connectivity | 12666 | 3231 | 3 | `tool/net/definitions.lua` |
| io | 2508 | 424 | 0 | `test/libc/stdio/sscanf_test.c` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1115 | 241 | 0 | `test/libc/intrin/mmap_test.c` |
| time | 151 | 65 | 0 | `test/libc/intrin/clock_gettime_test.c` |
| serialization | 47 | 6 | 0 | `test/libc/stdio/sprintf_s.inc` |
| regex | 319 | 98 | 0 | `test/libc/str/regex_test.c` |
| events | 672 | 206 | 0 | `test/libc/calls/poll_test.c` |
| tests | 18784 | 433 | 0 | `test/libc/stdio/sscanf_test.c` |
| docs | 4047 | 1485 | 1 | `tool/net/definitions.lua` |
| debt | 2146 | 473 | 0 | `dsp/audio/cosmoaudio/miniaudio.h` |
| mutation | 71989 | 2322 | 17 | `dsp/audio/cosmoaudio/miniaudio.h` |
| dead_code | 6953 | 2541 | 1 | `tool/net/definitions.lua` |
| credential | 41 | 9 | 0 | `tool/net/demo/unix-info.lua` |
| threat | 398 | 17 | 0 | `test/tool/net/sha_test.lua` |
| ml_ai | 1051 | 339 | 0 | `libc/complex.h` |
| ui | 4 | 3 | 0 | `tool/viz/life.c` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/libc/stdio/sscanf_test.c` (Hits: 303)
- `ape/apeinstall.sh` (Hits: 103)
- `test/libc/calls/open_test.c` (Hits: 84)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **runtime.h** (`libc/runtime/runtime.h`) — 731 inbound connections
2. **calls.h** (`libc/calls/calls.h`) — 609 inbound connections
3. **dce.h** (`libc/dce.h`) — 602 inbound connections
4. **errno.h** (`libc/errno.h`) — 468 inbound connections
5. **testlib.h** (`libc/testlib/testlib.h`) — 461 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Makefile** (`Makefile`) — 166 outbound dependencies
2. **redbean.c** (`tool/net/redbean.c`) — 123 outbound dependencies
3. **printvideo.c** (`tool/viz/printvideo.c`) — 85 outbound dependencies
4. **turfwar.c** (`net/turfwar/turfwar.c`) — 75 outbound dependencies
5. **sig.c** (`libc/intrin/sig.c`) — 62 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__vcscanf` **(Many-Argument Workhorses)** (@ `libc/stdio/vcscanf.c`) -> Impact: **907.7** | LOC: 797
  * *Intent:* * All standard features are supported, except for positional argument * references (e.g. `%n$`) specified by POSIX.1-2001 (but not ISO C99). * This im...
- `main` **(Many-Argument Workhorses)** (@ `examples/romanize.c`) -> Impact: **734.2** | LOC: 931
- `__fmt` **(Many-Argument Workhorses)** (@ `libc/stdio/fmt.c`) -> Impact: **708.3** | LOC: 694
  * *Intent:* * - `%#s` datum (radix 256 null-terminated ibm cp437) * - `%#x` int (radix 16 hexadecimal w/ 0x prefix if not zero) * * This implements most of ANSI C...
- `kformat` **(Many-Argument Workhorses)** (@ `libc/intrin/kprintf.greg.c`) -> Impact: **600.4** | LOC: 604
- `getAvailableFeatures` **(Many-Argument Workhorses)** (@ `libc/intrin/x86.c`) -> Impact: **557.8** | LOC: 289
- `Parse` **(Many-Argument Workhorses)** (@ `tool/net/ljson.c`) -> Impact: **518.8** | LOC: 481
- `ma_dr_wav_init__internal` **(Many-Argument Workhorses)** (@ `dsp/audio/cosmoaudio/miniaudio.h`) -> Impact: **494.3** | LOC: 540
- `ma_result_from_errno` **(Compute Cores)** (@ `dsp/audio/cosmoaudio/miniaudio.h`) -> Impact: **394.9** | LOC: 402
  * *Intent:* #include <errno.h>
- `ma_dr_mp3_L3_huffman` **(Many-Argument Workhorses)** (@ `dsp/audio/cosmoaudio/miniaudio.h`) -> Impact: **383.1** | LOC: 951
- `PrintLambda` **(Many-Argument Workhorses)** (@ `tool/lambda/lib/print.c`) -> Impact: **340.7** | LOC: 298

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `dsp/audio/cosmoaudio` | 4 | 66493.22 | 49.68% | 26.14% |
| `libc/intrin` | 479 | 24013.9 | 18.86% | 28.27% |
| `libc/calls` | 414 | 21952.52 | 31.48% | 30.5% |
| `libc/sysv/consts` | 1214 | 14391.88 | 0.0% | 0.07% |
| `tool/net` | 30 | 13229.18 | 36.53% | 15.46% |
| `libc/stdio` | 181 | 10259.86 | 17.31% | 28.78% |
| `examples` | 66 | 9649.0 | 37.24% | 0.0% |
| `libc` | 35 | 7547.71 | 2.1% | 0.68% |
| `tool/viz` | 36 | 7247.36 | 50.63% | 27.06% |
| `tool/plinko/lib` | 68 | 6541.63 | 37.29% | 27.82% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `tool/net/definitions.lua` -> **100.0%** Exposure
- `libc/dlopen/stubs.c` -> **99.9999%** Exposure
- `.github/ISSUE_TEMPLATE/02-bug-medium.yml` -> **99.9997%** Exposure
- `.github/ISSUE_TEMPLATE/03-bug-high.yml` -> **99.9997%** Exposure
- `.github/ISSUE_TEMPLATE/04-bug-critical.yml` -> **99.9997%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `ape/ape-m1.c` -> **100.0%** Exposure
- `ape/loader.c` -> **100.0%** Exposure
- `dsp/audio/cosmoaudio/test.c` -> **100.0%** Exposure
- `dsp/core/alaw.c` -> **100.0%** Exposure
- `dsp/core/byte2double.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tool/net/definitions.lua` -> **481** Orphaned Functions | **0** Duplicates
- `test/libc/xed/x86ild_popular_i86_2_test.c` -> **310** Orphaned Functions | **0** Duplicates
- `test/libc/xed/x86ild_popular_i86_test.c` -> **307** Orphaned Functions | **0** Duplicates
- `test/libc/xed/x86ild_popular_binary_test.c` -> **231** Orphaned Functions | **0** Duplicates
- `test/libc/xed/x86ild_popular_logical_test.c` -> **182** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `net/http/ssh.c` -> **98.6837%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `97` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `18743` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `dsp/audio/cosmoaudio/miniaudio.h` (OBJECTIVE-C | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 14.544)
- **Top Global Matches:** file_cluster_4: 14.544, file_cluster_12: 16.17, file_cluster_15: 17.391
- **Magnitude:** 66041.4 | **LOC:** 95646 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **54** in-repo importer(s); it depends on **56**; blast radius 0.897; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.7%), Guard Balance (formerly Safety Score) (72.6%)
- **Documentation Coverage:** 99.2868% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ma_dr_wav_init__internal` **(Many-Argument Workhorses)** (Impact: 494.3)
  * `ma_result_from_errno` **(Compute Cores)** (Impact: 394.9)
    * *Intent:* #include <errno.h>
  * `ma_dr_mp3_L3_huffman` **(Many-Argument Workhorses)** (Impact: 383.1)
  * `ma_dr_mp3_init_internal` **(Many-Argument Workhorses)** (Impact: 272.8)
    * *Intent:* #endif
  * `ma_device_init_internal__wasapi` **(Many-Argument Workhorses)** (Impact: 234.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 8426 instances
* *Memory Alloc (weighted view):* 47
* *State Mutation (weighted view):* 29486
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12314`, `structural_boundaries: 8972`, `args: 4229`, `func_start: 4525`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1857`, `state_mutation: 12634`, `dead_code: 2`, `planned_debt: 88`, `fragile_debt: 42`
* *Architecture:* `io: 17`, `api: 153`, `import: 96`
* *Defense:* `doc: 78`, `immutability_locks: 3509`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.897
  * `Choke Point (Betweenness):` 0.020785 | `Ripple Effect (Closeness):` 0.071278
  * `Imports (Out-Degree: 95):` AAudio.h, AVFoundation.h, AudioToolbox.h, AvailabilityMacros.h, CoreAudio.h, OpenSLES.h, OpenSLES_Android.h, TargetConditionals.h...
  * `Imported By (In-Degree: 54):` (Excluded from Brief to save tokens)

### `libc/stdckdint.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 4.682)
- **Top Global Matches:** file_cluster_17: 4.682, file_cluster_2: 5.311, file_cluster_15: 6.519
- **Magnitude:** 6454.33 | **LOC:** 626 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **55** in-repo importer(s); it depends on **2**; blast radius 1.426; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Complexity Load (formerly Cognitive Load) (59.1%), Guard Balance (formerly Safety Score) (58.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (20.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 106
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 79`, `args: 38`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 52`
* *Architecture:* `import: 2`
* *Defense:* `safety: 9`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.426
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.084404
  * `Imports (Out-Degree: 1):` limits, type_traits
  * `Imported By (In-Degree: 55):` (Excluded from Brief to save tokens)

### `tool/net/redbean.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.787)
- **Top Global Matches:** file_cluster_4: 6.787, file_cluster_16: 7.828, file_cluster_15: 10.254
- **Magnitude:** 6071.14 | **LOC:** 7318 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **123**; blast radius 0.325; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.8%), Guard Balance (formerly Safety Score) (71.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.4%)
- **Documentation Coverage:** 99.7151% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HandleConnection` **(Compute Cores)** (Impact: 94.6)
  * `StoreAsset` **(Many-Argument Workhorses)** (Impact: 83.5)
  * `ServeAsset` **(Many-Argument Workhorses)** (Impact: 66.8)
  * `ConfigureCertificate` **(Many-Argument Workhorses)** (Impact: 55.9)
  * `HandleMessages` **(Compute Cores)** (Impact: 55.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 65 instances
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 954 instances
* *High Risk Execution (weighted view):* 13
* *Concurrency (weighted view):* 84
* *Memory Alloc (weighted view):* 21
* *State Mutation (weighted view):* 3212
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1275`, `structural_boundaries: 1246`, `args: 1014`, `func_start: 362`, `class_start: 96`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 15`, `state_mutation: 1304`, `planned_debt: 16`, `fragile_debt: 2`
* *Architecture:* `io: 21`, `api: 19`, `concurrency: 29`, `import: 124`
* *Defense:* `safety: 173`, `doc: 3`, `sync_locks: 12`, `immutability_locks: 192`, `cleanup: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.325
  * `Choke Point (Betweenness):` 0.000114 | `Ripple Effect (Closeness):` 0.000599
  * `Imports (Out-Degree: 278):` sections.internal.h, assert.h, atomic.h, calls.h, pledge.h, dirent.h, flock.h, iovec.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `libc/intrin/demangle.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.288)
- **Top Global Matches:** file_cluster_6: 5.288, file_cluster_4: 9.168, file_cluster_8: 15.71
- **Magnitude:** 4329.56 | **LOC:** 4488 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.099; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.3%)
- **Documentation Coverage:** 91.9679% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `demangle_read_type_impl` **(Many-Argument Workhorses)** (Impact: 294.6)
  * `demangle_read_uqname` **(Compute Cores)** (Impact: 206.5)
    * *Intent:* /* * read unqualified-name, unqualified name are operator-name, ctor-dtor-name, * source-name */
  * `demangle_push_type_qualifier` **(Many-Argument Workhorses)** (Impact: 179.6)
  * `demangle_read_encoding_impl` **(Compute Cores)** (Impact: 110.8)
  * `demangle` **(Many-Argument Workhorses)** (Impact: 104.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 675 instances
* *High Risk Execution (weighted view):* 6
* *State Mutation (weighted view):* 2068
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1047`, `structural_boundaries: 1066`, `args: 121`, `func_start: 89`, `class_start: 56`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 7`, `state_mutation: 718`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 102`, `import: 4`
* *Defense:* `safety: 87`, `doc: 11`, `immutability_locks: 59`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.00015
  * `Imports (Out-Degree: 7):` stdalign.h, stdbool.h, stddef.h, stdint.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `dsp/mpeg/pl_mpeg.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.055)
- **Top Global Matches:** file_cluster_4: 5.055, file_cluster_15: 8.637, file_cluster_16: 9.765
- **Magnitude:** 2839.66 | **LOC:** 4381 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 0.168; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.0%), Guard Balance (formerly Safety Score) (71.6%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `plm_video_decode_block` **(Many-Argument Workhorses)** (Impact: 76.9)
  * `plm_demux_seek` **(Many-Argument Workhorses)** (Impact: 69.7)
  * `plm_audio_decode_frame` **(Compute Cores)** (Impact: 54.5)
  * `plm_decode` **(Compute Cores)** (Impact: 39.3)
  * `plm_video_decode_macroblock` **(Compute Cores)** (Impact: 30.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 349 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1480
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 430`, `structural_boundaries: 328`, `args: 267`, `func_start: 126`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 782`, `dead_code: 1`
* *Architecture:* `io: 5`, `api: 277`, `import: 6`
* *Defense:* `safety: 53`, `immutability_locks: 69`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.168
  * `Choke Point (Betweenness):` 2.7e-05 | `Ripple Effect (Closeness):` 0.000299
  * `Imports (Out-Degree: 16):` cosmotime.h, stdint.h, stdio.h, stdlib.h, string.h, time.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `libc/stdio/fmt.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.031)
- **Top Global Matches:** file_cluster_8: 6.031, file_cluster_6: 13.654, file_cluster_4: 22.351
- **Magnitude:** 2696.16 | **LOC:** 1561 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **26**; blast radius 0.18; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.7%), Guard Balance (formerly Safety Score) (87.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 43.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__fmt` **(Many-Argument Workhorses)** (Impact: 708.3)
    * *Intent:* * - `%#s` datum (radix 256 null-terminated ibm cp437) * - `%#x` int (radix 16 hexadecimal w/ 0x pref...
  * `__fmt_stoa` **(Many-Argument Workhorses)** (Impact: 230.0)
    * *Intent:* /** * Converts string to array. * * This is used by __fmt() to implement the %s and %c directives. T...
  * `__fmt_ntoa_format` **(Many-Argument Workhorses)** (Impact: 164.0)
  * `__fmt_bround` **(Many-Argument Workhorses)** (Impact: 66.8)
    * *Intent:* // round to prec hex digits after the "." // prec1 = incoming precision (after ".")
  * `__fmt_ntoa2` **(Many-Argument Workhorses)** (Impact: 46.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 432 instances
* *State Mutation (weighted view):* 1305
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 499`, `structural_boundaries: 163`, `args: 20`, `func_start: 17`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 441`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 6`, `import: 26`
* *Defense:* `safety: 10`, `doc: 3`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.18
  * `Choke Point (Betweenness):` 0.00071 | `Ripple Effect (Closeness):` 0.049607
  * `Imports (Out-Degree: 43):` assert.h, ctype.h, errno.h, conv.h, divmod10.internal.h, internal.h, itoa.h, bsr.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `net/turfwar/turfwar.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.006)
- **Top Global Matches:** file_cluster_4: 6.006, file_cluster_15: 9.884, file_cluster_16: 10.489
- **Magnitude:** 2364.88 | **LOC:** 2951 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **75**; blast radius 0.091; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HttpWorker` **(Compute Cores)** (Impact: 144.8)
    * *Intent:* // make thousands of http client handler threads // load balance incoming connections for port 8080 ...
  * `Read` **(Many-Argument Workhorses)** (Impact: 69.6)
  * `main` **(Many-Argument Workhorses)** (Impact: 50.2)
  * `SslRead` **(Many-Argument Workhorses)** (Impact: 38.1)
  * `GetOpts` **(Compute Cores)** (Impact: 31.8)
    * *Intent:* // parses cli arguments
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 32 instances
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 320 instances
* *Concurrency (weighted view):* 84
* *Memory Alloc (weighted view):* 9
* *State Mutation (weighted view):* 1223
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 377`, `structural_boundaries: 565`, `args: 177`, `func_start: 91`, `class_start: 120`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 22`, `state_mutation: 583`, `dead_code: 12`, `unreferenced_by_name: 5`
* *Architecture:* `io: 21`, `api: 95`, `concurrency: 34`, `import: 75`
* *Defense:* `safety: 27`, `doc: 3`, `sync_locks: 10`, `immutability_locks: 75`, `cleanup: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 172):` assert.h, atomic.h, calls.h, pledge.h, iovec.h, rusage.h, sigaction.h, siginfo.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/nesemu1.cc` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.059)
- **Top Global Matches:** file_cluster_6: 7.059, file_cluster_8: 10.922, file_cluster_4: 14.347
- **Magnitude:** 1938.32 | **LOC:** 1869 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **46**; blast radius 0.091; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (94.8%), Guard Balance (formerly Safety Score) (80.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (20.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (5.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PpuAccess` **(Many-Argument Workhorses)** (Impact: 84.0)
    * *Intent:* // External I/O: read or write
  * `RenderingTick` **(I/O & Config Routines)** (Impact: 75.6)
  * `ReadKeyboard` **(I/O & Config Routines)** (Impact: 70.0)
  * `Write` **(Compute Cores)** (Impact: 60.4)
  * `Access` **(Many-Argument Workhorses)** (Impact: 56.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 342 instances
* *Memory Alloc (weighted view):* 7
* *State Mutation (weighted view):* 1112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 488`, `structural_boundaries: 160`, `args: 84`, `func_start: 56`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 3`, `state_mutation: 428`, `planned_debt: 3`, `unreferenced_by_name: 3`
* *Architecture:* `io: 5`, `import: 46`
* *Defense:* `safety: 2`, `doc: 1`, `sync_locks: 6`, `immutability_locks: 17`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 92):` cosmoaudio.h, core.h, half.h, illumination.h, scale.h, itoa8.h, quant.h, tty.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libc/vga/tty.greg.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.292)
- **Top Global Matches:** file_cluster_4: 6.292, file_cluster_16: 6.674, file_cluster_15: 8.822
- **Magnitude:** 1657.22 | **LOC:** 1398 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **13**; blast radius 0.136; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.2%)
- **Documentation Coverage:** 94.0594% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_TtyWrite` **(Many-Argument Workhorses)** (Impact: 112.5)
  * `TtySelectGraphicsRendition` **(Compute Cores)** (Impact: 81.2)
  * `_StartTty` **(Many-Argument Workhorses)** (Impact: 51.5)
  * `TtyCsi` **(Compute Cores)** (Impact: 46.7)
  * `TtySetType` **(Many-Argument Workhorses)** (Impact: 32.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 277 instances
* *State Mutation (weighted view):* 871
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 327`, `structural_boundaries: 338`, `args: 111`, `func_start: 85`, `class_start: 6`
* *Risk/State:* `state_mutation: 317`, `unreferenced_by_name: 2`
* *Architecture:* `api: 13`, `import: 13`
* *Defense:* `safety: 53`, `doc: 6`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.136
  * `Choke Point (Betweenness):` 7.7e-05 | `Ripple Effect (Closeness):` 0.000599
  * `Imports (Out-Degree: 26):` ctype.h, bing.internal.h, itoa.h, directmap.h, safemacros.h, pc.internal.h, str.h, thompike.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `libc/intrin/kprintf.greg.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.492)
- **Top Global Matches:** file_cluster_4: 7.492, file_cluster_6: 8.02, file_cluster_15: 14.276
- **Magnitude:** 1604.1 | **LOC:** 1172 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **111** in-repo importer(s); it depends on **50**; blast radius 1.5; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.1%), Guard Balance (formerly Safety Score) (84.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 85.1852% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `kformat` **(Many-Argument Workhorses)** (Impact: 600.4)
  * `kloghandle` **(I/O & Config Routines)** (Impact: 31.9)
    * *Intent:* // returns log handle or -1 if logging shouldn't happen
  * `klog` **(Many-Argument Workhorses)** (Impact: 28.8)
    * *Intent:* #endif /* __x86_64__ */
  * `kemitquote` **(Many-Argument Workhorses)** (Impact: 11.8)
  * `_klog_serial` **(Defensive Guards)** (Impact: 7.8)
    * *Intent:* #ifdef __x86_64__
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 272 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 833
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 85`, `args: 19`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 289`, `dead_code: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 28`, `concurrency: 1`, `import: 51`
* *Defense:* `safety: 12`, `doc: 4`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.5
  * `Choke Point (Betweenness):` 0.009649 | `Ripple Effect (Closeness):` 0.086461
  * `Imports (Out-Degree: 56):` cosmo.h, dce.h, errno.h, divmod10.internal.h, magnumstrs.internal.h, asmflag.h, atomic.h, getenv.h...
  * `Imported By (In-Degree: 111):` (Excluded from Brief to save tokens)

### `libc/stdio/vcscanf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.026)
- **Top Global Matches:** file_cluster_6: 7.026, file_cluster_4: 11.653, file_cluster_8: 15.282
- **Magnitude:** 1533.42 | **LOC:** 968 | **CtrlFlow:** 41.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **13**; blast radius 0.185; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.3%)
- **Documentation Coverage:** 5.8824% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__vcscanf` **(Many-Argument Workhorses)** (Impact: 907.7)
    * *Intent:* * All standard features are supported, except for positional argument * references (e.g. `%n$`) spec...
  * `ConsumeWhitespace` **(Stateful Encapsulated Methods)** (Impact: 11.9)
  * `CharsetAdd` **(C Struct Operations)** (Impact: 11.3)
  * `Buffer` **(Stateful Encapsulated Methods)** (Impact: 11.2)
  * `IsSpace` **(Stateful Encapsulated Methods)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 183 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 556
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 348`, `structural_boundaries: 128`, `args: 7`, `func_start: 6`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 190`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `import: 13`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 9.6e-05 | `Ripple Effect (Closeness):` 0.042147
  * `Imports (Out-Degree: 17):` ctype.h, errno.h, conv.h, limits.h, mem.h, runtime.h, stdckdint.h, str.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `tool/net/definitions.lua` (LUA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.321)
- **Top Global Matches:** file_cluster_11: 6.321, file_cluster_15: 7.056, file_cluster_2: 8.543
- **Magnitude:** 1495.36 | **LOC:** 8033 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **50** in-repo importer(s); blast radius 3.95; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.5%), Mutation Surface (formerly State Flux) (33.5%), Guard Balance (formerly Safety Score) (32.5%)
- **Documentation Coverage:** 1.8672% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unix.utimensat` **(Parameter Forwarders)** (Impact: 2.9)
    * *Intent:* --- possible to edit the timestamps on the symbolic link itself, --- rather than the file it points ...
  * `Database:apply_changeset` **(Parameter Forwarders)** (Impact: 2.7)
  * `OnProcessCreate` **(Parameter Forwarders)** (Impact: 2.5)
    * *Intent:* --- --- If this function is defined it'll be called from the main process --- each time redbean fork...
  * `Barf` **(Parameter Forwarders)** (Impact: 2.5)
    * *Intent:* --- --- --- For example: --- --- assert(Barf('x.txt', 'abc123')) --- assert(Barf('x.txt', 'XX', 0, 0...
  * `ProgramTokenBucket` **(Parameter Forwarders)** (Impact: 2.5)
    * *Intent:* --- or ProgramTrustedIp() addresses where these rate limits don't apply. --- --- It's assumed will b...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 492`, `args: 482`, `func_start: 482`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 40`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 481`
* *Architecture:* `api: 482`
* *Defense:* `doc: 1982`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.95
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007487
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 50):` (Excluded from Brief to save tokens)

### `libc/intrin/x86.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.166)
- **Top Global Matches:** file_cluster_8: 7.166, file_cluster_6: 17.356, file_cluster_3: 20.234
- **Magnitude:** 1386.06 | **LOC:** 855 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.091; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.9%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getAvailableFeatures` **(Many-Argument Workhorses)** (Impact: 557.8)
  * `getIntelProcessorTypeAndSubtype` **(Many-Argument Workhorses)** (Impact: 227.7)
  * `getAMDProcessorTypeAndSubtype` **(Many-Argument Workhorses)** (Impact: 160.9)
  * `__cpu_indicator_init` **(I/O & Config Routines)** (Impact: 11.4)
    * *Intent:* // A constructor function that is sets __cpu_model and __cpu_features2 with // the right values. Thi...
  * `detectX86FamilyModel` **(Stateful Encapsulated Methods)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 132 instances
* *State Mutation (weighted view):* 397
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 401`, `structural_boundaries: 91`, `args: 142`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 133`, `fragile_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `import: 1`
* *Defense:* `safety: 2`, `doc: 5`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` x86.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/kilo.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.049)
- **Top Global Matches:** file_cluster_6: 5.049, file_cluster_4: 11.282, file_cluster_8: 13.282
- **Magnitude:** 1364.36 | **LOC:** 1449 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.091; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (79.7%), Complexity Load (formerly Cognitive Load) (79.4%), Connectivity (formerly Api Exposure) (9.2%), Dead Code Surface (formerly Dead Code) (1.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `editorProcessKeypress` **(Compute Cores)** (Impact: 89.1)
    * *Intent:* /* Process events arriving from the standard input, which is, the user * is typing stuff on the term...
  * `editorUpdateSyntax` **(Compute Cores)** (Impact: 62.6)
    * *Intent:* /* Set every byte of row->hl (that corresponds to every character in the line) * to the right syntax...
  * `editorReadKey` **(Compute Cores)** (Impact: 59.4)
    * *Intent:* /* Read a key from the terminal put in raw mode, trying to handle * escape sequences. */
  * `editorFind` **(Compute Cores)** (Impact: 48.9)
    * *Intent:* /* =============================== Find mode ================================ */ #define KILO_QUERY_...
  * `editorMoveCursor` **(Compute Cores)** (Impact: 48.9)
    * *Intent:* /* ========================= Editor events handling ======================== */ /* Handle cursor pos...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 10 instances
* *Amplified Cascading Flux:* 245 instances
* *High Risk Execution (weighted view):* 5
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 751
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 321`, `structural_boundaries: 155`, `args: 70`, `func_start: 33`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 6`, `state_mutation: 261`, `dead_code: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 15`, `api: 39`, `import: 16`
* *Defense:* `safety: 11`, `immutability_locks: 20`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 47):` calls.h, termios.h, weirdtypes.h, ctype.h, errno.h, log.h, alg.h, arraylist2.internal.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ape/loader.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.786)
- **Top Global Matches:** file_cluster_4: 5.786, file_cluster_6: 8.371, file_cluster_16: 12.393
- **Magnitude:** 1285.32 | **LOC:** 1128 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.091; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.3%), Complexity Load (formerly Cognitive Load) (80.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Spawn` **(Many-Argument Workhorses)** (Impact: 130.2)
  * `TryElf` **(Many-Argument Workhorses)** (Impact: 117.3)
  * `Printf` **(Many-Argument Workhorses)** (Impact: 45.0)
  * `Mmap` **(Stateful Encapsulated Methods)** (Impact: 37.9)
  * `Pread` **(Stateful Encapsulated Methods)** (Impact: 32.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 229 instances
* *State Mutation (weighted view):* 690
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 112`, `args: 41`, `func_start: 28`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 232`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 12`, `import: 1`
* *Defense:* `doc: 1`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ape.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tool/net/lsqlite3.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.904)
- **Top Global Matches:** file_cluster_12: 6.904, file_cluster_16: 7.036, file_cluster_15: 9.598
- **Magnitude:** 1264.12 | **LOC:** 2856 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.168; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (64.1%), Complexity Load (formerly Cognitive Load) (53.9%), Debt Markers (formerly Tech Debt) (7.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `db_do_next_row` **(Compute Cores)** (Impact: 27.0)
  * `db_register_function` **(Many-Argument Workhorses)** (Impact: 23.8)
    * *Intent:* /* ** Register a normal function ** Params: db, function name, number arguments, [ callback | step, ...
  * `dbvm_bind_index` **(Stateful Encapsulated Methods)** (Impact: 23.4)
    * *Intent:* /* ** ======================================================= ** Virtual Machine - Bind ** =========...
  * `db_apply_changeset` **(Compute Cores)** (Impact: 21.6)
  * `db_exec_callback` **(Many-Argument Workhorses)** (Impact: 20.2)
    * *Intent:* /* ** Params: db, sql, callback, user ** returns: code [, errmsg] ** ** Callback: ** Params: user, n...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 144 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 479
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 291`, `args: 991`, `func_start: 164`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 191`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 13`, `import: 9`
* *Defense:* `safety: 1`, `immutability_locks: 70`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.168
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.00015
  * `Imports (Out-Degree: 7):` weirdtypes.h, gc.h, mem.h, str.h, lauxlib.h, lua.h, luaconf.h, extensions.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tool/viz/printvideo.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.183)
- **Top Global Matches:** file_cluster_4: 8.183, file_cluster_12: 11.353, file_cluster_16: 11.526
- **Magnitude:** 1260.42 | **LOC:** 1460 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **85**; blast radius 0.091; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.0%), Guard Balance (formerly Safety Score) (77.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (20.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ReadKeyboard` **(Compute Cores)** (Impact: 131.1)
  * `DescribeAdjustments` **(Compute Cores)** (Impact: 39.7)
  * `TranscodeVideo` **(Compute Cores)** (Impact: 27.5)
  * `GetOpts` **(Stateful Encapsulated Methods)** (Impact: 24.1)
  * `main` **(Compute Cores)** (Impact: 21.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 228 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 734
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 309`, `structural_boundaries: 322`, `args: 84`, `func_start: 51`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 8`, `state_mutation: 278`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 10`, `api: 9`, `import: 85`
* *Defense:* `safety: 17`, `doc: 1`, `immutability_locks: 11`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 143):` cosmoaudio.h, core.h, half.h, illumination.h, pl_mpeg.h, scale.h, quant.h, tty.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libc/intrin/mmap.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.625)
- **Top Global Matches:** file_cluster_6: 9.625, file_cluster_4: 9.818, file_cluster_12: 15.145
- **Magnitude:** 1259.2 | **LOC:** 1269 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **79** in-repo importer(s); it depends on **47**; blast radius 0.488; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.8%), Complexity Load (formerly Cognitive Load) (74.4%)
- **Documentation Coverage:** 85.3659% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__mmap_impl` **(Many-Argument Workhorses)** (Impact: 163.7)
  * `sys_mmap_nt` **(Many-Argument Workhorses)** (Impact: 76.3)
  * `__mremap` **(Many-Argument Workhorses)** (Impact: 69.6)
  * `__muntrack` **(Many-Argument Workhorses)** (Impact: 54.1)
    * *Intent:* #endif
  * `__mremap_impl` **(Many-Argument Workhorses)** (Impact: 35.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 183 instances
* *State Mutation (weighted view):* 562
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 252`, `structural_boundaries: 247`, `args: 33`, `func_start: 32`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 196`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 5`
* *Architecture:* `api: 8`, `concurrency: 1`, `import: 47`
* *Defense:* `safety: 38`, `doc: 3`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.488
  * `Choke Point (Betweenness):` 0.005501 | `Ripple Effect (Closeness):` 0.066524
  * `Imports (Out-Degree: 72):` sections.internal.h, assert.h, calls.h, internal.h, state.internal.h, rlimit.h, sigset.internal.h, syscall-sysv.internal.h...
  * `Imported By (In-Degree: 79):` (Excluded from Brief to save tokens)

### `tool/viz/life.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.118)
- **Top Global Matches:** file_cluster_4: 7.118, file_cluster_16: 8.118, file_cluster_15: 10.551
- **Magnitude:** 1218.46 | **LOC:** 1448 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **55**; blast radius 0.091; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.0%), Guard Balance (formerly Safety Score) (74.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (20.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LoadFile` **(Compute Cores)** (Impact: 58.4)
  * `ReadKeyboard` **(Compute Cores)** (Impact: 47.0)
  * `RasterZoomed` **(Many-Argument Workhorses)** (Impact: 41.6)
  * `WindowProc` **(Many-Argument Workhorses)** (Impact: 40.3)
  * `OnMouse` **(Compute Cores)** (Impact: 36.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 190 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 654
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 263`, `args: 129`, `func_start: 80`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 3`, `state_mutation: 274`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 2`, `import: 55`
* *Defense:* `safety: 7`, `doc: 1`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 120):` scale.h, calls.h, sigaction.h, termios.h, winsize.h, termios.h, cosmotime.h, ctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `libc/system/cocmd.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.793)
- **Top Global Matches:** file_cluster_4: 7.793, file_cluster_6: 8.012, file_cluster_16: 13.942
- **Magnitude:** 1187.44 | **LOC:** 1209 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **32**; blast radius 0.1; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.9%), Complexity Load (formerly Cognitive Load) (80.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_cocmd` **(Many-Argument Workhorses)** (Impact: 91.3)
  * `Tokenize` **(Compute Cores)** (Impact: 85.2)
  * `TryBuiltin` **(Compute Cores)** (Impact: 48.4)
  * `GetVar` **(Stateful Encapsulated Methods)** (Impact: 26.7)
  * `Rm` **(Compute Cores)** (Impact: 19.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 197 instances
* *State Mutation (weighted view):* 594
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 368`, `structural_boundaries: 254`, `args: 62`, `func_start: 48`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 28`, `state_mutation: 200`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 14`, `api: 1`, `import: 32`
* *Defense:* `safety: 5`, `doc: 1`, `immutability_locks: 21`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.1
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.000639
  * `Imports (Out-Degree: 65):` assert.h, calls.h, stat.h, timespec.h, cosmotime.h, ctype.h, dce.h, errno.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tool/plinko/lib/plinko.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.459)
- **Top Global Matches:** file_cluster_16: 6.459, file_cluster_15: 7.429, file_cluster_4: 8.654
- **Magnitude:** 1161.58 | **LOC:** 1095 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **34**; blast radius 0.116; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.7%), Complexity Load (formerly Cognitive Load) (88.5%), Guard Balance (formerly Safety Score) (77.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Plinko` **(Many-Argument Workhorses)** (Impact: 55.2)
  * `DispatchFuncall` **(Many-Argument Workhorses)** (Impact: 44.6)
  * `DispatchCond` **(Many-Argument Workhorses)** (Impact: 27.8)
  * `DispatchLet1` **(Many-Argument Workhorses)** (Impact: 22.2)
  * `DispatchPrint` **(Many-Argument Workhorses)** (Impact: 17.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 171 instances
* *State Mutation (weighted view):* 565
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 198`, `args: 253`, `func_start: 82`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 4`, `state_mutation: 223`, `fragile_debt: 1`, `unreferenced_by_name: 51`
* *Architecture:* `io: 2`, `api: 48`, `import: 34`
* *Defense:* `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 2.8e-05 | `Ripple Effect (Closeness):` 0.00015
  * `Imports (Out-Degree: 58):` calls.h, sigaction.h, syscall-sysv.internal.h, errno.h, likely.h, strace.h, countbranch.h, countexpr.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `ape/ape-m1.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.838)
- **Top Global Matches:** file_cluster_4: 5.838, file_cluster_16: 7.879, file_cluster_15: 9.828
- **Magnitude:** 1136.38 | **LOC:** 1140 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **40** in-repo importer(s); it depends on **20**; blast radius 0.388; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.4%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Spawn` **(Many-Argument Workhorses)** (Impact: 144.2)
  * `TryElf` **(Many-Argument Workhorses)** (Impact: 88.4)
  * `main` **(Many-Argument Workhorses)** (Impact: 88.1)
  * `pthread_jit_write_protect_np_workaround` **(Compute Cores)** (Impact: 19.6)
  * `Commandv` **(Stateful Encapsulated Methods)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 175 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 597
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 171`, `args: 61`, `func_start: 47`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 247`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 8`, `concurrency: 3`, `import: 20`
* *Defense:* `safety: 27`, `immutability_locks: 52`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.388
  * `Choke Point (Betweenness):` 0.007353 | `Ripple Effect (Closeness):` 0.060475
  * `Imports (Out-Degree: 34):` assert.h, dispatch.h, dlfcn.h, errno.h, fcntl.h, OSCacheControl.h, limits.h, pthread.h...
  * `Imported By (In-Degree: 40):` (Excluded from Brief to save tokens)

### `libc/calls/read-nt.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.603)
- **Top Global Matches:** file_cluster_4: 7.603, file_cluster_6: 8.389, file_cluster_15: 14.121
- **Magnitude:** 1080.44 | **LOC:** 1088 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **49**; blast radius 0.146; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ProcessKeyEvent` **(Many-Argument Workhorses)** (Impact: 97.0)
  * `IngestConsoleInputRecord` **(Compute Cores)** (Impact: 93.0)
  * `InterceptTerminalCommands` **(Many-Argument Workhorses)** (Impact: 52.3)
    * *Intent:* // Intercept ANSI TTY commands that enable features.
  * `CountConsoleInputBytesBlockingImpl` **(Many-Argument Workhorses)** (Impact: 47.5)
  * `ProcessMouseEvent` **(Many-Argument Workhorses)** (Impact: 44.5)
    * *Intent:* // To use the tty mouse events feature: // - write(1, "\e[?1000;1002;1015;1006h") to enable // - wri...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 134 instances
* *State Mutation (weighted view):* 412
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 231`, `args: 49`, `func_start: 41`, `class_start: 29`
* *Risk/State:* `state_mutation: 144`, `dead_code: 1`, `unreferenced_by_name: 6`
* *Architecture:* `api: 45`, `concurrency: 2`, `import: 49`
* *Defense:* `safety: 14`, `doc: 1`, `sync_locks: 1`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.146
  * `Choke Point (Betweenness):` 0.001368 | `Ripple Effect (Closeness):` 0.05032
  * `Imports (Out-Degree: 90):` assert.h, internal.h, sig.internal.h, state.internal.h, iovec.h, sigset.internal.h, timespec.h, timespec.internal.h...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `tool/net/lfuncs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.32)
- **Top Global Matches:** file_cluster_15: 7.32, file_cluster_12: 7.773, file_cluster_16: 7.793
- **Magnitude:** 1027.08 | **LOC:** 1306 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **59**; blast radius 0.092; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.3%), Complexity Load (formerly Cognitive Load) (87.7%), Guard Balance (formerly Safety Score) (68.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LuaSlurp` **(Compute Cores)** (Impact: 32.9)
    * *Intent:* // Slurp(path:str[, i:int[, j:int]]) // ├─→ data:str // └─→ nil, unix.Errno
  * `LuaBarf` **(Compute Cores)** (Impact: 25.3)
    * *Intent:* // Barf(path:str, data:str[, mode:int[, flags:int[, offset:int]]]) // ├─→ true // └─→ nil, unix.Errn...
  * `LuaGetHostOs` **(Compute Cores)** (Impact: 23.8)
  * `LuaBenchmark` **(Compute Cores)** (Impact: 21.4)
  * `LuaCompress2` **(Stateful Encapsulated Methods)** (Impact: 16.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 136 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 506
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 176`, `args: 348`, `func_start: 101`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 234`, `unreferenced_by_name: 84`
* *Architecture:* `io: 4`, `api: 86`, `import: 59`
* *Defense:* `safety: 42`, `immutability_locks: 46`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.092
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.000416
  * `Imports (Out-Degree: 80):` cdecimate2xuint8x8.h, bsdstdlib.h, calls.h, rusage.h, stat.h, timespec.h, cosmo.h, cosmotime.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/picol.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.436)
- **Top Global Matches:** file_cluster_6: 5.436, file_cluster_4: 10.683, file_cluster_8: 14.286
- **Magnitude:** 913.14 | **LOC:** 679 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.091; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (81.5%), Guard Balance (formerly Safety Score) (80.6%), Connectivity (formerly Api Exposure) (11.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `picolCommandMath` **(Many-Argument Workhorses)** (Impact: 64.3)
  * `picolEval` **(Many-Argument Workhorses)** (Impact: 42.6)
    * *Intent:* /* EVAL! */
  * `picolParseString` **(Compute Cores)** (Impact: 35.3)
  * `picolCommandCallProc` **(Many-Argument Workhorses)** (Impact: 31.3)
  * `picolGetToken` **(Compute Cores)** (Impact: 28.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 22 instances
* *Amplified Cascading Flux:* 141 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 446
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 156`, `args: 29`, `func_start: 29`, `class_start: 27`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 164`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 35`, `import: 3`
* *Defense:* `safety: 6`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `ctl/unique_ptr.h` (CPP) | Magnitude: 57.24 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 38, immutability_locks: 29, func_start: 19
- `ctl/is_signed.h` (CPP) | Magnitude: 15.2 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 4, macros: 2, class_start: 1, globals: 1
- `ctl/is_unsigned.h` (CPP) | Magnitude: 15.2 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 4, macros: 2, class_start: 1, globals: 1
- `ctl/array.h` (CPP) | Magnitude: 118.7 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 158, structural_boundaries: 67, immutability_locks: 60, func_start: 35
- `ctl/allocator.h` (CPP) | Magnitude: 34.3 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 39, immutability_locks: 14, core_var_decl: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `test/libc/calls/reservefd_test.c` (C) | Magnitude: 88.38 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 55, import: 26, state_mutation: 17, structural_boundaries: 14
- `test/libc/calls/getrandom_test.c` (C) | Magnitude: 244.94 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 149, state_mutation: 53, structural_boundaries: 46, import: 26
- `test/libc/calls/renameat_test.c` (C) | Magnitude: 40.34 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: test: 65, indent_spaces: 57, args: 17, io: 15
- `test/libc/intrin/cosmo_once_test.c` (C) | Magnitude: 54.94 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 37, pointers: 12, structural_boundaries: 9, state_mutation: 7
- `test/libc/calls/openatemp_test.c` (C) | Magnitude: 26.8 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 45, test: 38, args: 14, import: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `libc/stdio/append.h` (C) | Magnitude: 25.6 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: macros: 13, api: 10, args: 9, immutability_locks: 6
- `test/libc/calls/stackoverflow1_test.c` (C) | Magnitude: 54.06 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 47, import: 26, structural_boundaries: 23, pointers: 16
- `libc/cosmo.h` (C) | Magnitude: 61.16 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 57, api: 44, pointers: 34, args: 33
- `libc/thread/mktls.c` (C) | Magnitude: 54.82 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 55, pointers: 41, structural_boundaries: 26, scientific: 22
- `libc/elf/getelfsegmentaddress.c` (C) | Magnitude: 12.08 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 12, pointers: 9, structural_boundaries: 7, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `test/net/http/ismimetype_test.c` (C) | Magnitude: 6.3 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: args: 8, indent_spaces: 8, test: 7, import: 3
- `test/libc/tinymath/cos_test.c` (C) | Magnitude: 8.5 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 23, test: 20, args: 7, scientific: 5
- `test/libc/tinymath/cosh_test.c` (C) | Magnitude: 12.96 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: test: 30, indent_spaces: 30, args: 9, import: 5
- `test/libc/tinymath/exp10_test.c` (C) | Magnitude: 10.34 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: test: 27, indent_spaces: 24, args: 9, import: 4
- `test/libc/tinymath/atanh_test.c` (C) | Magnitude: 12.78 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 30, test: 28, import: 6, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `libc/intrin/mempcpy.c` (C) | Magnitude: 3.3 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 4, pointers: 4, indent_spaces: 2, args: 1
- `libc/stdio/gets.c` (C) | Magnitude: 2.7 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: import: 2, pointers: 2, structural_boundaries: 1, args: 1
- `test/libc/tinymath/complex_test.c` (C) | Magnitude: 4.6 | Delta: **0.118** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 10, scientific: 9, test: 4, core_var_decl: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `libc/intrin/unlockfileex.c` (C) | Magnitude: 6.52 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 11, import: 7, structural_boundaries: 2, api: 2
- `libc/intrin/swapcontext.S` (ASSEMBLY) | Magnitude: 9.42 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 23, structural_boundaries: 10, args: 10, pointers: 3
- `libc/intrin/strlen16.c` (C) | Magnitude: 45.28 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 30, state_mutation: 12, pointers: 12, core_var_decl: 9
- `test/libc/str/bzero_test.c` (C) | Magnitude: 21.8 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 61, import: 8, state_mutation: 4, pointers: 3
- `test/libc/x/utf16to8_test.c` (C) | Magnitude: 23.76 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: state_mutation: 19, indent_spaces: 13, test: 8, import: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `test/libc/mem/critbit0_test.c` (C) | Magnitude: 92.14 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 92, pointers: 57, structural_boundaries: 31, test: 28
- `test/dsp/core/mulaw_test.c` (C) | Magnitude: 30.7 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 96, test: 14, import: 9, func_start: 5
- `libc/mem/leaks.c` (C) | Magnitude: 19.62 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 10, import: 9, pointers: 8
- `test/libc/str/chacha20poly1305_test.c` (C) | Magnitude: 114.56 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 140, core_var_decl: 30, design_snake_case: 30, design_short_vars: 22
- `libc/intrin/hilbert.c` (C) | Magnitude: 85.76 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 36, state_mutation: 24, core_var_decl: 18, design_snake_case: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `libc/stdio/swprintf.c` (C) | Magnitude: 3.52 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: import: 2, indent_spaces: 2, args: 1, func_start: 1
- `dsp/core/c1331s.h` (C) | Magnitude: 12.22 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 11, state_mutation: 8, macros: 2, core_var_decl: 2
- `dsp/tty/mpsadbw.S` (ASSEMBLY) | Magnitude: 13.12 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 3, args: 2, globals: 2, planned_debt: 1
- `libc/calls/struct/statfs-xnu.internal.h` (C) | Magnitude: 16.5 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 2, macros: 2, class_start: 1
- `libc/sock/closesocket-nt.c` (C) | Magnitude: 6.9 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: import: 5, indent_spaces: 5, structural_boundaries: 3, pointers: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `libc/intrin/divmodti4.c` (C) | Magnitude: 42.6 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 20, state_mutation: 12, core_var_decl: 12, design_snake_case: 12
- `test/libc/stdio/dumphexc_test.c` (C) | Magnitude: 4.32 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 6, args: 4, indent_spaces: 3, func_start: 2
- `libc/nt/ntdllimport.h` (C) | Magnitude: 15.62 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 16, macros: 5, import: 2
- `test/dsp/tty/rgb2ansi_test.c` (C) | Magnitude: 4.34 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: dead_code: 8, import: 2, indent_spaces: 2, structural_boundaries: 1
- `libc/calls/struct/ucontext-freebsd.internal.h` (C) | Magnitude: 21.62 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 11, class_start: 10, api: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `libc/runtime/zipos-open.c` (C) | Magnitude: 246.34 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 162, pointers: 65, branch: 52, structural_boundaries: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `ctl/uninitialized_fill.h` (CPP) | Magnitude: 14.26 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 8, branch: 2, safety: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `libc/calls/struct/siginfo.internal.h` (C) | Magnitude: 17.2 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: macros: 3, immutability_locks: 3, args: 2, safety_bypasses: 2
- `libc/thread/pthread_cond_signal.c` (C) | Magnitude: 11.24 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: pointers: 11, indent_spaces: 10, import: 5, branch: 3
- `libc/calls/struct/sigaction.internal.h` (C) | Magnitude: 31.26 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 40, indent_spaces: 31, class_start: 16, api: 15
- `test/libc/fmt/basename_test.c` (C) | Magnitude: 8.4 | Delta: **0.141** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: test: 16, indent_spaces: 12, func_start: 4, unreferenced_by_name: 4
- `libc/isystem/stdlib.h` (C) | Magnitude: 15.44 | Delta: **0.146** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: import: 16, args: 4, macros: 4, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `libc/proc/fork-sysv.c` (C) | Magnitude: 30.88 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 12, import: 7, inline_asm: 7
- `libc/sock/socketpair-nt.c` (C) | Magnitude: 82.08 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 70, import: 18, branch: 14, state_mutation: 14
- `tool/viz/od16.c` (C) | Magnitude: 91.8 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 62, branch: 18, state_mutation: 17, import: 12
- `libc/calls/posix_fadvise-nt.c` (C) | Magnitude: 69.18 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 15, branch: 13, import: 12
- `examples/ctrlc.c` (C) | Magnitude: 48.64 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 51, branch: 13, import: 8, io: 6

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tool/net/definitions.lua` -> Churn: **70.55%** | Cog Load: 0.0% | Debt: 100.0%
- `libc/dlopen/stubs.c` -> Churn: **63.09%** | Cog Load: 0.0% | Debt: 99.9999%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `dsp/audio/cosmoaudio/miniaudio.h` -> **Justine Tunney** (100.0% isolated ownership) | Magnitude: 66041.4
- `libc/stdckdint.h` -> **Justine Tunney** (100.0% isolated ownership) | Magnitude: 6454.33
- `libc/intrin/demangle.c` -> **Justine Tunney** (100.0% isolated ownership) | Magnitude: 4329.56
- `dsp/mpeg/pl_mpeg.h` -> **Justine Tunney** (100.0% isolated ownership) | Magnitude: 2839.66
- `libc/stdio/fmt.c` -> **Justine Tunney** (100.0% isolated ownership) | Magnitude: 2696.16

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `dsp/audio/cosmoaudio/miniaudio.h` -> **Severity: 2.078** (Bridge: 0.0208 * Flux: 99.9998%)
- `libc/intrin/kprintf.greg.c` -> **Severity: 0.965** (Bridge: 0.0096 * Flux: 100.0%)
- `libc/testlib/trace.c` -> **Severity: 0.846** (Bridge: 0.0085 * Flux: 99.9999%)
- `ape/ape-m1.c` -> **Severity: 0.735** (Bridge: 0.0074 * Flux: 100.0%)
- `tool/curl/curl.c` -> **Severity: 0.621** (Bridge: 0.0062 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `libc/thread/thread.h` -> **Severity: 8.681** (Embedded: 0.1085 * Error Risk: 80.0%)
- `libc/runtime/runtime.h` -> **Severity: 8.162** (Embedded: 0.161 * Error Risk: 50.6896%)
- `libc/intrin/describeflags.h` -> **Severity: 7.765** (Embedded: 0.0857 * Error Risk: 90.5687%)
- `libc/stdio/stdio.h` -> **Severity: 7.471** (Embedded: 0.0934 * Error Risk: 80.0%)
- `libc/intrin/kprintf.greg.c` -> **Severity: 7.274** (Embedded: 0.0865 * Error Risk: 84.1276%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `libc/runtime/runtime.h` -> **Severity: 1083.5** (Blast Radius: 10.835 * Doc Risk: 100.0%)
- `libc/testlib/testlib.h` -> **Severity: 614.3** (Blast Radius: 6.143 * Doc Risk: 100.0%)
- `tool/plinko/lib/plinko.h` -> **Severity: 322.4** (Blast Radius: 3.224 * Doc Risk: 100.0%)
- `libc/intrin/stracef.greg.c` -> **Severity: 266.3** (Blast Radius: 2.663 * Doc Risk: 100.0%)
- `libc/thread/posixthread.internal.h` -> **Severity: 211.695** (Blast Radius: 2.207 * Doc Risk: 95.92%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1616 literal sites + 43 sites through wrappers = 1659
- **`memory_alloc`:** 1801 literal sites + 16541 sites through wrappers = 18342
- **`panics_and_aborts`:** 1956 literal sites + 209 sites through wrappers = 2165

- `ASSERT_EQ` (macro, memory_alloc, via Assert): 3242 call sites in 203 files -- `libc/testlib/testlib.h`
- `EXPECT_EQ` (macro, memory_alloc, via Assert): 3214 call sites in 183 files -- `libc/testlib/testlib.h`
- `ASSERT_SYS` (macro, memory_alloc, via Assert): 2354 call sites in 121 files -- `libc/testlib/testlib.h`
- `printf` (function, memory_alloc, via vfprintf): 785 call sites in 114 files -- `libc/stdio/printf.c`
- `EXPECT_SYS` (macro, memory_alloc, via Assert): 587 call sites in 59 files -- `libc/testlib/testlib.h`
- `EXPECT_TRUE` (macro, memory_alloc, via Assert): 534 call sites in 69 files -- `libc/testlib/testlib.h`
- `fputc` (function, memory_alloc, via FLOCKFILE): 377 call sites in 30 files -- `libc/stdio/fputc.c`
- `fprintf` (function, memory_alloc, via FLOCKFILE): 294 call sites in 88 files -- `libc/stdio/fprintf.c`
- `ASSERT_TRUE` (macro, memory_alloc, via Assert): 279 call sites in 51 files -- `libc/testlib/testlib.h`
- `fputs` (function, memory_alloc, via FLOCKFILE): 268 call sites in 38 files -- `libc/stdio/fputs.c`
- `EXPECT_NE` (macro, memory_alloc, via Assert): 264 call sites in 43 files -- `libc/testlib/testlib.h`
- `BENCHMARK` (macro, memory_alloc, via timespec_real): 190 call sites in 32 files -- `libc/testlib/benchmark.h`
*(+626 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 63270 call pairs -- scoped 21.8%, unique 33.4%, ambiguous 5.9%, external 39.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 51046 | 14.4% | 39.6% | 6.3% | 39.7% |
| objective-c | 8825 | 63.0% | 2.8% | 0.2% | 34.0% |
| cpp | 2121 | 29.0% | 17.6% | 22.2% | 31.3% |
| lua | 1020 | 22.4% | 27.5% | 0.4% | 49.8% |
| shell | 111 | 6.3% | 0.0% | 0.0% | 93.7% |
| python | 94 | 13.8% | 0.0% | 0.0% | 86.2% |
| assembly | 49 | 38.8% | 44.9% | 10.2% | 6.1% |
| makefile | 4 | 0.0% | 0.0% | 0.0% | 100.0% |

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
