# ARCHITECTURAL_BRIEF: zap
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/zigzap/zap.git` |
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
- **Scope:** 167 analyzed artifact(s), 44884 LOC.
- **Load-bearing artifact:** `src/zap.zig` -- 42 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `facil.io/tests/slowloris.c` -- pulls in 28 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `facil.io/lib/facil/fio.c` at magnitude 6298.6 (structural weight, not risk).
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
| Total Artifacts | 185 |
| Analyzed Artifacts (Scanned) | 167 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 18 |
| Total LOC | 44884 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 90.3% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5167 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4421 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 21.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2253 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 7 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 72 | 30823 | 43.1% |
| ZIG | 55 | 12615 | 32.9% |
| MARKDOWN | 15 | 0 | 9.0% |
| HTML | 7 | 504 | 4.2% |
| YAML | 6 | 184 | 3.6% |
| PLAINTEXT | 4 | 0 | 2.4% |
| SHELL | 4 | 47 | 2.4% |
| NIX | 2 | 124 | 1.2% |
| JAVASCRIPT | 1 | 59 | 0.6% |
| MAKEFILE | 1 | 528 | 0.6% |

## 4.1 SOURCE ENCODINGS
All 167 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 24%, Data / Markup / Trivial 23%, Encapsulated Accessors Files 13%, Declarative / Non-Code 12%, Large Core Modules (3) 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 148 | 88.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 19 | 11.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 18*

**Composition by Extension & Reason:**
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2385 LOC)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.bin`: 2x Excluded (Unsupported Extension: '.bin')
- `.lock`: 2x Excluded (Unsupported Extension: '.lock')
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 1x Unsupported Format (.patch)
- `.exe`: 1x Excluded (Explicitly Denied Extension: '.exe')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 80.4 | 14.0 | 4.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 82.4 | 36.3 | 45.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 15.4 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 23.0 | 7.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 64.1 | 3.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 21.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 41.1 | 2.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 56.6 | 66.3 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5247 | 76 | 17 | `src/deps/cimport.zig` |
| cleanup | 243 | 49 | 4 | `facil.io/lib/facil/fio.c` |
| guards | 3622 | 118 | 56 | `facil.io/lib/facil/fio.c` |
| danger | 2231 | 88 | 18 | `src/deps/cimport.zig` |
| concurrency | 97 | 24 | 1 | `examples/endpoint/users.zig` |
| connectivity | 5974 | 132 | 23 | `src/deps/cimport.zig` |
| io | 194 | 25 | 2 | `facil.io/makefile` |
| crypto | 0 | 0 | 0 | - |
| ipc | 100 | 27 | 1 | `facil.io/lib/facil/fio.c` |
| time | 31 | 9 | 0 | `facil.io/lib/facil/fio.c` |
| serialization | 7 | 2 | 0 | `examples/endpoint/html/index.html` |
| regex | 3 | 2 | 0 | `facil.io/scripts/new/app` |
| events | 324 | 28 | 2 | `facil.io/lib/facil/fio.c` |
| tests | 107 | 10 | 0 | `src/tests/test_auth.zig` |
| docs | 2368 | 101 | 24 | `facil.io/lib/facil/fio.h` |
| debt | 752 | 89 | 11 | `facil.io/lib/facil/fio.c` |
| mutation | 11245 | 120 | 105 | `src/deps/cimport.zig` |
| dead_code | 1343 | 61 | 7 | `src/deps/cimport.zig` |
| credential | 114 | 5 | 0 | `examples/middleware/middleware.zig` |
| threat | 18 | 4 | 0 | `facil.io/lib/facil/fio.c` |
| ml_ai | 85 | 23 | 1 | `src/deps/cimport.zig` |
| ui | 27 | 4 | 0 | `examples/endpoint/html/index.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `facil.io/makefile` (Hits: 106)
- `facil.io/scripts/new/cleanup` (Hits: 10)
- `facil.io/lib/facil/fio.c` (Hits: 9)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **zap.zig** (`src/zap.zig`) — 42 inbound connections
2. **fio.h** (`facil.io/lib/facil/fio.h`) — 39 inbound connections
3. **fiobject.h** (`facil.io/lib/facil/fiobj/fiobject.h`) — 28 inbound connections
4. **fio.c** (`facil.io/lib/facil/fio.c`) — 26 inbound connections
5. **fio_cli.h** (`facil.io/lib/facil/cli/fio_cli.h`) — 15 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **slowloris.c** (`facil.io/tests/slowloris.c`) — 28 outbound dependencies
2. **README.md** (`README.md`) — 27 outbound dependencies
3. **fio.c** (`facil.io/lib/facil/fio.c`) — 24 outbound dependencies
4. **fio.h** (`facil.io/lib/facil/fio.h`) — 16 outbound dependencies
5. **zap.zig** (`src/zap.zig`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `http_mime_parse` **(Many-Argument Workhorses)** (@ `facil.io/lib/facil/http/parsers/http_mime_parser.h`) -> Impact: **180.6** | LOC: 212
  * *Intent:* /** * Consumes data from a streaming buffer. * * The data might be partially consumed, in which case the unconsumed data * should be resent to the par...
- `http_sendfile2` **(Many-Argument Workhorses)** (@ `facil.io/lib/facil/http/http.c`) -> Impact: **168.2** | LOC: 228
  * *Intent:* /** * Sends the response headers and the specified file (the response's body). * * Returns -1 eton error and 0 on success. * * AFTER THIS FUNCTION IS ...
- `fio_cli_set_arg` **(Many-Argument Workhorses)** (@ `facil.io/lib/facil/cli/fio_cli.c`) -> Impact: **167.9** | LOC: 182
- `http1_consume_header_transfer_encoding` **(Many-Argument Workhorses)** (@ `facil.io/lib/facil/http/parsers/http1_parser.h`) -> Impact: **155.0** | LOC: 111
  * *Intent:* #ifndef HTTP1_ALLOW_CHUNKED_IN_MIDDLE_OF_HEADER
- `fio_url_parse` **(Many-Argument Workhorses)** (@ `facil.io/lib/facil/fio.c`) -> Impact: **132.1** | LOC: 217
  * *Intent:* * i.e.: /index.html?page=1#list * * * `host:port/complete_path?query#target` * * i.e.: * example.com/index.html * example.com:8080/index.html * * * `s...
- `Create` **(Defensive Guards)** (@ `src/App.zig`) -> Impact: **106.4** | LOC: 459
  * *Intent:* /// creates an App with custom app context /// /// About App Contexts: /// /// ```zig /// const MyContext = struct { /// // You may (optionally) defin...
- `http_add2hash2` **(Many-Argument Workhorses)** (@ `facil.io/lib/facil/http/http.c`) -> Impact: **104.2** | LOC: 174
  * *Intent:* * * i.e.: * * * "name[]" references a nested Array (nested in the Hash). * * "name[key]" references a nested Hash. * * "name[][key]" references a nest...
