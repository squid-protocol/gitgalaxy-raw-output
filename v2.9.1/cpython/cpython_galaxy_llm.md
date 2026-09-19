# ARCHITECTURAL_BRIEF: cpython
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/python/cpython` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1675 analyzed artifact(s), 645574 LOC.
- **Load-bearing artifact:** `Include/Python.h` -- 318 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Include/Python.h` -- pulls in 94 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Objects/unicodeobject.c` at magnitude 12157.8 (structural weight, not risk).
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
| Total Artifacts | 5595 |
| Analyzed Artifacts (Scanned) | 1675 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3920 |
| Total LOC | 645574 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 29.9% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5796 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1763 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.4925 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 105 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 1061 | 573897 | 63.3% |
| PYTHON | 265 | 46273 | 15.8% |
| XML | 78 | 8 | 4.7% |
| PLAINTEXT | 57 | 0 | 3.4% |
| MARKDOWN | 51 | 0 | 3.0% |
| SHELL | 49 | 1262 | 2.9% |
| BATCH | 27 | 1605 | 1.6% |
| OBJECTIVE-C | 16 | 906 | 1.0% |
| HTML | 11 | 4014 | 0.7% |
| MAKEFILE | 9 | 3351 | 0.5% |
| YAML | 9 | 340 | 0.5% |
| JAVASCRIPT | 7 | 1366 | 0.4% |
| JSON | 7 | 282 | 0.4% |
| CPP | 7 | 3620 | 0.4% |
| POWERSHELL | 6 | 249 | 0.4% |
| M4 | 5 | 6743 | 0.3% |
| KOTLIN | 3 | 112 | 0.2% |
| CSV | 3 | 995 | 0.2% |
| CSS | 2 | 488 | 0.1% |
| ASSEMBLY | 2 | 63 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `4.705`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +4.71; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 26%, Encapsulated Accessors Files 21%, Data / Markup / Trivial 18%, Large Core Modules (3) 12%, Many-Argument Workhorses Files 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1559 | 93.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 108 | 6.4% |
| Static: Minified & Vendor Opaque Mass | 8 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3920*

**Composition by Extension & Reason:**
- `.py`: 2001x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 56 LOC), 1x Excluded (Machine-Generated Source Code Signature: 2475 LOC)
- `.rst`: 396x Excluded (Unsupported Extension: '.rst'), 391x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dectest`: 143x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 113x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 72547 LOC exceeds safe regex boundaries), 1x Excluded (Embedded Hex Payload: 14899 hex tokens in 7516 LOC)
- `.toml`: 71x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Unsupported Format (.toml), 5x Excluded (Unsupported Extension: '.toml')
- `.xml`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars), 1x Excluded (Monolithic Amalgamation: 30918 LOC exceeds safe regex boundaries)
- `.vcxproj`: 54x Excluded (Unsupported Extension: '.vcxproj'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.vcxproj)
- `.png`: 54x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 27x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 17x Unsupported Format (.undeterminable), 3x Excluded (Binary Format Detected)
- `.filters`: 51x Excluded (Unsupported Extension: '.filters'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wxs`: 44x Unsupported Format (.wxs)
- `.h`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 113 LOC), 1x Excluded (Machine-Generated Source Code Signature: 949 LOC)
- `.yml`: 35x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wixproj`: 30x Unsupported Format (.wixproj)
- `.json`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 2435 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.0 | 31.1 | 23.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 55.7 | 72.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 16.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 25.1 | 2.3 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 16.4 | 3.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 53.4 | 83.2 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 70.0 | 1.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.4 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 7.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 54.7 | 50.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 161858 | 1139 | 255 | `Modules/expat/xmlparse.c` |
| cleanup | 427 | 111 | 0 | `Makefile.pre.in` |
| guards | 50926 | 1072 | 81 | `Modules/clinic/posixmodule.c.h` |
| danger | 21878 | 964 | 33 | `Modules/clinic/posixmodule.c.h` |
| concurrency | 1206 | 131 | 0 | `Include/cpython/pyatomic_std.h` |
| connectivity | 14928 | 1160 | 22 | `Modules/_decimal/libmpdec/mpdecimal.h` |
| io | 1823 | 271 | 2 | `Tools/freeze/freeze.py` |
| crypto | 6 | 4 | 0 | `Tools/ssl/multissltests.py` |
| ipc | 398 | 66 | 0 | `Modules/socketmodule.c` |
| time | 197 | 34 | 0 | `Modules/timemodule.c` |
| serialization | 34 | 13 | 0 | `Makefile.pre.in` |
| regex | 193 | 78 | 0 | `Tools/jit/_optimizers.py` |
| events | 1953 | 137 | 0 | `configure.ac` |
| tests | 172 | 17 | 0 | `Objects/dictobject.c` |
| docs | 1655 | 312 | 2 | `Tools/gdb/libpython.py` |
| debt | 2892 | 431 | 4 | `Tools/peg_generator/pegen/c_generator.py` |
| mutation | 131575 | 1074 | 223 | `Objects/unicodeobject.c` |
| dead_code | 4886 | 607 | 7 | `Modules/_testclinic.c` |
| credential | 26 | 15 | 0 | `Tools/jit/_optimizers.py` |
| threat | 14862 | 699 | 22 | `Modules/clinic/posixmodule.c.h` |
| ml_ai | 1105 | 121 | 0 | `Modules/_decimal/libmpdec/mpdecimal.c` |
| ui | 276 | 26 | 0 | `Doc/_static/tachyon-example-heatmap.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Tools/freeze/freeze.py` (Hits: 56)
- `Tools/ssl/multissltests.py` (Hits: 48)
- `Makefile.pre.in` (Hits: 44)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Python.h** (`Include/Python.h`) — 318 inbound connections
2. **pycore_modsupport.h** (`Include/internal/pycore_modsupport.h`) — 177 inbound connections
3. **pycore_runtime.h** (`Include/internal/pycore_runtime.h`) — 149 inbound connections
4. **pycore_gc.h** (`Include/internal/pycore_gc.h`) — 113 inbound connections
5. **sys.c** (`Modules/_testlimitedcapi/sys.c`) — 105 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Python.h** (`Include/Python.h`) — 94 outbound dependencies
2. **pylifecycle.c** (`Python/pylifecycle.c`) — 51 outbound dependencies
3. **compiler.md** (`InternalDocs/compiler.md`) — 49 outbound dependencies
4. **ceval.h** (`Python/ceval.h`) — 47 outbound dependencies
5. **unicodeobject.c** (`Objects/unicodeobject.c`) — 41 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `doProlog` **(Many-Argument Workhorses)** (@ `Modules/expat/xmlparse.c`) -> Impact: **1105.1** | LOC: 1075
- `sock_initobj_impl` **(Many-Argument Workhorses)** (@ `Modules/socketmodule.c`) -> Impact: **930.1** | LOC: 2044
- `_socket_socket_sendmsg_impl` **(Many-Argument Workhorses)** (@ `Modules/socketmodule.c`) -> Impact: **889.3** | LOC: 2012
- `parserCreate` **(Many-Argument Workhorses)** (@ `Modules/expat/xmlparse.c`) -> Impact: **852.0** | LOC: 1707
- `tok_get_normal_mode` **(Many-Argument Workhorses)** (@ `Parser/lexer/lexer.c`) -> Impact: **656.5** | LOC: 891
- `convertsimple` **(Many-Argument Workhorses)** (@ `Python/getargs.c`) -> Impact: **531.4** | LOC: 671
  * *Intent:* */
- `_Py_CheckRecursiveCall` **(Many-Argument Workhorses)** (@ `Python/ceval.c`) -> Impact: **522.1** | LOC: 1677
  * *Intent:* /* The function _Py_EnterRecursiveCallTstate() only calls _Py_CheckRecursiveCall() if the stack pointer is between the stack base and c_stack_hard_lim...
- `_io_FileIO___init___impl` **(Many-Argument Workhorses)** (@ `Modules/_io/fileio.c`) -> Impact: **508.2** | LOC: 1100
- `_Py_dg_dtoa` **(Many-Argument Workhorses)** (@ `Python/dtoa.c`) -> Impact: **504.0** | LOC: 609
  * *Intent:* call to _Py_dg_freedtoa. */
- `doContent` **(Many-Argument Workhorses)** (@ `Modules/expat/xmlparse.c`) -> Impact: **501.1** | LOC: 482

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Modules` | 112 | 84839.52 | 41.11% | 38.24% |
| `Python` | 110 | 79623.74 | 45.36% | 35.12% |
| `Objects` | 52 | 70491.2 | 45.37% | 31.69% |
| `Modules/clinic` | 79 | 35130.54 | 47.12% | 0.47% |
| `Modules/expat` | 23 | 13929.22 | 24.34% | 11.22% |
| `Modules/_decimal/libmpdec` | 35 | 13899.7 | 34.56% | 25.14% |
| `Modules/_hacl` | 30 | 9939.82 | 21.45% | 6.55% |
| `Modules/_io` | 9 | 7694.08 | 69.29% | 45.59% |
| `Modules/_ctypes` | 7 | 7353.28 | 60.43% | 34.26% |
| `PC` | 28 | 7149.0 | 31.67% | 23.83% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Include/internal/pycore_pyarena.h` -> **100.0%** Exposure
- `Include/internal/pycore_traceback.h` -> **100.0%** Exposure
- `Modules/tkappinit.c` -> **100.0%** Exposure
- `Python/dynamic_annotations.c` -> **100.0%** Exposure
- `Modules/_testclinic.c` -> **99.9999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Android/android-env.sh` -> **100.0%** Exposure
- `Mac/BuildScript/resources/update_shell_profile.command` -> **100.0%** Exposure
- `Mac/BuildScript/scripts/postflight.patch-profile` -> **100.0%** Exposure
- `Misc/python-config.sh.in` -> **100.0%** Exposure
- `Modules/makesetup` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Modules/_testclinic.c` -> **110** Orphaned Functions | **0** Duplicates
- `Modules/_decimal/libmpdec/mpsignal.c` -> **105** Orphaned Functions | **0** Duplicates
- `Modules/_ssl.c` -> **94** Orphaned Functions | **0** Duplicates
- `Modules/_cursesmodule.c` -> **89** Orphaned Functions | **0** Duplicates
- `Python/import.c` -> **75** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `62` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6289` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Objects/unicodeobject.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 12157.8 | **LOC:** 14992 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 53.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **41**; blast radius 0.34; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unicode_fromformat_arg` **(Many-Argument Workhorses)** (Impact: 284.7)
    * *Intent:* #define F_LONG 1 #define F_LONGLONG 2 #define F_SIZE 3 #define F_PTRDIFF 4 #define F_INTMAX 5
  * `_PyUnicode_DecodeUnicodeEscapeInternal2` **(Many-Argument Workhorses)** (Impact: 205.6)
    * *Intent:* /* --- Unicode Escape Codec ----------------------------------------------- */
  * `replace` **(Many-Argument Workhorses)** (Impact: 157.0)
  * `PyUnicode_DecodeUTF7Stateful` **(Many-Argument Workhorses)** (Impact: 123.8)
    * *Intent:* /* The decoder. The only state we preserve is our read position, * i.e. how many characters we have ...
  * `charmap_encoding_error` **(Many-Argument Workhorses)** (Impact: 108.2)
    * *Intent:* /* handle an error in _PyUnicode_EncodeCharmap() Return 0 on success, -1 on error */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1610 instances
* *State Mutation (weighted view):* 4935
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2669`, `structural_boundaries: 1463`, `args: 747`, `func_start: 354`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 108`, `state_mutation: 1715`, `dead_code: 8`, `planned_debt: 2`, `fragile_debt: 6`
* *Architecture:* `api: 275`, `import: 77`
* *Defense:* `safety: 296`, `doc: 1`, `immutability_locks: 479`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.34
  * `Choke Point (Betweenness):` 2.7e-05 | `Ripple Effect (Closeness):` 0.000796
  * `Imports (Out-Degree: 38):` Python.h, unicodeobject.c.h, pycore_abstract.h, pycore_bytes_methods.h, pycore_bytesobject.h, pycore_ceval.h, pycore_codecs.h, pycore_critical_section.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Modules/expat/xmlparse.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 9987.94 | **LOC:** 9225 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.2%), Guard Balance (formerly Safety Score) (94.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `doProlog` **(Many-Argument Workhorses)** (Impact: 1105.1)
  * `parserCreate` **(Many-Argument Workhorses)** (Impact: 852.0)
  * `doContent` **(Many-Argument Workhorses)** (Impact: 501.1)
  * `unsignedCharToPrintable` **(Compute Cores)** (Impact: 393.8)
    * *Intent:* #if XML_GE == 1
  * `storeAtts` **(Many-Argument Workhorses)** (Impact: 298.5)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1115 instances
* *State Mutation (weighted view):* 3595
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2135`, `structural_boundaries: 1413`, `args: 333`, `func_start: 176`, `class_start: 103`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 1365`, `dead_code: 15`, `fragile_debt: 4`, `unreferenced_by_name: 70`
* *Architecture:* `io: 2`, `api: 103`, `import: 25`
* *Defense:* `safety: 118`, `immutability_locks: 524`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` ascii.h, assert.h, errno.h, expat.h, expat_config.h, fcntl.h, internal.h, limits.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Objects/typeobject.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 7294.5 | **LOC:** 12874 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 27.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **30**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (81.5%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PyType_FromMetaclass` **(Many-Argument Workhorses)** (Impact: 198.0)
  * `update_one_slot` **(Many-Argument Workhorses)** (Impact: 101.5)
    * *Intent:* * There are some further special cases for specific slots, like supporting * __hash__ = None for tp_...
  * `inherit_slots` **(Many-Argument Workhorses)** (Impact: 77.3)
  * `subtype_dealloc` **(Many-Argument Workhorses)** (Impact: 52.2)
  * `object_getstate_default` **(Many-Argument Workhorses)** (Impact: 51.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 783 instances
* *State Mutation (weighted view):* 2474
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1866`, `structural_boundaries: 1311`, `args: 847`, `func_start: 418`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 193`, `state_mutation: 908`, `dead_code: 9`, `planned_debt: 4`, `fragile_debt: 15`, `unreferenced_by_name: 60`
* *Architecture:* `api: 96`, `import: 30`
* *Defense:* `safety: 280`, `doc: 1`, `test: 32`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` Python.h, typeobject.c.h, opcode.h, pycore_abstract.h, pycore_call.h, pycore_cell.h, pycore_code.h, pycore_descrobject.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/_decimal/libmpdec/mpdecimal.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 7242.28 | **LOC:** 9016 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.2%)
- **Documentation Coverage:** 48.1848% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_mpd_qdivmod` **(Many-Argument Workhorses)** (Impact: 94.4)
    * *Intent:* /* Internal function. */
  * `_mpd_qdiv` **(Many-Argument Workhorses)** (Impact: 90.7)
    * *Intent:* /* Divide a by b. */
  * `mpd_qpowmod` **(Many-Argument Workhorses)** (Impact: 85.9)
    * *Intent:* /* The powmod function: (base**exp) % mod */
  * `mpd_qpow` **(Many-Argument Workhorses)** (Impact: 83.0)
    * *Intent:* /* The power function: base**exp */
  * `_mpd_base_ndivmod` **(Many-Argument Workhorses)** (Impact: 69.6)
    * *Intent:* * Internal function for large numbers: * * q, r = divmod(coeff(a), coeff(b)) * * Strategy: Multiply ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 917 instances
* *High Risk Execution (weighted view):* 8
* *State Mutation (weighted view):* 2898
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1364`, `structural_boundaries: 738`, `args: 367`, `func_start: 304`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 12`, `state_mutation: 1064`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 73`
* *Architecture:* `api: 198`, `import: 16`
* *Defense:* `safety: 115`, `doc: 32`, `immutability_locks: 454`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` assert.h, basearith.h, bits.h, constants.h, convolute.h, crt.h, fenv.h, float.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/socketmodule.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 6191.94 | **LOC:** 9359 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 18.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.8%), Complexity Load (formerly Cognitive Load) (72.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sock_initobj_impl` **(Many-Argument Workhorses)** (Impact: 930.1)
  * `_socket_socket_sendmsg_impl` **(Many-Argument Workhorses)** (Impact: 889.3)
  * `getsockaddrarg` **(Many-Argument Workhorses)** (Impact: 418.3)
    * *Intent:* through len_ret. */
  * `makesockaddr` **(Many-Argument Workhorses)** (Impact: 164.9)
    * *Intent:* to determine what kind of address it really is. */ /*ARGSUSED*/
  * `socket_exec` **(Many-Argument Workhorses)** (Impact: 124.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 546 instances
* *State Mutation (weighted view):* 1735
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1188`, `structural_boundaries: 814`, `args: 498`, `func_start: 128`, `class_start: 111`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 643`, `dead_code: 7`, `fragile_debt: 6`, `unreferenced_by_name: 14`
* *Architecture:* `io: 23`, `api: 36`, `import: 39`
* *Defense:* `safety: 63`, `doc: 1`, `immutability_locks: 38`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` AvailabilityMacros.h, Python.h, Rpc.h, addrinfo.h, inet.h, socketmodule.c.h, fcntl.h, getaddrinfo.c...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/clinic/posixmodule.c.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 6011.66 | **LOC:** 13615 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 14.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.1%), Complexity Load (formerly Cognitive Load) (48.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `os_posix_spawn` **(Many-Argument Workhorses)** (Impact: 54.6)
  * `os_posix_spawnp` **(Many-Argument Workhorses)** (Impact: 54.6)
  * `os_sendfile` **(Many-Argument Workhorses)** (Impact: 54.1)
  * `os_timerfd_settime` **(Stateful Encapsulated Methods)** (Impact: 53.7)
  * `os_startfile` **(Many-Argument Workhorses)** (Impact: 52.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 681 instances
* *State Mutation (weighted view):* 2176
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1607`, `structural_boundaries: 359`, `args: 932`, `func_start: 229`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 12`, `state_mutation: 814`, `unreferenced_by_name: 1`
* *Architecture:* `io: 12`, `import: 5`
* *Defense:* `safety: 7`, `immutability_locks: 358`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` pycore_abstract.h, pycore_gc.h, pycore_long.h, pycore_modsupport.h, pycore_runtime.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Objects/longobject.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5648.12 | **LOC:** 6969 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 0.34; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `long_format_binary` **(Many-Argument Workhorses)** (Impact: 161.0)
    * *Intent:* if alternate is nonzero. */
  * `PyLong_AsNativeBytes` **(Many-Argument Workhorses)** (Impact: 159.0)
  * `long_pow` **(Many-Argument Workhorses)** (Impact: 140.0)
    * *Intent:* /* pow(v, w, x) */
  * `_PyLong_AsByteArray` **(Many-Argument Workhorses)** (Impact: 89.4)
  * `PyLong_FromString` **(Many-Argument Workhorses)** (Impact: 89.2)
    * *Intent:* /* Parses an int from a bytestring. Leading and trailing whitespace will be * ignored. * * If succes...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 933 instances
* *State Mutation (weighted view):* 2855
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1091`, `structural_boundaries: 478`, `args: 338`, `func_start: 170`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 222`, `state_mutation: 989`, `dead_code: 14`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `api: 115`, `import: 15`
* *Defense:* `safety: 203`, `doc: 2`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.34
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.000796
  * `Imports (Out-Degree: 13):` Python.h, longobject.c.h, float.h, pycore_bitutils.h, pycore_call.h, pycore_freelist.h, pycore_initconfig.h, pycore_long.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Modules/_pickle.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5527.5 | **LOC:** 8277 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.5%)
- **Documentation Coverage:** 99.2806% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `save_reduce` **(Many-Argument Workhorses)** (Impact: 187.5)
    * *Intent:* /* We're saving obj, and args is the 2-thru-5 tuple returned by the * appropriate __reduce__ method ...
  * `save` **(Many-Argument Workhorses)** (Impact: 145.2)
  * `save_global` **(Many-Argument Workhorses)** (Impact: 141.2)
  * `batch_dict` **(Many-Argument Workhorses)** (Impact: 82.9)
    * *Intent:* /* iter is an iterator giving (key, value) pairs, and we batch up chunks of * MARK key value ... key...
  * `save_long` **(Many-Argument Workhorses)** (Impact: 68.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 724 instances
* *State Mutation (weighted view):* 2239
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1263`, `structural_boundaries: 808`, `args: 400`, `func_start: 208`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 791`, `dead_code: 1`, `planned_debt: 6`, `fragile_debt: 12`, `unreferenced_by_name: 18`
* *Architecture:* `io: 1`, `api: 10`, `import: 16`
* *Defense:* `safety: 102`, `doc: 6`, `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` Python.h, _pickle.c.h, pycore_bytesobject.h, pycore_ceval.h, pycore_critical_section.h, pycore_long.h, pycore_moduleobject.h, pycore_object.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Objects/dictobject.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 5388.06 | **LOC:** 8326 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 55.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.1%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.0%)
- **Documentation Coverage:** 49.5807% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dictiter_iternextitem` **(Stateful Encapsulated Methods)** (Impact: 440.9)
  * `_PyDict_FromKeys` **(Many-Argument Workhorses)** (Impact: 74.8)
    * *Intent:* /* Internal version of dict.from_keys(). It is subclass-friendly. */
  * `dict_setdefault_ref_lock_held` **(Many-Argument Workhorses)** (Impact: 73.6)
  * `dictresize` **(Many-Argument Workhorses)** (Impact: 63.5)
    * *Intent:* */
  * `store_instance_attr_lock_held` **(Many-Argument Workhorses)** (Impact: 56.3)
    * *Intent:* // Called with either the object's lock or the dict's lock held // depending on whether or not a dic...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 579 instances
* *State Mutation (weighted view):* 1801
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1108`, `structural_boundaries: 708`, `args: 466`, `func_start: 282`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 161`, `state_mutation: 643`, `dead_code: 5`, `planned_debt: 5`, `fragile_debt: 4`, `unreferenced_by_name: 70`
* *Architecture:* `api: 97`, `import: 19`
* *Defense:* `safety: 278`, `doc: 5`, `test: 60`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` Python.h, dictobject.c.h, pycore_bitutils.h, pycore_call.h, pycore_ceval.h, pycore_code.h, pycore_critical_section.h, pycore_dict.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/_ssl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4430.3 | **LOC:** 7422 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 26.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fill_and_set_sslerror` **(Many-Argument Workhorses)** (Impact: 135.0)
  * `_get_peer_alt_names` **(Many-Argument Workhorses)** (Impact: 110.0)
  * `newPySSLSocket` **(Many-Argument Workhorses)** (Impact: 97.1)
  * `_ssl__SSLContext_impl` **(Many-Argument Workhorses)** (Impact: 86.2)
  * `_ssl__SSLSocket_read_impl` **(Many-Argument Workhorses)** (Impact: 84.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 592 instances
* *State Mutation (weighted view):* 1825
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1056`, `structural_boundaries: 540`, `args: 435`, `func_start: 159`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 641`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 5`, `unreferenced_by_name: 94`
* *Architecture:* `io: 1`, `api: 21`, `import: 28`
* *Defense:* `safety: 32`, `immutability_locks: 85`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` Python.h, _ssl.h, cert.c, debughelpers.c, misc.c, _ssl_data_111.h, _ssl_data_300.h, _ssl_data_340.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Python/ceval.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4160.18 | **LOC:** 3840 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 14.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 0.392; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.7%), Complexity Load (formerly Cognitive Load) (83.3%), Guard Balance (formerly Safety Score) (81.7%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_Py_CheckRecursiveCall` **(Many-Argument Workhorses)** (Impact: 522.1)
    * *Intent:* /* The function _Py_EnterRecursiveCallTstate() only calls _Py_CheckRecursiveCall() if the stack poin...
  * `_Py_ReachedRecursionLimitWithMargin` **(Many-Argument Workhorses)** (Impact: 491.9)
  * `_Py_EnterRecursiveCallUnchecked` **(Many-Argument Workhorses)** (Impact: 419.3)
  * `initialize_locals` **(Many-Argument Workhorses)** (Impact: 179.1)
  * `_PyEval_ImportFrom` **(Many-Argument Workhorses)** (Impact: 88.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 273 instances
* *State Mutation (weighted view):* 880
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 606`, `structural_boundaries: 328`, `args: 207`, `func_start: 115`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 42`, `high_risk_execution: 2`, `state_mutation: 334`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 3`
* *Architecture:* `api: 173`, `import: 9`
* *Defense:* `safety: 100`, `doc: 5`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.392
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.002937
  * `Imports (Out-Degree: 3):` ceval.h, ceval_macros.h, stack.h, executor_cases.c.h, generated_cases.c.h, opcode_targets.h, pycore_long.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Modules/_datetimemodule.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4125.4 | **LOC:** 7910 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wrap_strftime` **(Many-Argument Workhorses)** (Impact: 123.2)
    * *Intent:* /* I sure don't want to reproduce the strftime code from the time module, * so this imports the modu...
  * `datetime_richcompare` **(Many-Argument Workhorses)** (Impact: 62.0)
  * `parse_hh_mm_ss_ff` **(Many-Argument Workhorses)** (Impact: 56.5)
  * `parse_isoformat_time` **(Many-Argument Workhorses)** (Impact: 54.5)
  * `delta_new_impl` **(Many-Argument Workhorses)** (Impact: 50.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 486 instances
* *State Mutation (weighted view):* 1497
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 920`, `structural_boundaries: 617`, `args: 461`, `func_start: 249`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 104`, `state_mutation: 525`, `dead_code: 5`, `planned_debt: 2`, `fragile_debt: 6`, `unreferenced_by_name: 35`
* *Architecture:* `api: 7`, `import: 11`
* *Defense:* `safety: 102`, `immutability_locks: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` Python.h, _datetimemodule.c.h, datetime.h, pycore_initconfig.h, pycore_long.h, pycore_object.h, pycore_pyatomic_ft_wrappers.h, pycore_time.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Python/codegen.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3912.06 | **LOC:** 6641 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 0.32; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.2%)
- **Documentation Coverage:** 49.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `codegen_sync_comprehension_generator` **(Many-Argument Workhorses)** (Impact: 106.1)
  * `codegen_nameop` **(Many-Argument Workhorses)** (Impact: 96.8)
  * `codegen_visit_expr` **(Many-Argument Workhorses)** (Impact: 96.0)
  * `codegen_comprehension` **(Many-Argument Workhorses)** (Impact: 83.1)
  * `codegen_async_comprehension_generator` **(Many-Argument Workhorses)** (Impact: 76.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 337 instances
* *State Mutation (weighted view):* 1047
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1064`, `structural_boundaries: 574`, `args: 295`, `func_start: 161`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 373`, `dead_code: 6`, `planned_debt: 1`, `fragile_debt: 4`
* *Architecture:* `api: 24`, `import: 18`
* *Defense:* `safety: 76`, `doc: 1`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.32
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.001074
  * `Imports (Out-Degree: 15):` Python.h, opcode.h, pycore_ast.h, pycore_c_array.h, pycore_ceval.h, pycore_code.h, pycore_compile.h, pycore_instruction_sequence.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Modules/_ctypes/_ctypes.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3718.42 | **LOC:** 6524 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (52.2%)
- **Documentation Coverage:** 96.7136% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_build_callargs` **(Many-Argument Workhorses)** (Impact: 95.2)
    * *Intent:* */
  * `Pointer_subscript` **(Many-Argument Workhorses)** (Impact: 80.5)
  * `PyCSimpleType_init` **(Many-Argument Workhorses)** (Impact: 77.0)
  * `c_void_p_from_param_impl` **(Many-Argument Workhorses)** (Impact: 71.5)
  * `_PyCData_set` **(Many-Argument Workhorses)** (Impact: 65.1)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 450 instances
* *State Mutation (weighted view):* 1403
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 833`, `structural_boundaries: 727`, `args: 376`, `func_start: 157`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 146`, `state_mutation: 503`, `dead_code: 5`, `planned_debt: 1`, `fragile_debt: 12`, `unreferenced_by_name: 30`
* *Architecture:* `api: 13`, `import: 14`
* *Defense:* `safety: 72`, `doc: 19`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` Python.h, _ctypes.c.h, ctypes.h, dlfcn.h, ffi.h, malloc.h, pycore_call.h, pycore_ceval.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/_decimal/clinic/_decimal.c.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 3493.8 | **LOC:** 6984 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.344; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Guard Balance (formerly Safety Score) (80.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (40.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_decimal_localcontext` **(Many-Argument Workhorses)** (Impact: 59.2)
  * `context_init` **(Stateful Encapsulated Methods)** (Impact: 47.0)
  * `_decimal_Decimal_quantize` **(Stateful Encapsulated Methods)** (Impact: 25.0)
  * `_decimal_Decimal_to_integral_value` **(Stateful Encapsulated Methods)** (Impact: 24.9)
  * `_decimal_Decimal_to_integral` **(Stateful Encapsulated Methods)** (Impact: 24.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 430 instances
* *State Mutation (weighted view):* 1382
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 666`, `structural_boundaries: 202`, `args: 622`, `func_start: 143`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 522`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `immutability_locks: 329`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.344
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000597
  * `Imports (Out-Degree: 4):` pycore_abstract.h, pycore_gc.h, pycore_modsupport.h, pycore_runtime.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Python/dtoa.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3370.26 | **LOC:** 2842 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Complexity Load (formerly Cognitive Load) (97.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_Py_dg_dtoa` **(Many-Argument Workhorses)** (Impact: 504.0)
    * *Intent:* call to _Py_dg_freedtoa. */
  * `_Py_dg_strtod` **(Many-Argument Workhorses)** (Impact: 360.1)
  * `bigcomp` **(Many-Argument Workhorses)** (Impact: 59.5)
    * *Intent:* Returns 0 on success, -1 on failure (e.g., due to a failed malloc call). */
  * `quorem` **(Many-Argument Workhorses)** (Impact: 31.0)
    * *Intent:* bits (28--31) are zero and bit 27 is set. */
  * `mult` **(Many-Argument Workhorses)** (Impact: 30.6)
    * *Intent:* /* multiply two Bigints. Returns a new Bigint, or NULL on failure. Ignores the signs of a and b. */...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 672 instances
* *State Mutation (weighted view):* 2025
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 572`, `structural_boundaries: 127`, `args: 56`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 1`, `state_mutation: 681`, `dead_code: 5`, `fragile_debt: 9`, `unreferenced_by_name: 4`
* *Architecture:* `api: 11`, `import: 6`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Python.h, float.h, pycore_dtoa.h, pycore_interp_structs.h, pycore_pystate.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/_decimal/_decimal.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3145.24 | **LOC:** 8056 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (80.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.6%)
- **Documentation Coverage:** 78.8435% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convert_op_cmp` **(Many-Argument Workhorses)** (Impact: 88.3)
    * *Intent:* is undefined. */
  * `context_setattrs` **(Many-Argument Workhorses)** (Impact: 82.1)
  * `_decimal_Decimal___format___impl` **(Many-Argument Workhorses)** (Impact: 80.3)
  * `dectuple_as_str` **(Compute Cores)** (Impact: 58.3)
    * *Intent:* /* Return a new C string representation of a DecimalTuple. */
  * `PyDecType_FromFloatExact` **(Many-Argument Workhorses)** (Impact: 48.0)
    * *Intent:* /* Return a PyDecObject or a subtype from a PyFloatObject. Conversion is exact. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 399 instances
* *State Mutation (weighted view):* 1217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 725`, `structural_boundaries: 576`, `args: 555`, `func_start: 184`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 419`, `dead_code: 2`, `unreferenced_by_name: 61`
* *Architecture:* `api: 9`, `import: 8`
* *Defense:* `safety: 37`, `doc: 26`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Python.h, _decimal.c.h, ctype.h, mpdecimal.h, pycore_object.h, pycore_pystate.h, pycore_typeobject.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Objects/bytesobject.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3108.14 | **LOC:** 3906 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.1%), Guard Balance (formerly Safety Score) (93.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_PyBytes_FormatEx` **(Many-Argument Workhorses)** (Impact: 429.8)
    * *Intent:* /* fmt%(v1,v2,...) is roughly equivalent to sprintf(fmt, v1, v2, ...) */
  * `_PyBytes_DecodeEscape2` **(Many-Argument Workhorses)** (Impact: 123.2)
    * *Intent:* /* Unescape a backslash-escaped string. */
  * `bytes_fromformat` **(Many-Argument Workhorses)** (Impact: 109.4)
  * `_Py_bytes_repr` **(Many-Argument Workhorses)** (Impact: 77.4)
  * `bytes_new_impl` **(Many-Argument Workhorses)** (Impact: 69.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 420 instances
* *State Mutation (weighted view):* 1270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 721`, `structural_boundaries: 343`, `args: 237`, `func_start: 102`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 430`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 39`
* *Architecture:* `api: 35`, `import: 26`
* *Defense:* `safety: 48`, `doc: 2`, `immutability_locks: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` Python.h, bytesobject.c.h, pycore_abstract.h, pycore_bytes_methods.h, pycore_bytesobject.h, pycore_call.h, pycore_ceval.h, pycore_format.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Python/initconfig.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3012.22 | **LOC:** 4859 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `config_parse_cmdline` **(Many-Argument Workhorses)** (Impact: 126.0)
    * *Intent:* /* Parse the command line arguments */
  * `PyConfig_Set` **(Compute Cores)** (Impact: 74.2)
  * `config_read` **(Many-Argument Workhorses)** (Impact: 61.2)
  * `_PyConfig_FromDict` **(Compute Cores)** (Impact: 53.2)
  * `config_read_complex_options` **(Compute Cores)** (Impact: 44.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 347 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 1127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 817`, `structural_boundaries: 503`, `args: 262`, `func_start: 142`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 2`, `state_mutation: 433`, `dead_code: 5`, `fragile_debt: 1`, `unreferenced_by_name: 38`
* *Architecture:* `api: 64`, `import: 20`
* *Defense:* `safety: 96`, `immutability_locks: 197`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` Python.h, config_common.h, fcntl.h, io.h, locale.h, osdefs.h, pycore_fileutils.h, pycore_getopt.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Python/flowgraph.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3009.68 | **LOC:** 4097 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 0.333; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.0%)
- **Documentation Coverage:** 48.7097% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `optimize_basic_block` **(Many-Argument Workhorses)** (Impact: 160.7)
  * `optimize_load_fast` **(Many-Argument Workhorses)** (Impact: 105.0)
    * *Intent:* * Using the above, we can optimize any LOAD_FAST{_LOAD_FAST} instructions * that meet the following ...
  * `basicblock_optimize_load_const` **(Many-Argument Workhorses)** (Impact: 76.4)
  * `const_folding_safe_multiply` **(Stateful Encapsulated Methods)** (Impact: 49.0)
    * *Intent:* #define MAX_INT_SIZE 128 /* bits */ #define MAX_COLLECTION_SIZE 256 /* items */ #define MAX_STR_SIZE...
  * `label_exception_targets` **(Compute Cores)** (Impact: 47.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 393 instances
* *State Mutation (weighted view):* 1219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 798`, `structural_boundaries: 473`, `args: 192`, `func_start: 116`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 433`, `dead_code: 1`, `planned_debt: 12`, `fragile_debt: 2`
* *Architecture:* `api: 28`, `import: 11`
* *Defense:* `safety: 183`, `doc: 7`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.333
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.002436
  * `Imports (Out-Degree: 9):` Python.h, opcode.h, pycore_c_array.h, pycore_compile.h, pycore_flowgraph.h, pycore_intrinsics.h, pycore_long.h, pycore_opcode_metadata.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Python/getargs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2970.48 | **LOC:** 3007 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.8%), Guard Balance (formerly Safety Score) (88.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convertsimple` **(Many-Argument Workhorses)** (Impact: 531.4)
    * *Intent:* */
  * `vgetargskeywords_impl` **(Many-Argument Workhorses)** (Impact: 311.1)
    * *Intent:* #define IS_END_OF_FORMAT(c) (c == '\0' || c == ';' || c == ':')
  * `vgetargskeywordsfast_impl` **(Many-Argument Workhorses)** (Impact: 188.9)
  * `vgetargs1_impl` **(Many-Argument Workhorses)** (Impact: 156.0)
  * `converttuple` **(Many-Argument Workhorses)** (Impact: 147.3)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 302 instances
* *State Mutation (weighted view):* 934
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 720`, `structural_boundaries: 317`, `args: 179`, `func_start: 53`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 330`, `dead_code: 3`, `fragile_debt: 4`, `unreferenced_by_name: 16`
* *Architecture:* `api: 28`, `import: 9`
* *Defense:* `safety: 51`, `immutability_locks: 160`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` Python.h, pycore_abstract.h, pycore_dict.h, pycore_modsupport.h, pycore_pyerrors.h, pycore_pylifecycle.h, pycore_pystate.h, pycore_tuple.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Objects/listobject.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2960.06 | **LOC:** 4308 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 18.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `list_sort_impl` **(Many-Argument Workhorses)** (Impact: 147.2)
  * `merge_hi` **(Many-Argument Workhorses)** (Impact: 90.0)
    * *Intent:* /* Merge the na elements starting at pa with the nb elements starting at * ssb.keys = ssa.keys + na ...
  * `merge_lo` **(Many-Argument Workhorses)** (Impact: 87.1)
    * *Intent:* /* Merge the na elements starting at ssa with the nb elements starting at * ssb.keys = ssa.keys + na...
  * `list_ass_subscript_lock_held` **(Many-Argument Workhorses)** (Impact: 64.4)
  * `list_ass_slice_lock_held` **(Many-Argument Workhorses)** (Impact: 51.5)
    * *Intent:* /* a[ilow:ihigh] = v if v != NULL. * del a[ilow:ihigh] if v == NULL. * * Special speed gimmick: when...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 418 instances
* *State Mutation (weighted view):* 1284
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 622`, `structural_boundaries: 342`, `args: 227`, `func_start: 124`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 91`, `state_mutation: 448`, `dead_code: 3`, `unreferenced_by_name: 34`
* *Architecture:* `api: 29`, `import: 18`
* *Defense:* `safety: 130`, `doc: 2`, `immutability_locks: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` Python.h, listobject.c.h, pycore_abstract.h, pycore_ceval.h, pycore_critical_section.h, pycore_dict.h, pycore_freelist.h, pycore_interp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Python/import.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2735.06 | **LOC:** 5744 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 18.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Debt Markers (formerly Tech Debt) (82.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.6%)
- **Documentation Coverage:** 47.389% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve_name` **(Many-Argument Workhorses)** (Impact: 97.0)
  * `PyImport_ImportModuleLevelObject` **(Many-Argument Workhorses)** (Impact: 95.9)
  * `import_run_extension` **(Many-Argument Workhorses)** (Impact: 82.9)
  * `_PyImport_LazyImportModuleLevelObject` **(Many-Argument Workhorses)** (Impact: 76.4)
  * `_PyImport_LoadLazyImportTstate` **(Many-Argument Workhorses)** (Impact: 71.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 241 instances
* *State Mutation (weighted view):* 741
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 702`, `structural_boundaries: 581`, `args: 288`, `func_start: 179`, `class_start: 54`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 259`, `dead_code: 2`, `fragile_debt: 22`, `unreferenced_by_name: 75`
* *Architecture:* `api: 84`, `import: 34`
* *Defense:* `safety: 136`, `doc: 41`, `immutability_locks: 69`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` Python.h, import.c.h, fcntl.h, marshal.h, pycore_audit.h, pycore_ceval.h, pycore_critical_section.h, pycore_dict.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Modules/clinic/_testclinic.c.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2605.18 | **LOC:** 4604 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (83.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `char_converter` **(Many-Argument Workhorses)** (Impact: 222.3)
  * `py_ssize_t_converter` **(Many-Argument Workhorses)** (Impact: 57.5)
  * `unsigned_char_converter` **(Many-Argument Workhorses)** (Impact: 48.0)
  * `posonly_keywords_opt_kwonly_opt` **(Stateful Encapsulated Methods)** (Impact: 30.4)
  * `keywords_opt_kwonly` **(Stateful Encapsulated Methods)** (Impact: 30.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 310 instances
* *State Mutation (weighted view):* 1069
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 534`, `structural_boundaries: 110`, `args: 273`, `func_start: 76`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 449`, `fragile_debt: 4`
* *Architecture:* `import: 6`
* *Defense:* `safety: 9`, `immutability_locks: 173`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.353
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.000597
  * `Imports (Out-Degree: 6):` pycore_abstract.h, pycore_gc.h, pycore_long.h, pycore_modsupport.h, pycore_runtime.h, pycore_tuple.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Objects/codeobject.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2587.98 | **LOC:** 3670 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **21**; blast radius 0.315; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.6%)
- **Documentation Coverage:** 45.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PyUnstable_Code_NewWithPosOnlyArgs` **(Many-Argument Workhorses)** (Impact: 121.0)
    * *Intent:* /****************** * the legacy "constructors" ******************/
  * `identify_unbound_names` **(Many-Argument Workhorses)** (Impact: 94.5)
    * *Intent:* #endif
  * `_PyCode_ConstantKey` **(Compute Cores)** (Impact: 70.3)
    * *Intent:* /****************** * other API ******************/
  * `code_new_impl` **(Many-Argument Workhorses)** (Impact: 66.9)
  * `intern_constants` **(Many-Argument Workhorses)** (Impact: 58.8)
    * *Intent:* constants. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 303 instances
* *State Mutation (weighted view):* 966
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 568`, `structural_boundaries: 342`, `args: 190`, `func_start: 123`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 360`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `api: 73`, `import: 21`
* *Defense:* `safety: 85`, `doc: 8`, `test: 7`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.315
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.002088
  * `Imports (Out-Degree: 19):` Python.h, codeobject.c.h, opcode.h, pycore_code.h, pycore_function.h, pycore_hashtable.h, pycore_index_pool.h, pycore_initconfig.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `Python/optimizer_bytecodes.c` -> Churn: **95.66%** | Cog Load: 72.1594% | Debt: 8.189%
- `Python/ceval.c` -> Churn: **84.66%** | Cog Load: 83.3452% | Debt: 9.0902%
- `Python/optimizer.c` -> Churn: **80.75%** | Cog Load: 66.121% | Debt: 8.6193%
- `Objects/dictobject.c` -> Churn: **79.96%** | Cog Load: 56.5234% | Debt: 33.244%
- `Objects/unicodeobject.c` -> Churn: **73.94%** | Cog Load: 79.0946% | Debt: 8.2317%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `Modules/expat/xmlparse.c` -> **Stan Ulbrych** (100.0% isolated ownership) | Magnitude: 9987.94
- `Modules/_decimal/clinic/_decimal.c.h` -> **Sergey B Kirpichev** (100.0% isolated ownership) | Magnitude: 3493.8
- `Python/dtoa.c` -> **Sergey B Kirpichev** (100.0% isolated ownership) | Magnitude: 3370.26
- `Python/flowgraph.c` -> **Mark Shannon** (100.0% isolated ownership) | Magnitude: 3009.68
- `Python/getargs.c` -> **Victor Stinner** (100.0% isolated ownership) | Magnitude: 2970.48

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Python/thread.c` -> **Severity: 0.786** (Bridge: 0.0079 * Flux: 99.9732%)
- `Include/internal/mimalloc/mimalloc/atomic.h` -> **Severity: 0.644** (Bridge: 0.008 * Flux: 80.2283%)
- `Include/internal/pycore_gc.h` -> **Severity: 0.377** (Bridge: 0.004 * Flux: 95.0056%)
- `Objects/mimalloc/os.c` -> **Severity: 0.275** (Bridge: 0.0028 * Flux: 99.9993%)
- `Include/internal/pycore_mimalloc.h` -> **Severity: 0.265** (Bridge: 0.0058 * Flux: 45.5672%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Include/internal/pycore_llist.h` -> **Severity: 8.979** (Embedded: 0.0946 * Error Risk: 94.9241%)
- `Include/cpython/funcobject.h` -> **Severity: 7.737** (Embedded: 0.0918 * Error Risk: 84.2905%)
- `Include/cpython/context.h` -> **Severity: 7.673** (Embedded: 0.0918 * Error Risk: 83.5974%)
- `Include/cpython/genobject.h` -> **Severity: 7.673** (Embedded: 0.0918 * Error Risk: 83.5974%)
- `Include/moduleobject.h` -> **Severity: 7.455** (Embedded: 0.0918 * Error Risk: 81.223%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Modules/_testlimitedcapi/sys.c` -> **Severity: 1661.2** (Blast Radius: 16.612 * Doc Risk: 100.0%)
- `Include/internal/pycore_runtime.h` -> **Severity: 1337.1** (Blast Radius: 13.371 * Doc Risk: 100.0%)
- `Objects/mimalloc/os.c` -> **Severity: 1141.7** (Blast Radius: 11.417 * Doc Risk: 100.0%)
- `Include/internal/pycore_pystate.h` -> **Severity: 1061.4** (Blast Radius: 10.614 * Doc Risk: 100.0%)
- `Include/internal/pycore_gc.h` -> **Severity: 1058.8** (Blast Radius: 10.588 * Doc Risk: 100.0%)

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
