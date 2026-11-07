# ARCHITECTURAL_BRIEF: nasm
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/netwide-assembler/nasm.git` |
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
- **Scope:** 959 analyzed artifact(s), 78610 LOC.
- **Load-bearing artifact:** `include/compiler.h` -- 88 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `include/compiler.h` -- pulls in 24 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `asm/preproc.c` at magnitude 8336.78 (structural weight, not risk).
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
| Total Artifacts | 1337 |
| Analyzed Artifacts (Scanned) | 959 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 378 |
| Total LOC | 78610 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 71.7% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2999 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.334 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1135 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 9 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ASSEMBLY | 446 | 19726 | 46.5% |
| JSON | 192 | 3143 | 20.0% |
| C | 135 | 41742 | 14.1% |
| PERL | 91 | 8707 | 9.5% |
| M4 | 40 | 770 | 4.2% |
| SHELL | 17 | 639 | 1.8% |
| PLAINTEXT | 11 | 0 | 1.1% |
| MAKEFILE | 7 | 1392 | 0.7% |
| EASYTRIEVE | 7 | 1554 | 0.7% |
| MARKDOWN | 5 | 0 | 0.5% |
| YAML | 2 | 39 | 0.2% |
| CSS | 2 | 239 | 0.2% |
| PYTHON | 2 | 583 | 0.2% |
| BATCH | 1 | 5 | 0.1% |
| LIVECODE | 1 | 71 | 0.1% |

## 4.1 SOURCE ENCODINGS
> 28 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 931 |
| cp1252 | cp1252-fallback | 22 |
| latin-1 | latin-1-fallback | 6 |

> 1 guessed file(s) read as double-byte text that decodes strictly as euc_jp / gbk / big5 / euc_kr: if that is the estate's code page, rescan with `--source-encoding euc_jp` (or the right one of those). E.g. `travis/test/br3174983.bin.t`.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 40%, Declarative / Non-Code 35%, Interface Declarations Files 4%, Large Core Modules (3) 4%, Compute Cores Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 928 | 96.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 30 | 3.1% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 378*

**Composition by Extension & Reason:**
- `.t`: 125x Excluded (Binary Format Detected), 42x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.stderr`: 86x Excluded (Unsupported Extension: '.stderr')
- `.asm`: 5x Excluded (Binary Format Detected), 4x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Excluded (Embedded Hex Payload: 8284 hex tokens in 1609 LOC)
- `.src`: 24x Excluded (Unsupported Extension: '.src')
- `.mac`: 13x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 163 LOC), 1x Zero-Density Threshold (LOC: 84, Signals: 0)
- `no_extension`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.h`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dat`: 6x Excluded (Unsupported Extension: '.dat')
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.guess`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sub`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.readme`: 1x Excluded (Unsupported Extension: '.README')
- `.rules`: 1x Excluded (Unsupported Extension: '.rules')
- `.ps`: 1x Excluded (Unsupported Extension: '.ps')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.0 | 8.8 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 94.3 | 13.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 5.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 11.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 98.5 | 0.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.1 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 29.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 405 | 71 | 0 | `asm/preproc.c` |
| cleanup | 188 | 61 | 0 | `Mkfiles/openwcom.mak` |
| guards | 3613 | 156 | 4 | `asm/preproc.c` |
| danger | 733 | 101 | 1 | `autoconf/helpers/compile` |
| concurrency | 176 | 27 | 0 | `Mkfiles/openwcom.mak` |
| connectivity | 1617 | 211 | 5 | `include/nasm.h` |
| io | 401 | 69 | 0 | `autoconf/helpers/compile` |
| crypto | 0 | 0 | 0 | - |
| ipc | 28 | 15 | 0 | `output/outelf.c` |
| time | 15 | 8 | 0 | `asm/nasm.c` |
| serialization | 6 | 1 | 0 | `Makefile.in` |
| regex | 745 | 37 | 0 | `doc/rdsrc.pl` |
| events | 62 | 23 | 0 | `autoconf/m4/pa_func_attribute.m4` |
| tests | 2020 | 19 | 0 | `travis/test/apx-cfcmovcc.asm` |
| docs | 16 | 7 | 0 | `asm/error.c` |
| debt | 1484 | 104 | 1 | `asm/pptok.pl` |
| mutation | 17523 | 206 | 16 | `asm/preproc.c` |
| dead_code | 584 | 192 | 1 | `travis/test/tmap.asm` |
| credential | 0 | 0 | 0 | - |
| threat | 2 | 1 | 0 | `test/bracedquote.asm` |
| ml_ai | 265 | 34 | 0 | `test/floatx.asm` |
| ui | 32 | 10 | 0 | `doc/nasmdoc.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `autoconf/helpers/compile` (Hits: 54)
- `travis/nasm-t.py` (Hits: 32)
- `Makefile.in` (Hits: 27)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **compiler.h** (`include/compiler.h`) — 88 inbound connections
2. **nasmlib.h** (`include/nasmlib.h`) — 60 inbound connections
3. **nasm.h** (`include/nasm.h`) — 44 inbound connections
4. **error.h** (`include/error.h`) — 35 inbound connections
5. **alloc.c** (`nasmlib/alloc.c`) — 34 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **compiler.h** (`include/compiler.h`) — 24 outbound dependencies
2. **nasm.c** (`asm/nasm.c`) — 20 outbound dependencies
3. **outelf.c** (`output/outelf.c`) — 17 outbound dependencies
4. **directiv.c** (`asm/directiv.c`) — 16 outbound dependencies
5. **outmacho.c** (`output/outmacho.c`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `byte_code_compile` **(Many-Argument Workhorses)** (@ `x86/insns.pl`) -> Impact: **895.3** | LOC: 599
  * *Intent:* # # The operands word lists the order of the operands: # # r = register field in the modr/m # m = modr/m # v = VEX "v" field or DFV # i = immediate # ...
- `do_directive` **(Many-Argument Workhorses)** (@ `asm/preproc.c`) -> Impact: **605.0** | LOC: 1101
  * *Intent:* /** * find and process preprocessor directive in passed line * Find out if a line contains a preprocessor directive, and deal * with it if so. * * If ...
- `matches` **(Many-Argument Workhorses)** (@ `disasm/disasm.c`) -> Impact: **532.5** | LOC: 811
  * *Intent:* * corresponds to the data stream in data and parse it into "ins" if * so. "ins" has already been partially initialized in disasm() to * point contain ...
- `process_ea` **(Many-Argument Workhorses)** (@ `asm/assemble.c`) -> Impact: **523.3** | LOC: 466
- `parse_line` **(Many-Argument Workhorses)** (@ `asm/parser.c`) -> Impact: **480.0** | LOC: 720
- `disasm` **(Many-Argument Workhorses)** (@ `disasm/disasm.c`) -> Impact: **359.1** | LOC: 401
- `process_arg` **(Many-Argument Workhorses)** (@ `asm/nasm.c`) -> Impact: **329.7** | LOC: 394
- `calcsize` **(Compute Cores)** (@ `asm/assemble.c`) -> Impact: **324.6** | LOC: 722
  * *Intent:* /* Common construct */ #define case3(x) case (x): case (x)+1: case (x)+2 #define case4(x) case3(x): case (x)+3 /* * calcsize() is assumed to be proces...
- `func_multisize` **(Many-Argument Workhorses)** (@ `x86/preinsns.pl`) -> Impact: **289.8** | LOC: 156
- `tokenize` **(Compute Cores)** (@ `asm/preproc.c`) -> Impact: **283.4** | LOC: 408
  * *Intent:* /* * Tokenize a line of text. This is a very simple process since we * don't need to parse the value out of e.g. numeric tokens: we * simply split one...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `asm` | 35 | 23545.6 | 52.62% | 18.99% |
| `output` | 22 | 14831.06 | 43.36% | 15.72% |
| `travis/test` | 413 | 6542.62 | 0.26% | 0.0% |
| `test` | 291 | 4764.98 | 1.0% | 0.0% |
| `x86` | 8 | 4161.74 | 44.74% | 10.7% |
| `disasm` | 7 | 3593.86 | 50.18% | 27.64% |
| `doc` | 14 | 3212.71 | 44.7% | 10.92% |
| `nasmlib` | 28 | 2594.18 | 47.71% | 45.98% |
| `misc` | 12 | 1630.88 | 44.43% | 16.15% |
| `include` | 25 | 1085.2 | 11.75% | 3.33% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `autoconf/m4/pa_func_attribute.m4` -> **100.0%** Exposure
- `common/errstubs.c` -> **99.9447%** Exposure
- `asm/srcfile.c` -> **99.8629%** Exposure
- `nasmlib/fileio.c` -> **99.6345%** Exposure
- `output/nullout.c` -> **99.593%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `asm/assemble.c` -> **100.0%** Exposure
- `asm/directiv.c` -> **100.0%** Exposure
- `asm/eval.c` -> **100.0%** Exposure
- `asm/exprlib.c` -> **100.0%** Exposure
- `asm/floats.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/Makefile.in` -> **22** Orphaned Functions | **0** Duplicates
- `asm/preproc.c` -> **16** Orphaned Functions | **0** Duplicates
- `nasmlib/saa.c` -> **15** Orphaned Functions | **0** Duplicates
- `Makefile.in` -> **12** Orphaned Functions | **0** Duplicates
- `asm/error.c` -> **10** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `637` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `asm/preproc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.975)
- **Top Global Matches:** file_cluster_4: 6.975, file_cluster_6: 9.525, file_cluster_16: 13.028
- **Magnitude:** 8336.78 | **LOC:** 9262 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **15**; blast radius 0.959; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Complexity Load (formerly Cognitive Load) (94.7%), Guard Balance (formerly Safety Score) (80.9%)
- **Documentation Coverage:** 88.8158% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_directive` **(Many-Argument Workhorses)** (Impact: 605.0)
    * *Intent:* /** * find and process preprocessor directive in passed line * Find out if a line contains a preproc...
  * `tokenize` **(Compute Cores)** (Impact: 283.4)
    * *Intent:* /* * Tokenize a line of text. This is a very simple process since we * don't need to parse the value...
  * `if_condition` **(Many-Argument Workhorses)** (Impact: 187.6)
    * *Intent:* /* * Determine whether one of the various `if' conditions is true or * not. * * We must free the tli...
  * `expand_smacro_with_params` **(Many-Argument Workhorses)** (Impact: 110.0)
    * *Intent:* /* * Expand one single-line macro instance given a specific macro and a * specific set of parameters...
  * `parse_smacro_template` **(Many-Argument Workhorses)** (Impact: 87.5)
    * *Intent:* * is set, set the nparam, varadic and params field in the template. * The varadic field is not used ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1480 instances
* *State Mutation (weighted view):* 4653
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1566`, `structural_boundaries: 1168`, `args: 353`, `func_start: 211`, `class_start: 117`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 1693`, `planned_debt: 4`, `fragile_debt: 6`, `unreferenced_by_name: 16`
* *Architecture:* `io: 1`, `api: 43`, `import: 15`
* *Defense:* `safety: 44`, `doc: 2`, `immutability_locks: 228`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.959
  * `Choke Point (Betweenness):` 0.000226 | `Ripple Effect (Closeness):` 0.008673
  * `Imports (Out-Degree: 41):` assemble.h, compiler.h, dbginfo.h, error.h, eval.h, hashtbl.h, listing.h, nasm.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `asm/assemble.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.429)
- **Top Global Matches:** file_cluster_8: 7.429, file_cluster_6: 10.682, file_cluster_4: 19.032
- **Magnitude:** 4319.52 | **LOC:** 4164 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.815; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_ea` **(Many-Argument Workhorses)** (Impact: 523.3)
  * `calcsize` **(Compute Cores)** (Impact: 324.6)
    * *Intent:* /* Common construct */ #define case3(x) case (x): case (x)+1: case (x)+2 #define case4(x) case3(x): ...
  * `matches` **(Many-Argument Workhorses)** (Impact: 250.7)
  * `gencode` **(Many-Argument Workhorses)** (Impact: 211.2)
  * `prefix_byte` **(Compute Cores)** (Impact: 84.1)
    * *Intent:* /* * Return the byte value of a legacy prefix (possibly depending on context) * Returns one of the e...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 639 instances
* *State Mutation (weighted view):* 1982
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1121`, `structural_boundaries: 574`, `args: 127`, `func_start: 61`, `class_start: 26`
* *Risk/State:* `state_mutation: 704`, `fragile_debt: 5`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 2`, `import: 10`
* *Defense:* `safety: 17`, `immutability_locks: 114`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.815
  * `Choke Point (Betweenness):` 4.9e-05 | `Ripple Effect (Closeness):` 0.007312
  * `Imports (Out-Degree: 25):` assemble.h, compiler.h, dbginfo.h, disp8.h, error.h, insns.h, listing.h, nasm.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `output/outelf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.81)
- **Top Global Matches:** file_cluster_6: 5.81, file_cluster_4: 12.265, file_cluster_8: 12.828
- **Magnitude:** 3085.28 | **LOC:** 3636 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.796; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `elf_deflabel` **(Many-Argument Workhorses)** (Impact: 208.6)
  * `elf_section_attrib` **(Many-Argument Workhorses)** (Impact: 187.4)
    * *Intent:* /* parse section attributes */
  * `elf64_out` **(Compute Cores)** (Impact: 156.8)
  * `elfx32_out` **(Compute Cores)** (Impact: 129.4)
  * `elf32_out` **(Compute Cores)** (Impact: 100.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 516 instances
* *State Mutation (weighted view):* 1739
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 619`, `structural_boundaries: 461`, `args: 108`, `func_start: 52`, `class_start: 54`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 707`, `fragile_debt: 4`
* *Architecture:* `api: 14`, `import: 17`
* *Defense:* `safety: 19`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.796
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` compiler.h, dwarf.h, elf.h, error.h, eval.h, hashtbl.h, nasm.h, nasmlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `output/outobj.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.607)
- **Top Global Matches:** file_cluster_6: 5.607, file_cluster_4: 9.694, file_cluster_8: 15.454
- **Magnitude:** 2756.14 | **LOC:** 2822 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.796; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.8%), Guard Balance (formerly Safety Score) (83.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `obj_deflabel` **(Many-Argument Workhorses)** (Impact: 169.6)
  * `obj_directive` **(Many-Argument Workhorses)** (Impact: 167.9)
  * `obj_segment` **(Many-Argument Workhorses)** (Impact: 149.9)
  * `obj_write_fixup` **(Many-Argument Workhorses)** (Impact: 145.1)
  * `obj_write_file` **(I/O & Config Routines)** (Impact: 104.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 511 instances
* *State Mutation (weighted view):* 1636
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 510`, `structural_boundaries: 300`, `args: 66`, `func_start: 43`, `class_start: 88`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 614`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 4`
* *Architecture:* `api: 8`, `import: 12`
* *Defense:* `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.796
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` asmutil.h, compiler.h, ctype.h, error.h, eval.h, nasm.h, nasmlib.h, nctype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `x86/insns.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.084)
- **Top Global Matches:** file_cluster_3: 9.084, file_cluster_8: 17.92, file_cluster_6: 30.527
- **Magnitude:** 2658.18 | **LOC:** 1672 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.796; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.0%), Guard Balance (formerly Safety Score) (86.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `byte_code_compile` **(Many-Argument Workhorses)** (Impact: 895.3)
    * *Intent:* # # The operands word lists the order of the operands: # # r = register field in the modr/m # m = mo...
  * `format_insn` **(Many-Argument Workhorses)** (Impact: 183.7)
  * `relaxed_forms` **(I/O & Config Routines)** (Impact: 52.5)
    * *Intent:* # Generate relaxed form patterns if applicable # * is used for an optional source operand, duplicati...
  * `decodify` **(Many-Argument Workhorses)** (Impact: 35.4)
    * *Intent:* # # Turn a code string into a sequence of bytes #
  * `startseq` **(Compute Cores)** (Impact: 32.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 430 instances
* *Memory Alloc (weighted view):* 23
* *State Mutation (weighted view):* 1290
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 694`, `structural_boundaries: 255`, `args: 24`, `func_start: 15`
* *Risk/State:* `state_mutation: 430`
* *Architecture:* `io: 8`, `api: 15`, `import: 3`
* *Defense:* `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.796
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bytecode, of, position
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `disasm/disasm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.18)
- **Top Global Matches:** file_cluster_8: 7.18, file_cluster_6: 11.238, file_cluster_4: 19.648
- **Magnitude:** 2464.66 | **LOC:** 1801 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 0.839; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.1%), Guard Balance (formerly Safety Score) (82.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `matches` **(Many-Argument Workhorses)** (Impact: 532.5)
    * *Intent:* * corresponds to the data stream in data and parse it into "ins" if * so. "ins" has already been par...
  * `disasm` **(Many-Argument Workhorses)** (Impact: 359.1)
  * `do_ea` **(Many-Argument Workhorses)** (Impact: 127.8)
    * *Intent:* /* * Process an effective address (ModRM) specification. */
  * `eatbyte` **(Many-Argument Workhorses)** (Impact: 93.3)
    * *Intent:* /* * This is called when we don't have a complete instruction. If it * is a standalone *single-byte*...
  * `append_evex_reg_deco` **(Stateful Encapsulated Methods)** (Impact: 21.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 397 instances
* *State Mutation (weighted view):* 1218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 474`, `structural_boundaries: 267`, `args: 49`, `func_start: 15`, `class_start: 14`
* *Risk/State:* `state_mutation: 424`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 46`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.839
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.001033
  * `Imports (Out-Degree: 15):` bytesex.h, compiler.h, disasm.h, disp8.h, insns.h, regdis.h, sync.h, tables.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `asm/nasm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.243)
- **Top Global Matches:** file_cluster_6: 6.243, file_cluster_8: 11.515, file_cluster_4: 13.438
- **Magnitude:** 2015.94 | **LOC:** 2170 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **20**; blast radius 1.061; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (75.9%), Guard Balance (formerly Safety Score) (75.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_arg` **(Many-Argument Workhorses)** (Impact: 329.7)
  * `help` **(Many-Argument Workhorses)** (Impact: 153.1)
  * `main` **(Many-Argument Workhorses)** (Impact: 94.1)
  * `assemble_file` **(Many-Argument Workhorses)** (Impact: 74.2)
  * `nasm_set_limit` **(Compute Cores)** (Impact: 48.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 302 instances
* *State Mutation (weighted view):* 932
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 503`, `structural_boundaries: 295`, `args: 83`, `func_start: 39`, `class_start: 20`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 328`, `unreferenced_by_name: 4`
* *Architecture:* `api: 16`, `import: 21`
* *Defense:* `safety: 11`, `immutability_locks: 58`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.061
  * `Choke Point (Betweenness):` 0.000629 | `Ripple Effect (Closeness):` 0.011301
  * `Imports (Out-Degree: 47):` assemble.h, compiler.h, error.h, eval.h, floats.h, iflag.h, insns.h, labels.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `asm/parser.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.997)
- **Top Global Matches:** file_cluster_3: 7.997, file_cluster_8: 17.128, file_cluster_6: 29.951
- **Magnitude:** 1837.22 | **LOC:** 1475 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.815; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.3%), Guard Balance (formerly Safety Score) (83.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_line` **(Many-Argument Workhorses)** (Impact: 480.0)
  * `parse_eops` **(Many-Argument Workhorses)** (Impact: 143.7)
    * *Intent:* /* * Parse an extended expression, used by db et al. "elem" is the element * size; initially comes f...
  * `parse_mref` **(Compute Cores)** (Impact: 55.3)
  * `process_size_override` **(Many-Argument Workhorses)** (Impact: 52.7)
  * `mref_set_optype` **(Stateful Encapsulated Methods)** (Impact: 34.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 292 instances
* *State Mutation (weighted view):* 902
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 436`, `structural_boundaries: 197`, `args: 53`, `func_start: 15`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 318`, `fragile_debt: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 3`, `import: 12`
* *Defense:* `safety: 2`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.815
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.007459
  * `Imports (Out-Degree: 22):` assemble.h, compiler.h, error.h, eval.h, floats.h, insns.h, nasm.h, nasmlib.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `output/outmacho.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.125)