- `resp_parse` **(Many-Argument Workhorses)** (@ `facil.io/lib/facil/redis/resp_parser.h`) -> Impact: **94.7** | LOC: 134
  * *Intent:* ***************************************************************************** */ /** * Returns the number of bytes to be resent. i.e., for a return va...
- `FIO_IGNORE_MACRO` **(Many-Argument Workhorses)** (@ `facil.io/lib/facil/http/http.c`) -> Impact: **86.4** | LOC: 128
  * *Intent:* /** * Connects to an HTTP server as a client. * * Upon a successful connection, the `on_response` callback is called with an * empty `http_s*` handler...
- `fio_ltoa` **(Many-Argument Workhorses)** (@ `facil.io/lib/facil/fio.c`) -> Impact: **83.7** | LOC: 153
  * *Intent:* /** * A helper function that writes a signed int64_t to a string. * * No overflow guard is provided, make sure there's at least 68 bytes * available (...

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `facil.io/lib/facil` | 3 | 7905.06 | 34.79% | 40.22% |
| `src/deps` | 1 | 6151.16 | 16.74% | 100.0% |
| `facil.io/lib/facil/fiobj` | 24 | 3756.24 | 17.69% | 19.24% |
| `facil.io/lib/facil/http` | 9 | 3443.54 | 15.58% | 14.2% |
| `src` | 15 | 2585.68 | 10.0% | 12.6% |
| `facil.io/lib/facil/http/parsers` | 4 | 2276.42 | 34.98% | 4.35% |
| `facil.io/tests` | 9 | 1893.82 | 22.88% | 0.0% |
| `facil.io/lib/facil/tls` | 3 | 730.76 | 16.74% | 31.46% |
| `facil.io/lib/facil/redis` | 3 | 695.58 | 18.95% | 20.33% |
| `facil.io/lib/facil/legacy` | 2 | 562.76 | 34.29% | 2.98% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/deps/cimport.zig` -> **100.0%** Exposure
- `facil.io/lib/facil/fio_zig.c` -> **99.9998%** Exposure
- `facil.io/lib/facil/fiobj/fiobj_hash.c` -> **88.9273%** Exposure
- `facil.io/lib/facil/fiobj/fiobj_str.c` -> **75.1487%** Exposure
- `facil.io/lib/facil/fiobj/fiobj_numbers.c` -> **71.3948%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `facil.io/lib/facil/fiobj/fio_siphash.c` -> **100.0%** Exposure
- `facil.io/lib/facil/fiobj/fiobj_json.c` -> **100.0%** Exposure
- `facil.io/lib/facil/fiobj/fiobject.c` -> **100.0%** Exposure
- `facil.io/lib/facil/http/http.c` -> **100.0%** Exposure
- `facil.io/lib/facil/http/parsers/http1_parser.h` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/deps/cimport.zig` -> **963** Orphaned Functions | **0** Duplicates
- `facil.io/lib/facil/http/http.c` -> **34** Orphaned Functions | **0** Duplicates
- `facil.io/lib/facil/fio.c` -> **26** Orphaned Functions | **0** Duplicates
- `facil.io/lib/facil/fiobj/fiobj_json.c` -> **13** Orphaned Functions | **0** Duplicates
- `facil.io/lib/facil/redis/redis_engine.c` -> **13** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `examples/middleware/middleware.zig` -> **100.0%** Exposure
- `examples/middleware_with_endpoint/middleware_with_endpoint.zig` -> **100.0%** Exposure
- `src/tests/test_auth.zig` -> **99.9958%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `542` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `facil.io/lib/facil/fio.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.021)
- **Top Global Matches:** file_cluster_4: 8.021, file_cluster_12: 9.609, file_cluster_16: 10.414
- **Magnitude:** 6298.6 | **LOC:** 11040 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **24**; blast radius 111.016; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.9%), Complexity Load (formerly Cognitive Load) (61.2%)
- **Documentation Coverage:** 60.5388% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fio_url_parse` **(Many-Argument Workhorses)** (Impact: 132.1)
    * *Intent:* * i.e.: /index.html?page=1#list * * * `host:port/complete_path?query#target` * * i.e.: * example.com...
  * `fio_ltoa` **(Many-Argument Workhorses)** (Impact: 83.7)
    * *Intent:* /** * A helper function that writes a signed int64_t to a string. * * No overflow guard is provided,...
  * `fio_base64_decode` **(Many-Argument Workhorses)** (Impact: 61.0)
    * *Intent:* */
  * `fio_expected_concurrency` **(Many-Argument Workhorses)** (Impact: 53.6)
    * *Intent:* /** * Returns the number of expected threads / processes to be used by facil.io. * * The pointers sh...
  * `fio_flush` **(Compute Cores)** (Impact: 43.2)
    * *Intent:* /** * `fio_flush` attempts to write any remaining data in the internal buffer to * the underlying fi...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 22 instances
* *Amplified Cascading Flux:* 935 instances
* *Memory Alloc (weighted view):* 15
* *State Mutation (weighted view):* 3155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1283`, `structural_boundaries: 1363`, `args: 527`, `func_start: 355`, `class_start: 79`
* *Risk/State:* `safety_bypasses: 152`, `high_risk_execution: 16`, `state_mutation: 1285`, `dead_code: 43`, `planned_debt: 4`, `fragile_debt: 2`, `unreferenced_by_name: 26`
* *Architecture:* `io: 9`, `api: 212`, `concurrency: 1`, `import: 36`
* *Defense:* `safety: 228`, `doc: 137`, `immutability_locks: 62`, `cleanup: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 111.016
  * `Choke Point (Betweenness):` 0.004447 | `Ripple Effect (Closeness):` 0.218459
  * `Imports (Out-Degree: 2):` inet.h, ctype.h, errno.h, fio.h, limits.h, netdb.h, in.h, tcp.h...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `src/deps/cimport.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 18.867)
- **Top Global Matches:** file_cluster_5: 18.867, file_cluster_7: 19.537, file_cluster_14: 19.794
- **Magnitude:** 6151.16 | **LOC:** 5497 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.935; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (29.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fio_risky_hash` **(Type Conversions)** (Impact: 76.5)
  * `fiobj_iseq` **(Type Conversions)** (Impact: 12.6)
  * `fiobj_obj2cstr` **(Type Conversions)** (Impact: 12.4)
  * `fiobj_type_is` **(Type Conversions)** (Impact: 9.8)
  * `fiobj_type` **(Type Conversions)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 378`, `args: 1113`, `func_start: 1052`, `class_start: 127`
* *Risk/State:* `safety_bypasses: 901`, `state_mutation: 187`, `planned_debt: 17`, `unreferenced_by_name: 963`
* *Architecture:* `api: 3857`, `import: 348`
* *Defense:* `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.935
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `facil.io/lib/facil/http/http.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.195)
- **Top Global Matches:** file_cluster_4: 5.195, file_cluster_12: 10.404, file_cluster_16: 10.562
- **Magnitude:** 2206.82 | **LOC:** 2714 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **11**; blast radius 9.927; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.5%), Complexity Load (formerly Cognitive Load) (67.9%)
- **Documentation Coverage:** 26.3354% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `http_sendfile2` **(Many-Argument Workhorses)** (Impact: 168.2)
    * *Intent:* /** * Sends the response headers and the specified file (the response's body). * * Returns -1 eton e...
  * `http_add2hash2` **(Many-Argument Workhorses)** (Impact: 104.2)
    * *Intent:* * * i.e.: * * * "name[]" references a nested Array (nested in the Hash). * * "name[key]" references ...
  * `FIO_IGNORE_MACRO` **(Many-Argument Workhorses)** (Impact: 86.4)
    * *Intent:* /** * Connects to an HTTP server as a client. * * Upon a successful connection, the `on_response` ca...
  * `http_set_cookie` **(Many-Argument Workhorses)** (Impact: 71.3)
    * *Intent:* /** * Sets a response cookie, taking ownership of the value object, but NOT the * name object (so na...
  * `hex2byte` **(Stateful Encapsulated Methods)** (Impact: 30.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 296 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 1013
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 434`, `structural_boundaries: 287`, `args: 119`, `func_start: 90`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 2`, `state_mutation: 421`, `dead_code: 4`, `planned_debt: 2`, `unreferenced_by_name: 34`
* *Architecture:* `io: 4`, `api: 59`, `import: 12`
* *Defense:* `safety: 63`, `doc: 58`, `immutability_locks: 43`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.927
  * `Choke Point (Betweenness):` 0.01171 | `Ripple Effect (Closeness):` 0.091831
  * `Imports (Out-Degree: 16):` ctype.h, fcntl.h, fio.h, http1.h, http_internal.h, http_mime_parser.h, signal.h, string.h...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `facil.io/lib/facil/fio.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.453)
- **Top Global Matches:** file_cluster_4: 6.453, file_cluster_15: 8.452, file_cluster_16: 9.435
- **Magnitude:** 1565.34 | **LOC:** 6338 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **39** in-repo importer(s); it depends on **16**; blast radius 85.583; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.7%)
- **Documentation Coverage:** 3.6765% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fio_str_utf8_select` **(Many-Argument Workhorses)** (Impact: 70.5)
    * *Intent:* /** * Takes a UTF-8 character selection information (UTF-8 position and length) and * updates the sa...
  * `fio_str_readfile` **(Many-Argument Workhorses)** (Impact: 46.1)
    * *Intent:* /** * Opens the file `filename` and pastes it's contents (or a slice ot it) at the * end of the Stri...
  * `fio_risky_hash` **(Many-Argument Workhorses)** (Impact: 42.7)
    * *Intent:* /* Computes a facil.io Risky Hash. */
  * `fio_str_replace` **(Many-Argument Workhorses)** (Impact: 36.4)
    * *Intent:* /** * Replaces the data in the String - replacing `old_len` bytes starting at * `start_pos`, with th...
  * `fio_str_capa_assert` **(Many-Argument Workhorses)** (Impact: 24.0)
    * *Intent:* * In fact, with some allocators (i.e., jemalloc), spacing increases for larger * allocations - meani...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 225 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 713
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 320`, `structural_boundaries: 502`, `args: 267`, `func_start: 63`, `class_start: 49`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 6`, `state_mutation: 263`, `planned_debt: 3`
* *Architecture:* `io: 4`, `api: 320`, `import: 18`
* *Defense:* `safety: 138`, `doc: 482`, `immutability_locks: 110`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 85.583
  * `Choke Point (Betweenness):` 0.001552 | `Ripple Effect (Closeness):` 0.269263
  * `Imports (Out-Degree: 1):` errno.h, fcntl.h, limits.h, in.h, signal.h, stdarg.h, stdint.h, stdio.h...
  * `Imported By (In-Degree: 39):` (Excluded from Brief to save tokens)

### `facil.io/lib/facil/http/parsers/http1_parser.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.548)
- **Top Global Matches:** file_cluster_8: 8.548, file_cluster_6: 16.418, file_cluster_3: 22.724
- **Magnitude:** 929.78 | **LOC:** 874 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 2.852; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.4%), Complexity Load (formerly Cognitive Load) (51.5%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `http1_consume_header_transfer_encoding` **(Many-Argument Workhorses)** (Impact: 155.0)
    * *Intent:* #ifndef HTTP1_ALLOW_CHUNKED_IN_MIDDLE_OF_HEADER
  * `http1_parse` **(Many-Argument Workhorses)** (Impact: 78.5)
    * *Intent:* * Returns the amount of data actually consumed by the parser. * * The value 0 indicates there wasn't...
  * `http1_consume_request_line` **(Many-Argument Workhorses)** (Impact: 65.0)
  * `http1_consume_body_chunked` **(Many-Argument Workhorses)** (Impact: 52.9)
  * `http1_atol16` **(Stateful Encapsulated Methods)** (Impact: 37.9)
    * *Intent:* /** Converts a String to a number using base 16, overflow limited to 113bytes */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 110 instances
