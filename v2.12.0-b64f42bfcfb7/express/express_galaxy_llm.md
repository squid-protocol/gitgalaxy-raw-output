# ARCHITECTURAL_BRIEF: express
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/expressjs/express` |
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
- **Scope:** 202 analyzed artifact(s), 16258 LOC.
- **Load-bearing artifact:** `test/support/utils.js` -- 9 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `examples/README.md` -- pulls in 25 dependencies, the widest assembly point in the scan.
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
| Total Artifacts | 213 |
| Analyzed Artifacts (Scanned) | 202 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 11 |
| Total LOC | 16258 |
| Volatility Index | 0.025 |
| % Scanned of codebase = | 94.8% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6446 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3287 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5078 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 27 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 141 | 15682 | 69.8% |
| HTML | 35 | 267 | 17.3% |
| PLAINTEXT | 13 | 1 | 6.4% |
| YAML | 5 | 264 | 2.5% |
| MARKDOWN | 4 | 0 | 2.0% |
| CSS | 4 | 44 | 2.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 201 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 41%, Data / Markup / Trivial 32%, Callbacks & Closures Files 12%, Large Core Modules (2) 7%, State Mutators Files 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 185 | 91.6% |
| Unknown | 1 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 16 | 7.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 11*

**Composition by Extension & Reason:**
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.hbs`: 3x Excluded (Unsupported Extension: '.hbs')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.send`: 1x Excluded (Unsupported Extension: '.send')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 64.7 | 6.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 33.6 | 44.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 1.0 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 71.8 | 6.3 | 2.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 35.4 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.5 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 26.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 53 | 16 | 0 | `test/express.json.js` |
| cleanup | 10 | 4 | 0 | `test/app.listen.js` |
| guards | 271 | 48 | 3 | `lib/response.js` |
| danger | 294 | 64 | 5 | `test/express.urlencoded.js` |
| concurrency | 47 | 13 | 0 | `examples/search/index.js` |
| connectivity | 449 | 100 | 6 | `test/app.router.js` |
| io | 190 | 39 | 2 | `test/res.sendFile.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 2 | 1 | 0 | `examples/web-service/index.js` |
| time | 17 | 8 | 0 | `test/res.sendFile.js` |
| serialization | 17 | 6 | 0 | `lib/response.js` |
| regex | 24 | 14 | 0 | `lib/response.js` |
| events | 206 | 69 | 2 | `lib/response.js` |
| tests | 3340 | 89 | 44 | `test/express.static.js` |
| docs | 160 | 44 | 1 | `lib/response.js` |
| debt | 171 | 44 | 2 | `test/express.static.js` |
| mutation | 3475 | 158 | 49 | `lib/response.js` |
| dead_code | 24 | 10 | 0 | `examples/mvc/controllers/user/index.js` |
| credential | 3 | 2 | 0 | `test/res.cookie.js` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 4 | 3 | 0 | `examples/search/public/client.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/res.sendFile.js` (Hits: 52)
- `test/res.render.js` (Hits: 23)
- `test/app.render.js` (Hits: 20)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **utils.js** (`test/support/utils.js`) — 9 inbound connections
2. **utils.js** (`lib/utils.js`) — 7 inbound connections
3. **db.js** (`examples/mvc/db.js`) — 3 inbound connections
4. **express.js** (`lib/express.js`) — 3 inbound connections
5. **index.js** (`examples/auth/index.js`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.md** (`examples/README.md`) — 25 outbound dependencies
2. **response.js** (`lib/response.js`) — 16 outbound dependencies
3. **res.sendFile.js** (`test/res.sendFile.js`) — 9 outbound dependencies
4. **index.js** (`examples/route-separation/index.js`) — 8 outbound dependencies
5. **application.js** (`lib/application.js`) — 8 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `send` **(Defensive Guards)** (@ `lib/response.js`) -> Impact: **45.7** | LOC: 94
  * *Intent:* /** * Send a response. * * Examples: * * res.send(Buffer.from('wahoo')); * res.send({ some: 'json' }); * res.send('<p>some html</p>'); * */...
- `exports` **(Compute Cores)** (@ `examples/mvc/lib/boot.js`) -> Impact: **38.3** | LOC: 73
- `sendfile` **(Many-Argument Workhorses)** (@ `lib/response.js`) -> Impact: **35.8** | LOC: 89
  * *Intent:* // pipe the send file stream
- `download` **(Defensive Guards)** (@ `lib/response.js`) -> Impact: **33.8** | LOC: 50
  * *Intent:* * and optional callback `callback(err)`. The callback is invoked * when the data transfer is complete, or when an error has * occurred. Be sure to che...
- `sendFile` **(Defensive Guards)** (@ `lib/response.js`) -> Impact: **28.1** | LOC: 43
  * *Intent:* * , file = req.params.file; * * req.user.mayViewFilesFrom(uid, function(yes){ * if (yes) { * res.sendFile('/uploads/' + uid + '/' + file); * } else { ...
- `stringify` **(Defensive Guards)** (@ `lib/response.js`) -> Impact: **23.6** | LOC: 25
  * *Intent:* /** * Stringify JSON, like JSON.stringify, but v8 optimized, with the * ability to escape characters that can trigger HTML sniffing. * */
- `render` **(Many-Argument Workhorses)** (@ `lib/application.js`) -> Impact: **22.7** | LOC: 54
  * *Intent:* * rendered template string. * * Example: * * app.render('email', { name: 'Tobi' }, function(err, html){ * // ... * }) * */
- `cookie` **(Many-Argument Workhorses)** (@ `lib/response.js`) -> Impact: **17.7** | LOC: 34
  * *Intent:* * * // "Remember Me" for 15 minutes * res.cookie('rememberme', '1', { expires: new Date(Date.now() + 900000), httpOnly: true }); * * // same as above ...
- `View` **(Defensive Guards)** (@ `lib/view.js`) -> Impact: **16.1** | LOC: 44
  * *Intent:* /** * Initialize a new `View` with the given `name`. * * Options: * * - `defaultEngine` the default template engine name * - `engines` template engine...
- `use` **(Defensive Guards)** (@ `lib/application.js`) -> Impact: **15.5** | LOC: 55
  * *Intent:* /** * Proxy `Router#use()` to add middleware to the app router. * See Router#use() documentation for details. * * If the _fn_ parameter is an express ...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `__monolith__` | 5 | 5098.38 | 0.0% | 0.0% |
| `test` | 70 | 2744.08 | 3.4% | 0.0% |
| `lib` | 6 | 1281.2 | 34.68% | 0.0% |
| `test/acceptance` | 18 | 307.62 | 1.19% | 0.0% |
| `examples/mvc/lib` | 1 | 89.56 | 64.75% | 0.0% |
| `examples/route-separation` | 4 | 84.74 | 17.95% | 0.0% |
| `test/support` | 3 | 69.24 | 6.86% | 0.0% |
| `examples/error-pages/views` | 5 | 68.78 | 0.0% | 0.0% |
| `examples/view-locals` | 2 | 57.26 | 12.7% | 0.0% |
| `examples/auth/views` | 3 | 55.94 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `lib/application.js` -> **100.0%** Exposure
- `lib/response.js` -> **100.0%** Exposure
- `lib/utils.js` -> **100.0%** Exposure
- `lib/view.js` -> **100.0%** Exposure
- `lib/request.js` -> **99.9739%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/app.use.js` -> **0** Orphaned Functions | **28** Duplicates
- `test/app.router.js` -> **0** Orphaned Functions | **11** Duplicates
- `test/app.route.js` -> **0** Orphaned Functions | **10** Duplicates
- `test/res.format.js` -> **0** Orphaned Functions | **10** Duplicates
- `test/app.render.js` -> **0** Orphaned Functions | **7** Duplicates

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
- **Unknown Dependencies:** `265` packages imported that bypass the Zero-Trust whitelist.

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/response.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.144)
- **Top Global Matches:** file_cluster_15: 8.144, file_cluster_4: 8.223, file_cluster_12: 8.677
- **Magnitude:** 623.3 | **LOC:** 1048 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 8.791; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.9%), Complexity Load (formerly Cognitive Load) (39.8%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send` **(Defensive Guards)** (Impact: 45.7)
    * *Intent:* /** * Send a response. * * Examples: * * res.send(Buffer.from('wahoo')); * res.send({ some: 'json' }...
  * `sendfile` **(Many-Argument Workhorses)** (Impact: 35.8)
    * *Intent:* // pipe the send file stream
  * `download` **(Defensive Guards)** (Impact: 33.8)
    * *Intent:* * and optional callback `callback(err)`. The callback is invoked * when the data transfer is complet...
  * `sendFile` **(Defensive Guards)** (Impact: 28.1)
    * *Intent:* * , file = req.params.file; * * req.user.mayViewFilesFrom(uid, function(yes){ * if (yes) { * res.sen...
  * `stringify` **(Defensive Guards)** (Impact: 23.6)
    * *Intent:* /** * Stringify JSON, like JSON.stringify, but v8 optimized, with the * ability to escape characters...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 88 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 273
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 132`, `args: 41`, `func_start: 48`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 97`
* *Architecture:* `io: 2`, `api: 10`, `concurrency: 1`, `import: 19`
* *Defense:* `safety: 61`, `doc: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.791
  * `Choke Point (Betweenness):` 7.5e-05 | `Ripple Effect (Closeness):` 0.013777
  * `Imports (Out-Degree: 1):` utils, content-disposition, cookie, cookie-signature, depd, encodeurl, escape-html, http-errors...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/application.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.073)
- **Top Global Matches:** file_cluster_15: 6.073, file_cluster_12: 7.297, file_cluster_11: 7.837
- **Magnitude:** 276.54 | **LOC:** 632 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 8.791; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (65.7%), Complexity Load (formerly Cognitive Load) (43.2%), Connectivity (formerly Api Exposure) (31.6%)
- **Documentation Coverage:** 15.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render` **(Many-Argument Workhorses)** (Impact: 22.7)
    * *Intent:* * rendered template string. * * Example: * * app.render('email', { name: 'Tobi' }, function(err, htm...
  * `use` **(Defensive Guards)** (Impact: 15.5)
    * *Intent:* /** * Proxy `Router#use()` to add middleware to the app router. * See Router#use() documentation for...
  * `set` **(Compute Cores)** (Impact: 12.0)
    * *Intent:* * Assign `setting` to `val`, or return `setting`'s value. * * app.set('foo', 'bar'); * app.set('foo'...
  * `handle` **(Many-Argument Workhorses)** (Impact: 9.3)
    * *Intent:* /** * Dispatch a req, res pair into the application. Starts pipeline processing. * * If no callback ...
  * `defaultConfiguration` **(I/O & Config Routines)** (Impact: 7.6)
    * *Intent:* /** * Initialize application configuration. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 66`, `args: 25`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 59`
* *Architecture:* `io: 1`, `api: 5`, `import: 11`
* *Defense:* `safety: 27`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.791
  * `Choke Point (Betweenness):` 0.000224 | `Ripple Effect (Closeness):` 0.013777
  * `Imports (Out-Degree: 2):` utils, view, debug, finalhandler, node:http, node:path, once, router
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/express.urlencoded.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.668)
- **Top Global Matches:** file_cluster_12: 7.668, file_cluster_10: 8.466, file_cluster_7: 9.578
- **Magnitude:** 187.72 | **LOC:** 829 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.948; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.4%), Concurrency Surface (formerly Concurrency) (13.1%), Complexity Load (formerly Cognitive Load) (11.2%), Connectivity (formerly Api Exposure) (4.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createApp` **(Callbacks & Closures)** (Impact: 5.1)
  * `createManyParams` **(Defensive Guards)** (Impact: 5.0)
  * `verify` **(Defensive Guards)** (Impact: 4.3)
  * `verify` **(Defensive Guards)** (Impact: 4.3)
  * `verify` **(Defensive Guards)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 71`, `args: 120`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 105`
* *Architecture:* `api: 4`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 8`, `test: 177`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., node:assert, node:async_hooks, node:buffer, supertest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/app.router.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.727)
- **Top Global Matches:** file_cluster_10: 6.727, file_cluster_15: 8.186, file_cluster_13: 9.122
- **Magnitude:** 176.18 | **LOC:** 1218 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 3.948; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (42.5%), Concurrency Surface (formerly Concurrency) (22.2%), Connectivity (formerly Api Exposure) (11.8%), Complexity Load (formerly Cognitive Load) (3.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fn3` **(State Mutators)** (Impact: 2.4)
  * `sawError` **(State Mutators)** (Impact: 2.4)
  * `sawError` **(State Mutators)** (Impact: 2.4)
  * `handleError` **(Parameter Forwarders)** (Impact: 2.4)
  * `sawError` **(State Mutators)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 134`, `args: 210`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 33`, `duplicate_logic: 11`
* *Architecture:* `io: 1`, `api: 65`, `concurrency: 9`, `import: 6`
* *Defense:* `safety: 9`, `test: 172`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .., utils, utils, after, node:assert, supertest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/express.json.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.492)
- **Top Global Matches:** file_cluster_10: 7.492, file_cluster_12: 7.806, file_cluster_15: 9.639
- **Magnitude:** 170.8 | **LOC:** 756 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.948; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (48.0%), Concurrency Surface (formerly Concurrency) (13.2%), Complexity Load (formerly Cognitive Load) (9.3%), Connectivity (formerly Api Exposure) (4.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createApp` **(Callbacks & Closures)** (Impact: 5.2)
  * `verify` **(Defensive Guards)** (Impact: 4.3)
  * `verify` **(Defensive Guards)** (Impact: 4.3)
  * `verify` **(Defensive Guards)** (Impact: 4.2)
  * `verify` **(Defensive Guards)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 65`, `args: 112`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 100`, `duplicate_logic: 4`
* *Architecture:* `api: 4`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 10`, `test: 149`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., node:assert, node:async_hooks, node:buffer, supertest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/utils.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.504)
- **Top Global Matches:** file_cluster_15: 7.504, file_cluster_10: 7.997, file_cluster_9: 8.336
- **Magnitude:** 136.6 | **LOC:** 272 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **8**; blast radius 28.586; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (66.6%), Guard Balance (formerly Safety Score) (57.2%), Complexity Load (formerly Cognitive Load) (36.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `acceptParams` **(Defensive Guards)** (Impact: 12.9)
    * *Intent:* /** * Parse accept params `str` returning an * object with `.value`, `.quality` and `.params`. * */
  * `compileETag` **(Defensive Guards)** (Impact: 12.5)
    * *Intent:* /** * Compile "etag" value to function. * */
  * `compileQueryParser` **(Defensive Guards)** (Impact: 12.5)
    * *Intent:* /** * Compile "query parser" value to function. * */
  * `compileTrust` **(Defensive Guards)** (Impact: 9.5)
    * *Intent:* /** * Compile "proxy trust" value to function. * */
  * `setCharset` **(Compute Cores)** (Impact: 5.9)
    * *Intent:* /** * Set the charset in a given Content-Type string. * */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 48`, `args: 14`, `func_start: 12`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `api: 13`, `import: 8`
* *Defense:* `safety: 15`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.586
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.032338
  * `Imports (Out-Degree: 0):` content-type, etag, mime-types, node:buffer, node:http, node:querystring, proxy-addr, qs
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `test/express.text.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.646)
- **Top Global Matches:** file_cluster_10: 7.646, file_cluster_12: 7.801, file_cluster_15: 9.702
- **Magnitude:** 127.26 | **LOC:** 567 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.948; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (48.7%), Concurrency Surface (formerly Concurrency) (29.2%), Complexity Load (formerly Cognitive Load) (10.4%), Connectivity (formerly Api Exposure) (5.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createApp` **(Callbacks & Closures)** (Impact: 5.1)
  * `verify` **(Defensive Guards)** (Impact: 4.3)
  * `verify` **(Defensive Guards)** (Impact: 4.2)
  * `verify` **(Defensive Guards)** (Impact: 4.2)
  * `verify` **(Callbacks & Closures)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 59`, `args: 85`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 76`, `duplicate_logic: 2`
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 4`, `test: 111`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., node:assert, node:async_hooks, node:buffer, supertest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/app.render.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.499)
- **Top Global Matches:** file_cluster_10: 6.499, file_cluster_12: 8.921, file_cluster_11: 9.392
- **Magnitude:** 123.98 | **LOC:** 393 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 3.948; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.7%), Complexity Load (formerly Cognitive Load) (25.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (16.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `View` **(State Mutators)** (Impact: 2.0)
  * `View` **(State Mutators)** (Impact: 2.0)
  * `View` **(State Mutators)** (Impact: 2.0)
  * `View` **(State Mutators)** (Impact: 1.9)
  * `render` **(Callbacks & Closures)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 56`, `args: 69`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 53`, `duplicate_logic: 7`
* *Architecture:* `io: 20`, `import: 4`
* *Defense:* `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .., tmpl, node:assert, node:path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/express.raw.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.379)
- **Top Global Matches:** file_cluster_10: 7.379, file_cluster_12: 7.735, file_cluster_15: 9.228
- **Magnitude:** 116.34 | **LOC:** 514 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.948; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.0%), Concurrency Surface (formerly Concurrency) (13.9%), Complexity Load (formerly Cognitive Load) (10.3%), Connectivity (formerly Api Exposure) (5.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createApp` **(Callbacks & Closures)** (Impact: 8.2)
  * `verify` **(Defensive Guards)** (Impact: 4.3)
  * `verify` **(Defensive Guards)** (Impact: 4.2)
  * `verify` **(Defensive Guards)** (Impact: 4.2)
  * `accept` **(Defensive Guards)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 63`, `args: 75`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 63`, `duplicate_logic: 2`
* *Architecture:* `api: 4`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 4`, `test: 96`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., node:assert, node:async_hooks, node:buffer, supertest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/request.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.616)
- **Top Global Matches:** file_cluster_11: 6.616, file_cluster_10: 6.713, file_cluster_15: 6.886
- **Magnitude:** 114.88 | **LOC:** 528 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 8.791; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.6%), Connectivity (formerly Api Exposure) (43.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `header` **(Defensive Guards)** (Impact: 12.3)
  * `host` **(Defensive Guards)** (Impact: 6.7)
    * *Intent:* /** * Parse the "Host" header field to a host. * * When the "trust proxy" setting trusts the socket ...
  * `protocol` **(I/O & Config Routines)** (Impact: 6.0)
    * *Intent:* /** * Return the protocol string "http" or "https" * when requested with TLS. When the "trust proxy"...
  * `is` **(Defensive Guards)** (Impact: 4.9)
    * *Intent:* * // When Content-Type is application/json * req.is('json'); * req.is('application/json'); * req.is(...
  * `hostname` **(Defensive Guards)** (Impact: 4.8)
    * *Intent:* /** * Parse the "Host" header field to a hostname. * * When the "trust proxy" setting trusts the soc...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 63`, `args: 20`, `func_start: 22`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `api: 10`, `import: 8`
* *Defense:* `safety: 12`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.791
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.013777
  * `Imports (Out-Degree: 0):` accepts, fresh, node:http, node:net, parseurl, proxy-addr, range-parser, type-is
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/view.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.997)
- **Top Global Matches:** file_cluster_15: 6.997, file_cluster_11: 7.085, file_cluster_16: 8.336
- **Magnitude:** 101.1 | **LOC:** 206 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 7.686; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (67.6%), Complexity Load (formerly Cognitive Load) (45.1%), Connectivity (formerly Api Exposure) (29.6%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `View` **(Defensive Guards)** (Impact: 16.1)
    * *Intent:* /** * Initialize a new `View` with the given `name`. * * Options: * * - `defaultEngine` the default ...
  * `resolve` **(Compute Cores)** (Impact: 9.6)
    * *Intent:* /** * Resolve the file within the given directory. * */
  * `render` **(Compute Cores)** (Impact: 6.5)
    * *Intent:* /** * Render with the given options. * */
  * `lookup` **(Compute Cores)** (Impact: 5.2)
    * *Intent:* /** * Lookup view by the given `name` * */
  * `onRender` **(Interface Declarations)** (Impact: 3.9)
    * *Intent:* // render, normalizing sync callbacks
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 34`, `args: 7`, `func_start: 10`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* `io: 8`, `api: 3`, `import: 4`
* *Defense:* `safety: 5`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.686
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012189
  * `Imports (Out-Degree: 0):` debug, node:fs, node:path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/mvc/lib/boot.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.188)
- **Top Global Matches:** file_cluster_1: 6.188, file_cluster_3: 48.261, file_cluster_8: 70.074
- **Magnitude:** 89.56 | **LOC:** 84 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 10.271; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (76.4%), Complexity Load (formerly Cognitive Load) (64.7%), Connectivity (formerly Api Exposure) (17.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exports` **(Compute Cores)** (Impact: 38.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 22`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `io: 7`, `api: 1`, `import: 4`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.271
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008955
  * `Imports (Out-Degree: 0):` .., node:fs, node:path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `test/app.param.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.243)
- **Top Global Matches:** file_cluster_10: 4.243, file_cluster_2: 6.992, file_cluster_13: 7.696
- **Magnitude:** 88.24 | **LOC:** 324 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.948; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.4%), Connectivity (formerly Api Exposure) (11.0%), Complexity Load (formerly Cognitive Load) (9.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 35`, `args: 59`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 23`
* *Architecture:* `api: 23`, `import: 2`
* *Defense:* `safety: 8`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., supertest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/Router.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.776)
- **Top Global Matches:** file_cluster_10: 6.776, file_cluster_12: 8.815, file_cluster_13: 10.161
- **Magnitude:** 84.6 | **LOC:** 637 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 3.948; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (48.4%), Guard Balance (formerly Safety Score) (44.2%), Concurrency Surface (formerly Concurrency) (28.0%), Complexity Load (formerly Cognitive Load) (6.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fn1` **(State Mutators)** (Impact: 2.2)
  * `fn2` **(State Mutators)** (Impact: 2.2)
  * `handler` **(Callbacks & Closures)** (Impact: 1.8)
  * `send` **(Callbacks & Closures)** (Impact: 1.6)
  * `testMethod` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 81`, `args: 138`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 29`
* *Architecture:* `api: 12`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 8`, `test: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .., utils, after, node:assert
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `History.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 77.76 | **LOC:** 3888 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/app.use.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.361)
- **Top Global Matches:** file_cluster_10: 6.361, file_cluster_2: 8.158, file_cluster_13: 8.346
- **Magnitude:** 71.7 | **LOC:** 543 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 3.948; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (39.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fn1` **(State Mutators)** (Impact: 2.2)
  * `fn2` **(State Mutators)** (Impact: 2.2)
  * `fn1` **(State Mutators)** (Impact: 2.2)
  * `fn2` **(State Mutators)** (Impact: 2.2)
  * `fn1` **(State Mutators)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 39`, `args: 80`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 28`
* *Architecture:* `import: 4`
* *Defense:* `test: 105`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., after, node:assert, supertest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/express.static.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.836)
- **Top Global Matches:** file_cluster_10: 6.836, file_cluster_12: 8.868, file_cluster_2: 9.961
- **Magnitude:** 58.32 | **LOC:** 816 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 3.948; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (37.1%), Complexity Load (formerly Cognitive Load) (4.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createApp` **(Callbacks & Closures)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 18`, `args: 153`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 36`, `planned_debt: 30`
* *Architecture:* `io: 3`, `import: 6`
* *Defense:* `safety: 2`, `test: 253`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .., utils, node:assert, node:buffer, node:path, supertest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/res.send.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.24)
- **Top Global Matches:** file_cluster_10: 4.24, file_cluster_2: 6.92, file_cluster_13: 7.668
- **Magnitude:** 56.96 | **LOC:** 570 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 3.948; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (39.9%), Complexity Load (formerly Cognitive Load) (4.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 53`, `args: 93`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 128`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .., utils, utils, node:assert, node:buffer, supertest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/auth/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.628)
- **Top Global Matches:** file_cluster_10: 6.628, file_cluster_15: 7.984, file_cluster_2: 8.378
- **Magnitude:** 53.86 | **LOC:** 135 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 7.439; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (59.6%), Complexity Load (formerly Cognitive Load) (51.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.9%), Connectivity (formerly Api Exposure) (7.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `authenticate` **(Defensive Guards)** (Impact: 10.7)
    * *Intent:* // Authenticate using our plain-object database of doom!
  * `restrict` **(State Mutators)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 18`, `args: 13`, `func_start: 2`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `io: 1`, `api: 6`, `import: 4`
* *Defense:* `safety: 1`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.439
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00995
  * `Imports (Out-Degree: 0):` .., express-session, node:path, pbkdf2-password
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `test/res.format.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.352)
- **Top Global Matches:** file_cluster_10: 7.352, file_cluster_12: 8.332, file_cluster_7: 10.055
- **Magnitude:** 53.6 | **LOC:** 249 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 3.948; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.2%), Complexity Load (formerly Cognitive Load) (8.9%), Connectivity (formerly Api Exposure) (2.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `default` **(Defensive Guards)** (Impact: 4.3)
  * `test` **(Callbacks & Closures)** (Impact: 2.9)
  * `default` **(Callbacks & Closures)** (Impact: 2.2)
  * `default` **(Callbacks & Closures)** (Impact: 2.0)
  * `text` **(Callbacks & Closures)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 12`, `args: 54`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 25`, `duplicate_logic: 10`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `safety: 6`, `test: 42`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., after, node:assert, supertest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/res.jsonp.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.015)
- **Top Global Matches:** file_cluster_7: 7.015, file_cluster_12: 7.741, file_cluster_10: 9.39
- **Magnitude:** 50.18 | **LOC:** 331 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 3.948; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (45.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.8%), Connectivity (formerly Api Exposure) (5.5%), Complexity Load (formerly Cognitive Load) (5.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 27`, `args: 56`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 24`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 2`, `test: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .., utils, node:assert, supertest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/res.render.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.514)
- **Top Global Matches:** file_cluster_10: 6.514, file_cluster_11: 7.531, file_cluster_12: 8.659
- **Magnitude:** 45.94 | **LOC:** 368 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 3.948; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (48.8%), Complexity Load (formerly Cognitive Load) (6.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createApp` **(Interface Declarations)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 33`, `args: 57`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 35`
* *Architecture:* `io: 23`, `import: 4`
* *Defense:* `test: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .., tmpl, node:path, supertest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/app.route.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.554)
- **Top Global Matches:** file_cluster_10: 6.554, file_cluster_15: 7.974, file_cluster_13: 8.748
- **Magnitude:** 45.5 | **LOC:** 198 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.948; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (88.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleError` **(Parameter Forwarders)** (Impact: 2.5)
  * `handleError` **(State Mutators)** (Impact: 2.4)
  * `handleError` **(State Mutators)** (Impact: 2.4)
  * `handleError` **(Parameter Forwarders)** (Impact: 2.4)
  * `handleError` **(State Mutators)** (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 28`, `args: 36`, `func_start: 15`
* *Risk/State:* `duplicate_logic: 10`
* *Architecture:* `concurrency: 9`, `import: 2`
* *Defense:* `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., supertest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/config.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.782)
- **Top Global Matches:** file_cluster_10: 5.782, file_cluster_11: 8.076, file_cluster_2: 9.412
- **Magnitude:** 44.86 | **LOC:** 208 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 3.948; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (35.8%), Connectivity (formerly Api Exposure) (10.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fn` **(Callbacks & Closures)** (Impact: 1.1)
  * `fn` **(Callbacks & Closures)** (Impact: 1.1)
  * `fn` **(Interface Declarations)** (Impact: 1.1)
  * `fn1` **(Interface Declarations)** (Impact: 1.1)
  * `fn2` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 46`, `args: 41`, `func_start: 5`
* *Risk/State:* `state_mutation: 19`, `duplicate_logic: 2`
* *Architecture:* `api: 17`, `import: 2`
* *Defense:* `test: 74`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.948
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., node:assert
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `examples/session/index.js` (JAVASCRIPT) | Magnitude: 25.46 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 4, core_var_decl: 4, design_snake_case: 4
- `test/acceptance/route-map.js` (JAVASCRIPT) | Magnitude: 15.78 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 36, test: 16, args: 11, closures: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `lib/request.js` (JAVASCRIPT) | Magnitude: 114.88 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 102, structural_boundaries: 63, core_var_decl: 40, design_snake_case: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `test/res.sendStatus.js` (JAVASCRIPT) | Magnitude: 15.68 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 29, args: 8, test: 8, closures: 8
- `test/acceptance/auth.js` (JAVASCRIPT) | Magnitude: 12.72 | Delta: **0.127** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 100, test: 38, args: 20, closures: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `lib/response.js` (JAVASCRIPT) | Magnitude: 623.3 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 405, structural_boundaries: 132, core_var_decl: 131, branch: 128
- `lib/view.js` (JAVASCRIPT) | Magnitude: 101.1 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 34, core_var_decl: 29, design_snake_case: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `.github/workflows/codeql.yml` (YAML) | Magnitude: 16.74 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 4, args: 3, import: 3
- `.github/workflows/scorecard.yml` (YAML) | Magnitude: 15.72 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 32, args: 8, import: 4, immutability_locks: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/session/redis.js` (JAVASCRIPT) | Magnitude: 25.5 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 6, core_var_decl: 6, design_snake_case: 5

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `test/app.render.js` -> **AkaHarshit** (100.0% isolated ownership) | Magnitude: 123.98
- `examples/auth/index.js` -> **Sam Tucker-Davis** (100.0% isolated ownership) | Magnitude: 53.86
- `test/res.jsonp.js` -> **Murat Kirazkaya** (100.0% isolated ownership) | Magnitude: 50.18

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/express.js` -> **Severity: 0.062** (Bridge: 0.0006 * Flux: 99.9665%)
- `lib/application.js` -> **Severity: 0.022** (Bridge: 0.0002 * Flux: 100.0%)
- `lib/response.js` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `test/support/utils.js` -> **Severity: 2.073** (Embedded: 0.0448 * Error Risk: 46.2925%)
- `lib/utils.js` -> **Severity: 1.851** (Embedded: 0.0323 * Error Risk: 57.2346%)
- `lib/express.js` -> **Severity: 1.037** (Embedded: 0.0178 * Error Risk: 58.3496%)
- `lib/application.js` -> **Severity: 0.905** (Embedded: 0.0138 * Error Risk: 65.6611%)
- `lib/response.js` -> **Severity: 0.894** (Embedded: 0.0138 * Error Risk: 64.9069%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `test/support/tmpl.js` -> **Severity: 1066.1** (Blast Radius: 10.661 * Doc Risk: 100.0%)
- `examples/mvc/lib/boot.js` -> **Severity: 1027.1** (Blast Radius: 10.271 * Doc Risk: 100.0%)
- `test/support/utils.js` -> **Severity: 970.732** (Blast Radius: 29.122 * Doc Risk: 33.3333%)
- `examples/auth/index.js` -> **Severity: 743.9** (Blast Radius: 7.439 * Doc Risk: 100.0%)
- `examples/content-negotiation/index.js` -> **Severity: 743.9** (Blast Radius: 7.439 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 690 call pairs -- scoped 2.9%, unique 0.0%, ambiguous 1.4%, external 95.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 690 | 2.9% | 0.0% | 1.4% | 95.7% |

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
