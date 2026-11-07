# ARCHITECTURAL_BRIEF: prometheus
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/prometheus/prometheus` |
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
- **Scope:** 1419 analyzed artifact(s), 306377 LOC.
- **Load-bearing artifact:** `model/labels/float.go` -- 184 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `cmd/prometheus/main.go` -- pulls in 69 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `scrape/testdata/ca.key` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 1591 |
| Analyzed Artifacts (Scanned) | 1419 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 172 |
| Total LOC | 306377 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 89.2% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6389 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0359 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 11.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.8734 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 157 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 679 | 253856 | 47.9% |
| YAML | 332 | 4056 | 23.4% |
| TYPESCRIPT | 242 | 39752 | 17.1% |
| JSON | 47 | 4667 | 3.3% |
| CSS | 29 | 1300 | 2.0% |
| MARKDOWN | 28 | 0 | 2.0% |
| PLAINTEXT | 18 | 5 | 1.3% |
| SHELL | 15 | 594 | 1.1% |
| JAVASCRIPT | 10 | 267 | 0.7% |
| MAKEFILE | 4 | 219 | 0.3% |
| XML | 4 | 0 | 0.3% |
| PROTO | 4 | 306 | 0.3% |
| HTML | 3 | 43 | 0.2% |
| YACC | 3 | 1283 | 0.2% |
| DOCKERFILE | 1 | 29 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 1414 |
| unknown | unknown | 5 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 36%, Callbacks & Closures Files 17%, Large Core Modules (3) 10%, Declarative / Non-Code 8%, Large Core Modules 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1373 | 96.8% |
| Unknown | 5 | 0.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 41 | 2.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 172*

**Composition by Extension & Reason:**
- `.md`: 40x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3284 LOC)
- `no_extension`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 3x Excluded (Binary Format Detected)
- `.test`: 20x Excluded (Unsupported Extension: '.test')
- `.yml`: 7x Excluded: Neighborhood Micro-Mass Limit Exceeded, 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 40012 LOC)
- `.prom`: 9x Excluded (Unsupported Extension: '.prom')
- `.go`: 1x Excluded (Machine-Generated Source Code Signature: 400 LOC), 1x Excluded (Machine-Generated Source Code Signature: 905 LOC), 1x Excluded (Machine-Generated Source Code Signature: 657 LOC)
- `.js`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 23 exceeds 500 chars)
- `.mod`: 5x Unsupported Format (.mod)
- `.sum`: 3x Excluded (Unsupported Extension: '.sum'), 2x Unsupported Format (.sum)
- `.json`: 1x Excluded (Static Asset Blob without Intent: 2334 LOC), 1x Excluded (Massive Static Asset Blob: 20001 LOC), 1x Excluded (Massive Static Asset Blob: 9760 LOC)
- `.cer`: 5x Excluded (Unsupported Extension: '.cer')
- `.libsonnet`: 4x Excluded (Unsupported Extension: '.libsonnet')
- `.snap`: 3x Unsupported Format (.snap)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.svg`: 2x Excluded (Machine-Generated Source Code Signature: 4 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 9.7 | 3.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 89.4 | 25.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 23.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 10.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 7.6 | 3.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 5.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 34.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 88.5 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 31.4 | 1.0 | 0.3 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 8.8 | 7.4 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 39.3 | 12.5 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5599 | 467 | 9 | `tsdb/head_test.go` |
| cleanup | 1392 | 220 | 1 | `tsdb/head_test.go` |
| guards | 7603 | 654 | 14 | `web/ui/mantine-ui/src/promql/functionDocs.tsx` |
| danger | 1836 | 297 | 3 | `tsdb/head_test.go` |
| concurrency | 2478 | 209 | 2 | `scrape/scrape_test.go` |
| connectivity | 9026 | 817 | 17 | `config/config.go` |
| io | 1025 | 254 | 2 | `web/ui/mantine-ui/src/promql/functionDocs.tsx` |
| crypto | 0 | 0 | 0 | - |
| ipc | 123 | 30 | 0 | `tsdb/fileutil/dir_windows.go` |
| time | 973 | 188 | 1 | `scrape/scrape_test.go` |
| serialization | 101 | 59 | 0 | `promql/value.go` |
| regex | 131 | 48 | 0 | `model/labels/regexp_test.go` |
| events | 413 | 67 | 0 | `discovery/aws/msk_test.go` |
| tests | 16719 | 315 | 18 | `tsdb/db_test.go` |
| docs | 18244 | 742 | 28 | `tsdb/db_test.go` |
| debt | 764 | 206 | 1 | `promql/parser/generated_parser.y` |
| mutation | 35706 | 815 | 64 | `tsdb/db_test.go` |
| dead_code | 3932 | 638 | 7 | `tsdb/head_test.go` |
| credential | 30 | 14 | 0 | `.github/workflows/prombench.yml` |
| threat | 5 | 5 | 0 | `discovery/hetzner/mock_test.go` |
| ml_ai | 1291 | 157 | 1 | `tsdb/db_test.go` |
| ui | 2332 | 159 | 1 | `web/ui/mantine-ui/src/pages/query/ExplainViews/BinaryExpr/VectorVector.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `web/ui/mantine-ui/src/promql/functionDocs.tsx` (Hits: 191)
- `web/ui/react-app/src/pages/targets/__testdata__/testdata.ts` (Hits: 69)
- `Makefile` (Hits: 38)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **float.go** (`model/labels/float.go`) — 184 inbound connections
2. **histogram.go** (`model/histogram/histogram.go`) — 107 inbound connections
3. **buffer.go** (`storage/buffer.go`) — 102 inbound connections
4. **discovery.go** (`discovery/discovery.go`) — 101 inbound connections
5. **targetgroup.go** (`discovery/targetgroup/targetgroup.go`) — 100 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **main.go** (`cmd/prometheus/main.go`) — 69 outbound dependencies
2. **scrape_test.go** (`scrape/scrape_test.go`) — 56 outbound dependencies
3. **db_test.go** (`tsdb/db_test.go`) — 51 outbound dependencies
4. **web.go** (`web/web.go`) — 49 outbound dependencies
5. **config_test.go** (`config/config_test.go`) — 48 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `aggregation` **(Many-Argument Workhorses)** (@ `promql/engine.go`) -> Impact: **315.2** | LOC: 364
  * *Intent:* // aggregation evaluates sum, avg, count, stdvar, stddev or quantile at one timestep on inputMatrix. // These functions produce one output series for ...
- `refresh` **(Many-Argument Workhorses)** (@ `discovery/aws/rds.go`) -> Impact: **268.2** | LOC: 528
- `eval` **(Many-Argument Workhorses)** (@ `promql/engine.go`) -> Impact: **254.7** | LOC: 557
  * *Intent:* // eval evaluates the given expression as the given AST expression node requires.
- `loadWAL` **(Many-Argument Workhorses)** (@ `tsdb/head_wal.go`) -> Impact: **242.2** | LOC: 434
- `analyzeCompletion` **(Many-Argument Workhorses)** (@ `web/ui/module/codemirror-promql/src/complete/hybrid.ts`) -> Impact: **240.0** | LOC: 320
  * *Intent:* // analyzeCompletion is going to determinate what should be autocompleted. // The value of the autocompletion is then calculate by the function buildC...
- `test` **(Many-Argument Workhorses)** (@ `cmd/promtool/unittest.go`) -> Impact: **225.3** | LOC: 332
  * *Intent:* // test performs the unit tests.
- `Checkpoint` **(Many-Argument Workhorses)** (@ `tsdb/wlog/checkpoint.go`) -> Impact: **215.9** | LOC: 301
  * *Intent:* // Checkpoint creates a compacted checkpoint of segments in range [from, to] in the given WAL. // It includes the most recent checkpoint if it exists....
- `aggregationK` **(Many-Argument Workhorses)** (@ `promql/engine.go`) -> Impact: **208.9** | LOC: 219
  * *Intent:* // aggregationK evaluates topk, bottomk, limitk, or limit_ratio at one timestep on inputMatrix. // Output that has the same labels as the input, but j...
- `main` **(I/O & Config Routines)** (@ `cmd/prometheus/main.go`) -> Impact: **186.8** | LOC: 1215
- `append` **(Many-Argument Workhorses)** (@ `scrape/scrape.go`) -> Impact: **173.4** | LOC: 309

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tsdb` | 42 | 23572.18 | 16.03% | 46.69% |
| `scrape/testdata` | 5 | 20000.0 | 0.0% | 0.0% |
| `promql` | 19 | 8710.48 | 17.96% | 43.01% |
| `scrape` | 10 | 6575.12 | 24.25% | 55.18% |
| `storage/remote` | 29 | 6226.8 | 15.07% | 61.29% |
| `tsdb/chunkenc` | 18 | 5417.44 | 25.22% | 50.72% |
| `web/ui/react-app` | 3 | 5017.78 | 0.0% | 0.0% |
| `model/histogram` | 9 | 4307.12 | 20.82% | 25.72% |
| `discovery/aws` | 20 | 4286.46 | 16.64% | 44.58% |
| `promql/parser` | 14 | 4119.48 | 21.0% | 25.58% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `rules/origin_test.go` -> **100.0%** Exposure
- `tsdb/mocks_test.go` -> **99.9999%** Exposure
- `tsdb/record/buffers.go` -> **99.9997%** Exposure
- `web/api/v1/errors_test.go` -> **99.9984%** Exposure
- `util/logging/file.go` -> **99.9905%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `config/config.go` -> **100.0%** Exposure
- `config/reload.go` -> **100.0%** Exposure
- `discovery/aws/aws.go` -> **100.0%** Exposure
- `discovery/aws/ec2.go` -> **100.0%** Exposure
- `discovery/aws/elasticache.go` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tsdb/head_test.go` -> **109** Orphaned Functions | **0** Duplicates
- `tsdb/db_test.go` -> **103** Orphaned Functions | **0** Duplicates
- `scrape/scrape_test.go` -> **100** Orphaned Functions | **0** Duplicates
- `tsdb/db_append_v2_test.go` -> **73** Orphaned Functions | **0** Duplicates
- `tsdb/head_append_v2_test.go` -> **57** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `discovery/stackit/mock_test.go` -> **99.9795%** Exposure
- `discovery/vultr/mock_test.go` -> **99.9431%** Exposure
- `notifier/manager_test.go` -> **10.1839%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `15` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6826` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `scrape/testdata/ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/servername.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `web/ui/react-app/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `promql/engine.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.954)
- **Top Global Matches:** file_cluster_4: 5.954, file_cluster_6: 8.954, file_cluster_15: 12.956
- **Magnitude:** 3962.8 | **LOC:** 4611 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 48.4%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **38**; blast radius 1.778; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.1%)
- **Documentation Coverage:** 53.9007% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `aggregation` **(Many-Argument Workhorses)** (Impact: 315.2)
    * *Intent:* // aggregation evaluates sum, avg, count, stdvar, stddev or quantile at one timestep on inputMatrix....
  * `eval` **(Many-Argument Workhorses)** (Impact: 254.7)
    * *Intent:* // eval evaluates the given expression as the given AST expression node requires.
  * `aggregationK` **(Many-Argument Workhorses)** (Impact: 208.9)
    * *Intent:* // aggregationK evaluates topk, bottomk, limitk, or limit_ratio at one timestep on inputMatrix. // O...
  * `VectorBinop` **(Many-Argument Workhorses)** (Impact: 128.4)
    * *Intent:* // VectorBinop evaluates a binary operation between two Vectors, excluding set operators.
  * `vectorElemBinop` **(Many-Argument Workhorses)** (Impact: 126.8)
    * *Intent:* // vectorElemBinop evaluates a binary operation between two Vector elements.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 468 instances
* *High Risk Execution (weighted view):* 15
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 1442
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 905`, `structural_boundaries: 513`, `args: 106`, `func_start: 106`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 19`, `state_mutation: 506`, `planned_debt: 8`, `unreferenced_by_name: 6`
* *Architecture:* `api: 70`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 42`, `doc: 347`, `test: 2`, `sync_locks: 5`, `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.778
  * `Choke Point (Betweenness):` 0.00162 | `Ripple Effect (Closeness):` 0.017502
  * `Imports (Out-Degree: 22):` bytes, heap, context, errors, fmt, prometheus, model, promslog...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `tsdb/db_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.477)