* *State Mutation (weighted view):* 332
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 239`, `structural_boundaries: 85`, `args: 29`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 112`, `fragile_debt: 1`
* *Architecture:* `api: 11`, `import: 7`
* *Defense:* `safety: 24`, `doc: 20`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.852
  * `Choke Point (Betweenness):` 0.001875 | `Ripple Effect (Closeness):` 0.048897
  * `Imports (Out-Degree: 1):` assert.h, stddef.h, stdint.h, stdio.h, stdlib.h, string.h, types.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `facil.io/lib/facil/fiobj/fiobj_data.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.246)
- **Top Global Matches:** file_cluster_4: 7.246, file_cluster_12: 8.785, file_cluster_16: 9.703
- **Magnitude:** 768.6 | **LOC:** 1184 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 3.129; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.1%), Complexity Load (formerly Cognitive Load) (44.1%)
- **Documentation Coverage:** 35.4917% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fiobj_data_test` **(I/O & Config Routines)** (Impact: 35.9)
    * *Intent:* #if DEBUG
  * `fiobj_data_seek` **(Compute Cores)** (Impact: 33.8)
    * *Intent:* /** * Moves the reading position to the requested position. */
  * `fiobj_data_puts` **(Many-Argument Workhorses)** (Impact: 23.8)
    * *Intent:* /** * Writes `length` bytes at the end of the IO stream, ignoring the reading * position, adding an ...
  * `fiobj_data_read2ch_file` **(Many-Argument Workhorses)** (Impact: 23.3)
  * `swallow_ch` **(Many-Argument Workhorses)** (Impact: 22.5)
    * *Intent:* ***************************************************************************** */ #if FIO_MEMCHAR /**...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Cascading Flux:* 87 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 263
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 161`, `args: 56`, `func_start: 45`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 13`, `state_mutation: 89`, `dead_code: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 7`, `api: 24`, `import: 12`
* *Defense:* `safety: 26`, `doc: 24`, `immutability_locks: 25`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.129
  * `Choke Point (Betweenness):` 0.001598 | `Ripple Effect (Closeness):` 0.081537
  * `Imports (Out-Degree: 6):` assert.h, errno.h, fcntl.h, fio.h, fio_tmpfile.h, fiobj_data.h, fiobj_str.h, string.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `facil.io/lib/facil/http/parsers/hpack.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.168)
- **Top Global Matches:** file_cluster_6: 6.168, file_cluster_4: 10.876, file_cluster_8: 15.041
- **Magnitude:** 727.62 | **LOC:** 1924 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 1.935; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (60.4%), Complexity Load (formerly Cognitive Load) (29.7%), Debt Markers (formerly Tech Debt) (8.0%)
- **Documentation Coverage:** 96.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hpack_test` **(I/O & Config Routines)** (Impact: 73.3)
    * *Intent:* ***************************************************************************** */ #if DEBUG #include ...
  * `huffman__print_tree` **(I/O & Config Routines)** (Impact: 37.4)
    * *Intent:* #define HUFFMAN_TREE_BUFFER (1 << 12)
  * `hpack_huffman_pack` **(Many-Argument Workhorses)** (Impact: 35.1)
  * `hpack_huffman_unpack` **(Many-Argument Workhorses)** (Impact: 24.0)
    * *Intent:* ***************************************************************************** */
  * `hpack_int_pack` **(Many-Argument Workhorses)** (Impact: 22.5)
    * *Intent:* ***************************************************************************** */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 22 instances
