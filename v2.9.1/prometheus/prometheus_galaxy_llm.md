# ARCHITECTURAL_BRIEF: prometheus
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/prometheus/prometheus` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1403 analyzed artifact(s), 303064 LOC.
- **Load-bearing artifact:** `util/testutil/testing.go` -- 260 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `web/api/v1/openapi_examples.go` -- pulls in 154 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `scrape/testdata/ca.cer` at magnitude 5000.0 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 1403 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 188 |
| Total LOC | 303064 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 88.2% |
| Dominant Lang | GO |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5446 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2887 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8198 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 89 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| GO | 676 | 251438 | 48.2% |
| YAML | 317 | 3284 | 22.6% |
| TYPESCRIPT | 242 | 39752 | 17.2% |
| JSON | 47 | 4667 | 3.3% |
| CSS | 29 | 1300 | 2.1% |
| MARKDOWN | 27 | 0 | 1.9% |
| PLAINTEXT | 23 | 10 | 1.6% |
| SHELL | 15 | 594 | 1.1% |
| JAVASCRIPT | 10 | 267 | 0.7% |
| MAKEFILE | 4 | 219 | 0.3% |
| XML | 4 | 0 | 0.3% |
| PROTO | 4 | 306 | 0.3% |
| HTML | 3 | 43 | 0.2% |
| DOCKERFILE | 1 | 29 | 0.1% |
| YACC | 1 | 1155 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `3.088`
> **Composition Archetype:** `Hub-Coupled App` (z +3.09; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 36%, Callbacks & Closures Files 15%, Declarative / Non-Code 9%, Large Core Modules 9%, Large Core Modules (3) 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1353 | 96.4% |
| Unknown | 10 | 0.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 40 | 2.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 188*

**Composition by Extension & Reason:**
- `.md`: 41x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3284 LOC)
- `.yml`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Monolithic Amalgamation: 40012 LOC exceeds safe regex boundaries)
- `no_extension`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Binary Format Detected), 2x Unsupported Format (.undeterminable)
- `.test`: 20x Excluded (Unsupported Extension: '.test')
- `.go`: 1x Excluded (Machine-Generated Source Code Signature: 400 LOC), 1x Excluded (Saturation: Line 71 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 905 LOC)
- `.prom`: 9x Excluded (Unsupported Extension: '.prom')
- `.js`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 23 exceeds 500 chars)
- `.mod`: 5x Unsupported Format (.mod)
- `.sum`: 3x Excluded (Unsupported Extension: '.sum'), 2x Unsupported Format (.sum)
- `.json`: 1x Excluded (Static Asset Blob without Intent: 2334 LOC), 1x Excluded (Massive Static Asset Blob: 20001 LOC), 1x Excluded (Massive Static Asset Blob: 9760 LOC)
- `.libsonnet`: 4x Excluded (Unsupported Extension: '.libsonnet')
- `.snap`: 3x Unsupported Format (.snap)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.svg`: 2x Excluded (Machine-Generated Source Code Signature: 4 LOC)
- `.xml`: 2x Excluded (Saturation: Line 1 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 10.1 | 4.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 29.4 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 21.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 11.1 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.8 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 5.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 34.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 88.5 | 0.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 31.4 | 1.0 | 0.2 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 8.6 | 7.4 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 39.1 | 12.5 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.9 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 15527 | 601 | 27 | `promql/parser/parse_test.go` |
| cleanup | 1389 | 219 | 1 | `tsdb/head_test.go` |
| guards | 7772 | 641 | 14 | `web/ui/mantine-ui/src/promql/functionDocs.tsx` |
| danger | 1825 | 293 | 3 | `tsdb/head_test.go` |
| concurrency | 2467 | 203 | 2 | `scrape/scrape_test.go` |
| connectivity | 9071 | 815 | 18 | `config/config.go` |
| io | 1013 | 251 | 2 | `web/ui/mantine-ui/src/promql/functionDocs.tsx` |
| crypto | 0 | 0 | 0 | - |
| ipc | 123 | 30 | 0 | `tsdb/fileutil/dir_windows.go` |
| time | 965 | 186 | 1 | `scrape/scrape_test.go` |
| serialization | 101 | 59 | 0 | `promql/value.go` |
| regex | 111 | 46 | 0 | `promql/promqltest/test.go` |
| events | 404 | 62 | 0 | `discovery/aws/msk_test.go` |
| tests | 16434 | 310 | 18 | `tsdb/db_test.go` |
| docs | 18076 | 724 | 28 | `tsdb/db_test.go` |
| debt | 739 | 197 | 1 | `promql/parser/generated_parser.y` |
| mutation | 35589 | 805 | 65 | `tsdb/db_test.go` |
| dead_code | 3614 | 569 | 7 | `tsdb/head_test.go` |
| credential | 19 | 12 | 0 | `discovery/moby/testdata/swarmprom/nodes.json` |
| threat | 150 | 51 | 0 | `discovery/registry.go` |
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

1. **testing.go** (`util/testutil/testing.go`) — 260 inbound connections
2. **errors.go** (`storage/errors.go`) — 201 inbound connections
3. **strconv.go** (`util/strutil/strconv.go`) — 132 inbound connections
4. **http.go** (`discovery/http/http.go`) — 114 inbound connections
5. **sync.go** (`tsdb/fileutil/sync.go`) — 103 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **openapi_examples.go** (`web/api/v1/openapi_examples.go`) — 154 outbound dependencies
2. **mock_test.go** (`discovery/openstack/mock_test.go`) — 140 outbound dependencies
3. **mock_test.go** (`discovery/digitalocean/mock_test.go`) — 134 outbound dependencies
4. **main.go** (`cmd/prometheus/main.go`) — 118 outbound dependencies
5. **functions.go** (`promql/functions.go`) — 99 outbound dependencies

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
- `main` **(I/O & Config Routines)** (@ `cmd/prometheus/main.go`) -> Impact: **228.8** | LOC: 1215
- `test` **(Many-Argument Workhorses)** (@ `cmd/promtool/unittest.go`) -> Impact: **225.3** | LOC: 332
  * *Intent:* // test performs the unit tests.
- `Checkpoint` **(Many-Argument Workhorses)** (@ `tsdb/wlog/checkpoint.go`) -> Impact: **215.9** | LOC: 301
  * *Intent:* // Checkpoint creates a compacted checkpoint of segments in range [from, to] in the given WAL. // It includes the most recent checkpoint if it exists....
- `aggregationK` **(Many-Argument Workhorses)** (@ `promql/engine.go`) -> Impact: **208.9** | LOC: 219
  * *Intent:* // aggregationK evaluates topk, bottomk, limitk, or limit_ratio at one timestep on inputMatrix. // Output that has the same labels as the input, but j...
- `unmarshalWithoutLabels` **(Many-Argument Workhorses)** (@ `prompb/io/prometheus/client/decoder.go`) -> Impact: **175.1** | LOC: 281

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `scrape/testdata` | 9 | 40000.0 | 0.0% | 0.0% |
| `tsdb` | 42 | 23824.48 | 16.26% | 46.75% |
| `promql` | 18 | 8839.22 | 18.98% | 38.86% |
| `scrape` | 10 | 6663.82 | 24.48% | 47.56% |
| `storage/remote` | 29 | 6349.4 | 15.79% | 56.43% |
| `tsdb/chunkenc` | 18 | 5421.34 | 25.24% | 44.65% |
| `web/ui/react-app` | 3 | 5017.78 | 0.0% | 0.0% |
| `tracing/testdata` | 1 | 5000.0 | 0.0% | 0.0% |
| `model/histogram` | 9 | 4340.02 | 20.86% | 23.92% |
| `discovery/aws` | 20 | 4331.66 | 16.72% | 47.49% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `rules/origin_test.go` -> **100.0%** Exposure
- `tsdb/mocks_test.go` -> **99.9999%** Exposure
- `tsdb/record/buffers.go` -> **99.9998%** Exposure
- `web/api/v1/errors_test.go` -> **99.9986%** Exposure
- `promql/parser/generated_parser.y` -> **99.9804%** Exposure
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
- `discovery/vultr/mock_test.go` -> **99.9431%** Exposure
- `notifier/manager_test.go` -> **20.5232%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `9363` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `scrape/testdata/ca.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/client.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/server.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/servername.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/testdata/servername.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tracing/testdata/ca.cer` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `web/ui/react-app/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `promql/engine.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3986.4 | **LOC:** 4611 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 48.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **43**; blast radius 0.418; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 53.9007% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `aggregation` **(Many-Argument Workhorses)** (Impact: 315.2)
    * *Intent:* // aggregation evaluates sum, avg, count, stdvar, stddev or quantile at one timestep on inputMatrix....
  * `eval` **(Many-Argument Workhorses)** (Impact: 254.7)
    * *Intent:* // eval evaluates the given expression as the given AST expression node requires.
  * `aggregationK` **(Many-Argument Workhorses)** (Impact: 208.9)
    * *Intent:* // aggregationK evaluates topk, bottomk, limitk, or limit_ratio at one timestep on inputMatrix. // O...
  * `VectorBinop` **(Many-Argument Workhorses)** (Impact: 141.1)
    * *Intent:* // VectorBinop evaluates a binary operation between two Vectors, excluding set operators.
  * `vectorElemBinop` **(Many-Argument Workhorses)** (Impact: 129.5)
    * *Intent:* // vectorElemBinop evaluates a binary operation between two Vector elements.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 469 instances
* *High Risk Execution (weighted view):* 15
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 1444
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 913`, `structural_boundaries: 513`, `args: 106`, `func_start: 106`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 19`, `state_mutation: 506`, `dead_code: 6`, `planned_debt: 8`, `unreferenced_by_name: 6`
* *Architecture:* `api: 70`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 42`, `doc: 347`, `test: 2`, `sync_locks: 5`, `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` bytes, heap, context, errors, fmt, prometheus, model, promslog...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/db_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 3352.78 | **LOC:** 9687 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 16.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **52**; blast radius 0.418; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.0%), Guard Balance (formerly Safety Score) (52.8%), Debt Markers (formerly Tech Debt) (44.1%)
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
* *Amplified Cascading Flux:* 389 instances
* *Concurrency (weighted view):* 77
* *Memory Alloc (weighted view):* 24
* *State Mutation (weighted view):* 1594
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 490`, `structural_boundaries: 597`, `args: 148`, `func_start: 148`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 68`, `state_mutation: 816`, `dead_code: 1`, `planned_debt: 9`, `fragile_debt: 4`, `unreferenced_by_name: 103`
* *Architecture:* `io: 5`, `api: 111`, `concurrency: 22`, `import: 1`
* *Defense:* `safety: 6`, `doc: 678`, `test: 1513`, `sync_locks: 4`, `immutability_locks: 14`, `cleanup: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` bufio, bytes, context, binary, errors, flag, float, fmt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/scrape_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 3065.8 | **LOC:** 6959 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 42.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **79**; blast radius 0.418; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Concurrency Surface (formerly Concurrency) (98.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.8%), Guard Balance (formerly Safety Score) (66.9%)
- **Documentation Coverage:** 86.0544% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testConvertClassicHistogramsToNHCB` **(Many-Argument Workhorses)** (Impact: 102.0)
  * `testScrapeLoopAppend` **(Many-Argument Workhorses)** (Impact: 34.3)
  * `TestScrapeLoopAppend_WithStorage` **(I/O & Config Routines)** (Impact: 30.6)
    * *Intent:* // TestScrapeLoopAppend_WithStorage tests appends and storage integration for the // large input fil...
  * `testScrapeLoopRun` **(Many-Argument Workhorses)** (Impact: 29.7)
  * `testScrapeLoopRunCreatesStaleMarkersOnSampleLimit` **(Many-Argument Workhorses)** (Impact: 24.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Race Conditions:* 74 instances
* *Amplified Cascading Flux:* 259 instances
* *High Risk Execution (weighted view):* 6
* *Concurrency (weighted view):* 467
* *Memory Alloc (weighted view):* 23
* *State Mutation (weighted view):* 1190
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 357`, `structural_boundaries: 389`, `args: 192`, `func_start: 192`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 64`, `high_risk_execution: 12`, `state_mutation: 672`, `planned_debt: 5`, `fragile_debt: 1`, `unreferenced_by_name: 100`
* *Architecture:* `io: 23`, `api: 102`, `concurrency: 97`, `import: 1`
* *Defense:* `safety: 20`, `doc: 230`, `test: 651`, `sync_locks: 21`, `immutability_locks: 7`, `cleanup: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` 2, __name__, amend, vnd.google.protobuf, bytes, gzip, context, binary...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/head_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2800.34 | **LOC:** 7918 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 17.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **58**; blast radius 0.418; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (83.4%), Debt Markers (formerly Tech Debt) (58.0%), Guard Balance (formerly Safety Score) (51.0%)
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
* *Amplified Cascading Flux:* 331 instances
* *Concurrency (weighted view):* 58
* *Memory Alloc (weighted view):* 22
* *State Mutation (weighted view):* 1283
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 468`, `structural_boundaries: 442`, `args: 130`, `func_start: 130`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 93`, `high_risk_execution: 2`, `state_mutation: 621`, `dead_code: 3`, `planned_debt: 6`, `fragile_debt: 5`, `unreferenced_by_name: 109`
* *Architecture:* `io: 2`, `api: 111`, `concurrency: 13`, `import: 1`
* *Defense:* `safety: 9`, `doc: 481`, `test: 1422`, `sync_locks: 11`, `immutability_locks: 20`, `cleanup: 130`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` __name__, a, a_unique, b, b_tens, c_ninety, context, decode_samples...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/db_append_v2_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2513.72 | **LOC:** 7705 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 30.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **37**; blast radius 0.418; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.7%), Guard Balance (formerly Safety Score) (53.0%), Debt Markers (formerly Tech Debt) (38.6%)
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
* *Amplified Cascading Flux:* 299 instances
* *Concurrency (weighted view):* 30
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 1260
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 355`, `structural_boundaries: 410`, `args: 93`, `func_start: 93`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 662`, `planned_debt: 8`, `fragile_debt: 3`, `unreferenced_by_name: 73`
* *Architecture:* `io: 3`, `api: 74`, `concurrency: 10`, `import: 1`
* *Defense:* `safety: 2`, `doc: 558`, `test: 1262`, `sync_locks: 3`, `immutability_locks: 6`, `cleanup: 85`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` bufio, context, float, fmt, v2, prometheus, testutil, promslog...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `model/histogram/float_histogram.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2194.2 | **LOC:** 2455 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.418; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (35.8%)
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
* *Structure:* `branch: 412`, `structural_boundaries: 217`, `args: 54`, `func_start: 54`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 11`, `state_mutation: 437`, `dead_code: 4`, `planned_debt: 2`, `unreferenced_by_name: 20`
* *Architecture:* `api: 41`, `import: 1`
* *Defense:* `safety: 10`, `doc: 218`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` errors, fmt, kahansum, math, strings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `web/ui/module/codemirror-promql/src/complete/hybrid.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 2020.97 | **LOC:** 1651 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.418; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.5%), Concurrency Surface (formerly Concurrency) (16.2%), Complexity Load (formerly Cognitive Load) (5.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 62`, `args: 19`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `io: 6`, `concurrency: 4`, `import: 8`
* *Defense:* `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` utils-test, hybrid, index, promql.terms, autocomplete, language, lezer-promql, nock
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `promql/functions.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1854.9 | **LOC:** 2383 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 12.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **99**; blast radius 0.418; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (43.7%)
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
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 218`, `dead_code: 2`, `planned_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 15`, `import: 1`
* *Defense:* `safety: 16`, `doc: 119`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` abs, absent, absent_over_time, acos, acosh, asin, asinh, atan...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/db.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1630.62 | **LOC:** 2632 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 15.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 0.418; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (86.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.7%)
- **Documentation Coverage:** 15.2174% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `open` **(Many-Argument Workhorses)** (Impact: 130.4)
    * *Intent:* // open returns a new DB in the given directory. // It initializes the lockfile, WAL, compactor, and...
  * `run` **(Compute Cores)** (Impact: 38.8)
  * `Querier` **(Many-Argument Workhorses)** (Impact: 36.7)
    * *Intent:* // Querier returns a new querier over the data partition for the given time range.
  * `blockChunkQuerierForRange` **(Many-Argument Workhorses)** (Impact: 36.6)
    * *Intent:* // blockChunkQuerierForRange returns individual block chunk queriers from the persistent blocks, in-...
  * `reloadBlocks` **(I/O & Config Routines)** (Impact: 29.4)
    * *Intent:* // reloadBlocks reloads blocks without touching head. // Blocks that are obsolete due to replacement...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 10 instances
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 180 instances
* *Concurrency (weighted view):* 104
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 572
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 394`, `structural_boundaries: 374`, `args: 71`, `func_start: 71`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 212`, `dead_code: 2`, `planned_debt: 5`, `unreferenced_by_name: 16`
* *Architecture:* `api: 103`, `concurrency: 24`, `import: 1`
* *Defense:* `safety: 110`, `doc: 256`, `sync_locks: 68`, `immutability_locks: 1`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` HEAD, block_range, context, duration, errors, fmt, v2, prometheus...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/head_append_v2_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1620.44 | **LOC:** 4891 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **39**; blast radius 0.418; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.8%), Guard Balance (formerly Safety Score) (49.9%), Debt Markers (formerly Tech Debt) (46.0%)
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
* *Amplified Cascading Flux:* 193 instances
* *Concurrency (weighted view):* 33
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 786
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 263`, `args: 65`, `func_start: 65`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 400`, `dead_code: 2`, `planned_debt: 6`, `fragile_debt: 1`, `unreferenced_by_name: 57`
* *Architecture:* `api: 57`, `concurrency: 8`, `import: 1`
* *Defense:* `safety: 2`, `doc: 309`, `test: 912`, `sync_locks: 2`, `immutability_locks: 3`, `cleanup: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` __name__, context, fmt, cmp, prometheus, testutil, go, config...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/head_append.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1607.54 | **LOC:** 2299 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 27.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.418; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.6%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.2%)
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
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 3`, `state_mutation: 245`, `dead_code: 8`, `planned_debt: 15`, `unreferenced_by_name: 2`
* *Architecture:* `api: 22`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 51`, `doc: 227`, `sync_locks: 36`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` context, errors, fmt, exemplar, histogram, labels, metadata, value...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/head_wal.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1540.56 | **LOC:** 1876 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **39**; blast radius 0.418; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (93.3%), Guard Balance (formerly Safety Score) (86.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 33.7838% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadWAL` **(Many-Argument Workhorses)** (Impact: 242.2)
  * `loadWBL` **(Many-Argument Workhorses)** (Impact: 133.8)
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
* *Structure:* `branch: 358`, `structural_boundaries: 303`, `args: 31`, `func_start: 31`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `state_mutation: 215`, `dead_code: 2`, `planned_debt: 6`, `unreferenced_by_name: 7`
* *Architecture:* `io: 1`, `api: 13`, `concurrency: 28`, `import: 1`
* *Defense:* `safety: 64`, `doc: 105`, `sync_locks: 21`, `immutability_locks: 3`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` json, errors, exemplars, fmt, prometheus, exemplar, histogram, labels...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scrape/scrape.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1531.34 | **LOC:** 2302 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 18.2%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **46**; blast radius 1.411; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.4%)
- **Documentation Coverage:** 72.2892% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `append` **(Many-Argument Workhorses)** (Impact: 173.4)
  * `scrapeAndReport` **(Many-Argument Workhorses)** (Impact: 56.0)
    * *Intent:* // scrapeAndReport performs a scrape and then appends the result to the storage // together with rep...
  * `checkAddError` **(Many-Argument Workhorses)** (Impact: 45.1)
    * *Intent:* // Adds samples to the appender, checking the error, and then returns the # of samples added, // whe...
  * `isSeriesPartOfFamily` **(Many-Argument Workhorses)** (Impact: 41.2)
    * *Intent:* // TODO(https://github.com/prometheus/prometheus/issues/17900): Move this to text and OM parser.
  * `endOfRunStaleness` **(Many-Argument Workhorses)** (Impact: 35.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 193 instances
* *Concurrency (weighted view):* 77
* *State Mutation (weighted view):* 600
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 327`, `structural_boundaries: 259`, `args: 67`, `func_start: 67`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 214`, `dead_code: 2`, `planned_debt: 8`, `unreferenced_by_name: 13`
* *Architecture:* `io: 11`, `api: 17`, `concurrency: 17`, `import: 1`
* *Defense:* `safety: 64`, `doc: 153`, `sync_locks: 56`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.411
  * `Choke Point (Betweenness):` 4.6e-05 | `Ripple Effect (Closeness):` 0.010733
  * `Imports (Out-Degree: 8):` bufio, bytes, content_type, context, err, errors, fallback_media_type, fmt...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `storage/remote/queue_manager.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1363.5 | **LOC:** 2321 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **48**; blast radius 0.418; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (42.1%)
- **Documentation Coverage:** 60.2564% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runShard` **(Many-Argument Workhorses)** (Impact: 49.6)
  * `populateV2TimeSeries` **(Many-Argument Workhorses)** (Impact: 43.1)
  * `sendWriteRequestWithBackoff` **(Many-Argument Workhorses)** (Impact: 35.2)
  * `NewQueueManager` **(Many-Argument Workhorses)** (Impact: 31.9)
    * *Intent:* // NewQueueManager builds a new QueueManager and starts a new // WAL watcher with queue manager as t...
  * `sendV2SamplesWithBackoff` **(Many-Argument Workhorses)** (Impact: 31.6)
    * *Intent:* // sendV2SamplesWithBackoff to the remote storage with backoff for recoverable errors.
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Race Conditions:* 23 instances
* *Amplified Cascading Flux:* 131 instances
* *Concurrency (weighted view):* 148
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 449
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 230`, `args: 60`, `func_start: 60`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 187`, `dead_code: 2`, `planned_debt: 14`, `unreferenced_by_name: 11`
* *Architecture:* `api: 20`, `concurrency: 33`, `import: 1`
* *Defense:* `safety: 16`, `doc: 132`, `sync_locks: 74`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` context, dataInRate, dataKeptRatio, dataOutDuration, dataOutRate, dataPending, dataPendingRate, desiredShards...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsdb/head.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 1318.62 | **LOC:** 2708 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 13.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **38**; blast radius 0.418; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.0%), Guard Balance (formerly Safety Score) (72.1%)
- **Documentation Coverage:** 23.8372% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Init` **(Defensive Guards)** (Impact: 74.1)
    * *Intent:* // Init loads data from the write ahead log and prepares the head for writes. // It should be called...
  * `gc` **(Many-Argument Workhorses)** (Impact: 47.3)
    * *Intent:* // gc garbage collects old chunks that are strictly before mint and removes // series entirely that ...
  * `NewHead` **(Many-Argument Workhorses)** (Impact: 38.0)
    * *Intent:* // NewHead opens the head block in dir.
  * `Delete` **(Many-Argument Workhorses)** (Impact: 36.1)
    * *Intent:* // Delete all samples in the range of [mint, maxt] for series that satisfy the given // label matche...
  * `loadMmappedChunks` **(Compute Cores)** (Impact: 28.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 134 instances
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 452
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 288`, `structural_boundaries: 360`, `args: 105`, `func_start: 105`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 184`, `planned_debt: 7`
* *Architecture:* `api: 111`, `concurrency: 3`, `import: 1`
* *Defense:* `safety: 49`, `doc: 248`, `sync_locks: 81`, `immutability_locks: 4`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.418
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` checkpoint_replay_duration, chunk_snapshot_load_duration, context, err, errors, first, fmt, v2...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tsdb/head_test.go` -> Churn: **83.4%** | Cog Load: 13.755% | Debt: 57.9614%
- `scrape/scrape_test.go` -> Churn: **77.8%** | Cog Load: 43.6696% | Debt: 53.7535%
- `tsdb/agent/db.go` -> Churn: **69.51%** | Cog Load: 43.658% | Debt: 62.9113%
- `scrape/manager.go` -> Churn: **66.11%** | Cog Load: 40.642% | Debt: 98.8618%
- `storage/remote/queue_manager_test.go` -> Churn: **63.96%** | Cog Load: 13.0787% | Debt: 50.5494%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `web/ui/module/codemirror-promql/src/complete/hybrid.test.ts` -> **Julius Volz** (100.0% isolated ownership) | Magnitude: 2020.97
- `discovery/aws/rds.go` -> **Matt** (100.0% isolated ownership) | Magnitude: 1059.66
- `prompb/io/prometheus/client/decoder.go` -> **Ben Kochie** (100.0% isolated ownership) | Magnitude: 738.34
- `rules/group.go` -> **Ben Kochie** (100.0% isolated ownership) | Magnitude: 666.52
- `tsdb/chunks/head_chunks.go` -> **Ben Kochie** (100.0% isolated ownership) | Magnitude: 579.28

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `discovery/http/http.go` -> **Severity: 0.028** (Bridge: 0.0003 * Flux: 99.6403%)
- `tsdb/chunks/chunks.go` -> **Severity: 0.009** (Bridge: 0.0001 * Flux: 99.9761%)
- `cmd/promtool/tsdb.go` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 99.998%)
- `discovery/targetgroup/targetgroup.go` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 99.9964%)
- `web/ui/mantine-ui/src/components/Accordion/Accordion.tsx` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 98.5211%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `discovery/targetgroup/targetgroup.go` -> **Severity: 8.51** (Embedded: 0.1107 * Error Risk: 76.8525%)
- `model/labels/regexp.go` -> **Severity: 8.343** (Embedded: 0.1002 * Error Risk: 83.288%)
- `discovery/discovery.go` -> **Severity: 5.79** (Embedded: 0.1012 * Error Risk: 57.2305%)
- `discovery/http/http.go` -> **Severity: 5.433** (Embedded: 0.0843 * Error Risk: 64.4922%)
- `discovery/refresh/refresh.go` -> **Severity: 4.613** (Embedded: 0.0639 * Error Risk: 72.1773%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `storage/errors.go` -> **Severity: 1895.6** (Blast Radius: 37.912 * Doc Risk: 50.0%)
- `model/labels/regexp.go` -> **Severity: 1742.557** (Blast Radius: 22.178 * Doc Risk: 78.5714%)
- `web/ui/module/codemirror-promql/src/parser/parser.ts` -> **Severity: 773.9** (Blast Radius: 7.739 * Doc Risk: 100.0%)
- `web/ui/mantine-ui/src/promql/utils.ts` -> **Severity: 554.8** (Blast Radius: 5.548 * Doc Risk: 100.0%)
- `web/ui/mantine-ui/src/state/initializeFromLocalStorage.ts` -> **Severity: 544.9** (Blast Radius: 5.449 * Doc Risk: 100.0%)

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