- **Top Global Matches:** file_cluster_12: 8.477, file_cluster_10: 9.151, file_cluster_15: 9.173
- **Magnitude:** 3330.18 | **LOC:** 9687 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 16.7%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **51**; blast radius 0.465; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.0%), Guard Balance (formerly Safety Score) (50.9%), Debt Markers (formerly Tech Debt) (44.0%)
- **Documentation Coverage:** 36.6279% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testOOOInterleavedImplicitCounterResets` **(Many-Argument Workhorses)** (Impact: 65.0)
  * `TestOOOHistogramCompactionWithCounterResets` **(I/O & Config Routines)** (Impact: 64.4)
  * `testChunkQuerierOOOQuery` **(Many-Argument Workhorses)** (Impact: 48.9)
  * `TestStaleSeriesCompaction` **(I/O & Config Routines)** (Impact: 30.8)
  * `testHistogramAppendAndQueryHelper` **(Many-Argument Workhorses)** (Impact: 28.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 20 instances
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 385 instances
* *Concurrency (weighted view):* 77
* *Memory Alloc (weighted view):* 24
* *State Mutation (weighted view):* 1586
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 482`, `structural_boundaries: 597`, `args: 148`, `func_start: 148`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 68`, `state_mutation: 816`, `planned_debt: 9`, `fragile_debt: 4`, `unreferenced_by_name: 103`
* *Architecture:* `io: 5`, `api: 111`, `concurrency: 22`, `import: 1`
* *Defense:* `safety: 6`, `doc: 678`, `test: 1513`, `sync_locks: 4`, `immutability_locks: 14`, `cleanup: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.465
  * `Choke Point (Betweenness):` 0.000219 | `Ripple Effect (Closeness):` 0.021285
  * `Imports (Out-Degree: 30):` bufio, bytes, context, binary, errors, flag, fmt, proto...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `scrape/scrape_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.538)
- **Top Global Matches:** file_cluster_12: 8.538, file_cluster_10: 9.346, file_cluster_15: 9.571
- **Magnitude:** 3009.4 | **LOC:** 6959 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **56**; blast radius 0.474; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Concurrency Surface (formerly Concurrency) (98.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.8%), Guard Balance (formerly Safety Score) (55.6%)
- **Documentation Coverage:** 86.0544% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testConvertClassicHistogramsToNHCB` **(Many-Argument Workhorses)** (Impact: 98.5)
  * `testScrapeLoopAppend` **(Many-Argument Workhorses)** (Impact: 34.3)
  * `testScrapeLoopRun` **(Many-Argument Workhorses)** (Impact: 29.7)
  * `TestScrapeLoopAppend_WithStorage` **(I/O & Config Routines)** (Impact: 29.1)
    * *Intent:* // TestScrapeLoopAppend_WithStorage tests appends and storage integration for the // large input fil...
  * `testScrapeLoopRunCreatesStaleMarkersOnSampleLimit` **(Many-Argument Workhorses)** (Impact: 24.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Race Conditions:* 74 instances
* *Amplified Cascading Flux:* 244 instances
* *High Risk Execution (weighted view):* 6
* *Concurrency (weighted view):* 467
* *Memory Alloc (weighted view):* 23
* *State Mutation (weighted view):* 1160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 341`, `structural_boundaries: 389`, `args: 192`, `func_start: 192`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 64`, `high_risk_execution: 12`, `state_mutation: 672`, `planned_debt: 5`, `fragile_debt: 1`, `unreferenced_by_name: 100`
* *Architecture:* `io: 23`, `api: 102`, `concurrency: 97`, `import: 1`
* *Defense:* `safety: 20`, `doc: 230`, `test: 651`, `sync_locks: 21`, `immutability_locks: 7`, `cleanup: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.474
  * `Choke Point (Betweenness):` 0.000645 | `Ripple Effect (Closeness):` 0.013338
  * `Imports (Out-Degree: 26):` bytes, gzip, context, binary, errors, fmt, proto, regexp...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tsdb/head_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.44)
- **Top Global Matches:** file_cluster_4: 8.44, file_cluster_12: 8.608, file_cluster_15: 10.232
- **Magnitude:** 2792.54 | **LOC:** 7918 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 17.6%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **43**; blast radius 0.845; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (83.4%), Debt Markers (formerly Tech Debt) (57.8%), Guard Balance (formerly Safety Score) (50.3%)
- **Documentation Coverage:** 36.8852% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BenchmarkLoadWLs` **(Many-Argument Workhorses)** (Impact: 58.8)
  * `TestHead_HighConcurrencyReadAndWrite` **(Compute Cores)** (Impact: 56.6)
    * *Intent:* // TestHead_HighConcurrencyReadAndWrite generates 1000 series with a step of 15s and fills a whole b...
  * `testHistogramStaleSampleHelper` **(Many-Argument Workhorses)** (Impact: 56.0)
  * `TestHistogramInWALAndMmapChunk` **(Compute Cores)** (Impact: 51.5)
  * `TestChunkSnapshot` **(I/O & Config Routines)** (Impact: 41.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 23 instances
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 330 instances
* *Concurrency (weighted view):* 58
* *Memory Alloc (weighted view):* 22
* *State Mutation (weighted view):* 1281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 464`, `structural_boundaries: 442`, `args: 130`, `func_start: 130`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 93`, `high_risk_execution: 2`, `state_mutation: 621`, `dead_code: 1`, `planned_debt: 6`, `fragile_debt: 5`, `unreferenced_by_name: 109`
* *Architecture:* `io: 2`, `api: 111`, `concurrency: 13`, `import: 1`
* *Defense:* `safety: 9`, `doc: 481`, `test: 1422`, `sync_locks: 11`, `immutability_locks: 20`, `cleanup: 130`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.845
  * `Choke Point (Betweenness):` 0.001132 | `Ripple Effect (Closeness):` 0.025977
  * `Imports (Out-Degree: 31):` context, json, fmt, cmp, prometheus, testutil, go, promslog...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `tsdb/db_append_v2_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.735)
- **Top Global Matches:** file_cluster_12: 8.735, file_cluster_4: 9.396, file_cluster_10: 9.811
- **Magnitude:** 2493.12 | **LOC:** 7705 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 30.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **36**; blast radius 0.364; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.7%), Guard Balance (formerly Safety Score) (50.9%), Debt Markers (formerly Tech Debt) (38.4%)
- **Documentation Coverage:** 34.3373% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testOOOInterleavedImplicitCounterResetsV2` **(Many-Argument Workhorses)** (Impact: 65.0)
  * `TestOOOHistogramCompactionWithCounterResets_AppendV2` **(I/O & Config Routines)** (Impact: 64.4)
  * `testChunkQuerierOOOQueryAppendV2` **(Many-Argument Workhorses)** (Impact: 48.9)
  * `testHistogramAppendAndQueryHelperAppendV2` **(Many-Argument Workhorses)** (Impact: 28.8)
  * `testQuerierOOOQueryAppendV2` **(Many-Argument Workhorses)** (Impact: 27.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 10 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 295 instances
* *Concurrency (weighted view):* 30
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 1252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 348`, `structural_boundaries: 410`, `args: 93`, `func_start: 93`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 662`, `planned_debt: 8`, `fragile_debt: 3`, `unreferenced_by_name: 73`
* *Architecture:* `io: 3`, `api: 74`, `concurrency: 10`, `import: 1`
* *Defense:* `safety: 2`, `doc: 558`, `test: 1262`, `sync_locks: 3`, `immutability_locks: 6`, `cleanup: 85`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` bufio, context, fmt, v2, prometheus, testutil, promslog, config...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `model/histogram/float_histogram.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.295)
- **Top Global Matches:** file_cluster_6: 6.295, file_cluster_8: 11.356, file_cluster_4: 13.587
- **Magnitude:** 2192.2 | **LOC:** 2455 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 17.252; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (79.3%), Complexity Load (formerly Cognitive Load) (35.8%)
- **Documentation Coverage:** 30.5882% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `kahanAddBuckets` **(Many-Argument Workhorses)** (Impact: 101.8)
    * *Intent:* // kahanAddBuckets works like addBuckets but it is used in FloatHistogram's KahanAdd method // and t...
  * `addBuckets` **(Many-Argument Workhorses)** (Impact: 82.4)
    * *Intent:* // addBuckets adds the buckets described by spansB/bucketsB to the buckets described by spansA/bucke...
  * `TrimBuckets` **(Many-Argument Workhorses)** (Impact: 67.1)
    * *Intent:* // TrimBuckets trims native histogram buckets.
  * `addCustomBucketsWithMismatches` **(Many-Argument Workhorses)** (Impact: 61.5)
    * *Intent:* // addCustomBucketsWithMismatches handles adding/subtracting custom bucket histograms // with mismat...
  * `detectResetWithMismatchedCustomBounds` **(Many-Argument Workhorses)** (Impact: 43.7)
    * *Intent:* // detectResetWithMismatchedCustomBounds checks if any bucket count has decreased when // comparing ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 372 instances
* *State Mutation (weighted view):* 1181
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 411`, `structural_boundaries: 217`, `args: 54`, `func_start: 54`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 11`, `state_mutation: 437`, `planned_debt: 2`, `unreferenced_by_name: 20`
* *Architecture:* `api: 41`, `import: 1`
* *Defense:* `safety: 10`, `doc: 218`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.252
  * `Choke Point (Betweenness):` 0.000107 | `Ripple Effect (Closeness):` 0.051588
  * `Imports (Out-Degree: 2):` errors, fmt, kahansum, math, strings
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `promql/functions.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.498)
- **Top Global Matches:** file_cluster_4: 6.498, file_cluster_15: 8.993, file_cluster_16: 9.957
- **Magnitude:** 1854.9 | **LOC:** 2383 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 12.5%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **18**; blast radius 0.494; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.4%), Complexity Load (formerly Cognitive Load) (43.7%)
- **Documentation Coverage:** 92.1875% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `instantValue` **(Many-Argument Workhorses)** (Impact: 81.4)
  * `extrapolatedRate` **(Many-Argument Workhorses)** (Impact: 74.6)
    * *Intent:* // extrapolatedRate is a utility function for rate/increase/delta. // It calculates the rate (allowi...
  * `funcAvgOverTime` **(Many-Argument Workhorses)** (Impact: 74.6)
    * *Intent:* // === avg_over_time(Matrix parser.ValueTypeMatrix) (Vector, Annotations) ===
  * `histogramRate` **(Many-Argument Workhorses)** (Impact: 67.5)
    * *Intent:* // histogramRate is a helper function for extrapolatedRate. It requires // points[0] to be a histogr...
  * `funcChanges` **(Many-Argument Workhorses)** (Impact: 62.9)
    * *Intent:* // === changes(Matrix parser.ValueTypeMatrix) (Vector, Annotations) ===
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 193 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 604
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 390`, `structural_boundaries: 309`, `args: 118`, `func_start: 118`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 218`, `planned_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 15`, `import: 1`
* *Defense:* `safety: 16`, `doc: 119`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.494
  * `Choke Point (Betweenness):` 4.7e-05 | `Ripple Effect (Closeness):` 0.01351
  * `Imports (Out-Degree: 11):` context, errors, fmt, natsort, regexp, model, histogram, labels...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tsdb/head_append_v2_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.372)
- **Top Global Matches:** file_cluster_4: 8.372, file_cluster_12: 9.687, file_cluster_10: 10.924
- **Magnitude:** 1614.24 | **LOC:** 4891 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **37**; blast radius 0.364; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.8%), Guard Balance (formerly Safety Score) (49.9%), Debt Markers (formerly Tech Debt) (45.7%)
- **Documentation Coverage:** 39.7638% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testHeadAppenderV2AppendStaleHistogram` **(Many-Argument Workhorses)** (Impact: 56.0)
  * `TestHistogramInWALAndMmapChunk_AppenderV2` **(Compute Cores)** (Impact: 51.5)
  * `TestChunkSnapshot_AppenderV2` **(I/O & Config Routines)** (Impact: 44.5)
  * `TestHeadAppenderV2_Delete_e2e` **(I/O & Config Routines)** (Impact: 30.5)
  * `TestHeadAppenderV2_Append_DifferentEncodingSameSeries` **(I/O & Config Routines)** (Impact: 26.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 19 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 192 instances
* *Concurrency (weighted view):* 33
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 784
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 263`, `args: 65`, `func_start: 65`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 400`, `planned_debt: 6`, `fragile_debt: 1`, `unreferenced_by_name: 57`
* *Architecture:* `api: 57`, `concurrency: 8`, `import: 1`
* *Defense:* `safety: 2`, `doc: 309`, `test: 912`, `sync_locks: 2`, `immutability_locks: 3`, `cleanup: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 29):` context, fmt, cmp, prometheus, testutil, go, config, exemplar...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/head_append.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.633)
- **Top Global Matches:** file_cluster_4: 5.633, file_cluster_6: 9.157, file_cluster_15: 12.237
- **Magnitude:** 1607.54 | **LOC:** 2299 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 27.3%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **15**; blast radius 1.076; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.2%)
- **Documentation Coverage:** 32.7957% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AppendHistogram` **(Many-Argument Workhorses)** (Impact: 68.6)
  * `commitFloats` **(Many-Argument Workhorses)** (Impact: 59.7)
    * *Intent:* // to its corresponding series. It handles various error cases such as out-of-order samples, // out-...
  * `commitHistograms` **(Many-Argument Workhorses)** (Impact: 52.2)
    * *Intent:* // For details on the commitHistograms function, see the commitFloats docs.
  * `commitFloatHistograms` **(Many-Argument Workhorses)** (Impact: 52.2)
    * *Intent:* // For details on the commitFloatHistograms function, see the commitFloats docs.
  * `AppendHistogramSTZeroSample` **(Many-Argument Workhorses)** (Impact: 44.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 210 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 665
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 352`, `structural_boundaries: 223`, `args: 71`, `func_start: 71`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 3`, `state_mutation: 245`, `dead_code: 2`, `planned_debt: 15`, `unreferenced_by_name: 2`
* *Architecture:* `api: 22`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 51`, `doc: 227`, `sync_locks: 36`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.076
  * `Choke Point (Betweenness):` 0.000361 | `Ripple Effect (Closeness):` 0.02628
  * `Imports (Out-Degree: 16):` context, errors, fmt, exemplar, histogram, labels, metadata, value...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `tsdb/db.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.92)
- **Top Global Matches:** file_cluster_4: 6.92, file_cluster_6: 8.656, file_cluster_15: 13.818
- **Magnitude:** 1593.62 | **LOC:** 2632 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 15.8%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **31**; blast radius 0.611; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (86.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.7%)
- **Documentation Coverage:** 15.2174% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `open` **(Many-Argument Workhorses)** (Impact: 130.4)
    * *Intent:* // open returns a new DB in the given directory. // It initializes the lockfile, WAL, compactor, and...
  * `run` **(Compute Cores)** (Impact: 38.8)
  * `Querier` **(Many-Argument Workhorses)** (Impact: 31.5)
    * *Intent:* // Querier returns a new querier over the data partition for the given time range.
  * `blockChunkQuerierForRange` **(Many-Argument Workhorses)** (Impact: 31.4)
    * *Intent:* // blockChunkQuerierForRange returns individual block chunk queriers from the persistent blocks, in-...
  * `reloadBlocks` **(I/O & Config Routines)** (Impact: 29.4)
    * *Intent:* // reloadBlocks reloads blocks without touching head. // Blocks that are obsolete due to replacement...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 10 instances
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 173 instances
* *Concurrency (weighted view):* 104
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 558
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 379`, `structural_boundaries: 374`, `args: 71`, `func_start: 71`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 212`, `planned_debt: 5`, `unreferenced_by_name: 16`
* *Architecture:* `api: 103`, `concurrency: 24`, `import: 1`
* *Defense:* `safety: 110`, `doc: 256`, `sync_locks: 68`, `immutability_locks: 1`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.611
  * `Choke Point (Betweenness):` 0.000401 | `Ripple Effect (Closeness):` 0.021773
  * `Imports (Out-Degree: 19):` context, errors, fmt, v2, prometheus, promslog, config, labels...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `tsdb/head_wal.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.036)