* *Amplified Cascading Flux:* 137 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 422
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 67`, `args: 22`, `func_start: 12`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 27`, `state_mutation: 148`, `unreferenced_by_name: 1`
* *Architecture:* `api: 8`, `import: 7`
* *Defense:* `safety: 63`, `doc: 15`, `test: 13`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.935
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fio.h, inttypes.h, stdint.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `facil.io/lib/facil/fiobj/mustache_parser.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.801)
- **Top Global Matches:** file_cluster_4: 5.801, file_cluster_16: 8.708, file_cluster_12: 10.317
- **Magnitude:** 699.42 | **LOC:** 1543 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 4.592; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.2%), Complexity Load (formerly Cognitive Load) (44.8%)
- **Documentation Coverage:** 65.9733% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mustache__load_file` **(Many-Argument Workhorses)** (Impact: 66.9)
  * `mustache__write_escaped` **(Many-Argument Workhorses)** (Impact: 29.1)
    * *Intent:* /** * used internally to write escaped text rather than clear text. */
  * `mustache_write_text` **(Stateful Encapsulated Methods)** (Impact: 21.5)
    * *Intent:* /** * This helper function should be used to write text to the output * stream (often used within th...
  * `mustache__load_data` **(Many-Argument Workhorses)** (Impact: 20.1)
  * `mustache__push_text_instruction` **(Many-Argument Workhorses)** (Impact: 14.2)
    * *Intent:* /* pushes text and padding instruction to the instruction array */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 135 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 455
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 101`, `args: 30`, `func_start: 16`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 185`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `io: 3`, `api: 15`, `import: 11`
* *Defense:* `safety: 17`, `doc: 40`, `immutability_locks: 25`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.592
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.059016
  * `Imports (Out-Degree: 0):` ctype.h, errno.h, fcntl.h, stdint.h, stdio.h, stdlib.h, string.h, strings.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `facil.io/tests/collisions.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.323)
- **Top Global Matches:** file_cluster_4: 7.323, file_cluster_16: 7.346, file_cluster_12: 7.923
- **Magnitude:** 547.04 | **LOC:** 894 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.935; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (69.4%), Complexity Load (formerly Cognitive Load) (33.5%), Dead Code Surface (formerly Dead Code) (10.0%), Connectivity (formerly Api Exposure) (2.2%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fio_risky_hash2` **(Many-Argument Workhorses)** (Impact: 42.5)
    * *Intent:* /* Computes a facil.io Risky Hash. */
  * `fio_risky_hash_old` **(Many-Argument Workhorses)** (Impact: 33.2)
    * *Intent:* #undef fio_risky_consume
  * `counter` **(Stateful Encapsulated Methods)** (Impact: 26.9)
  * `add_bad4xxhash` **(I/O & Config Routines)** (Impact: 14.3)
    * *Intent:* * U64 v4 = seed - PRIME64_1; * * do { * v1 += XXH_get64bits(p) * PRIME64_2; * p += 8; * v1 = XXH_rot...
  * `load_words` **(I/O & Config Routines)** (Impact: 13.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 73 instances
* *State Mutation (weighted view):* 303
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 73`, `args: 46`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 157`, `dead_code: 8`, `unreferenced_by_name: 3`
* *Architecture:* `api: 12`, `import: 7`
* *Defense:* `safety: 27`, `doc: 3`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.935
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` fio.h, fio_cli.h, xxhash.c, xxhash.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `facil.io/lib/facil/legacy/fio_mem.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.309)
- **Top Global Matches:** file_cluster_16: 7.309, file_cluster_12: 7.554, file_cluster_4: 8.071
- **Magnitude:** 538.82 | **LOC:** 807 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 49.336; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (68.6%), Guard Balance (formerly Safety Score) (67.6%), Dead Code Surface (formerly Dead Code) (7.6%)
- **Documentation Coverage:** 84.7458% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fio_memcpy` **(Many-Argument Workhorses)** (Impact: 39.6)
    * *Intent:* ***************************************************************************** */
  * `sys_realloc` **(Stateful Encapsulated Methods)** (Impact: 15.5)
  * `fio_realloc2` **(Many-Argument Workhorses)** (Impact: 15.3)
    * *Intent:* /** * Re-allocates memory. An attept to avoid copying the data is made only for big * memory allocat...
  * `arena_lock` **(Stateful Encapsulated Methods)** (Impact: 15.0)
    * *Intent:* ***************************************************************************** */ /* returned a locke...
  * `fio_malloc_test` **(I/O & Config Routines)** (Impact: 14.1)
    * *Intent:* ***************************************************************************** */ #if DEBUG && !FIO_F...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 97 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 313
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 143`, `args: 69`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 119`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 22`, `import: 5`
* *Defense:* `safety: 54`, `doc: 16`, `immutability_locks: 5`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 49.336
  * `Choke Point (Betweenness):` 0.002276 | `Ripple Effect (Closeness):` 0.140343
  * `Imports (Out-Degree: 2):` fio_mem.h, pthread.h, mman.h, time.h, unistd.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/fio.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 10.012)
