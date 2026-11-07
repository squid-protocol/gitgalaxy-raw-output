# ARCHITECTURAL_BRIEF: node
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/nodejs/node` |
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
- **Scope:** 8761 analyzed artifact(s), 605408 LOC.
- **Load-bearing artifact:** `test/common/tmpdir.js` -- 751 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `doc/api/index.md` -- pulls in 66 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `.npmrc` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 47394 |
| Analyzed Artifacts (Scanned) | 8761 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 38633 |
| Total LOC | 605408 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 18.5% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7377 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2936 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.2833 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 248 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 7258 | 445289 | 82.8% |
| CPP | 542 | 136818 | 6.2% |
| PLAINTEXT | 251 | 125 | 2.9% |
| MARKDOWN | 180 | 0 | 2.1% |
| PYTHON | 156 | 7039 | 1.8% |
| TYPESCRIPT | 119 | 2837 | 1.4% |
| JSON | 116 | 2577 | 1.3% |
| C | 108 | 7402 | 1.2% |
| BMS | 18 | 86 | 0.2% |
| SHELL | 4 | 128 | 0.0% |
| MAKEFILE | 3 | 2177 | 0.0% |
| YAML | 1 | 10 | 0.0% |
| NIX | 1 | 99 | 0.0% |
| ASSEMBLY | 1 | 25 | 0.0% |
| XML | 1 | 0 | 0.0% |
| M4 | 1 | 2 | 0.0% |
| BATCH | 1 | 794 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 8639 |
| unknown | unknown | 121 |
| utf-8 | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 41%, Data / Markup / Trivial 19%, Large Core Modules (2) 9%, Callbacks & Closures Files 9%, State Mutators Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 8326 | 95.0% |
| Unknown | 121 | 1.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 308 | 3.5% |
| Static: Minified & Vendor Opaque Mass | 6 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 38633*

**Composition by Extension & Reason:**
- `.js`: 13092x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 16x Excluded: Neighborhood Micro-Mass Limit Exceeded, 8x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.h`: 6986x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.c`: 2734x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cc`: 2684x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 1394x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 10x Unsupported Format (.undeterminable), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.txt`: 1153x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.rs`: 979x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cpp`: 850x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 841x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3866 LOC)
- `.s`: 775x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.hpp`: 635x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 525x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Static Asset Blob without Intent: 1009 LOC)
- `.py`: 527x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 437x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 4636 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2904 LOC)
- `.mjs`: 410x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 24x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Saturation: Line 10 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 10.5 | 2.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.6 | 29.6 | 45.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 22.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 10.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.5 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 76.9 | 1.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 40.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 7627 | 1239 | 1 | `src/cares_wrap.cc` |
| cleanup | 4435 | 1896 | 2 | `test/parallel/test-readline-interface.js` |
| guards | 32639 | 3179 | 6 | `lib/internal/util/inspect.js` |
| danger | 8565 | 2094 | 2 | `test/fixtures/keys/Makefile` |
| concurrency | 20531 | 2552 | 5 | `test/parallel/test-runner-mock-timers.js` |
| connectivity | 4854 | 1374 | 1 | `typings/primordials.d.ts` |
| io | 12806 | 3176 | 4 | `test/parallel/test-fs-null-bytes.js` |
| crypto | 503 | 449 | 0 | `test/parallel/test-crypto-fips.js` |
| ipc | 3710 | 1408 | 1 | `src/stream_pipe.cc` |
| time | 2149 | 787 | 0 | `test/parallel/test-runner-mock-timers.js` |
| serialization | 595 | 288 | 0 | `test/parallel/test-mime-api.js` |
| regex | 2523 | 710 | 0 | `test/parallel/test-runner-cli.js` |
| events | 20206 | 2892 | 6 | `test/parallel/test-readline-interface.js` |
| tests | 40544 | 4866 | 10 | `test/parallel/test-runner-mocking.js` |
| docs | 1888 | 249 | 0 | `lib/internal/quic/quic.js` |
| debt | 4626 | 1508 | 1 | `Makefile` |
| mutation | 122276 | 7366 | 26 | `configure.py` |
| dead_code | 4910 | 1079 | 1 | `src/js_native_api_v8.cc` |
| credential | 2963 | 30 | 0 | `src/node_root_certs.h` |
| threat | 213 | 59 | 0 | `test/parallel/test-punycode.js` |
| ml_ai | 58 | 7 | 0 | `typings/primordials.d.ts` |
| ui | 141 | 35 | 0 | `test/parallel/test-util-inspect.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/parallel/test-fs-null-bytes.js` (Hits: 184)
- `Makefile` (Hits: 169)
- `test/parallel/test-trace-events-fs-async.js` (Hits: 165)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **tmpdir.js** (`test/common/tmpdir.js`) — 751 inbound connections
2. **common.js** (`benchmark/common.js`) — 451 inbound connections
3. **h.cjs** (`test/fixtures/test-runner/shards/h.cjs`) — 441 inbound connections
4. **index.mjs** (`test/common/index.mjs`) — 315 inbound connections
5. **errors.js** (`lib/internal/errors.js`) — 228 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.md** (`doc/api/index.md`) — 66 outbound dependencies
2. **node.cc** (`src/node.cc`) — 59 outbound dependencies
3. **env.h** (`src/env.h`) — 40 outbound dependencies
4. **test-module-loading.js** (`test/sequential/test-module-loading.js`) — 39 outbound dependencies
5. **inspector_agent.cc** (`src/inspector_agent.cc`) — 39 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `formatIterator` **(Many-Argument Workhorses)** (@ `lib/internal/util/inspect.js`) -> Impact: **423.3** | LOC: 551
- `constructor` **(Many-Argument Workhorses)** (@ `lib/repl.js`) -> Impact: **415.5** | LOC: 690
- `isRecoverableError` **(Many-Argument Workhorses)** (@ `lib/internal/repl/utils.js`) -> Impact: **302.4** | LOC: 782
  * *Intent:* // If the error is that we've unexpectedly ended the input, // then let the user try to recover by adding more input. // Note: `e` (the original excep...