- **Top Global Matches:** file_cluster_6: 6.036, file_cluster_8: 12.551, file_cluster_4: 12.589
- **Magnitude:** 1536.96 | **LOC:** 1876 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **26**; blast radius 1.093; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (93.3%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.2%)
- **Documentation Coverage:** 33.7838% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadWAL` **(Many-Argument Workhorses)** (Impact: 242.2)
  * `loadWBL` **(Many-Argument Workhorses)** (Impact: 131.6)
  * `processWALSamples` **(Many-Argument Workhorses)** (Impact: 82.2)
    * *Intent:* // processWALSamples adds the samples it receives to the head and passes // the buffer received to a...
  * `loadChunkSnapshot` **(I/O & Config Routines)** (Impact: 57.7)
    * *Intent:* // loadChunkSnapshot replays the chunk snapshot and restores the Head state from it. If there was an...
  * `processWBLSamples` **(Compute Cores)** (Impact: 38.4)
    * *Intent:* // processWBLSamples adds the samples it receives to the head and passes // the buffer received to a...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 193 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 123
* *Memory Alloc (weighted view):* 28
* *State Mutation (weighted view):* 601
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 356`, `structural_boundaries: 303`, `args: 31`, `func_start: 31`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `state_mutation: 215`, `planned_debt: 6`, `unreferenced_by_name: 7`
* *Architecture:* `io: 1`, `api: 13`, `concurrency: 28`, `import: 1`
* *Defense:* `safety: 64`, `doc: 105`, `sync_locks: 21`, `immutability_locks: 3`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.093
  * `Choke Point (Betweenness):` 0.000947 | `Ripple Effect (Closeness):` 0.031852
  * `Imports (Out-Degree: 17):` json, errors, fmt, prometheus, exemplar, histogram, labels, metadata...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `scrape/scrape.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.369)
- **Top Global Matches:** file_cluster_4: 6.369, file_cluster_12: 11.045, file_cluster_15: 11.079
- **Magnitude:** 1522.64 | **LOC:** 2302 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 18.2%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **41**; blast radius 1.491; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.4%), Guard Balance (formerly Safety Score) (62.7%)
- **Documentation Coverage:** 72.2892% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `append` **(Many-Argument Workhorses)** (Impact: 173.4)
  * `scrapeAndReport` **(Many-Argument Workhorses)** (Impact: 56.0)
    * *Intent:* // scrapeAndReport performs a scrape and then appends the result to the storage // together with rep...
  * `checkAddError` **(Many-Argument Workhorses)** (Impact: 42.4)
    * *Intent:* // Adds samples to the appender, checking the error, and then returns the # of samples added, // whe...
  * `isSeriesPartOfFamily` **(Many-Argument Workhorses)** (Impact: 41.2)
    * *Intent:* // TODO(https://github.com/prometheus/prometheus/issues/17900): Move this to text and OM parser.
  * `endOfRunStaleness` **(Many-Argument Workhorses)** (Impact: 35.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 190 instances
* *Concurrency (weighted view):* 77
* *State Mutation (weighted view):* 594
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 321`, `structural_boundaries: 259`, `args: 67`, `func_start: 67`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 214`, `planned_debt: 8`, `unreferenced_by_name: 13`
* *Architecture:* `io: 11`, `api: 17`, `concurrency: 17`, `import: 1`
* *Defense:* `safety: 64`, `doc: 153`, `sync_locks: 56`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.491
  * `Choke Point (Betweenness):` 0.000943 | `Ripple Effect (Closeness):` 0.020713
  * `Imports (Out-Degree: 16):` bufio, bytes, context, errors, fmt, gzip, config, model...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `storage/remote/queue_manager.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.869)