- **Top Global Matches:** file_cluster_14: 10.012, file_cluster_7: 11.301, file_cluster_5: 11.652
- **Magnitude:** 496.44 | **LOC:** 592 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **1**; blast radius 31.577; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (80.8%), Test Surface (formerly Verification) (80.0%), Dead Code Surface (formerly Dead Code) (15.5%)
- **Documentation Coverage:** 85.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fiobj_obj2cstr` **(Type Conversions)** (Impact: 12.4)
  * `fiobj_type_is` **(Type Conversions)** (Impact: 9.8)
  * `fiobj_type` **(Type Conversions)** (Impact: 8.9)
  * `fiobj_obj2num` **(Type Conversions)** (Impact: 7.5)
  * `fiobj_type_vtable` **(Type Conversions)** (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 67`, `args: 163`, `func_start: 137`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 125`, `dead_code: 6`
* *Architecture:* `api: 210`, `import: 13`
* *Defense:* `doc: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.577
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.146517
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `facil.io/lib/facil/tls/fio_tls_openssl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.355)
- **Top Global Matches:** file_cluster_12: 8.355, file_cluster_4: 8.806, file_cluster_16: 10.415
- **Magnitude:** 481.3 | **LOC:** 1017 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 1.935; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.5%), Debt Markers (formerly Tech Debt) (54.3%)
- **Documentation Coverage:** 40.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fio_tls_handshake` **(Many-Argument Workhorses)** (Impact: 56.5)
  * `fio_tls_build_context` **(Compute Cores)** (Impact: 37.6)
    * *Intent:* /** Called when the library specific data for the context should be built */
  * `fio_tls_read` **(Stateful Encapsulated Methods)** (Impact: 30.4)
    * *Intent:* /* TODO: this is an example implementation - fix for specific library. */ /** * Implement reading fr...
  * `fio_tls_write` **(Stateful Encapsulated Methods)** (Impact: 30.4)
    * *Intent:* /** * Implement writing to a file descriptor. Should behave like the file system * `write` call. * *...
  * `fio_tls_cert_add` **(Many-Argument Workhorses)** (Impact: 21.0)
    * *Intent:* /** * Adds a certificate a new SSL/TLS context / settings object. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 38 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 176`, `args: 54`, `func_start: 42`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 50`, `dead_code: 12`, `planned_debt: 12`, `unreferenced_by_name: 7`
* *Architecture:* `api: 20`, `import: 9`
* *Defense:* `safety: 12`, `doc: 24`, `immutability_locks: 23`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.935
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` fio.h, fio_tls.h, bio.h, err.h, ssl.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `facil.io/lib/facil/http/http1.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.934)
- **Top Global Matches:** file_cluster_12: 6.934, file_cluster_16: 7.071, file_cluster_4: 9.097
- **Magnitude:** 460.46 | **LOC:** 910 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 5.149; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.4%), Complexity Load (formerly Cognitive Load) (34.8%)
- **Documentation Coverage:** 41.6978% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `headers2str` **(Stateful Encapsulated Methods)** (Impact: 57.5)
  * `http1_consume_data` **(Stateful Encapsulated Methods)** (Impact: 26.3)
    * *Intent:* ***************************************************************************** */
  * `http1_http2websocket_server` **(Stateful Encapsulated Methods)** (Impact: 17.9)
  * `http1_new` **(Many-Argument Workhorses)** (Impact: 17.2)
    * *Intent:* ***************************************************************************** */ /** Creates an HTTP...
  * `http1_on_body_chunk` **(Stateful Encapsulated Methods)** (Impact: 15.0)
    * *Intent:* /** called when a body chunk is parsed. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 99`, `args: 53`, `func_start: 44`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 56`, `dead_code: 4`, `unreferenced_by_name: 12`
* *Architecture:* `api: 7`, `import: 8`
* *Defense:* `safety: 14`, `doc: 26`, `immutability_locks: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.149
  * `Choke Point (Betweenness):` 0.005752 | `Ripple Effect (Closeness):` 0.063815
  * `Imports (Out-Degree: 14):` assert.h, fio.h, fiobj.h, http1.h, http1_parser.h, http_internal.h, stddef.h, websockets.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `facil.io/tests/random.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.45)
- **Top Global Matches:** file_cluster_16: 5.45, file_cluster_15: 8.254, file_cluster_17: 8.673
- **Magnitude:** 453.56 | **LOC:** 735 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 1.935; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (79.0%), Complexity Load (formerly Cognitive Load) (35.1%), Connectivity (formerly Api Exposure) (0.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 23.1)
  * `scan_batch` **(Many-Argument Workhorses)** (Impact: 22.3)
    * *Intent:* significant digit is the most recent trit. n is the batch size. */ #if HWD_BITS == 32
  * `run_test` **(Stateful Encapsulated Methods)** (Impact: 21.5)
  * `compute_pvalue` **(Compute Cores)** (Impact: 18.8)
    * *Intent:* #endif
  * `scan_batch` **(Stateful Encapsulated Methods)** (Impact: 13.3)
    * *Intent:* #else
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 278
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 43`, `args: 28`, `func_start: 19`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 102`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 1`, `import: 13`
* *Defense:* `safety: 1`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.935
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` assert.h, fcntl.h, fio.h, float.h, inttypes.h, math.h, stdbool.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `facil.io/lib/facil/http/parsers/http_mime_parser.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.072)
- **Top Global Matches:** file_cluster_3: 7.072, file_cluster_8: 21.043, file_cluster_6: 33.883
- **Magnitude:** 439.44 | **LOC:** 351 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 2.668; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.5%), Complexity Load (formerly Cognitive Load) (48.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `http_mime_parse` **(Many-Argument Workhorses)** (Impact: 180.6)
    * *Intent:* /** * Consumes data from a streaming buffer. * * The data might be partially consumed, in which case...
  * `http_mime_parser_init` **(Stateful Encapsulated Methods)** (Impact: 21.6)
    * *Intent:* ***************************************************************************** */ /** takes the HTTP ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 231
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 25`, `args: 9`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 81`, `dead_code: 2`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 42`, `doc: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.668
  * `Choke Point (Betweenness):` 0.000467 | `Ripple Effect (Closeness):` 0.059763
  * `Imports (Out-Degree: 1):` stdint.h, stdlib.h, string.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `facil.io/lib/facil/redis/redis_engine.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.987)
