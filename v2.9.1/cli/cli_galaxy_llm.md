# ARCHITECTURAL_BRIEF: cli
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/npm/cli.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 2994 analyzed artifact(s), 712880 LOC.
- **Load-bearing artifact:** `test/fixtures/mock-npm.js` -- 88 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `workspaces/arborist/test/fixtures/reify-cases/dep-installed-without-bin-link.js` -- pulls in 50 dependencies, the widest assembly point in the scan.
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
| Total Artifacts | 6752 |
| Analyzed Artifacts (Scanned) | 2994 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3758 |
| Total LOC | 712880 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 44.3% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7644 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1978 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.405 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 84 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JSON | 1827 | 549845 | 61.0% |
| JAVASCRIPT | 579 | 161951 | 19.3% |
| PLAINTEXT | 488 | 1 | 16.3% |
| MARKDOWN | 76 | 0 | 2.5% |
| HTML | 10 | 663 | 0.3% |
| SHELL | 9 | 305 | 0.3% |
| BATCH | 3 | 35 | 0.1% |
| POWERSHELL | 2 | 80 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Flat Modular Platform`
> **Architectural Drift Z-Score:** `6.661`
> **Composition Archetype:** `Flat Modular Platform` (z +6.66; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 81%, Declarative / Non-Code 4%, Callbacks & Closures Files 4%, Large Core Modules (2) 4%, Large Core Modules 2%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1381 | 46.1% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Minified & Vendor Opaque Mass | 1049 | 35.0% |
| Static: Literature & Documentation | 563 | 18.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3758*

**Composition by Extension & Reason:**
- `.json`: 849x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Massive Static Asset Blob: 2778 LOC), 4x Excluded (Static Asset Blob without Intent: 2496 LOC)
- `.js`: 803x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 5408 LOC), 1x Excluded (Machine-Generated Source Code Signature: 151 LOC)
- `.tgz`: 783x Excluded (Explicitly Denied Extension: '.tgz')
- `no_extension`: 159x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable)
- `.md`: 154x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 8 LOC), 1x Excluded (Machine-Generated Source Code Signature: 736 LOC)
- `.cjs`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Machine-Generated Source Code Signature: 23 LOC), 2x Excluded (Machine-Generated Source Code Signature: 152 LOC)
- `.py`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 5x Excluded (Unsupported Extension: '.lock')
- `.cmd`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cc`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cts`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mts`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 7.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.8 | 14.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.3 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 81.0 | 3.1 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 11.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 8.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 98.8 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.4 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 53.0 | 1.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 19.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 83 | 38 | 0 | `lib/commands/ls.js` |
| cleanup | 15 | 10 | 0 | `lib/commands/team.js` |
| guards | 2619 | 290 | 0 | `workspaces/arborist/lib/shrinkwrap.js` |
| danger | 4108 | 321 | 1 | `workspaces/arborist/test/fixtures/reify-cases/audit-fix-old-tap.js` |
| concurrency | 9903 | 384 | 2 | `workspaces/arborist/test/arborist/build-ideal-tree.js` |
| connectivity | 1026 | 423 | 1 | `scripts/template-oss/node-integration-yml.hbs` |
| io | 1699 | 177 | 0 | `test/lib/commands/cache.js` |
| crypto | 8 | 8 | 0 | `lib/utils/sbom-cyclonedx.js` |
| ipc | 10 | 6 | 0 | `workspaces/arborist/test/fixtures/reify-cases/tap-with-yarn-lock.js` |
| time | 156 | 44 | 0 | `workspaces/libnpmexec/test/with-lock.js` |
| serialization | 2024 | 225 | 0 | `workspaces/arborist/test/fixtures/reify-cases/tap-with-yarn-lock.js` |
| regex | 1124 | 201 | 0 | `test/lib/commands/diff.js` |
| events | 1092 | 144 | 0 | `workspaces/config/lib/definitions/definitions.js` |
| tests | 779 | 147 | 0 | `workspaces/arborist/test/fixtures/reify-cases/tap-with-yarn-lock.js` |
| docs | 181 | 24 | 0 | `workspaces/arborist/test/fixtures/reify-cases/tap-with-yarn-lock.js` |
| debt | 545 | 142 | 0 | `workspaces/arborist/test/edge.js` |
| mutation | 20933 | 582 | 14 | `workspaces/arborist/test/arborist/reify.js` |
| dead_code | 560 | 274 | 0 | `workspaces/arborist/lib/arborist/build-ideal-tree.js` |
| credential | 3653 | 603 | 2 | `workspaces/arborist/test/fixtures/reify-cases/audit-fix-old-tap.js` |
| threat | 409 | 91 | 0 | `workspaces/arborist/test/isolated-mode.js` |
| ml_ai | 1 | 1 | 0 | `lib/utils/completion.sh` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/lib/commands/cache.js` (Hits: 181)
- `workspaces/arborist/test/arborist/reify.js` (Hits: 178)
- `workspaces/arborist/test/isolated-mode.js` (Hits: 159)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **mock-npm.js** (`test/fixtures/mock-npm.js`) — 88 inbound connections
2. **package-json.hbs** (`scripts/template-oss/package-json.hbs`) — 32 inbound connections
3. **clean-snapshot.js** (`test/fixtures/clean-snapshot.js`) — 22 inbound connections
4. **tmock.js** (`test/fixtures/tmock.js`) — 21 inbound connections
5. **node.js** (`workspaces/arborist/lib/node.js`) — 19 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **dep-installed-without-bin-link.js** (`workspaces/arborist/test/fixtures/reify-cases/dep-installed-without-bin-link.js`) — 50 outbound dependencies
2. **build-ideal-tree.js** (`workspaces/arborist/lib/arborist/build-ideal-tree.js`) — 28 outbound dependencies
3. **reify.js** (`workspaces/arborist/lib/arborist/reify.js`) — 28 outbound dependencies
4. **node.js** (`workspaces/arborist/lib/node.js`) — 20 outbound dependencies
5. **reify.js** (`workspaces/arborist/test/arborist/reify.js`) — 18 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `exports` **(Many-Argument Workhorses)** (@ `workspaces/arborist/test/fixtures/reify-cases/tap-with-yarn-lock.js`) -> Impact: **1013.2** | LOC: 20581
  * *Intent:* // generated from test/fixtures/tap-with-yarn-lock
- `errorMessage` **(Many-Argument Workhorses)** (@ `lib/utils/error-message.js`) -> Impact: **184.7** | LOC: 369
- `exports` **(Many-Argument Workhorses)** (@ `workspaces/arborist/test/fixtures/reify-cases/audit-fix-old-tap.js`) -> Impact: **167.4** | LOC: 13387
  * *Intent:* // generated from test/fixtures/audit-fix-old-tap
- `logHandler` **(Many-Argument Workhorses)** (@ `workspaces/config/test/index.js`) -> Impact: **153.4** | LOC: 947
- `exports` **(Compute Cores)** (@ `workspaces/arborist/test/fixtures/reify-cases/dep-installed-without-bin-link.js`) -> Impact: **144.9** | LOC: 523
  * *Intent:* // generated from test/fixtures/dep-installed-without-bin-link
- `buildLegacyLockfile` **(Many-Argument Workhorses)** (@ `workspaces/arborist/lib/shrinkwrap.js`) -> Impact: **119.8** | LOC: 156
- `filter` **(Many-Argument Workhorses)** (@ `workspaces/arborist/lib/arborist/reify.js`) -> Impact: **114.6** | LOC: 318
- `root` **(Compute Cores)** (@ `workspaces/arborist/lib/node.js`) -> Impact: **112.5** | LOC: 271
- `extract` **(Many-Argument Workhorses)** (@ `workspaces/arborist/test/arborist/build-ideal-tree.js`) -> Impact: **108.7** | LOC: 1293
- `apply` **(Many-Argument Workhorses)** (@ `workspaces/arborist/test/isolated-mode.js`) -> Impact: **106.0** | LOC: 1839

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `test/lib/commands` | 66 | 10059.36 | 22.64% | 0.0% |
| `lib/commands` | 67 | 6635.62 | 53.98% | 46.33% |
| `workspaces/arborist/lib` | 37 | 5931.82 | 54.4% | 14.52% |
| `__monolith__` | 10 | 5118.28 | 5.85% | 0.0% |
| `workspaces/arborist/lib/arborist` | 7 | 3958.74 | 97.0% | 35.07% |
| `lib/utils` | 35 | 2970.24 | 49.26% | 6.99% |
| `workspaces/arborist/test/arborist` | 10 | 2964.8 | 14.3% | 0.0% |
| `workspaces/arborist/test` | 35 | 2896.84 | 8.17% | 0.0% |
| `test/lib/utils` | 21 | 1581.98 | 42.33% | 0.0% |
| `test/lib` | 8 | 1485.24 | 42.67% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `workspaces/libnpmexec/lib/get-bin-from-manifest.js` -> **99.9992%** Exposure
- `scripts/template-oss/root.js` -> **99.7527%** Exposure
- `lib/commands/fund.js` -> **99.386%** Exposure
- `workspaces/arborist/bin/prune.js` -> **99.3307%** Exposure
- `lib/commands/pack.js` -> **98.4904%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `bin/npm` -> **100.0%** Exposure
- `bin/npx` -> **100.0%** Exposure
- `lib/utils/completion.sh` -> **100.0%** Exposure
- `scripts/smoke-tests.sh` -> **100.0%** Exposure
- `bin/npx-cli.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `workspaces/arborist/test/edge.js` -> **0** Orphaned Functions | **106** Duplicates
- `test/lib/commands/profile.js` -> **3** Orphaned Functions | **35** Duplicates
- `test/lib/base-cmd.js` -> **0** Orphaned Functions | **16** Duplicates
- `workspaces/arborist/test/dep-valid.js` -> **0** Orphaned Functions | **14** Duplicates
- `workspaces/libnpmexec/test/with-lock.js` -> **0** Orphaned Functions | **7** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `mock-registry/lib/provenance.js` -> **100.0%** Exposure
- `test/lib/commands/publish.js` -> **99.9997%** Exposure
- `mock-registry/lib/index.js` -> **99.9943%** Exposure
- `workspaces/config/test/definitions/definitions.js` -> **99.6009%** Exposure
- `workspaces/libnpmpublish/test/publish.js` -> **98.8988%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1301` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `workspaces/arborist/test/arborist/reify.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1186.42 | **LOC:** 4016 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (63.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.5%), Connectivity (formerly Api Exposure) (28.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkPackageLock` **(Callbacks & Closures)** (Impact: 42.7)
  * `extract` **(I/O & Config Routines)** (Impact: 23.7)
  * `abbrevpj` **(I/O & Config Routines)** (Impact: 19.6)
  * `onTime` **(Callbacks & Closures)** (Impact: 18.9)
  * `extract` **(Callbacks & Closures)** (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 39 instances
* *Amplified Cascading Flux:* 31 instances
* *Concurrency (weighted view):* 623
* *State Mutation (weighted view):* 169
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 638`, `args: 338`, `func_start: 58`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 107`, `dead_code: 4`, `planned_debt: 3`
* *Architecture:* `io: 178`, `api: 7`, `concurrency: 428`, `import: 64`
* *Defense:* `safety: 26`, `sync_locks: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` index.js, signal-handling.js, advisory-bulk.json, reify-cases, tnock, utils.js, string-locale-compare, fs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `workspaces/arborist/lib/shrinkwrap.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1179.46 | **LOC:** 1183 | **CtrlFlow:** 37.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **15**; blast radius 0.943; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.5%), Guard Balance (formerly Safety Score) (86.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildLegacyLockfile` **(Many-Argument Workhorses)** (Impact: 119.8)
  * `metaFromLock` **(Many-Argument Workhorses)** (Impact: 74.2)
  * `assertNoNewer` **(Defensive Guards)** (Impact: 56.5)
    * *Intent:* // check to make sure that there are no packages newer than or missing from the hidden lockfile
  * `metaFromNode` **(Many-Argument Workhorses)** (Impact: 51.1)
  * `add` **(Defensive Guards)** (Impact: 49.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 137 instances
* *Concurrency (weighted view):* 95
* *State Mutation (weighted view):* 418
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 107`, `args: 47`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `state_mutation: 144`, `dead_code: 14`, `planned_debt: 3`, `fragile_debt: 3`
* *Architecture:* `io: 1`, `api: 6`, `concurrency: 25`, `import: 15`
* *Defense:* `safety: 77`, `sync_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.943
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.002339
  * `Imports (Out-Degree: 2):` consistent-resolve.js, override-resolves.js, relpath.js, spec-from-lock.js, version-from-tgz.js, yarn-lock.js, string-locale-compare, name-from-folder...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `workspaces/arborist/lib/arborist/reify.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1143.88 | **LOC:** 1627 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `filter` **(Many-Argument Workhorses)** (Impact: 114.6)
  * `reify` **(Compute Cores)** (Impact: 67.0)
    * *Intent:* // public method
  * `updateNodes` **(Compute Cores)** (Impact: 61.1)
  * `filterDirectDependencies` **(Compute Cores)** (Impact: 34.6)
  * `buildLinkedActualForDiff` **(Stateful Encapsulated Methods)** (Impact: 28.6)
    * *Intent:* // Build a flat actual tree wrapper for linked installs so the diff can correctly match store entrie...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 37 instances
* *Amplified Cascading Flux:* 102 instances
* *Concurrency (weighted view):* 274
* *State Mutation (weighted view):* 319
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 309`, `structural_boundaries: 208`, `args: 82`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 115`, `dead_code: 24`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* `io: 3`, `api: 5`, `concurrency: 89`, `import: 28`
* *Defense:* `safety: 70`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` add-rm-pkg-deps.js, audit-report.js, calc-dep-flags.js, debug.js, diff.js, isolated-classes.js, optional-set.js, relpath.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `workspaces/arborist/lib/arborist/build-ideal-tree.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1095.3 | **LOC:** 1595 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (93.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildDepStep` **(I/O & Config Routines)** (Impact: 70.8)
  * `nodeFromSpec` **(Many-Argument Workhorses)** (Impact: 57.4)
  * `applyUserRequestsToNode` **(Compute Cores)** (Impact: 52.0)
  * `visit` **(Defensive Guards)** (Impact: 40.2)
  * `loadPeerSet` **(Compute Cores)** (Impact: 37.4)
    * *Intent:* // load all peer deps and meta-peer deps into the node's parent // At the end of this, the node's pe...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 26 instances
* *Amplified Cascading Flux:* 81 instances
* *Concurrency (weighted view):* 205
* *State Mutation (weighted view):* 258
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 321`, `structural_boundaries: 152`, `args: 60`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 96`, `dead_code: 28`, `planned_debt: 4`, `fragile_debt: 11`
* *Architecture:* `io: 4`, `api: 1`, `concurrency: 75`, `import: 28`
* *Defense:* `safety: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` realpath.js, add-rm-pkg-deps.js, calc-dep-flags.js, can-place-dep.js, debug.js, from-path.js, link.js, node.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `workspaces/arborist/test/arborist/build-ideal-tree.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1071.24 | **LOC:** 4574 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (61.7%), Connectivity (formerly Api Exposure) (38.3%), Complexity Load (formerly Cognitive Load) (20.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extract` **(Many-Argument Workhorses)** (Impact: 108.7)
  * `warn` **(Many-Argument Workhorses)** (Impact: 85.5)
  * `rootAndWs` **(Many-Argument Workhorses)** (Impact: 78.6)
    * *Intent:* // The following trees caused an infinite loop in a workspace // https://github.com/npm/cli/issues/3...
  * `printIdeal` **(Many-Argument Workhorses)** (Impact: 29.9)
  * `pj` **(I/O & Config Routines)** (Impact: 23.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 578
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 577`, `args: 243`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 109`, `state_mutation: 14`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 7`
* *Architecture:* `io: 9`, `api: 16`, `concurrency: 538`, `import: 16`
* *Defense:* `safety: 18`, `doc: 2`, `sync_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` .., audit.json, utils.js, mock-registry, a, node:fs, node:path, npm-package-arg...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `workspaces/arborist/lib/node.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1055.9 | **LOC:** 1632 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **20**; blast radius 1.819; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.0%), Guard Balance (formerly Safety Score) (83.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `root` **(Compute Cores)** (Impact: 112.5)
  * `constructor` **(I/O & Config Routines)** (Impact: 69.3)
    * *Intent:* #global #meta #root #workspaces
  * `canReplaceWith` **(Defensive Guards)** (Impact: 30.2)
    * *Intent:* // is it safe to replace one node with another? check the edges to // make sure no one will get upse...
  * `fsParent` **(Defensive Guards)** (Impact: 28.1)
  * `canDedupe` **(Compute Cores)** (Impact: 26.7)
    * *Intent:* // return true if it's safe to remove this node, because anything that // is depending on it would b...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 150 instances
* *State Mutation (weighted view):* 461
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 362`, `structural_boundaries: 157`, `args: 75`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 161`, `dead_code: 25`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 21`, `import: 20`
* *Defense:* `safety: 82`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.819
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.006348
  * `Imports (Out-Degree: 1):` case-insensitive-map.js, consistent-resolve.js, debug.js, edge.js, gather-dep-set.js, inventory.js, override-set.js, printable.js...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `workspaces/config/lib/definitions/definitions.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 908.16 | **LOC:** 2473 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 0.943; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.1%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `flatten` **(Many-Argument Workhorses)** (Impact: 40.6)
  * `flatten` **(Many-Argument Workhorses)** (Impact: 33.7)
    * *Intent:* // basic flattening function, just copy it over camelCase
  * `buildOmitList` **(Defensive Guards)** (Impact: 30.5)
  * `flatten` **(Many-Argument Workhorses)** (Impact: 17.6)
  * `flatten` **(Defensive Guards)** (Impact: 17.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 143 instances
* *State Mutation (weighted view):* 474
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 429`, `structural_boundaries: 41`, `args: 61`, `func_start: 56`
* *Risk/State:* `safety_bypasses: 48`, `state_mutation: 188`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 3`, `duplicate_logic: 6`
* *Architecture:* `io: 14`, `api: 1`, `import: 7`
* *Defense:* `safety: 33`, `sync_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.943
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001336
  * `Imports (Out-Degree: 1):` type-defs.js, definition.js, ci-info, node:fs, node:os, node:path, node:querystring
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `workspaces/config/lib/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 825.34 | **LOC:** 1035 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.4%), Guard Balance (formerly Safety Score) (83.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadObject` **(Many-Argument Workhorses)** (Impact: 42.8)
  * `validate` **(Defensive Guards)** (Impact: 33.2)
  * `loadLocalPrefix` **(Defensive Guards)** (Impact: 23.4)
  * `setCredentialsByURI` **(Compute Cores)** (Impact: 22.5)
  * `invalidHandler` **(Defensive Guards)** (Impact: 21.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 94 instances
* *Concurrency (weighted view):* 73
* *State Mutation (weighted view):* 319
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 124`, `args: 78`, `func_start: 64`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 131`, `dead_code: 12`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 12`, `concurrency: 28`, `import: 17`
* *Defense:* `safety: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` env-replace.js, errors.js, nerf-dart.js, parse-field.js, set-envs.js, type-defs.js, type-description.js, map-workspaces...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `workspaces/config/test/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 803.24 | **LOC:** 1871 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (62.4%), Guard Balance (formerly Safety Score) (62.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `logHandler` **(Many-Argument Workhorses)** (Impact: 153.4)
  * `logHandler` **(Compute Cores)** (Impact: 33.3)
  * `readFile` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `logHandler` **(Callbacks & Closures)** (Impact: 10.8)
  * `logHandler` **(Callbacks & Closures)** (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 46 instances
* *Amplified Cascading Flux:* 28 instances
* *Concurrency (weighted view):* 347
* *State Mutation (weighted view):* 168
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 236`, `args: 147`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 112`, `dead_code: 1`
* *Architecture:* `io: 11`, `api: 2`, `concurrency: 117`, `import: 6`
* *Defense:* `safety: 31`, `test: 1`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` .., definition.js, type-defs.js, node:fs, node:path, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/commands/unpublish.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 783.82 | **LOC:** 654 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (59.7%), Complexity Load (formerly Cognitive Load) (39.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 202
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 114`, `args: 34`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 13`
* *Architecture:* `concurrency: 102`, `import: 3`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mock-npm, mock-registry, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/commands/profile.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 702.24 | **LOC:** 1160 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (57.0%), Complexity Load (formerly Cognitive Load) (49.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (3.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `password` **(Defensive Guards)** (Impact: 16.2)
  * `set` **(Defensive Guards)** (Impact: 13.6)
  * `password` **(Compute Cores)** (Impact: 10.6)
  * `set` **(Defensive Guards)** (Impact: 7.9)
  * `set` **(Defensive Guards)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 49 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 460
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 244`, `args: 136`, `func_start: 77`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 30`, `fragile_debt: 5`, `duplicate_logic: 35`, `unreferenced_by_name: 3`
* *Architecture:* `concurrency: 215`, `import: 4`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mock-npm, tmock, node:util, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `workspaces/arborist/lib/query-selector-all.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 558.68 | **LOC:** 959 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.558; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.2%), Mutation Surface (formerly State Flux) (99.1%), Complexity Load (formerly Cognitive Load) (86.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nodeMatches` **(Many-Argument Workhorses)** (Impact: 54.6)
  * `hasParent` **(Many-Argument Workhorses)** (Impact: 45.9)
    * *Intent:* // checks if a given node has a direct parent in any of the nodes provided in // the compare nodes a...
  * `semverPseudo` **(I/O & Config Routines)** (Impact: 37.5)
  * `vulnPseudo` **(Defensive Guards)** (Impact: 26.4)
  * `attributeMatch` **(Defensive Guards)** (Impact: 26.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 39 instances
* *Concurrency (weighted view):* 62
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 183`, `args: 81`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 47`, `dead_code: 14`, `planned_debt: 4`
* *Architecture:* `io: 1`, `api: 30`, `concurrency: 22`, `import: 9`
* *Defense:* `safety: 37`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000334
  * `Imports (Out-Degree: 1):` string-locale-compare, query, minimatch, node:path, npm-package-arg, npm-registry-fetch, pacote, proc-log...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `workspaces/libnpmexec/test/with-lock.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 547.04 | **LOC:** 359 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.302; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (74.7%), Complexity Load (formerly Cognitive Load) (50.0%), Connectivity (formerly Api Exposure) (13.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `utimes` **(Defensive Guards)** (Impact: 5.9)
  * `rmdirSync` **(Defensive Guards)** (Impact: 5.9)
  * `mkdir` **(Defensive Guards)** (Impact: 5.8)
  * `stat` **(Defensive Guards)** (Impact: 5.8)
  * `mockRmdirSync` **(Callbacks & Closures)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 48 instances
* *Amplified Cascading Flux:* 21 instances
* *Concurrency (weighted view):* 361
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 162`, `args: 82`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 51`, `duplicate_logic: 7`
* *Architecture:* `io: 72`, `api: 1`, `concurrency: 121`, `import: 5`
* *Defense:* `safety: 21`, `test: 1`, `sync_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:fs, node:os, node:path, promises, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mock-registry/lib/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 543.62 | **LOC:** 674 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Credential Material (formerly Secrets Risk) (100.0%), Concurrency Surface (formerly Concurrency) (99.7%), Complexity Load (formerly Cognitive Load) (92.6%)
- **Documentation Coverage:** 97.4026% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tnock` **(Defensive Guards)** (Impact: 35.6)
  * `noMatch` **(Defensive Guards)** (Impact: 23.3)
  * `putPackagePayload` **(Defensive Guards)** (Impact: 15.9)
  * `publish` **(Compute Cores)** (Impact: 13.0)
  * `mocks` **(Callbacks & Closures)** (Impact: 12.7)
    * *Intent:* // Used in Arborist to mock the registry from fixture data on disk // Will eat up all GET requests t...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 50 instances
* *Concurrency (weighted view):* 59
* *State Mutation (weighted view):* 179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 70`, `args: 64`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `state_mutation: 79`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 5`, `api: 29`, `concurrency: 14`, `import: 8`
* *Defense:* `safety: 12`, `doc: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` arborist, json-stringify-safe, nock, node:fs, promises, node:path, npm-package-arg, pacote
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/commands/team.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 519.02 | **LOC:** 433 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (73.0%), Complexity Load (formerly Cognitive Load) (50.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (3.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `result` **(Callbacks & Closures)** (Impact: 23.8)
  * `mockTeam` **(Callbacks & Closures)** (Impact: 3.8)
  * `cleanSnapshot` **(Parameter Forwarders)** (Impact: 1.6)
  * `lsTeams` **(Interface Declarations)** (Impact: 1.4)
  * `add` **(State Mutators)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 60 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 414
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 111`, `args: 54`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 114`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mock-npm, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/commands/ls.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 511.2 | **LOC:** 589 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 0.686; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (87.6%), Complexity Load (formerly Cognitive Load) (87.0%), Guard Balance (formerly Safety Score) (85.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exec` **(Compute Cores)** (Impact: 61.8)
  * `getHumanOutputItem` **(Compute Cores)** (Impact: 41.3)
  * `getJsonOutputItem` **(Many-Argument Workhorses)** (Impact: 37.8)
  * `filterBySelectedWorkspaces` **(Compute Cores)** (Impact: 24.7)
  * `mapEdgesToNodes` **(Compute Cores)** (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 54 instances
* *Concurrency (weighted view):* 27
* *State Mutation (weighted view):* 166
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 66`, `args: 33`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 58`, `dead_code: 6`, `planned_debt: 1`
* *Architecture:* `api: 5`, `concurrency: 7`, `import: 9`
* *Defense:* `safety: 16`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.686
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000668
  * `Imports (Out-Degree: 1):` arborist-cmd.js, installed-deep.js, string-locale-compare, arborist, archy, node:path, npm-package-arg, proc-log...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/utils/error-message.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 498.0 | **LOC:** 454 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.353; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.6%), Complexity Load (formerly Cognitive Load) (80.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `errorMessage` **(Many-Argument Workhorses)** (Impact: 184.7)
  * `getError` **(Defensive Guards)** (Impact: 29.6)
  * `getExitCodeFromError` **(Defensive Guards)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 85 instances
* *State Mutation (weighted view):* 265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 47`, `args: 10`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 95`, `dead_code: 1`, `fragile_debt: 4`
* *Architecture:* `io: 2`, `api: 2`, `import: 9`
* *Defense:* `safety: 41`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000334
  * `Imports (Out-Degree: 0):` did-you-mean.js, explain-eresolve.js, redact, node:fs, node:path, node:util, parse-conflict-json, proc-log...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `workspaces/arborist/lib/arborist/isolated-reifier.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 486.58 | **LOC:** 473 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 57.1%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 0.666; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.1%), Guard Balance (formerly Safety Score) (92.3%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assignCommonProperties` **(Defensive Guards)** (Impact: 63.5)
  * `processDeps` **(Many-Argument Workhorses)** (Impact: 21.2)
  * `createBundledTree` **(I/O & Config Routines)** (Impact: 20.4)
  * `processEdges` **(Stateful Encapsulated Methods)** (Impact: 19.9)
  * `makeIdealGraph` **(I/O & Config Routines)** (Impact: 19.4)
    * *Intent:* /** * Create an ideal graph. * * An implementation of npm RFC-0042 * https://github.com/npm/rfcs/blo...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 49 instances
* *Concurrency (weighted view):* 108
* *State Mutation (weighted view):* 177
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 64`, `args: 34`, `func_start: 15`
* *Risk/State:* `state_mutation: 79`, `planned_debt: 5`, `fragile_debt: 7`
* *Architecture:* `io: 1`, `api: 6`, `concurrency: 23`, `import: 6`
* *Defense:* `safety: 8`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.666
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001093
  * `Imports (Out-Degree: 1):` isolated-classes.js, node:crypto, node:fs, node:path, pacote, treeverse
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `workspaces/arborist/test/shrinkwrap.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 485.94 | **LOC:** 1726 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Guard Balance (formerly Safety Score) (64.9%), Connectivity (formerly Api Exposure) (25.3%), Complexity Load (formerly Cognitive Load) (18.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getData` **(Many-Argument Workhorses)** (Impact: 93.1)
  * `cleanSnapshot` **(Callbacks & Closures)** (Impact: 14.1)
  * `loadAndReset` **(Callbacks & Closures)** (Impact: 8.4)
  * `normalizePath` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 26 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 267
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 163`, `args: 76`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 54`
* *Architecture:* `io: 26`, `api: 3`, `concurrency: 137`, `import: 13`
* *Defense:* `safety: 5`, `sync_locks: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` index.js, calc-dep-flags.js, link.js, node.js, shrinkwrap.js, yarn-lock.js, index.js, node:fs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `workspaces/arborist/test/isolated-mode.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 481.1 | **LOC:** 2383 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 83.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.4%), Guard Balance (formerly Safety Score) (51.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.9%), Complexity Load (formerly Cognitive Load) (23.0%)
- **Documentation Coverage:** 98.7261% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `apply` **(Many-Argument Workhorses)** (Impact: 106.0)
  * `apply` **(Defensive Guards)** (Impact: 21.9)
  * `apply` **(Defensive Guards)** (Impact: 17.4)
  * `apply` **(Defensive Guards)** (Impact: 10.0)
  * `apply` **(Defensive Guards)** (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 174
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 272`, `args: 127`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 20`, `dead_code: 1`, `planned_debt: 4`, `unreferenced_by_name: 1`
* *Architecture:* `io: 159`, `api: 1`, `concurrency: 149`, `import: 6`
* *Defense:* `safety: 38`, `doc: 2`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` arborist, isolated-nock, node:fs, node:os, node:path, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/npm.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 427.84 | **LOC:** 789 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (68.0%), Complexity Load (formerly Cognitive Load) (49.7%), Connectivity (formerly Api Exposure) (14.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `chdir` **(Callbacks & Closures)** (Impact: 20.0)
  * `globals` **(Compute Cores)** (Impact: 16.5)
  * `config` **(Callbacks & Closures)** (Impact: 10.0)
  * `load` **(Callbacks & Closures)** (Impact: 5.9)
  * `cleanSnapshot` **(Callbacks & Closures)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 37 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 312
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 149`, `args: 67`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 30`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 127`, `import: 12`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` base-cmd.js, npm.js, cmd-list.js, mock-npm.js, definition.js, mock-globals, promises, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/commands/audit.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 427.76 | **LOC:** 2241 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (67.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (20.9%), Complexity Load (formerly Cognitive Load) (19.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cleanSnapshot` **(I/O & Config Routines)** (Impact: 20.7)
  * `getTarget` **(I/O & Config Routines)** (Impact: 19.9)
  * `verify` **(I/O & Config Routines)** (Impact: 9.7)
  * `verify` **(I/O & Config Routines)** (Impact: 2.8)
  * `manifestWithValidSigs` **(I/O & Config Routines)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 305
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 247`, `args: 70`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 10`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 45`, `concurrency: 275`, `import: 7`
* *Defense:* `sync_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mock-npm, mock-registry, repo-mock, node:fs, node:path, node:zlib, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/trust-cmd.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 426.16 | **LOC:** 849 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (74.0%), Complexity Load (formerly Cognitive Load) (49.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (6.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read` **(I/O & Config Routines)** (Impact: 11.4)
  * `read` **(I/O & Config Routines)** (Impact: 9.3)
  * `read` **(I/O & Config Routines)** (Impact: 7.0)
  * `read` **(I/O & Config Routines)** (Impact: 5.5)
  * `read` **(I/O & Config Routines)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 43 instances
* *Concurrency (weighted view):* 312
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 117`, `args: 47`, `func_start: 10`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 47`
* *Architecture:* `concurrency: 97`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` trust-cmd.js, mock-npm.js, mock-registry, proc-log, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/commands/completion.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 421.14 | **LOC:** 335 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (82.5%), Complexity Load (formerly Cognitive Load) (50.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (6.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `globals` **(Callbacks & Closures)** (Impact: 18.2)
  * `globals` **(Defensive Guards)** (Impact: 4.9)
  * `loadMockCompletionComp` **(Callbacks & Closures)** (Impact: 2.8)
  * `loadMockCompletion` **(Callbacks & Closures)** (Impact: 2.0)
  * `globals` **(Callbacks & Closures)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 50 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 350
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 112`, `args: 39`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 32`
* *Architecture:* `io: 4`, `concurrency: 100`, `import: 4`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mock-npm, node:fs, node:path, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `workspaces/arborist/lib/arborist/reify.js` -> Churn: **53.02%** | Cog Load: 97.088% | Debt: 11.6438%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `test/lib/commands/unpublish.js` -> **Umesh More** (100.0% isolated ownership) | Magnitude: 783.82
- `test/lib/commands/profile.js` -> **Josh Soref** (100.0% isolated ownership) | Magnitude: 702.24
- `workspaces/libnpmexec/test/with-lock.js` -> **Jon Jensen** (100.0% isolated ownership) | Magnitude: 547.04
- `test/lib/commands/team.js` -> **Josh Soref** (100.0% isolated ownership) | Magnitude: 519.02
- `workspaces/arborist/test/isolated-mode.js` -> **Manzoor Wani** (83.3% isolated ownership) | Magnitude: 481.1

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `test/fixtures/mock-npm.js` -> **Severity: 1.735** (Embedded: 0.0294 * Error Risk: 59.0179%)
- `test/fixtures/mock-logs.js` -> **Severity: 1.236** (Embedded: 0.0152 * Error Risk: 81.3147%)
- `test/fixtures/tmock.js` -> **Severity: 1.195** (Embedded: 0.0185 * Error Risk: 64.5656%)
- `workspaces/arborist/lib/node.js` -> **Severity: 0.527** (Embedded: 0.0063 * Error Risk: 83.0561%)
- `test/fixtures/clean-snapshot.js` -> **Severity: 0.475** (Embedded: 0.0073 * Error Risk: 64.5656%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `test/fixtures/mock-npm.js` -> **Severity: 1556.748** (Blast Radius: 17.074 * Doc Risk: 91.1765%)
- `test/fixtures/tmock.js` -> **Severity: 1071.5** (Blast Radius: 10.715 * Doc Risk: 100.0%)
- `test/fixtures/mock-logs.js` -> **Severity: 767.3** (Blast Radius: 7.673 * Doc Risk: 100.0%)
- `workspaces/arborist/bin/lib/options.js` -> **Severity: 278.3** (Blast Radius: 2.783 * Doc Risk: 100.0%)
- `test/fixtures/clean-snapshot.js` -> **Severity: 274.6** (Blast Radius: 2.746 * Doc Risk: 100.0%)

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