- **Top Global Matches:** file_cluster_4: 6.869, file_cluster_15: 9.144, file_cluster_9: 9.77
- **Magnitude:** 1340.9 | **LOC:** 2321 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **33**; blast radius 0.487; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (42.1%)
- **Documentation Coverage:** 60.2564% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runShard` **(Many-Argument Workhorses)** (Impact: 49.6)
  * `populateV2TimeSeries` **(Many-Argument Workhorses)** (Impact: 43.1)
  * `sendWriteRequestWithBackoff` **(Many-Argument Workhorses)** (Impact: 33.2)
  * `sendV2SamplesWithBackoff` **(Many-Argument Workhorses)** (Impact: 31.6)
    * *Intent:* // sendV2SamplesWithBackoff to the remote storage with backoff for recoverable errors.
  * `sendSamplesWithBackoff` **(Many-Argument Workhorses)** (Impact: 30.4)
    * *Intent:* // sendSamplesWithBackoff to the remote storage with backoff for recoverable errors.
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Race Conditions:* 23 instances
* *Amplified Cascading Flux:* 129 instances
* *Concurrency (weighted view):* 148
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 445
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 230`, `args: 60`, `func_start: 60`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 187`, `planned_debt: 14`, `unreferenced_by_name: 11`
* *Architecture:* `api: 20`, `concurrency: 33`, `import: 1`
* *Defense:* `safety: 16`, `doc: 132`, `sync_locks: 74`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.487
  * `Choke Point (Betweenness):` 0.000123 | `Ripple Effect (Closeness):` 0.003803
  * `Imports (Out-Degree: 18):` context, errors, fmt, proto, remote, prometheus, model, promslog...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `promql/parser/generated_parser.y` (YACC | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.93)
- **Top Global Matches:** file_cluster_15: 7.93, file_cluster_16: 8.859, file_cluster_2: 9.153
- **Magnitude:** 1310.9 | **LOC:** 1356 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Complexity Load (formerly Cognitive Load) (93.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 81.98% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `maybe_label` **(Compute Cores)** (Impact: 36.0)
    * *Intent:* // Inside of grouping options label names can be recognized as keywords by the lexer. This is a list...
  * `metric_identifier` **(Compute Cores)** (Impact: 31.1)
    * *Intent:* ;
  * `binary_expr` **(Compute Cores)** (Impact: 26.4)
    * *Intent:* ; /* * Binary expressions. */ // Operator precedence only works if each of those is listed separatel...
  * `nl` **(Compute Cores)** (Impact: 19.7)
  * `histogram_desc_item` **(Compute Cores)** (Impact: 18.4)
    * *Intent:* ;
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 201 instances
* *State Mutation (weighted view):* 628
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 296`, `structural_boundaries: 60`, `args: 581`, `func_start: 178`, `class_start: 1`
* *Risk/State:* `state_mutation: 226`, `duplicate_logic: 47`, `unreferenced_by_name: 9`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.364
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/head.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.661)
- **Top Global Matches:** file_cluster_15: 7.661, file_cluster_10: 8.177, file_cluster_16: 8.772
- **Magnitude:** 1291.52 | **LOC:** 2708 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 13.3%
- **Blast Radius:** changing it is visible to **31** in-repo importer(s); it depends on **29**; blast radius 2.851; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.0%), Guard Balance (formerly Safety Score) (57.7%)
- **Documentation Coverage:** 22.8125% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Init` **(Defensive Guards)** (Impact: 72.7)
    * *Intent:* // Init loads data from the write ahead log and prepares the head for writes. // It should be called...
  * `gc` **(Compute Cores)** (Impact: 47.3)
    * *Intent:* // gc garbage collects old chunks that are strictly before mint and removes // series entirely that ...
  * `NewHead` **(Many-Argument Workhorses)** (Impact: 38.0)
    * *Intent:* // NewHead opens the head block in dir.
  * `Delete` **(Many-Argument Workhorses)** (Impact: 29.4)
    * *Intent:* // Delete all samples in the range of [mint, maxt] for series that satisfy the given // label matche...
  * `truncateChunksBefore` **(Compute Cores)** (Impact: 28.7)
    * *Intent:* // truncateChunksBefore removes all chunks from the series that // have no timestamp at or after min...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 133 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 450
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 360`, `args: 105`, `func_start: 105`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 184`, `planned_debt: 7`, `unreferenced_by_name: 28`
* *Architecture:* `api: 99`, `concurrency: 3`, `import: 1`
* *Defense:* `safety: 49`, `doc: 248`, `sync_locks: 81`, `immutability_locks: 4`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.851
  * `Choke Point (Betweenness):` 0.001522 | `Ripple Effect (Closeness):` 0.033079
  * `Imports (Out-Degree: 21):` context, errors, fmt, v2, prometheus, promslog, config, exemplar...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `web/api/v1/api.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.968)