- **Top Global Matches:** file_cluster_12: 6.987, file_cluster_16: 7.554, file_cluster_7: 9.302
- **Magnitude:** 435.26 | **LOC:** 955 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 2.573; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.8%), Debt Markers (formerly Tech Debt) (61.0%)
- **Documentation Coverage:** 56.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fiobj2resp___internal` **(Compute Cores)** (Impact: 23.0)
    * *Intent:* ***************************************************************************** */
  * `FIO_IGNORE_MACRO` **(Compute Cores)** (Impact: 23.0)
  * `resp_on_sub_message` **(Stateful Encapsulated Methods)** (Impact: 18.9)
    * *Intent:* ***************************************************************************** */ /** a local static ...
  * `redis_on_close` **(C Struct Operations)** (Impact: 15.6)
    * *Intent:* /** Called when the connection was closed, but will not run concurrently */
  * `redis_on_connect` **(C Struct Operations)** (Impact: 14.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 146`, `args: 56`, `func_start: 46`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 81`, `dead_code: 7`, `planned_debt: 3`, `unreferenced_by_name: 13`
* *Architecture:* `api: 6`, `import: 4`
* *Defense:* `safety: 7`, `doc: 25`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.573
  * `Choke Point (Betweenness):` 0.001592 | `Ripple Effect (Closeness):` 0.019277
  * `Imports (Out-Degree: 12):` fio.h, fiobj.h, redis_engine.h, resp_parser.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `facil.io/lib/facil/http/websockets.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.059)
- **Top Global Matches:** file_cluster_12: 7.059, file_cluster_7: 8.562, file_cluster_5: 9.313
- **Magnitude:** 424.26 | **LOC:** 732 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **12**; blast radius 5.066; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.2%), Debt Markers (formerly Tech Debt) (38.8%)
- **Documentation Coverage:** 52.1222% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `websocket_on_pubsub_message_direct_internal` **(Stateful Encapsulated Methods)** (Impact: 23.1)
  * `websocket_write_impl` **(Stateful Encapsulated Methods)** (Impact: 20.9)
  * `websocket_attach` **(Many-Argument Workhorses)** (Impact: 19.4)
  * `websocket_optimize4broadcasts` **(Stateful Encapsulated Methods)** (Impact: 18.9)
    * *Intent:* * consumption (minimize duplication or WebSocket network data). * * This function allows enablement ...
  * `websocket_on_unwrapped` **(Stateful Encapsulated Methods)** (Impact: 18.1)
    * *Intent:* ***************************************************************************** */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 45 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 148
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 139`, `args: 52`, `func_start: 39`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 58`, `unreferenced_by_name: 11`
* *Architecture:* `api: 19`, `import: 13`
* *Defense:* `safety: 7`, `doc: 32`, `immutability_locks: 4`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.066
  * `Choke Point (Betweenness):` 0.003333 | `Ripple Effect (Closeness):` 0.056195
  * `Imports (Out-Degree: 8):` inet.h, endian.h, errno.h, fio.h, fiobj.h, http.h, http_internal.h, stdio.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `facil.io/lib/facil/cli/fio_cli.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.396)
- **Top Global Matches:** file_cluster_8: 7.396, file_cluster_6: 11.644, file_cluster_4: 19.978
- **Magnitude:** 421.82 | **LOC:** 432 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **7**; blast radius 6.864; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (80.0%), Guard Balance (formerly Safety Score) (65.5%)
- **Documentation Coverage:** 61.5385% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fio_cli_set_arg` **(Many-Argument Workhorses)** (Impact: 167.9)
  * `AVOID_MACRO` **(Many-Argument Workhorses)** (Impact: 61.7)
  * `fio_cli_get_line_type` **(Stateful Encapsulated Methods)** (Impact: 29.4)
  * `fio_cli_map_line2alias` **(Stateful Encapsulated Methods)** (Impact: 13.9)
    * *Intent:* ***************************************************************************** */
  * `fio_cli_unnamed` **(Compute Cores)** (Impact: 4.6)
    * *Intent:* /** Returns the unrecognized argument using a 0 based `index`. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 41`, `args: 15`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 40`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `api: 9`, `import: 8`
* *Defense:* `safety: 8`, `doc: 6`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.864
  * `Choke Point (Betweenness):` 0.000274 | `Ripple Effect (Closeness):` 0.084714
  * `Imports (Out-Degree: 3):` fio.h, fio_cli.h, stdint.h, stdio.h, stdlib.h, string.h, strings.h
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `facil.io/lib/facil/fiobj/fiobj_json.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.933)
- **Top Global Matches:** file_cluster_4: 7.933, file_cluster_6: 10.75, file_cluster_12: 11.695
- **Magnitude:** 421.56 | **LOC:** 623 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 3.181; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.6%), Complexity Load (formerly Cognitive Load) (59.3%)
- **Documentation Coverage:** 24.7124% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fiobj_obj2json_task` **(Many-Argument Workhorses)** (Impact: 53.3)
  * `write_safe_str` **(Many-Argument Workhorses)** (Impact: 46.2)
    * *Intent:* ***************************************************************************** */ /** Writes a JSON f...
  * `fiobj_obj2json2` **(Many-Argument Workhorses)** (Impact: 13.1)
    * *Intent:* /** * Formats an object into a JSON string, appending the JSON string to an * existing String. Remem...
  * `fiobj_json_add2parser` **(Stateful Encapsulated Methods)** (Impact: 13.0)
    * *Intent:* ***************************************************************************** */
  * `fiobj_test_json` **(I/O & Config Routines)** (Impact: 10.6)
    * *Intent:* ***************************************************************************** */ #if DEBUG
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 223
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 69`, `args: 45`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 17`, `high_risk_execution: 1`, `state_mutation: 89`, `dead_code: 2`, `unreferenced_by_name: 13`
* *Architecture:* `api: 9`, `import: 8`
* *Defense:* `safety: 15`, `doc: 17`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.181
  * `Choke Point (Betweenness):` 0.00163 | `Ripple Effect (Closeness):` 0.082702
  * `Imports (Out-Degree: 10):` assert.h, ctype.h, fio.h, fio_json_parser.h, fiobj_json.h, math.h, stdlib.h, string.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/request.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.792)
- **Top Global Matches:** file_cluster_12: 7.792, file_cluster_4: 9.246, file_cluster_5: 9.804
- **Magnitude:** 419.56 | **LOC:** 947 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 8.802; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (68.6%), Mutation Surface (formerly State Flux) (56.8%), Guard Balance (formerly Safety Score) (45.3%)
- **Documentation Coverage:** 18.2796% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseBinfilesFrom` **(Many-Argument Workhorses)** (Impact: 49.5)
  * `setCookie` **(Type Conversions)** (Impact: 30.6)
    * *Intent:* /// Set a response cookie
  * `parseAcceptHeaders` **(Defensive Guards)** (Impact: 28.2)
    * *Intent:* /// Parses `Accept:` http header into `list`, ordered from highest q factor to lowest
  * `getParamSlice` **(Defensive Guards)** (Impact: 11.2)
    * *Intent:* /// similar to getParamStr, except it will return the part of the querystring /// after the equals s...
  * `format` **(Defensive Guards)** (Impact: 9.2)
    * *Intent:* /// format function for printing file upload data
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 11 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 106`, `args: 47`, `func_start: 47`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 22`, `dead_code: 1`, `planned_debt: 6`, `fragile_debt: 3`
* *Architecture:* `io: 3`, `api: 61`, `import: 5`
* *Defense:* `safety: 65`, `doc: 157`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.802
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.131041
  * `Imports (Out-Degree: 4):` fio.zig, http.zig, std, util.zig, zap.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `facil.io/lib/facil/fiobj/fiobject.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.206)