- **Top Global Matches:** file_cluster_4: 7.125, file_cluster_6: 7.659, file_cluster_16: 13.681
- **Magnitude:** 1834.16 | **LOC:** 2530 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.796; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.3%), Complexity Load (formerly Cognitive Load) (70.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `macho_output` **(Compute Cores)** (Impact: 99.7)
  * `add_reloc` **(Many-Argument Workhorses)** (Impact: 90.5)
  * `macho_symdef` **(Many-Argument Workhorses)** (Impact: 79.9)
  * `macho_section` **(Many-Argument Workhorses)** (Impact: 68.4)
  * `macho_dbg_output` **(Many-Argument Workhorses)** (Impact: 39.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 328 instances
* *State Mutation (weighted view):* 1071
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 330`, `structural_boundaries: 302`, `args: 96`, `func_start: 41`, `class_start: 75`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 415`, `fragile_debt: 3`
* *Architecture:* `api: 11`, `import: 16`
* *Defense:* `safety: 6`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.796
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` compiler.h, dwarf.h, error.h, hashtbl.h, ilog2.h, labels.h, macho.h, nasm.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/rdsrc.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.063)
- **Top Global Matches:** file_cluster_8: 9.063, file_cluster_6: 11.706, file_cluster_4: 19.477
- **Magnitude:** 1662.1 | **LOC:** 1291 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.796; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.2%), Complexity Load (formerly Cognitive Load) (84.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_html` **(Compute Cores)** (Impact: 92.3)
  * `got_para` **(I/O & Config Routines)** (Impact: 49.8)
  * `write_txt` **(I/O & Config Routines)** (Impact: 45.8)
  * `word_html` **(Compute Cores)** (Impact: 40.7)
  * `word_txt` **(Compute Cores)** (Impact: 31.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 388 instances
* *Memory Alloc (weighted view):* 15
* *State Mutation (weighted view):* 1171
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 409`, `structural_boundaries: 194`, `args: 28`, `func_start: 27`
* *Risk/State:* `state_mutation: 395`, `planned_debt: 1`, `fragile_debt: 5`
* *Architecture:* `io: 8`, `api: 27`, `import: 1`
* *Defense:* `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.796
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Spec
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `output/outbin.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.799)
- **Top Global Matches:** file_cluster_6: 7.799, file_cluster_8: 9.745, file_cluster_4: 15.725
- **Magnitude:** 1589.06 | **LOC:** 1637 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.796; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.5%), Guard Balance (formerly Safety Score) (82.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bin_cleanup` **(I/O & Config Routines)** (Impact: 151.2)
  * `bin_assign_attributes` **(Many-Argument Workhorses)** (Impact: 114.0)
  * `bin_read_attribute` **(Many-Argument Workhorses)** (Impact: 92.2)
  * `bin_directive` **(Many-Argument Workhorses)** (Impact: 66.7)
  * `bin_out` **(Compute Cores)** (Impact: 47.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 303 instances
* *State Mutation (weighted view):* 949
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 348`, `structural_boundaries: 156`, `args: 32`, `func_start: 22`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 343`, `fragile_debt: 2`
* *Architecture:* `api: 1`, `import: 11`
* *Defense:* `safety: 1`, `immutability_locks: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.796
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` compiler.h, error.h, eval.h, labels.h, nasm.h, nasmlib.h, nctype.h, outform.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `output/outieee.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.03)
- **Top Global Matches:** file_cluster_6: 8.03, file_cluster_8: 9.517, file_cluster_4: 16.048
- **Magnitude:** 1439.2 | **LOC:** 1491 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.796; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ieee_write_fixup` **(Many-Argument Workhorses)** (Impact: 159.6)
    * *Intent:* /* * this routine is unalduterated bloatware. I usually don't do this * but I might as well see what...
  * `ieee_segment` **(Many-Argument Workhorses)** (Impact: 105.3)
    * *Intent:* /* * segment registry */
  * `ieee_write_file` **(I/O & Config Routines)** (Impact: 69.0)
  * `ieee_deflabel` **(Many-Argument Workhorses)** (Impact: 62.0)
    * *Intent:* /* * callback for labels */
  * `ieee_out` **(Compute Cores)** (Impact: 33.7)
    * *Intent:* /* * Put data out */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 245 instances
* *State Mutation (weighted view):* 789
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 294`, `structural_boundaries: 209`, `args: 40`, `func_start: 26`, `class_start: 59`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 299`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `api: 4`, `import: 11`
* *Defense:* `safety: 1`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.796
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` asmutil.h, compiler.h, ctype.h, error.h, nasm.h, nasmlib.h, nctype.h, outform.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `output/outcoff.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.751)
- **Top Global Matches:** file_cluster_6: 5.751, file_cluster_4: 12.469, file_cluster_8: 12.659
- **Magnitude:** 1207.7 | **LOC:** 1406 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 0.834; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `coff_section_names` **(Many-Argument Workhorses)** (Impact: 156.1)
  * `coff_out` **(Compute Cores)** (Impact: 87.2)
  * `coff_deflabel` **(Many-Argument Workhorses)** (Impact: 62.6)
  * `coff_directives` **(Many-Argument Workhorses)** (Impact: 52.1)
  * `coff_write` **(I/O & Config Routines)** (Impact: 28.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 195 instances
* *State Mutation (weighted view):* 621
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 120`, `args: 46`, `func_start: 26`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 231`, `fragile_debt: 1`
* *Architecture:* `api: 4`, `import: 14`
* *Defense:* `safety: 9`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.001033
  * `Imports (Out-Degree: 23):` compiler.h, error.h, eval.h, ilog2.h, nasm.h, nasmlib.h, nctype.h, outform.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `doc/genps.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.8)
- **Top Global Matches:** file_cluster_8: 7.8, file_cluster_6: 11.561, file_cluster_4: 19.693
- **Magnitude:** 1116.84 | **LOC:** 1311 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.796; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ps_flow_lines` **(Many-Argument Workhorses)** (Impact: 84.8)
  * `ps_break_pages` **(Compute Cores)** (Impact: 51.4)
    * *Intent:* # # This formats lines inside the global @pslines array into pages, # updating the page and y-coordi...
  * `ps_break_lines` **(Compute Cores)** (Impact: 47.5)
    * *Intent:* # # Break or convert paragraphs into lines, and push them # onto the @pslines array. #
  * `mkparaarray` **(Compute Cores)** (Impact: 44.0)
    * *Intent:* # element in the array contains (font, string), # where font can be one of: # -1 end link # -2 begin...
  * `ps_string` **(Compute Cores)** (Impact: 12.2)
    * *Intent:* # Generate a PostScript string
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 37 instances
* *Amplified Cascading Flux:* 259 instances
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 798
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 233`, `args: 27`, `func_start: 15`
* *Risk/State:* `state_mutation: 280`, `dead_code: 8`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 12`, `api: 15`, `import: 2`
* *Defense:* `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.796
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Spec, font
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/floats.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.432)
- **Top Global Matches:** file_cluster_8: 5.432, file_cluster_6: 14.717, file_cluster_3: 22.185
- **Magnitude:** 1042.04 | **LOC:** 903 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 0.906; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.9%), Complexity Load (formerly Cognitive Load) (81.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `float_const` **(Many-Argument Workhorses)** (Impact: 165.4)
  * `ieee_flconvert` **(Many-Argument Workhorses)** (Impact: 99.7)
    * *Intent:* /* * --------------------------------------------------------------------------- * convert * -------...
  * `ieee_flconvert_bin` **(Many-Argument Workhorses)** (Impact: 57.8)
    * *Intent:* /* Handle floating-point numbers with radix 2^bits and binary exponent */
  * `to_packed_bcd` **(Many-Argument Workhorses)** (Impact: 41.5)
  * `ieee_round` **(Stateful Encapsulated Methods)** (Impact: 32.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 172 instances
* *State Mutation (weighted view):* 535
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 101`, `args: 21`, `func_start: 13`, `class_start: 4`
* *Risk/State:* `state_mutation: 191`, `unreferenced_by_name: 3`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `safety: 2`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.906
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.008102
  * `Imports (Out-Degree: 7):` compiler.h, error.h, floats.h, nasm.h, nctype.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `asm/eval.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.002)
- **Top Global Matches:** file_cluster_6: 8.002, file_cluster_8: 10.19, file_cluster_4: 15.695
- **Magnitude:** 918.44 | **LOC:** 1041 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **10**; blast radius 1.066; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expr6` **(Compute Cores)** (Impact: 81.6)
  * `evaluate` **(Many-Argument Workhorses)** (Impact: 45.4)
  * `expr5` **(Compute Cores)** (Impact: 44.5)
  * `rexp3` **(Compute Cores)** (Impact: 44.1)
  * `add_vectors` **(Stateful Encapsulated Methods)** (Impact: 35.1)
    * *Intent:* /* * Add two vector datatypes. We have some bizarre behaviour on far- * absolute segment types: we p...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 143 instances
* *State Mutation (weighted view):* 436
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 322`, `structural_boundaries: 173`, `args: 51`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `state_mutation: 150`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 10`
* *Defense:* `safety: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.066
  * `Choke Point (Betweenness):` 9.3e-05 | `Ripple Effect (Closeness):` 0.011301
  * `Imports (Out-Degree: 17):` assemble.h, compiler.h, error.h, eval.h, floats.h, ilog2.h, labels.h, nasm.h...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `x86/preinsns.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.027)
- **Top Global Matches:** file_cluster_8: 8.027, file_cluster_6: 12.685, file_cluster_4: 20.867
- **Magnitude:** 900.52 | **LOC:** 669 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.796; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.1%), Guard Balance (formerly Safety Score) (83.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `func_multisize` **(Many-Argument Workhorses)** (Impact: 289.8)
  * `process_insn` **(Compute Cores)** (Impact: 29.4)
  * `substitute` **(Compute Cores)** (Impact: 27.7)
    * *Intent:* # # Substitute variables in a pattern #
  * `parse_args` **(Compute Cores)** (Impact: 27.4)
    * *Intent:* # # Macro helper functions for common constructs # # Parse arguments handling variable setting
  * `adjust_fl_zu` **(Many-Argument Workhorses)** (Impact: 23.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 143 instances
* *State Mutation (weighted view):* 430
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 300`, `structural_boundaries: 154`, `args: 24`, `func_start: 11`
* *Risk/State:* `state_mutation: 144`, `fragile_debt: 6`
* *Architecture:* `io: 2`, `api: 11`, `import: 3`
* *Defense:* `safety: 1`, `sync_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.796
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` integer, macro, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `output/outaout.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.594)
- **Top Global Matches:** file_cluster_6: 5.594, file_cluster_4: 11.994, file_cluster_8: 13.057
- **Magnitude:** 798.58 | **LOC:** 896 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.796; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `aout_deflabel` **(Many-Argument Workhorses)** (Impact: 157.6)
  * `aout_out` **(Compute Cores)** (Impact: 100.4)
  * `aout_add_gsym_reloc` **(Many-Argument Workhorses)** (Impact: 51.0)
    * *Intent:* * RELTYPE_GOT references require the _exact_ symbol address to be * used; RELTYPE_ABSOLUTE reference...
  * `aout_add_gotoff_reloc` **(C Struct Operations)** (Impact: 17.5)
    * *Intent:* /* * This routine deals with ..gotoff relocations. These _must_ refer * to a symbol, due to a perver...
  * `aout_fixup_relocs` **(C Struct Operations)** (Impact: 15.7)
    * *Intent:* /* * a.out files have the curious property that all references to * things in the data or bss sectio...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 109 instances
* *State Mutation (weighted view):* 377
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 96`, `args: 25`, `func_start: 16`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 159`
* *Architecture:* `api: 5`, `import: 11`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.796
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` compiler.h, error.h, eval.h, nasm.h, nasmlib.h, nctype.h, outform.h, outlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/quote.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.582)
- **Top Global Matches:** file_cluster_8: 8.582, file_cluster_3: 15.705, file_cluster_6: 20.848
- **Magnitude:** 750.76 | **LOC:** 571 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **5**; blast radius 0.919; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.7%), Guard Balance (formerly Safety Score) (86.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nasm_unquote_anystr` **(Many-Argument Workhorses)** (Impact: 155.1)
  * `nasm_quote` **(Many-Argument Workhorses)** (Impact: 100.5)
    * *Intent:* * quote.c */ #include "compiler.h" #include "nasmlib.h" #include "quote.h" #include "nctype.h" #incl...
  * `nasm_skip_string` **(Compute Cores)** (Impact: 31.7)
    * *Intent:* /* * Find the end of a quoted string; returns the pointer to the terminating * character (either the...
  * `emit_utf8` **(Many-Argument Workhorses)** (Impact: 13.1)
  * `nasm_quote_cstr` **(Defensive Guards)** (Impact: 3.9)
    * *Intent:* /* * Same as nasm_quote, but take the length of a C string; * the lenp argument is optional. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 139 instances
* *State Mutation (weighted view):* 424
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 59`, `args: 8`, `func_start: 8`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 146`, `unreferenced_by_name: 4`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 9`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.919
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.010079
  * `Imports (Out-Degree: 7):` compiler.h, error.h, nasmlib.h, nctype.h, quote.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `asm/directiv.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.786)
- **Top Global Matches:** file_cluster_8: 6.786, file_cluster_6: 17.531, file_cluster_3: 19.723
- **Magnitude:** 622.7 | **LOC:** 652 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 0.835; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_directives` **(Compute Cores)** (Impact: 192.9)
    * *Intent:* /* * Process a line from the assembler and try to handle it if it * is a directive. Return true if t...
  * `set_cpu` **(Compute Cores)** (Impact: 39.2)
  * `parse_directive_line` **(Many-Argument Workhorses)** (Impact: 27.6)
  * `get_bits` **(Stateful Encapsulated Methods)** (Impact: 12.7)
  * `directive_valid` **(Compute Cores)** (Impact: 10.6)
    * *Intent:* /* * Check to see if a string matches a valid directive name (sans [], * whitespace must be already ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 107 instances
* *State Mutation (weighted view):* 321
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 105`, `args: 8`, `func_start: 6`, `class_start: 7`
* *Risk/State:* `state_mutation: 107`, `fragile_debt: 2`
* *Architecture:* `api: 4`, `import: 16`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.835
  * `Choke Point (Betweenness):` 4.7e-05 | `Ripple Effect (Closeness):` 0.007769
  * `Imports (Out-Degree: 29):` assemble.h, compiler.h, error.h, eval.h, floats.h, iflag.h, ilog2.h, labels.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `travis/nasm-t.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.476)
- **Top Global Matches:** file_cluster_4: 7.476, file_cluster_6: 10.796, file_cluster_12: 11.63
- **Magnitude:** 614.28 | **LOC:** 599 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.796; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.7%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_run` **(Compute Cores)** (Impact: 54.0)
  * `test_update` **(Compute Cores)** (Impact: 28.5)
    * *Intent:* # # Compile sources and generate new targets
  * `prepare_desc` **(Many-Argument Workhorses)** (Impact: 26.1)
  * `hexdump` **(Compute Cores)** (Impact: 16.8)
  * `exec_nasm` **(Compute Cores)** (Impact: 15.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 111 instances
* *State Mutation (weighted view):* 352
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 92`, `args: 23`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 4`, `state_mutation: 130`, `fragile_debt: 2`
* *Architecture:* `io: 32`, `api: 22`, `import: 9`
* *Defense:* `safety: 5`, `test: 8`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.796
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` argparse, difflib, filecmp, fnmatch, json, os, re, subprocess...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/labels.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.416)
- **Top Global Matches:** file_cluster_6: 6.416, file_cluster_4: 8.003, file_cluster_16: 15.218
- **Magnitude:** 588.94 | **LOC:** 720 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **6**; blast radius 1.245; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.2%), Guard Balance (formerly Safety Score) (73.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `define_label` **(Many-Argument Workhorses)** (Impact: 72.8)
    * *Intent:* /* * The "normal" argument decides if we should update the local segment * base name or not. */
  * `declare_label_lptr` **(Many-Argument Workhorses)** (Impact: 50.6)
  * `out_symdef` **(Compute Cores)** (Impact: 30.3)
    * *Intent:* /* * Emit a symdef to the output and the debug format backends. */
  * `set_label_mangle` **(Compute Cores)** (Impact: 24.1)
    * *Intent:* /* * Set a prefix or suffix */
  * `mangle_label_name` **(Stateful Encapsulated Methods)** (Impact: 21.6)
    * *Intent:* /* * Format a label name with appropriate prefixes and suffixes */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 86 instances
* *State Mutation (weighted view):* 270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 124`, `args: 34`, `func_start: 21`, `class_start: 18`
* *Risk/State:* `state_mutation: 98`, `fragile_debt: 3`, `unreferenced_by_name: 6`
* *Architecture:* `api: 12`, `import: 6`
* *Defense:* `safety: 7`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.245
  * `Choke Point (Betweenness):` 0.000398 | `Ripple Effect (Closeness):` 0.014917
  * `Imports (Out-Degree: 14):` compiler.h, error.h, hashtbl.h, labels.h, nasm.h, nasmlib.h
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `misc/omfdump.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.252)
- **Top Global Matches:** file_cluster_16: 6.252, file_cluster_4: 7.956, file_cluster_15: 8.869
- **Magnitude:** 588.06 | **LOC:** 819 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.796; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.4%), Guard Balance (formerly Safety Score) (65.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dump_fixdat` **(Many-Argument Workhorses)** (Impact: 39.1)
    * *Intent:* /* helper routine used in fixup and modend dumps */
  * `dump_segdef` **(Stateful Encapsulated Methods)** (Impact: 33.6)
    * *Intent:* /* SEGDEF16 or SEGDEF32 */
  * `hexdump_data` **(Stateful Encapsulated Methods)** (Impact: 28.1)
  * `dump_pubdef` **(Stateful Encapsulated Methods)** (Impact: 26.7)
  * `dump_fixupp` **(Stateful Encapsulated Methods)** (Impact: 19.9)
    * *Intent:* /* FIXUPP16 or FIXUPP32 */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 85 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 260
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 77`, `args: 33`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 90`
* *Architecture:* `io: 3`, `api: 5`, `import: 3`
* *Defense:* `safety: 31`, `immutability_locks: 64`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.796
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bytesex.h, compiler.h, ctype.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `output/outas86.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.203)
- **Top Global Matches:** file_cluster_8: 8.203, file_cluster_3: 17.013, file_cluster_6: 19.936
- **Magnitude:** 560.36 | **LOC:** 580 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.796; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.8%), Guard Balance (formerly Safety Score) (76.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `as86_deflabel` **(Many-Argument Workhorses)** (Impact: 59.3)
  * `as86_write_section` **(Many-Argument Workhorses)** (Impact: 52.3)
  * `as86_out` **(Compute Cores)** (Impact: 49.5)
  * `as86_add_piece` **(C Struct Operations)** (Impact: 38.5)
  * `as86_write` **(I/O & Config Routines)** (Impact: 35.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 85 instances
* *State Mutation (weighted view):* 276
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 70`, `args: 18`, `func_start: 11`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 106`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 5`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.796
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` compiler.h, error.h, nasm.h, nasmlib.h, nctype.h, outform.h, outlib.h, raa.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `asm/strfunc.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 20.45)
- **Top Global Matches:** file_cluster_1: 20.45, file_cluster_3: 28.188, file_cluster_8: 49.916
- **Magnitude:** 511.52 | **LOC:** 330 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 0.881; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.7%), Guard Balance (formerly Safety Score) (84.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `utf8_to_16be` **(Many-Argument Workhorses)** (Impact: 57.7)
    * *Intent:* /* * Convert a string in UTF-8 format to UTF-16BE */
  * `utf8_to_16le` **(Many-Argument Workhorses)** (Impact: 57.3)
    * *Intent:* /* Copyright 1996-2009 The NASM Authors - All Rights Reserved */ /* * strfunc.c * * String transform...
  * `utf8_to_32be` **(Many-Argument Workhorses)** (Impact: 51.5)
    * *Intent:* /* * Convert a string in UTF-8 format to UTF-32BE */
  * `utf8_to_32le` **(Many-Argument Workhorses)** (Impact: 51.0)
    * *Intent:* /* * Convert a string in UTF-8 format to UTF-32LE */
  * `string_transform` **(Stateful Encapsulated Methods)** (Impact: 5.7)
    * *Intent:* /* * Apply a specific string transform and return it in a nasm_malloc'd * buffer, returning the leng...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 93 instances
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 24`, `args: 5`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 95`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 22`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.881
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007947
  * `Imports (Out-Degree: 3):` nasm.h, nasmlib.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `nasmlib/mmap.c` (C) | Magnitude: 61.46 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 39, pointers: 25, structural_boundaries: 23, core_var_decl: 15
- `nasmlib/md5c.c` (C) | Magnitude: 103.22 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 108, args: 70, pointers: 44, state_mutation: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `travis/test/apx-shifts.bin.t` (PERL) | Magnitude: 16.06 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 36, decorators: 24
- `travis/test/nasmformat-aout.out.t` (PERL) | Magnitude: 11.04 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 1, decorators: 1
- `travis/test/nasmformat-bin.out.t` (PERL) | Magnitude: 11.04 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 1, decorators: 1
- `travis/test/nasmformat-elf32.out.t` (PERL) | Magnitude: 11.04 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 1, decorators: 1
- `travis/test/nasmformat-elf64.out.t` (PERL) | Magnitude: 11.04 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 1, decorators: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `travis/test/loopoffs.asm` (ASSEMBLY) | Magnitude: 14.98 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 8, indent_tabs: 5, args: 4, func_start: 4
- `test/loopoffs.asm` (ASSEMBLY) | Magnitude: 14.98 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 8, indent_tabs: 5, args: 4, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `asm/exprdump.c` (C) | Magnitude: 29.24 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 30, branch: 14, structural_boundaries: 10, pointers: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `travis/test/xchg.asm` (ASSEMBLY) | Magnitude: 22.9 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: args: 159, indent_tabs: 140, structural_boundaries: 10, state_mutation: 5
- `test/xchg.asm` (ASSEMBLY) | Magnitude: 22.9 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: args: 159, indent_tabs: 140, structural_boundaries: 10, state_mutation: 5
- `travis/test/avx512-vp2intersect.asm` (ASSEMBLY) | Magnitude: 15.5 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: test: 17, pointers: 10, args: 8, macros: 2
- `test/br3392472.asm` (ASSEMBLY) | Magnitude: 1.32 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, macros: 2, func_start: 1
- `nasmlib/zerobuf.c` (C) | Magnitude: 11.56 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: import: 2, globals: 1, immutability_locks: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `travis/test/avx512cd.asm` (ASSEMBLY) | Magnitude: 16.86 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: test: 85, pointers: 66, args: 60, reflection_metaprogramming: 6
- `test/avx512cd.asm` (ASSEMBLY) | Magnitude: 16.86 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: test: 85, pointers: 66, args: 60, reflection_metaprogramming: 6
- `test/memleak.asm` (ASSEMBLY) | Magnitude: 16.34 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 11, args: 11, comprehensions: 5
- `test/ccmp2.asm` (ASSEMBLY) | Magnitude: 15.2 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 8, args: 6, immutability_locks: 2
- `travis/test/a32offs.asm` (ASSEMBLY) | Magnitude: 10.02 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 4, func_start: 4, unreferenced_by_name: 4, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `autogen.sh` (SHELL) | Magnitude: 57.14 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 38, indent_spaces: 19, io: 17, branch: 15
- `test/nasm` (SHELL) | Magnitude: 42.4 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 17, indent_spaces: 14, state_mutation: 10, io: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `asm/preproc.c` -> Churn: **100.0%** | Cog Load: 94.6526% | Debt: 13.4109%
- `asm/nasm.c` -> Churn: **75.87%** | Cog Load: 94.3342% | Debt: 9.3833%
- `nasmlib/file.c` -> Churn: **69.86%** | Cog Load: 80.9816% | Debt: 72.507%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `asm/preproc.c` -> **H. Peter Anvin (Intel)** (100.0% isolated ownership) | Magnitude: 8336.78
- `asm/assemble.c` -> **H. Peter Anvin (Intel)** (100.0% isolated ownership) | Magnitude: 4319.52
- `output/outelf.c` -> **bonsthie** (100.0% isolated ownership) | Magnitude: 3085.28
- `x86/insns.pl` -> **H. Peter Anvin (Intel)** (100.0% isolated ownership) | Magnitude: 2658.18
- `disasm/disasm.c` -> **RMarx1456** (100.0% isolated ownership) | Magnitude: 2464.66

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `asm/nasm.c` -> **Severity: 0.063** (Bridge: 0.0006 * Flux: 100.0%)
- `asm/labels.c` -> **Severity: 0.04** (Bridge: 0.0004 * Flux: 100.0%)
- `asm/preproc.c` -> **Severity: 0.023** (Bridge: 0.0002 * Flux: 100.0%)
- `asm/error.c` -> **Severity: 0.012** (Bridge: 0.0001 * Flux: 99.9999%)
- `nasmlib/alloc.c` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `include/compiler.h` -> **Severity: 4.327** (Embedded: 0.0947 * Error Risk: 45.6952%)
- `include/nasmlib.h` -> **Severity: 3.128** (Embedded: 0.0658 * Error Risk: 47.5295%)
- `include/nasm.h` -> **Severity: 2.36** (Embedded: 0.0461 * Error Risk: 51.1626%)
- `nasmlib/alloc.c` -> **Severity: 2.351** (Embedded: 0.0347 * Error Risk: 67.6936%)
- `include/bytesex.h` -> **Severity: 2.102** (Embedded: 0.0402 * Error Risk: 52.2781%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `include/compiler.h` -> **Severity: 6069.5** (Blast Radius: 60.695 * Doc Risk: 100.0%)
- `include/nasmlib.h` -> **Severity: 1724.8** (Blast Radius: 17.248 * Doc Risk: 100.0%)
- `include/nasm.h` -> **Severity: 962.4** (Blast Radius: 9.624 * Doc Risk: 100.0%)
- `include/bytesex.h` -> **Severity: 895.3** (Blast Radius: 8.953 * Doc Risk: 100.0%)
- `autoconf/m4/pa_add_flags.m4` -> **Severity: 611.4** (Blast Radius: 6.114 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 1363 literal sites + 18 sites through wrappers = 1381
- **`memory_alloc`:** 158 literal sites + 421 sites through wrappers = 579
- **`panics_and_aborts`:** 340 literal sites + 5 sites through wrappers = 345

- `nasm_free` (function, memory_alloc, primitive): 228 call sites in 29 files -- `nasmlib/alloc.c`
- `saa_free` (function, memory_alloc, via nasm_free): 45 call sites in 9 files -- `nasmlib/saa.c`
- `addtotemp` (function, memory_alloc, via nasm_realloc): 19 call sites in 1 files -- `asm/eval.c`
- `unknown_expr` (function, memory_alloc, via addtotemp): 19 call sites in 1 files -- `asm/eval.c`
- `scalarvect` (function, memory_alloc, via addtotemp): 18 call sites in 1 files -- `asm/eval.c`
- `stdscan_reset` (function, memory_alloc, via stdscan_pop): 15 call sites in 8 files -- `asm/stdscan.c`
- `nasm_realloc` (function, memory_alloc, primitive): 14 call sites in 9 files -- `nasmlib/alloc.c`
- `test_fail` (function, debug_prints, primitive): 10 call sites in 1 files -- `travis/nasm-t.py`
- `finishtemp` (function, memory_alloc, via addtotemp): 9 call sites in 1 files -- `asm/eval.c`
- `hash_free` (function, memory_alloc, via nasm_free): 9 call sites in 8 files -- `nasmlib/hashtbl.c`
- `nasm_delete` (macro, memory_alloc, via nasm_free): 6 call sites in 1 files -- `include/nasmlib.h`
- `xmalloc` (function, memory_alloc, primitive): 4 call sites in 1 files -- `misc/omfdump.c`
*(+30 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 5813 call pairs -- scoped 33.6%, unique 23.2%, ambiguous 0.6%, external 42.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 4596 | 39.6% | 28.5% | 0.3% | 31.6% |
| perl | 638 | 14.1% | 0.0% | 3.0% | 82.9% |
| m4 | 281 | 1.4% | 13.2% | 0.0% | 85.4% |
| python | 132 | 25.0% | 0.0% | 0.0% | 75.0% |
| shell | 100 | 9.0% | 0.0% | 0.0% | 91.0% |
| livecode | 51 | 0.0% | 0.0% | 0.0% | 100.0% |
| assembly | 14 | 0.0% | 0.0% | 0.0% | 100.0% |
| easytrieve | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