- **Top Global Matches:** file_cluster_4: 6.968, file_cluster_6: 9.121, file_cluster_15: 13.405
- **Magnitude:** 1227.28 | **LOC:** 2322 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **44**; blast radius 0.8; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.5%)
- **Documentation Coverage:** 76.25% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rules` **(Compute Cores)** (Impact: 61.7)
  * `targets` **(Compute Cores)** (Impact: 38.2)
  * `labelValues` **(Defensive Guards)** (Impact: 33.1)
  * `metricMetadata` **(Compute Cores)** (Impact: 31.9)
  * `series` **(Defensive Guards)** (Impact: 30.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 108 instances
* *Concurrency (weighted view):* 9
* *Memory Alloc (weighted view):* 11
* *State Mutation (weighted view):* 341
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 327`, `structural_boundaries: 386`, `args: 63`, `func_start: 64`, `class_start: 36`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 125`, `unreferenced_by_name: 4`
* *Architecture:* `io: 1`, `api: 178`, `concurrency: 4`, `import: 1`
* *Defense:* `safety: 88`, `doc: 87`, `immutability_locks: 3`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.8
  * `Choke Point (Betweenness):` 0.000264 | `Ripple Effect (Closeness):` 0.006402
  * `Imports (Out-Degree: 23):` context, sha1, hex, json, errors, fmt, regexp, go...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `tsdb/querier_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.765)