- **Top Global Matches:** file_cluster_16: 6.206, file_cluster_15: 7.401, file_cluster_12: 8.057
- **Magnitude:** 354.52 | **LOC:** 621 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **10**; blast radius 8.995; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.2%), Complexity Load (formerly Cognitive Load) (57.5%)
- **Documentation Coverage:** 66.7556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fiobj_each2` **(Many-Argument Workhorses)** (Impact: 24.0)
    * *Intent:* * (unlike `fiobj_each2`). * * The callback task function must accept an object and an opaque user po...
  * `fiobj_iseq____internal_complex__` **(Compute Cores)** (Impact: 17.5)
    * *Intent:* /** used internally for complext nested tests (Array / Hash types) */
  * `fiobj_iseq_simple` **(Stateful Encapsulated Methods)** (Impact: 14.5)
    * *Intent:* ***************************************************************************** */ #include <fiobj_has...
  * `fiobj_dealloc_task` **(Stateful Encapsulated Methods)** (Impact: 11.2)
    * *Intent:* ***************************************************************************** */
  * `fiobj_task_wrapper` **(C Struct Operations)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 70 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 215
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 89`, `args: 33`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 75`, `dead_code: 5`, `unreferenced_by_name: 10`
* *Architecture:* `api: 24`, `import: 10`
* *Defense:* `safety: 15`, `doc: 9`, `immutability_locks: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.995
  * `Choke Point (Betweenness):` 0.002236 | `Ripple Effect (Closeness):` 0.12497
  * `Imports (Out-Degree: 8):` fio.h, fiobj_ary.h, fiobj_hash.h, fiobj_numbers.h, fiobject.h, stdarg.h, stdint.h, stdio.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/App.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.808)