- `formatRaw` **(Many-Argument Workhorses)** (@ `lib/internal/util/inspect.js`) -> Impact: **294.3** | LOC: 295
- `WriteByteVectorLiteral` **(Many-Argument Workhorses)** (@ `src/node_snapshotable.cc`) -> Impact: **277.8** | LOC: 1000
- `objectComparisonStart` **(Many-Argument Workhorses)** (@ `lib/internal/util/comparisons.js`) -> Impact: **271.9** | LOC: 160
- `parse` **(Many-Argument Workhorses)** (@ `lib/url.js`) -> Impact: **260.5** | LOC: 330
- `emitKeys` **(Compute Cores)** (@ `lib/internal/readline/utils.js`) -> Impact: **211.2** | LOC: 293
  * *Intent:* */
- `OptionsParser::Parse` **(Many-Argument Workhorses)** (@ `src/node_options-inl.h`) -> Impact: **208.3** | LOC: 197
- `setupPreview` **(Many-Argument Workhorses)** (@ `lib/internal/repl/utils.js`) -> Impact: **199.9** | LOC: 376

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `test/fixtures/keys` | 101 | 490000.25 | 0.0% | 0.0% |
| `test/parallel` | 4082 | 101581.71 | 7.34% | 0.0% |
| `deps/openssl/openssl/apps` | 14 | 70000.0 | 0.0% | 0.0% |
| `src` | 264 | 41399.12 | 17.94% | 29.5% |
| `lib` | 55 | 22042.8 | 46.34% | 3.9% |
| `lib/internal` | 53 | 10398.71 | 45.68% | 5.89% |
| `test/es-module` | 223 | 8901.96 | 8.52% | 0.0% |
| `__monolith__` | 24 | 8035.16 | 10.64% | 2.5% |
| `lib/internal/streams` | 19 | 6230.98 | 67.03% | 13.47% |
| `lib/internal/util` | 8 | 5307.36 | 46.81% | 2.04% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `benchmark/async_hooks/promises.js` -> **100.0%** Exposure
- `typings/internalBinding/buffer.d.ts` -> **100.0%** Exposure
- `typings/internalBinding/http_parser.d.ts` -> **100.0%** Exposure
- `typings/internalBinding/inspector.d.ts` -> **100.0%** Exposure
- `typings/internalBinding/messaging.d.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `android_configure.py` -> **100.0%** Exposure
- `configure.py` -> **100.0%** Exposure
- `benchmark/_cli.js` -> **100.0%** Exposure
- `benchmark/_http-benchmarkers.js` -> **100.0%** Exposure
- `benchmark/assert/deepequal-buffer.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/js_native_api_v8.cc` -> **137** Orphaned Functions | **2** Duplicates
- `src/node_http2.cc` -> **105** Orphaned Functions | **0** Duplicates
- `src/env.cc` -> **89** Orphaned Functions | **0** Duplicates
- `src/quic/session.cc` -> **88** Orphaned Functions | **0** Duplicates
- `src/crypto/crypto_tls.cc` -> **79** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `test/parallel/test-crypto.js` -> **100.0%** Exposure
- `test/parallel/test-tls-use-after-free-regression.js` -> **100.0%** Exposure
- `src/node_root_certs.h` -> **100.0%** Exposure
- `test/parallel/test-tls-cert-ext-encoding.js` -> **99.9999%** Exposure
- `test/parallel/test-tls-root-certificates.js` -> **99.999%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `9` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `20086` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/npm/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/openssl/openssl/apps/ca-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/openssl/openssl/apps/client.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/openssl/openssl/apps/dsa-ca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/openssl/openssl/apps/dsa-pca.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/openssl/openssl/apps/dsa1024.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/openssl/openssl/apps/dsa512.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/openssl/openssl/apps/dsap.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/openssl/openssl/apps/pca-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/openssl/openssl/apps/privkey.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/openssl/openssl/apps/rsa8192.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/openssl/openssl/apps/s1024key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/openssl/openssl/apps/s512-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/openssl/openssl/apps/server.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `deps/openssl/openssl/apps/server2.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/fixtures/0-dns/0-dns-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/fixtures/dotenv/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/fixtures/keys/agent1-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/fixtures/keys/agent1.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/fixtures/keys/agent10-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/fixtures/keys/agent10.pfx` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/fixtures/keys/agent11-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/fixtures/keys/agent2-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/fixtures/keys/agent3-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.058
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/inspector/main_thread_interface.cc` (CPP) | Magnitude: 142.62 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 191, structural_boundaries: 73, args: 49, func_start: 41
- `src/memory_tracker.h` (CPP) | Magnitude: 25.96 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 144, indent_spaces: 135, immutability_locks: 99, core_var_decl: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `test/parallel/test-fs-cp-async-filter-child-folder.mjs` (JAVASCRIPT) | Magnitude: 1.9 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 8, import: 6, indent_spaces: 3, core_var_decl: 3
- `test/parallel/test-console-diagnostics-channels.js` (JAVASCRIPT) | Magnitude: 25.1 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 37, core_var_decl: 15, design_snake_case: 12, state_mutation: 5
- `lib/internal/streams/duplex.js` (JAVASCRIPT) | Magnitude: 134.58 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 104, state_mutation: 29, reflection_metaprogramming: 28, branch: 23
- `test/pseudo-tty/test-assert-colors.js` (JAVASCRIPT) | Magnitude: 3.46 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 11, test: 9, args: 7
- `test/parallel/test-net-write-cb-on-destroy-before-connect.js` (JAVASCRIPT) | Magnitude: 15.38 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 12, core_var_decl: 5, design_snake_case: 5, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `test/parallel/test-fs-promises-file-handle-write.js` (JAVASCRIPT) | Magnitude: 26.88 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 40, core_var_decl: 21, concurrency: 18, structural_boundaries: 15
- `src/tracing/agent.h` (CPP) | Magnitude: 62.38 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 63, args: 22, immutability_locks: 17
- `test/wasi/test-wasi-start-validation.js` (JAVASCRIPT) | Magnitude: 27.72 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 117, structural_boundaries: 28, core_var_decl: 25, design_snake_case: 24
- `lib/internal/async_local_storage/async_hooks.js` (JAVASCRIPT) | Magnitude: 69.2 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 14, args: 14, func_start: 13
- `lib/internal/js_stream_socket.js` (JAVASCRIPT) | Magnitude: 147.12 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 151, structural_boundaries: 37, state_mutation: 29, args: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `test/sequential/test-cli-syntax-bad.js` (JAVASCRIPT) | Magnitude: 8.66 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 7, args: 5, test: 5
- `test/parallel/test-inspector-network-arbitrary-data.js` (JAVASCRIPT) | Magnitude: 19.66 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 21, core_var_decl: 7, import: 6, design_snake_case: 5
- `src/crypto/crypto_kmac.cc` (CPP) | Magnitude: 1.28 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 134, structural_boundaries: 46, pointers: 41, branch: 30
- `src/tty_wrap.h` (CPP) | Magnitude: 16.64 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 11, args: 5, macros: 4
- `test/addons/openssl-client-cert-engine/testengine.cc` (CPP) | Magnitude: 34.4 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 12, args: 10, import: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `test/parallel/test-debugger-watchers.mjs` (JAVASCRIPT) | Magnitude: 16.52 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 19, concurrency: 14, test: 12
- `test/fixtures/es-module-loaders/hooks-initialize.mjs` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 3, args: 1, func_start: 1, io: 1
- `test/parallel/test-compile-cache-api-options-portable-env.js` (JAVASCRIPT) | Magnitude: 14.28 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 54, test: 12, regex_execution: 12, io: 10
- `test/parallel/test-compile-cache-api-env.js` (JAVASCRIPT) | Magnitude: 14.24 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 63, test: 14, regex_execution: 12, core_var_decl: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `test/fixtures/test-runner/root-duration.mjs` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 3, args: 2, closures: 2, thread_sleeps: 2
- `test/fixtures/test-runner/output/coverage-with-mock.mjs` (JAVASCRIPT) | Magnitude: 0.01 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 7, test_skip: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/node_options.h` (CPP) | Magnitude: 82.06 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 430, core_var_decl: 177, design_snake_case: 173, structural_boundaries: 127
- `test/parallel/test-tls-get-ca-certificates-worker-no-use-system-ca.js` (JAVASCRIPT) | Magnitude: 18.02 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 31, core_var_decl: 10, concurrency: 9, structural_boundaries: 6
- `test/parallel/test-http2-create-client-secure-session.js` (JAVASCRIPT) | Magnitude: 20.7 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 63, core_var_decl: 13, test: 10, design_snake_case: 10
- `benchmark/buffers/buffer-compare.js` (JAVASCRIPT) | Magnitude: 9.72 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 10, core_var_decl: 5, design_snake_case: 5, design_short_vars: 3
- `src/inspector_profiler.h` (CPP) | Magnitude: 33.82 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 46, safety: 27, immutability_locks: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `test/js-native-api/test_number/test_number.c` (C) | Magnitude: 16.26 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 62, pointers: 21, structural_boundaries: 5, args: 5
- `test/js-native-api/test_promise/test_promise.c` (C) | Magnitude: 19.86 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 33, pointers: 11, structural_boundaries: 7, args: 4
- `test/js-native-api/test_sharedarraybuffer/test_sharedarraybuffer.c` (C) | Magnitude: 32.1 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 81, pointers: 25, structural_boundaries: 12, safety: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/callback_queue.h` (CPP) | Magnitude: 19.02 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 30, safety: 10, args: 9
- `src/crypto/crypto_argon2.h` (CPP) | Magnitude: 0.03 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 13, args: 13, immutability_locks: 9
- `test/fixtures/keys/selfsigned-no-keycertsign/https_renew_cert.sh` (SHELL) | Magnitude: 0.0 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 2, branch: 1, safety: 1
- `test/cctest/test_string_bytes.cc` (CPP) | Magnitude: 13.56 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 53, test: 15, core_var_decl: 12, design_snake_case: 12
- `test/cctest/inspector/test_node_protocol.cc` (CPP) | Magnitude: 3.16 | Delta: **0.122** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 14, core_var_decl: 6, pointers: 5, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `test/fixtures/workload/fibonacci-sigint.js` (JAVASCRIPT) | Magnitude: 0.0 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 3, structural_boundaries: 2, safety: 2, indent_spaces: 2
- `test/parallel/test-crypto-keygen-async-elliptic-curve-jwk-rsa.js` (JAVASCRIPT) | Magnitude: 15.68 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 26, test: 14, safety: 10, import: 3
- `benchmark/crypto/rsa-encrypt-decrypt-throughput.js` (JAVASCRIPT) | Magnitude: 0.13 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 20, core_var_decl: 17, design_snake_case: 13, io: 6
- `test/addons/stringbytes-external-exceed-max/test-stringbytes-external-exceed-max-by-1-binary.js` (JAVASCRIPT) | Magnitude: 20.66 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 10, core_var_decl: 10, design_camel_case: 6, import: 4
- `test/parallel/test-webcrypto-export-import.js` (JAVASCRIPT) | Magnitude: 95.88 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 355, concurrency: 60, test: 56, structural_boundaries: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/api/embed_helpers.cc` (CPP) | Magnitude: 138.98 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 221, pointers: 102, structural_boundaries: 47, branch: 35
- `test/common/child_process.js` (JAVASCRIPT) | Magnitude: 142.38 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 119, branch: 29, safety: 29, core_var_decl: 19
- `src/crypto/crypto_context.cc` (CPP) | Magnitude: 10.62 | Delta: **0.129** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1557, pointers: 380, branch: 319, structural_boundaries: 286
- `lib/internal/fs/cp/cp.js` (JAVASCRIPT) | Magnitude: 263.38 | Delta: **0.132** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 283, structural_boundaries: 68, branch: 60, concurrency: 38
- `src/stream_base.cc` (CPP) | Magnitude: 422.7 | Delta: **0.134** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 567, pointers: 208, structural_boundaries: 113, branch: 102

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `test/parallel/test-buffer-bytelength.js` (JAVASCRIPT) | Magnitude: 19.96 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: test: 46, indent_spaces: 22, core_var_decl: 19, design_snake_case: 18
- `test/parallel/test-experimental-shared-value-conveyor.js` (JAVASCRIPT) | Magnitude: 41.62 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 23, core_var_decl: 7, design_snake_case: 7, ipc_rpc_bridges: 6
- `test/parallel/test-runner-plan.mjs` (JAVASCRIPT) | Magnitude: 39.46 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 114, structural_boundaries: 35, concurrency: 22, events: 22
- `lib/internal/cluster/worker.js` (JAVASCRIPT) | Magnitude: 101.94 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 24, state_mutation: 10, concurrency: 10, ipc_rpc_bridges: 10
- `test/js-native-api/6_object_wrap/myobject.cc` (CPP) | Magnitude: 57.64 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 169, pointers: 51, structural_boundaries: 27, func_start: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `benchmark/url/url-searchparams-inspect.js` (JAVASCRIPT) | Magnitude: 34.3 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 26, core_var_decl: 12, design_snake_case: 12, branch: 8
- `test/parallel/test-timers-nan-duration-warning.js` (JAVASCRIPT) | Magnitude: 13.6 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 38, core_var_decl: 12, design_snake_case: 8, time_date_logic: 6
- `test/parallel/test-timers-negative-duration-warning.js` (JAVASCRIPT) | Magnitude: 13.6 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 38, core_var_decl: 12, design_snake_case: 8, time_date_logic: 6
- `lib/internal/main/check_syntax.js` (JAVASCRIPT) | Magnitude: 48.72 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 39, import: 10, branch: 9, structural_boundaries: 9
- `benchmark/fs/bench-filehandle-pipetosync.js` (JAVASCRIPT) | Magnitude: 105.62 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 64, core_var_decl: 25, structural_boundaries: 18, design_snake_case: 18

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/node_sqlite.cc` -> Churn: **76.86%** | Cog Load: 25.6285% | Debt: 52.7246%
- `lib/internal/test_runner/test.js` -> Churn: **73.74%** | Cog Load: 94.3849% | Debt: 11.7947%
- `lib/repl.js` -> Churn: **73.74%** | Cog Load: 94.1797% | Debt: 9.879%
- `src/node_options.cc` -> Churn: **73.74%** | Cog Load: 75.4285% | Debt: 23.8166%
- `src/node_zlib.cc` -> Churn: **73.74%** | Cog Load: 51.9855% | Debt: 96.3736%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/internal/util/inspect.js` -> **Hiroki Osame** (100.0% isolated ownership) | Magnitude: 3568.6
- `lib/fs.js` -> **Juan José** (100.0% isolated ownership) | Magnitude: 2069.16
- `lib/internal/streams/readable.js` -> **Thomas Watson** (100.0% isolated ownership) | Magnitude: 1599.24
- `lib/internal/util/comparisons.js` -> **Ruben Bridgewater** (100.0% isolated ownership) | Magnitude: 1197.7
- `lib/url.js` -> **René** (100.0% isolated ownership) | Magnitude: 1195.2

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/internal/util.js` -> **Severity: 0.052** (Bridge: 0.0005 * Flux: 99.9694%)
- `src/node_errors.cc` -> **Severity: 0.05** (Bridge: 0.0007 * Flux: 71.7126%)
- `src/node.cc` -> **Severity: 0.044** (Bridge: 0.0004 * Flux: 99.9238%)
- `lib/internal/errors.js` -> **Severity: 0.035** (Bridge: 0.0004 * Flux: 99.9658%)
- `lib/internal/url.js` -> **Severity: 0.031** (Bridge: 0.0003 * Flux: 99.9975%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/internal/test/binding.js` -> **Severity: 4.155** (Embedded: 0.071 * Error Risk: 58.4884%)
- `test/common/tmpdir.js` -> **Severity: 3.948** (Embedded: 0.0782 * Error Risk: 50.4629%)
- `benchmark/common.js` -> **Severity: 3.061** (Embedded: 0.0515 * Error Risk: 59.4775%)
- `test/common/index.js` -> **Severity: 2.82** (Embedded: 0.058 * Error Risk: 48.6251%)
- `lib/internal/errors.js` -> **Severity: 2.538** (Embedded: 0.0431 * Error Risk: 58.8505%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/internal/test/binding.js` -> **Severity: 3635.2** (Blast Radius: 36.352 * Doc Risk: 100.0%)
- `test/common/tmpdir.js` -> **Severity: 2470.75** (Blast Radius: 49.415 * Doc Risk: 50.0%)
- `test/common/index.js` -> **Severity: 2435.518** (Blast Radius: 50.371 * Doc Risk: 48.3516%)
- `lib/internal/errors.js` -> **Severity: 1782.817** (Blast Radius: 25.938 * Doc Risk: 68.7338%)
- `lib/internal/util.js` -> **Severity: 1344.942** (Blast Radius: 16.686 * Doc Risk: 80.603%)

- **Mainframe skeleton completeness:** n/a (no channel has facts) (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: none.

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 2753 literal sites + 40 sites through wrappers = 2793
- **`memory_alloc`:** 1715 literal sites + 338 sites through wrappers = 2053
- **`panics_and_aborts`:** 4495 literal sites + 118 sites through wrappers = 4613

- `CHECK_ENV_NOT_IN_GC` (macro, memory_alloc, via CheckGCAccess): 66 call sites in 2 files -- `src/js_native_api_v8.h`
- `napi_create_object` (function, memory_alloc, via CHECK_ENV_NOT_IN_GC): 54 call sites in 19 files -- `src/js_native_api_v8.cc`
- `NAPI_PREAMBLE` (macro, memory_alloc, via CHECK_ENV_NOT_IN_GC): 52 call sites in 2 files -- `src/js_native_api_v8.h`
- `fail` (function, panics_and_aborts, primitive): 24 call sites in 1 files -- `benchmark/net/tcp-raw-pipe.js`
- `napi_create_uint32` (function, memory_alloc, via CHECK_ENV_NOT_IN_GC): 22 call sites in 16 files -- `src/js_native_api_v8.cc`
- `fail` (function, panics_and_aborts, primitive): 19 call sites in 1 files -- `benchmark/net/tcp-raw-c2s.js`
- `napi_get_undefined` (function, memory_alloc, via CHECK_ENV_NOT_IN_GC): 18 call sites in 14 files -- `src/js_native_api_v8.cc`
- `fail` (function, panics_and_aborts, primitive): 16 call sites in 1 files -- `benchmark/net/tcp-raw-s2c.js`
- `PROCEDURE` (macro, memory_alloc, via napi_is_exception_pending): 15 call sites in 1 files -- `test/js-native-api/test_object/test_exceptions.c`
- `napi_create_int32` (function, memory_alloc, via CHECK_ENV_NOT_IN_GC): 15 call sites in 12 files -- `src/js_native_api_v8.cc`
- `napi_create_double` (function, memory_alloc, via CHECK_ENV_NOT_IN_GC): 12 call sites in 9 files -- `src/js_native_api_v8.cc`
- `napi_get_global` (function, memory_alloc, via CHECK_ENV_NOT_IN_GC): 12 call sites in 10 files -- `src/js_native_api_v8.cc`
*(+85 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 90892 call pairs -- scoped 21.3%, unique 4.4%, ambiguous 28.2%, external 46.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cpp | 44837 | 19.5% | 6.1% | 25.6% | 48.8% |
| javascript | 43250 | 23.8% | 0.0% | 32.7% | 43.5% |
| c | 2102 | 3.7% | 59.0% | 0.2% | 37.0% |
| python | 622 | 25.9% | 0.0% | 0.0% | 74.1% |
| shell | 30 | 13.3% | 0.0% | 0.0% | 86.7% |
| typescript | 29 | 13.8% | 0.0% | 6.9% | 79.3% |
| makefile | 22 | 0.0% | 0.0% | 0.0% | 100.0% |

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