- **Top Global Matches:** file_cluster_15: 6.765, file_cluster_10: 7.062, file_cluster_11: 8.297
- **Magnitude:** 1135.16 | **LOC:** 4014 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **25**; blast radius 0.435; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.0%), Guard Balance (formerly Safety Score) (53.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (33.9%), Debt Markers (formerly Tech Debt) (23.6%)
- **Documentation Coverage:** 42.1622% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LabelValues` **(Many-Argument Workhorses)** (Impact: 37.4)
  * `TestPopulateWithTombSeriesIterators` **(I/O & Config Routines)** (Impact: 27.5)
  * `createIdxChkReaders` **(Many-Argument Workhorses)** (Impact: 26.6)
    * *Intent:* // Index: labels -> postings -> chunkMetas -> chunkRef. // ChunkReader: ref -> vals.
  * `BenchmarkQueries` **(Compute Cores)** (Impact: 24.4)
  * `TestPostingsForMatchers` **(I/O & Config Routines)** (Impact: 19.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 116 instances
* *Memory Alloc (weighted view):* 18
* *State Mutation (weighted view):* 369
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 202`, `structural_boundaries: 290`, `args: 98`, `func_start: 98`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 11`, `state_mutation: 137`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 29`
* *Architecture:* `api: 88`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 3`, `doc: 97`, `test: 230`, `immutability_locks: 2`, `cleanup: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.435
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.02126
  * `Imports (Out-Degree: 20):` context, errors, fmt, v2, histogram, labels, storage, chunkenc...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `promql/promqltest/test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.775)
- **Top Global Matches:** file_cluster_4: 5.775, file_cluster_6: 10.51, file_cluster_15: 11.359
- **Magnitude:** 1133.28 | **LOC:** 1842 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **27**; blast radius 2.076; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.4%), Guard Balance (formerly Safety Score) (56.5%)
- **Documentation Coverage:** 31.8627% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compareResult` **(Compute Cores)** (Impact: 72.5)
    * *Intent:* // compareResult compares the result value with the defined expectation.
  * `parseEval` **(Many-Argument Workhorses)** (Impact: 66.8)
  * `runInstantQuery` **(Many-Argument Workhorses)** (Impact: 54.5)
  * `compareNativeHistogram` **(Many-Argument Workhorses)** (Impact: 34.4)
    * *Intent:* // compareNativeHistogram is helper function to compare two native histograms // which can tolerate ...
  * `spansMatch` **(Compute Cores)** (Impact: 33.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 99 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 12
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 322`, `structural_boundaries: 351`, `args: 79`, `func_start: 79`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 3`, `state_mutation: 127`, `planned_debt: 1`, `unreferenced_by_name: 9`
* *Architecture:* `api: 39`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 58`, `doc: 69`, `test: 21`, `immutability_locks: 2`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.076
  * `Choke Point (Betweenness):` 0.000476 | `Ripple Effect (Closeness):` 0.01705
  * `Imports (Out-Degree: 12):` context, embed, errors, fmt, regexp, model, exemplar, histogram...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `tsdb/index/index.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.09)
- **Top Global Matches:** file_cluster_4: 6.09, file_cluster_15: 10.571, file_cluster_10: 11.064
- **Magnitude:** 1103.1 | **LOC:** 1875 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **19**; blast radius 1.434; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (55.0%), Debt Markers (formerly Tech Debt) (50.0%), Complexity Load (formerly Cognitive Load) (34.6%)
- **Documentation Coverage:** 56.2963% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `newReader` **(Many-Argument Workhorses)** (Impact: 49.1)
  * `Postings` **(Many-Argument Workhorses)** (Impact: 48.0)
  * `AddSeries` **(Many-Argument Workhorses)** (Impact: 40.8)
    * *Intent:* // AddSeries adds the series one at a time along with its chunks.
  * `LabelValues` **(Many-Argument Workhorses)** (Impact: 37.9)
    * *Intent:* // LabelValues returns value tuples that exist for the given label name. // It is not safe to use th...
  * `writePostingsToTmpFiles` **(I/O & Config Routines)** (Impact: 34.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 111 instances
* *Concurrency (weighted view):* 12
* *Memory Alloc (weighted view):* 15
* *State Mutation (weighted view):* 345
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 332`, `args: 77`, `func_start: 77`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 123`, `planned_debt: 6`, `unreferenced_by_name: 21`
* *Architecture:* `io: 2`, `api: 85`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 86`, `doc: 145`, `immutability_locks: 4`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.434
  * `Choke Point (Betweenness):` 0.000201 | `Ripple Effect (Closeness):` 0.034066
  * `Imports (Out-Degree: 6):` bufio, context, binary, errors, fmt, labels, storage, chunks...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `discovery/aws/rds.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.609)
- **Top Global Matches:** file_cluster_4: 6.609, file_cluster_6: 10.288, file_cluster_9: 12.123
- **Magnitude:** 1053.06 | **LOC:** 1000 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **24**; blast radius 0.764; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (62.3%)
- **Documentation Coverage:** 37.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `refresh` **(Many-Argument Workhorses)** (Impact: 268.2)
  * `initRdsClient` **(Defensive Guards)** (Impact: 18.7)
  * `describeDBClusters` **(Compute Cores)** (Impact: 14.0)
  * `describeDBInstances` **(Many-Argument Workhorses)** (Impact: 12.2)
  * `describeAllDBClusters` **(Defensive Guards)** (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 172 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 669
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 66`, `args: 11`, `func_start: 11`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 325`, `unreferenced_by_name: 4`
* *Architecture:* `api: 19`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 12`, `doc: 30`, `sync_locks: 9`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.764
  * `Choke Point (Betweenness):` 1.9e-05 | `Ripple Effect (Closeness):` 0.004952
  * `Imports (Out-Degree: 6):` context, errors, fmt, aws, config, credentials, stscreds, rds...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `util/pool/pool.go` (GO) | Magnitude: 39.26 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 47, structural_boundaries: 12, branch: 10, doc: 10
- `web/ui/mantine-ui/src/pages/query/TimeInput.tsx` (TYPESCRIPT) | Magnitude: 6.64 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 79, core_var_decl: 32, structural_boundaries: 19, design_snake_case: 19
- `web/ui/mantine-ui/src/pages/query/ExpressionInput.tsx` (TYPESCRIPT) | Magnitude: 36.14 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 287, structural_boundaries: 51, core_var_decl: 48, ui_framework: 37
- `web/ui/react-app/src/index.tsx` (TYPESCRIPT) | Magnitude: 18.52 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 6, core_var_decl: 5, import: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `web/ui/mantine-ui/src/pages/query/ExpressionInput.tsx.old` (TYPESCRIPT) | Magnitude: 62.18 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 297, core_var_decl: 46, structural_boundaries: 44, ui_framework: 30
- `web/ui/react-app/src/pages/tsdbStatus/TSDBStatus.test.tsx` (TYPESCRIPT) | Magnitude: 243.93 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 166, structural_boundaries: 23, comprehensions: 19, core_var_decl: 19
- `tsdb/wlog/watcher_test.go` (GO) | Magnitude: 313.02 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 667, test: 109, structural_boundaries: 90, state_mutation: 66
- `discovery/ionos/ionos.go` (GO) | Magnitude: 43.08 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 55, structural_boundaries: 17, doc: 16, api: 13
- `model/rulefmt/rulefmt_test.go` (GO) | Magnitude: 69.8 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 256, indent_spaces: 58, test: 38, pointers: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `web/ui/module/codemirror-promql/src/promql.ts` (TYPESCRIPT) | Magnitude: 51.48 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 62, structural_boundaries: 22, api: 12, args: 11
- `storage/remote/azuread/azuread_test.go` (GO) | Magnitude: 78.32 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 362, pointers: 46, doc: 38, structural_boundaries: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tsdb/compact_test.go` (GO) | Magnitude: 712.04 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 1843, structural_boundaries: 190, test: 171, state_mutation: 139
- `promql/functions_internal_test.go` (GO) | Magnitude: 20.36 | Delta: **0.142** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 89, scientific: 17, test: 10, structural_boundaries: 8
- `rules/alerting_test.go` (GO) | Magnitude: 303.98 | Delta: **0.146** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 959, test: 107, state_mutation: 57, branch: 52
- `cmd/prometheus/query_log_test.go` (GO) | Magnitude: 237.5 | Delta: **0.156** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 350, branch: 65, structural_boundaries: 47, test: 45

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `discovery/targetgroup/targetgroup.go` (GO) | Magnitude: 59.12 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 61, structural_boundaries: 19, api: 17, doc: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tsdb/record/record_test.go` (GO) | Magnitude: 196.82 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 687, test: 81, state_mutation: 55, core_var_decl: 35
- `tsdb/agent/series_test.go` (GO) | Magnitude: 80.12 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 91, structural_boundaries: 17, test: 13, doc: 10
- `config/config_test.go` (GO) | Magnitude: 228.4 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 3029, test: 225, pointers: 102, closures: 50
- `web/api/v1/openapi.go` (GO) | Magnitude: 104.74 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 179, doc: 51, structural_boundaries: 27, branch: 20
- `cmd/prometheus/reload_test.go` (GO) | Magnitude: 67.24 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 153, structural_boundaries: 23, test: 13, branch: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `web/ui/react-app/src/pages/index.ts` (TYPESCRIPT) | Magnitude: 16.66 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, import: 11, indent_spaces: 10, core_var_decl: 10
- `discovery/install/install.go` (GO) | Magnitude: 15.58 | Delta: **0.255** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 26, doc: 7, structural_boundaries: 2, import: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `discovery/triton/triton_test.go` (GO) | Magnitude: 51.46 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 190, test: 60, args: 12, func_start: 12
- `.github/workflows/stale.yml` (YAML) | Magnitude: 16.48 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 20, args: 9, branch: 2, structural_boundaries: 2
- `Makefile` (MAKEFILE) | Magnitude: 110.92 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 82, io: 38, func_start: 36, api: 35
- `discovery/digitalocean/mock_test.go` (GO) | Magnitude: 44.84 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 551, indent_tabs: 40, structural_boundaries: 21, doc: 12
- `web/ui/ui.go` (GO) | Magnitude: 25.76 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 33, doc: 10, branch: 9, structural_boundaries: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `model/textparse/nhcbparse.go` (GO) | Magnitude: 232.4 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 242, branch: 61, structural_boundaries: 47, state_mutation: 41
- `tsdb/head_test.go` (GO) | Magnitude: 2792.54 | Delta: **0.168** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 6099, test: 1422, state_mutation: 621, doc: 481

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `web/ui/react-app/src/pages/graph/GraphTabContent.test.tsx` (TYPESCRIPT) | Magnitude: 15.86 | Delta: **0.073** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 9, test: 7, ui_framework: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `scripts/check_release_notes.sh` (SHELL) | Magnitude: 1.59 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 30, io: 16, indent_spaces: 9, debug_prints: 7
- `model/labels/sharding_stringlabels.go` (GO) | Magnitude: 47.64 | Delta: **0.197** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_tabs: 27, state_mutation: 12, core_var_decl: 12, design_short_vars: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `web/ui/react-app/src/pages/graph/Legend.tsx` (TYPESCRIPT) | Magnitude: 55.1 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 23, branch: 19, core_var_decl: 17
- `tsdb/record/record.go` (GO) | Magnitude: 722.22 | Delta: **0.143** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 752, branch: 172, structural_boundaries: 167, api: 88

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tsdb/head_test.go` -> Churn: **83.4%** | Cog Load: 13.7049% | Debt: 57.8178%
- `scrape/scrape_test.go` -> Churn: **77.8%** | Cog Load: 42.8365% | Debt: 53.5955%
- `tsdb/agent/db.go` -> Churn: **69.51%** | Cog Load: 43.658% | Debt: 62.0348%
- `scrape/manager.go` -> Churn: **66.11%** | Cog Load: 40.642% | Debt: 98.7347%
- `storage/remote/queue_manager_test.go` -> Churn: **63.96%** | Cog Load: 12.9602% | Debt: 50.1374%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `discovery/aws/rds.go` -> **Matt** (100.0% isolated ownership) | Magnitude: 1053.06
- `prompb/io/prometheus/client/decoder.go` -> **Ben Kochie** (100.0% isolated ownership) | Magnitude: 708.94
- `rules/group.go` -> **Ben Kochie** (100.0% isolated ownership) | Magnitude: 640.22
- `tsdb/chunks/head_chunks.go` -> **Ben Kochie** (100.0% isolated ownership) | Magnitude: 579.28
- `tsdb/wlog/wlog.go` -> **Ben Kochie** (100.0% isolated ownership) | Magnitude: 531.92

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `tsdb/block.go` -> **Severity: 0.293** (Bridge: 0.003 * Flux: 97.6608%)
- `promql/engine.go` -> **Severity: 0.162** (Bridge: 0.0016 * Flux: 99.9999%)
- `tsdb/head.go` -> **Severity: 0.152** (Bridge: 0.0015 * Flux: 99.8732%)
- `discovery/discovery.go` -> **Severity: 0.144** (Bridge: 0.0015 * Flux: 97.9469%)
- `promql/value.go` -> **Severity: 0.13** (Bridge: 0.0013 * Flux: 99.9783%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `model/histogram/histogram.go` -> **Severity: 7.694** (Embedded: 0.1043 * Error Risk: 73.7385%)
- `storage/buffer.go` -> **Severity: 6.639** (Embedded: 0.0851 * Error Risk: 78.0104%)
- `tsdb/chunkenc/bstream.go` -> **Severity: 5.85** (Embedded: 0.0824 * Error Risk: 70.9508%)
- `model/labels/float.go` -> **Severity: 5.819** (Embedded: 0.1095 * Error Risk: 53.1387%)
- `model/histogram/generic.go` -> **Severity: 4.949** (Embedded: 0.0699 * Error Risk: 70.8403%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `model/histogram/generic.go` -> **Severity: 1378.676** (Blast Radius: 19.781 * Doc Risk: 69.697%)
- `tsdb/chunkenc/bstream.go` -> **Severity: 732.063** (Blast Radius: 11.591 * Doc Risk: 63.1579%)
- `tsdb/fileutil/mmap.go` -> **Severity: 629.4** (Blast Radius: 6.294 * Doc Risk: 100.0%)
- `model/histogram/float_histogram.go` -> **Severity: 527.708** (Blast Radius: 17.252 * Doc Risk: 30.5882%)
- `storage/buffer.go` -> **Severity: 497.179** (Blast Radius: 7.972 * Doc Risk: 62.3656%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 50158 call pairs -- scoped 25.0%, unique 6.1%, ambiguous 31.0%, external 37.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| go | 48298 | 25.2% | 6.4% | 32.1% | 36.4% |
| typescript | 1565 | 23.7% | 0.0% | 2.4% | 73.9% |
| shell | 148 | 20.3% | 0.0% | 0.0% | 79.7% |
| yacc | 142 | 0.0% | 0.0% | 0.0% | 100.0% |
| javascript | 5 | 0.0% | 0.0% | 0.0% | 100.0% |

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