- **Top Global Matches:** file_cluster_12: 8.808, file_cluster_4: 9.087, file_cluster_5: 9.741
- **Magnitude:** 347.12 | **LOC:** 501 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 10.382; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (61.0%), Guard Balance (formerly Safety Score) (44.7%), Mutation Surface (formerly State Flux) (36.9%), Complexity Load (formerly Cognitive Load) (19.5%)
- **Documentation Coverage:** 49.3671% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Create` **(Defensive Guards)** (Impact: 106.4)
    * *Intent:* /// creates an App with custom app context /// /// About App Contexts: /// /// ```zig /// const MyCo...
  * `checkEndpointType` **(Compute Cores)** (Impact: 25.2)
  * `onRequest` **(Defensive Guards)** (Impact: 21.4)
  * `onRequest` **(Defensive Guards)** (Impact: 20.2)
  * `Authenticating` **(Defensive Guards)** (Impact: 18.1)
    * *Intent:* /// Wrap an endpoint with an Authenticator
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 5 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 26`, `args: 30`, `func_start: 24`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 8`, `planned_debt: 1`
* *Architecture:* `api: 27`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 37`, `doc: 55`, `sync_locks: 7`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.382
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.135612
  * `Imports (Out-Degree: 1):` std, zap.zig
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/http_auth.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.305)
- **Top Global Matches:** file_cluster_4: 7.305, file_cluster_6: 10.365, file_cluster_12: 12.036
- **Magnitude:** 336.08 | **LOC:** 615 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 15.214; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (68.3%), Guard Balance (formerly Safety Score) (35.7%), Debt Markers (formerly Tech Debt) (13.3%), Complexity Load (formerly Cognitive Load) (4.6%)
- **Documentation Coverage:** 14.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `UserPassSession` **(Defensive Guards)** (Impact: 65.5)
    * *Intent:* /// /// Comptime Parameters: /// /// - `Lookup` must implement .get([]const u8) -> []const u8 for us...
  * `_internal_authenticateRequest` **(Defensive Guards)** (Impact: 42.6)
  * `Basic` **(Defensive Guards)** (Impact: 37.6)
    * *Intent:* /// HTTP Basic Authentication RFC 7617. /// "Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==" /// ...
  * `authenticateUserPass` **(Defensive Guards)** (Impact: 18.6)
    * *Intent:* /// Use this to decode the auth_header into user:pass, lookup pass in lookup. /// Note: usually, you...
  * `logout` **(Defensive Guards)** (Impact: 13.8)
    * *Intent:* /// Check for session token cookie, remove the token from the valid tokens
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 17 instances
* *Memory Alloc (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 64`, `args: 30`, `func_start: 30`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `planned_debt: 5`
* *Architecture:* `api: 30`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 56`, `doc: 132`, `sync_locks: 10`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.214
  * `Choke Point (Betweenness):` 0.000134 | `Ripple Effect (Closeness):` 0.135612
  * `Imports (Out-Degree: 1):` std, zap.zig
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `facil.io/tests/slowloris.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.96)
- **Top Global Matches:** file_cluster_8: 6.96, file_cluster_6: 17.253, file_cluster_3: 20.139
- **Magnitude:** 315.26 | **LOC:** 548 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 1.935; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (59.2%), Concurrency Surface (formerly Concurrency) (53.6%), Complexity Load (formerly Cognitive Load) (29.8%), Dead Code Surface (formerly Dead Code) (8.8%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 50.1)
    * *Intent:* ***************************************************************************** */
  * `test_server` **(Compute Cores)** (Impact: 28.4)
    * *Intent:* ***************************************************************************** */
  * `attack_server` **(Compute Cores)** (Impact: 25.4)
    * *Intent:* ***************************************************************************** */
  * `wait__internal` **(C Struct Operations)** (Impact: 18.6)
    * *Intent:* ***************************************************************************** */ /** Waits for socke...
  * `test_server_task` **(Stateful Encapsulated Methods)** (Impact: 15.5)
    * *Intent:* /* a single tester thread */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 44 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 67`, `args: 33`, `func_start: 9`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 46`, `dead_code: 4`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 2`, `concurrency: 2`, `import: 30`
* *Defense:* `safety: 21`, `doc: 9`, `test: 8`, `immutability_locks: 8`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.935
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` inet.h, ctype.h, errno.h, fcntl.h, limits.h, netdb.h, in.h, tcp.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `facil.io/lib/facil/fiobj/fio_json_parser.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.179)
- **Top Global Matches:** file_cluster_8: 7.179, file_cluster_6: 17.485, file_cluster_3: 20.064
- **Magnitude:** 305.04 | **LOC:** 688 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 2.411; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.1%), Complexity Load (formerly Cognitive Load) (47.4%)
- **Documentation Coverage:** 45.8945% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `seek2marker` **(Many-Argument Workhorses)** (Impact: 31.3)
    * *Intent:* ***************************************************************************** */ /** * finds the fir...
  * `utf8_from_u32` **(Stateful Encapsulated Methods)** (Impact: 11.4)
    * *Intent:* ***************************************************************************** */ #ifdef __cplusplus ...
  * `seek2eos` **(Stateful Encapsulated Methods)** (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 79 instances
* *State Mutation (weighted view):* 241
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 59`, `args: 25`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 83`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `safety: 16`, `doc: 22`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.06231
  * `Imports (Out-Degree: 0):` ctype.h, math.h, stdint.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `facil.io/lib/facil/http/http1.c` (C) | Magnitude: 460.46 | Delta: **0.137** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 606, pointers: 387, branch: 110, structural_boundaries: 99

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `facil.io/tests/parse_url.c` (C) | Magnitude: 5.92 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 18, explicit_casts: 8, structural_boundaries: 2, branch: 1
- `facil.io/lib/facil/http/http_internal.c` (C) | Magnitude: 132.84 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1181, args: 72, core_var_decl: 43, state_mutation: 36
- `facil.io/lib/facil/fiobj/fiobj_hash.c` (C) | Magnitude: 176.9 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 166, pointers: 98, args: 42, structural_boundaries: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/app/auth.zig` (ZIG) | Magnitude: 16.74 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 66, core_var_decl: 19, design_snake_case: 11, structural_boundaries: 9
- `facil.io/makefile` (MAKEFILE) | Magnitude: 110.26 | Delta: **0.12** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 203, structural_boundaries: 131, io: 106, core_var_decl: 62
- `src/tests/test_recvfile_notype.zig` (ZIG) | Magnitude: 18.14 | Delta: **0.15** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 89, safety: 26, core_var_decl: 21, structural_boundaries: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `facil.io/tests/collisions.c` (C) | Magnitude: 547.04 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 552, state_mutation: 157, pointers: 123, bitwise_ops: 109

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/zap.zig` -> **Severity: 1.405** (Bridge: 0.0198 * Flux: 70.9739%)
- `facil.io/lib/facil/http/http.c` -> **Severity: 1.171** (Bridge: 0.0117 * Flux: 100.0%)
- `facil.io/lib/facil/http/http1.c` -> **Severity: 0.57** (Bridge: 0.0058 * Flux: 99.1774%)
- `facil.io/lib/facil/fio.c` -> **Severity: 0.445** (Bridge: 0.0044 * Flux: 99.9997%)
- `facil.io/lib/facil/http/websockets.c` -> **Severity: 0.333** (Bridge: 0.0033 * Flux: 99.9787%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `facil.io/lib/facil/fio.h` -> **Severity: 15.544** (Embedded: 0.2693 * Error Risk: 57.7273%)
- `facil.io/lib/facil/fio.c` -> **Severity: 15.05** (Embedded: 0.2185 * Error Risk: 68.8908%)
- `src/fio.zig` -> **Severity: 11.843** (Embedded: 0.1465 * Error Risk: 80.8309%)
- `src/zap.zig` -> **Severity: 11.363** (Embedded: 0.2535 * Error Risk: 44.8187%)
- `facil.io/lib/facil/fiobj/fiobj_numbers.c` -> **Severity: 10.247** (Embedded: 0.1301 * Error Risk: 78.7805%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `facil.io/lib/facil/fio.c` -> **Severity: 6720.775** (Blast Radius: 111.016 * Doc Risk: 60.5388%)
- `facil.io/lib/facil/legacy/fio_mem.c` -> **Severity: 4181.019** (Blast Radius: 49.336 * Doc Risk: 84.7458%)
- `src/fio.zig` -> **Severity: 2684.045** (Blast Radius: 31.577 * Doc Risk: 85.0%)
- `facil.io/lib/facil/fiobj/fiobject.h` -> **Severity: 1129.004** (Blast Radius: 34.85 * Doc Risk: 32.3961%)
- `src/Logging.zig` -> **Severity: 782.4** (Blast Radius: 8.802 * Doc Risk: 88.8889%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 632 literal sites + 1 sites through wrappers = 633
- **`memory_alloc`:** 219 literal sites + 47 sites through wrappers = 266
- **`panics_and_aborts`:** 352 literal sites + 8 sites through wrappers = 360

- `FIO_MALLOC` (macro, memory_alloc, primitive): 7 call sites in 1 files -- `facil.io/lib/facil/fio.h`
- `fio_timer_clear_all` (function, memory_alloc, primitive): 6 call sites in 1 files -- `facil.io/lib/facil/fio.c`
- `fio_ls_push` (function, memory_alloc, via FIO_MALLOC): 4 call sites in 4 files -- `facil.io/lib/facil/fio.h`
- `fio_str_new2` (function, memory_alloc, via FIO_MALLOC): 4 call sites in 3 files -- `facil.io/lib/facil/fio.h`
- `mustache_free` (function, memory_alloc, primitive): 4 call sites in 2 files -- `facil.io/lib/facil/fiobj/mustache_parser.h`
- `fio_defer_thread_pool_join` (function, memory_alloc, primitive): 3 call sites in 1 files -- `facil.io/lib/facil/fio.c`
- `http_settings_free` (function, memory_alloc, primitive): 3 call sites in 1 files -- `facil.io/lib/facil/http/http.c`
- `fio_channel_free` (function, memory_alloc, primitive): 2 call sites in 1 files -- `facil.io/lib/facil/fio.c`
- `fio_subscription_free` (function, memory_alloc, via fio_channel_free): 2 call sites in 1 files -- `facil.io/lib/facil/fio.c`
- `fio_tls_accept` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `facil.io/lib/facil/fio.c`
- `fio_tls_connect` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `facil.io/lib/facil/fio.c`
- `fio_tls_destroy` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `facil.io/lib/facil/fio.c`
*(+11 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 6862 call pairs -- scoped 30.8%, unique 11.7%, ambiguous 3.7%, external 53.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 5002 | 32.2% | 16.0% | 2.3% | 49.4% |
| zig | 1782 | 27.3% | 0.0% | 7.6% | 65.1% |
| html | 40 | 32.5% | 0.0% | 0.0% | 67.5% |
| javascript | 25 | 4.0% | 0.0% | 0.0% | 96.0% |
| shell | 13 | 0.0% | 0.0% | 0.0% | 100.0% |

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
