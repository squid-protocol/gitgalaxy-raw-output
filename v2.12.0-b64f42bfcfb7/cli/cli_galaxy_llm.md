# ARCHITECTURAL_BRIEF: cli
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/npm/cli.git` |
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
- **Scope:** 386 analyzed artifact(s), 84268 LOC.
- **Load-bearing artifact:** `test/fixtures/mock-npm.js` -- 89 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `lib/npm.js` -- pulls in 17 dependencies, the widest assembly point in the scan.
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
| Analyzed Artifacts (Scanned) | 386 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6366 |
| Total LOC | 84268 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 5.7% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6681 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2822 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6165 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 42 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 308 | 77560 | 79.8% |
| YAML | 31 | 3604 | 8.0% |
| JSON | 10 | 2063 | 2.6% |
| HTML | 10 | 663 | 2.6% |
| PLAINTEXT | 9 | 1 | 2.3% |
| SHELL | 7 | 262 | 1.8% |
| MARKDOWN | 6 | 0 | 1.6% |
| BATCH | 3 | 35 | 0.8% |
| POWERSHELL | 2 | 80 | 0.5% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 385 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 24%, Data / Markup / Trivial 20%, Large Core Modules (2) 18%, Callbacks & Closures Files 15%, Large Core Modules (3) 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 371 | 96.1% |
| Unknown | 1 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 14 | 3.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6366*

**Composition by Extension & Reason:**
- `.json`: 3938x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 14810 LOC), 1x Excluded (Massive Static Asset Blob: 16237 LOC)
- `.js`: 1116x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tgz`: 783x Excluded (Explicitly Denied Extension: '.tgz')
- `.md`: 228x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 161x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cjs`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cmd`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cc`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cts`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mts`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 28.0 | 7.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 87.0 | 43.6 | 51.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 13.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 76.4 | 7.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 51.7 | 62.2 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 32.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 30.8 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.1 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 58.4 | 5.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 65.3 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 116 | 21 | 0 | `tap-snapshots/test/lib/utils/error-message.js.test.cjs` |
| cleanup | 11 | 7 | 0 | `lib/commands/team.js` |
| guards | 1258 | 185 | 10 | `lib/utils/display.js` |
| danger | 1520 | 211 | 10 | `tap-snapshots/test/lib/docs.js.test.cjs` |
| concurrency | 6718 | 230 | 49 | `test/lib/commands/ls.js` |
| connectivity | 442 | 197 | 2 | `scripts/template-oss/node-integration-yml.hbs` |
| io | 852 | 115 | 5 | `test/lib/commands/cache.js` |
| crypto | 2 | 2 | 0 | `lib/utils/sbom-cyclonedx.js` |
| ipc | 3 | 3 | 0 | `lib/commands/config.js` |
| time | 51 | 19 | 0 | `mock-globals/test/index.js` |
| serialization | 1137 | 99 | 5 | `test/lib/commands/ls.js` |
| regex | 677 | 118 | 4 | `test/lib/commands/diff.js` |
| events | 826 | 98 | 4 | `tap-snapshots/test/lib/commands/doctor.js.test.cjs` |
| tests | 391 | 126 | 2 | `test/lib/utils/reify-finish.js` |
| docs | 185 | 41 | 1 | `tap-snapshots/test/lib/commands/search.js.test.cjs` |
| debt | 531 | 111 | 4 | `.github/workflows/node-integration.yml` |
| mutation | 12154 | 315 | 73 | `tap-snapshots/test/lib/docs.js.test.cjs` |
| dead_code | 169 | 89 | 2 | `mock-registry/lib/index.js` |
| credential | 65 | 14 | 0 | `test/lib/commands/ls.js` |
| threat | 1 | 1 | 0 | `lib/cli/entry.js` |
| ml_ai | 1 | 1 | 0 | `lib/utils/completion.sh` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/lib/commands/cache.js` (Hits: 181)
- `test/lib/commands/audit.js` (Hits: 45)
- `test/lib/commands/exec.js` (Hits: 37)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **mock-npm.js** (`test/fixtures/mock-npm.js`) — 89 inbound connections
2. **base-cmd.js** (`lib/base-cmd.js`) — 49 inbound connections
3. **clean-snapshot.js** (`test/fixtures/clean-snapshot.js`) — 23 inbound connections
4. **tmock.js** (`test/fixtures/tmock.js`) — 21 inbound connections
5. **auth.js** (`lib/utils/auth.js`) — 15 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **npm.js** (`lib/npm.js`) — 17 outbound dependencies
2. **publish.js** (`lib/commands/publish.js`) — 15 outbound dependencies
3. **cache.js** (`lib/commands/cache.js`) — 14 outbound dependencies
4. **view.js** (`lib/commands/view.js`) — 14 outbound dependencies
5. **exit-handler.js** (`test/lib/cli/exit-handler.js`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `errorMessage` **(Many-Argument Workhorses)** (@ `lib/utils/error-message.js`) -> Impact: **174.2** | LOC: 367
- `toCyclonedxItem` **(Defensive Guards)** (@ `lib/utils/sbom-cyclonedx.js`) -> Impact: **77.6** | LOC: 98
- `prettyView` **(Many-Argument Workhorses)** (@ `lib/commands/view.js`) -> Impact: **68.0** | LOC: 112
- `jsonParse` **(I/O & Config Routines)** (@ `test/lib/commands/ls.js`) -> Impact: **65.9** | LOC: 1406
- `publish` **(Many-Argument Workhorses)** (@ `lib/commands/publish.js`) -> Impact: **62.5** | LOC: 142
- `exec` **(Compute Cores)** (@ `lib/commands/ls.js`) -> Impact: **61.8** | LOC: 162
- `getUsage` **(Many-Argument Workhorses)** (@ `lib/base-cmd.js`) -> Impact: **55.8** | LOC: 111
- `exec` **(Defensive Guards)** (@ `lib/commands/unpublish.js`) -> Impact: **54.6** | LOC: 87
- `enable2fa` **(Defensive Guards)** (@ `lib/commands/profile.js`) -> Impact: **49.7** | LOC: 117
- `execCommandClass` **(Many-Argument Workhorses)** (@ `lib/npm.js`) -> Impact: **44.1** | LOC: 82
  * *Intent:* // Unified command execution for both top-level commands and subcommands // Supports n-depth subcommands, workspaces, and definitions

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `test/lib/commands` | 67 | 10150.42 | 19.18% | 0.0% |
| `lib/commands` | 67 | 6389.32 | 53.45% | 34.18% |
| `__monolith__` | 13 | 5135.0 | 4.5% | 0.0% |
| `lib/utils` | 35 | 2836.44 | 47.9% | 4.82% |
| `tap-snapshots/test/lib` | 2 | 1421.92 | 0.0% | 0.0% |
| `test/lib/utils` | 21 | 1384.08 | 41.39% | 0.0% |
| `test/lib` | 8 | 1354.54 | 36.54% | 0.0% |
| `tap-snapshots/test/lib/commands` | 26 | 1239.84 | 0.0% | 0.0% |
| `scripts` | 13 | 1210.12 | 61.54% | 8.58% |
| `lib` | 7 | 929.32 | 54.86% | 12.21% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/workflows/ci.yml` -> **100.0%** Exposure
- `.github/workflows/ci-npmcli-docs.yml` -> **99.9999%** Exposure
- `.github/workflows/ci-libnpmaccess.yml` -> **99.9997%** Exposure
- `.github/workflows/ci-libnpmdiff.yml` -> **99.9997%** Exposure
- `.github/workflows/ci-libnpmexec.yml` -> **99.9997%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `bin/npm` -> **100.0%** Exposure
- `bin/npx` -> **100.0%** Exposure
- `lib/utils/completion.sh` -> **100.0%** Exposure
- `scripts/smoke-tests.sh` -> **100.0%** Exposure
- `bin/npx-cli.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/lib/commands/profile.js` -> **2** Orphaned Functions | **42** Duplicates
- `mock-registry/lib/index.js` -> **27** Orphaned Functions | **0** Duplicates
- `.github/workflows/ci.yml` -> **0** Orphaned Functions | **20** Duplicates
- `test/lib/base-cmd.js` -> **0** Orphaned Functions | **16** Duplicates
- `.github/workflows/ci-release.yml` -> **0** Orphaned Functions | **13** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `mock-registry/lib/provenance.js` -> **100.0%** Exposure
- `test/lib/commands/publish.js` -> **99.9997%** Exposure
- `mock-registry/lib/index.js` -> **99.9943%** Exposure
- `test/lib/utils/display.js` -> **98.0093%** Exposure
- `test/lib/commands/token.js` -> **29.3829%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `833` packages imported that bypass the Zero-Trust whitelist.

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tap-snapshots/test/lib/docs.js.test.cjs` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.695)
- **Top Global Matches:** file_cluster_12: 6.695, file_cluster_2: 6.898, file_cluster_7: 7.634
- **Magnitude:** 1389.38 | **LOC:** 6244 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 38.5%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (67.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.4%), Credential Material (formerly Secrets Risk) (9.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 4`
* *Risk/State:* `safety_bypasses: 89`, `state_mutation: 1289`
* *Architecture:* `io: 24`
* *Defense:* `sync_locks: 78`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/commands/ls.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.028)
- **Top Global Matches:** file_cluster_12: 8.028, file_cluster_10: 8.067, file_cluster_2: 8.992
- **Magnitude:** 1126.58 | **LOC:** 5408 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (51.8%), Complexity Load (formerly Cognitive Load) (23.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `jsonParse` **(I/O & Config Routines)** (Impact: 65.9)
  * `redactCwdObj` **(Defensive Guards)** (Impact: 7.7)
  * `mock` **(Many-Argument Workhorses)** (Impact: 7.0)
  * `mock` **(Many-Argument Workhorses)** (Impact: 6.7)
  * `mockWorkspaces` **(Many-Argument Workhorses)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 97 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 867
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 407`, `args: 152`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 49`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 382`, `import: 5`
* *Defense:* `safety: 10`, `sync_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` clean-snapshot, mock-npm.js, node:fs, node:path, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/commands/profile.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.49)
- **Top Global Matches:** file_cluster_10: 7.49, file_cluster_12: 8.045, file_cluster_11: 8.145
- **Magnitude:** 718.34 | **LOC:** 1160 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (51.9%), Complexity Load (formerly Cognitive Load) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `password` **(Defensive Guards)** (Impact: 12.0)
  * `set` **(Defensive Guards)** (Impact: 10.7)
  * `password` **(Compute Cores)** (Impact: 10.6)
  * `set` **(Defensive Guards)** (Impact: 7.3)
  * `set` **(Defensive Guards)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 60 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 515
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 244`, `args: 136`, `func_start: 77`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 30`, `fragile_debt: 5`, `duplicate_logic: 42`, `unreferenced_by_name: 2`
* *Architecture:* `concurrency: 215`, `import: 4`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mock-npm, tmock, node:util, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/commands/unpublish.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.389)
- **Top Global Matches:** file_cluster_10: 6.389, file_cluster_12: 6.447, file_cluster_2: 7.205
- **Magnitude:** 655.5 | **LOC:** 654 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (52.8%), Complexity Load (formerly Cognitive Load) (39.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (8.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 202
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 114`, `args: 34`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 13`
* *Architecture:* `concurrency: 102`, `import: 3`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mock-npm, mock-registry, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `mock-registry/lib/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.224)
- **Top Global Matches:** file_cluster_15: 6.224, file_cluster_10: 7.234, file_cluster_11: 7.767
- **Magnitude:** 510.82 | **LOC:** 674 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.353; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Credential Material (formerly Secrets Risk) (100.0%), Concurrency Surface (formerly Concurrency) (99.7%), Debt Markers (formerly Tech Debt) (99.4%)
- **Documentation Coverage:** 97.9592% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tnock` **(Defensive Guards)** (Impact: 35.6)
  * `noMatch` **(Defensive Guards)** (Impact: 20.7)
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
* *Structure:* `branch: 82`, `structural_boundaries: 70`, `args: 64`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `state_mutation: 79`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 27`
* *Architecture:* `io: 5`, `api: 1`, `concurrency: 14`, `import: 8`
* *Defense:* `safety: 12`, `doc: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` arborist, json-stringify-safe, nock, node:fs, promises, node:path, npm-package-arg, pacote
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/commands/ls.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.674)
- **Top Global Matches:** file_cluster_6: 7.674, file_cluster_4: 8.001, file_cluster_15: 14.736
- **Magnitude:** 496.7 | **LOC:** 589 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 3.077; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (87.6%), Complexity Load (formerly Cognitive Load) (86.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exec` **(Compute Cores)** (Impact: 61.8)
  * `getJsonOutputItem` **(Compute Cores)** (Impact: 37.6)
  * `getHumanOutputItem` **(Compute Cores)** (Impact: 34.2)
  * `filterBySelectedWorkspaces` **(Compute Cores)** (Impact: 18.2)
  * `mapEdgesToNodes` **(Compute Cores)** (Impact: 14.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 54 instances
* *Concurrency (weighted view):* 27
* *State Mutation (weighted view):* 166
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 66`, `args: 33`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 58`, `planned_debt: 1`
* *Architecture:* `api: 5`, `concurrency: 7`, `import: 9`
* *Defense:* `safety: 16`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.077
  * `Choke Point (Betweenness):` 6.1e-05 | `Ripple Effect (Closeness):` 0.005195
  * `Imports (Out-Degree: 2):` arborist-cmd.js, installed-deep.js, string-locale-compare, arborist, archy, node:path, npm-package-arg, proc-log...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/utils/error-message.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.851)
- **Top Global Matches:** file_cluster_8: 8.851, file_cluster_6: 18.618, file_cluster_3: 20.265
- **Magnitude:** 480.3 | **LOC:** 454 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **9**; blast radius 6.576; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.7%), Guard Balance (formerly Safety Score) (72.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `errorMessage` **(Many-Argument Workhorses)** (Impact: 174.2)
  * `getError` **(Defensive Guards)** (Impact: 27.5)
  * `getExitCodeFromError` **(Defensive Guards)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 261
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 47`, `args: 10`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 95`, `fragile_debt: 4`
* *Architecture:* `io: 2`, `api: 1`, `import: 9`
* *Defense:* `safety: 41`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.576
  * `Choke Point (Betweenness):` 0.001486 | `Ripple Effect (Closeness):` 0.092969
  * `Imports (Out-Degree: 2):` did-you-mean.js, explain-eresolve.js, redact, node:fs, node:path, node:util, parse-conflict-json, proc-log...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `test/lib/commands/team.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.983)
- **Top Global Matches:** file_cluster_10: 6.983, file_cluster_11: 8.112, file_cluster_13: 8.637
- **Magnitude:** 460.32 | **LOC:** 433 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (52.8%), Complexity Load (formerly Cognitive Load) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mockTeam` **(Callbacks & Closures)** (Impact: 3.8)
  * `cleanSnapshot` **(Parameter Forwarders)** (Impact: 1.6)
  * `lsTeams` **(Interface Declarations)** (Impact: 1.4)
  * `add` **(State Mutators)** (Impact: 1.1)
  * `create` **(State Mutators)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 60 instances
* *Concurrency (weighted view):* 414
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 111`, `args: 54`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 114`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mock-npm, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `smoke-tests/test/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.258)
- **Top Global Matches:** file_cluster_9: 8.258, file_cluster_12: 12.841, file_cluster_10: 13.068
- **Magnitude:** 418.34 | **LOC:** 408 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (54.6%), Complexity Load (formerly Cognitive Load) (50.0%), Connectivity (formerly Api Exposure) (6.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `abbrevManifest` **(I/O & Config Routines)** (Impact: 24.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 47 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 350
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 118`, `args: 29`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 26`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `concurrency: 115`, `import: 3`
* *Defense:* `safety: 4`, `sync_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` setup.js, node:path, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/commands/view.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.912)
- **Top Global Matches:** file_cluster_4: 6.912, file_cluster_9: 10.236, file_cluster_15: 10.739
- **Magnitude:** 404.16 | **LOC:** 489 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (91.3%), Complexity Load (formerly Cognitive Load) (85.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prettyView` **(Many-Argument Workhorses)** (Impact: 68.0)
  * `packageOutput` **(Defensive Guards)** (Impact: 28.9)
  * `getData` **(Defensive Guards)** (Impact: 27.7)
  * `viewPackage` **(Compute Cores)** (Impact: 23.4)
  * `cleanup` **(Defensive Guards)** (Impact: 20.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 47 instances
* *Concurrency (weighted view):* 23
* *State Mutation (weighted view):* 143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 69`, `args: 33`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 49`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 13`, `import: 14`
* *Defense:* `safety: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` base-cmd.js, error-message.js, format-bytes.js, output-error.js, queryable.js, json-parse-even-better-errors, promises, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/commands/completion.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.726)
- **Top Global Matches:** file_cluster_12: 8.726, file_cluster_7: 8.932, file_cluster_5: 10.466
- **Magnitude:** 401.74 | **LOC:** 335 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (61.3%), Complexity Load (formerly Cognitive Load) (50.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `globals` **(Defensive Guards)** (Impact: 4.5)
  * `loadMockCompletionComp` **(Callbacks & Closures)** (Impact: 2.8)
  * `loadMockCompletion` **(Callbacks & Closures)** (Impact: 2.0)
  * `globals` **(Parameter Forwarders)** (Impact: 1.6)
  * `globals` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 50 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 350
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 112`, `args: 39`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 32`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `concurrency: 100`, `import: 4`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mock-npm, node:fs, node:path, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/commands/audit.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.987)
- **Top Global Matches:** file_cluster_12: 7.987, file_cluster_7: 8.493, file_cluster_5: 10.004
- **Magnitude:** 395.36 | **LOC:** 2241 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (56.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.7%), Complexity Load (formerly Cognitive Load) (21.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cleanSnapshot` **(I/O & Config Routines)** (Impact: 18.8)
  * `manifestWithValidSigs` **(I/O & Config Routines)** (Impact: 2.5)
  * `manifestWithInvalidSigs` **(I/O & Config Routines)** (Impact: 2.4)
  * `manifestWithValidAttestations` **(Annotated & Test Methods)** (Impact: 2.2)
  * `manifestWithMultipleValidAttestations` **(Annotated & Test Methods)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 305
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 247`, `args: 70`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 79`, `state_mutation: 10`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 3`, `unreferenced_by_name: 3`
* *Architecture:* `io: 45`, `concurrency: 275`, `import: 7`
* *Defense:* `sync_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mock-npm, mock-registry, repo-mock, node:fs, node:path, node:zlib, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/commands/outdated.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.203)
- **Top Global Matches:** file_cluster_15: 7.203, file_cluster_12: 7.551, file_cluster_10: 7.618
- **Magnitude:** 388.16 | **LOC:** 734 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (52.5%), Complexity Load (formerly Cognitive Load) (48.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `packument` **(I/O & Config Routines)** (Impact: 7.2)
  * `mockWorkspaces` **(Defensive Guards)** (Impact: 4.0)
  * `mockNpm` **(Parameter Forwarders)** (Impact: 3.0)
  * `cleanSnapshot` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 48 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 335
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 112`, `args: 39`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 22`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 95`, `import: 4`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` clean-snapshot, mock-npm, mock-registry, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/npm.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.612)
- **Top Global Matches:** file_cluster_12: 7.612, file_cluster_10: 8.906, file_cluster_7: 9.2
- **Magnitude:** 380.94 | **LOC:** 789 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (55.6%), Complexity Load (formerly Cognitive Load) (49.8%), Connectivity (formerly Api Exposure) (14.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cleanSnapshot` **(Callbacks & Closures)** (Impact: 3.5)
  * `exec` **(State Mutators)** (Impact: 2.0)
  * `execWorkspaces` **(State Mutators)** (Impact: 2.0)
  * `globals` **(Parameter Forwarders)** (Impact: 1.8)
  * `config` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 38 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 317
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 149`, `args: 67`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 30`, `duplicate_logic: 2`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 127`, `import: 12`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` base-cmd.js, npm.js, cmd-list.js, mock-npm.js, definition.js, mock-globals, promises, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/base-cmd.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.609)
- **Top Global Matches:** file_cluster_6: 6.609, file_cluster_4: 12.275, file_cluster_8: 13.478
- **Magnitude:** 373.3 | **LOC:** 436 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **49** in-repo importer(s); it depends on **8**; blast radius 51.359; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getUsage` **(Many-Argument Workhorses)** (Impact: 55.8)
  * `flags` **(Compute Cores)** (Impact: 38.2)
  * `validateFlags` **(Many-Argument Workhorses)** (Impact: 37.0)
    * *Intent:* // Validate flags and throw errors for unknown flags or unexpected positionals
  * `checkExpected` **(Defensive Guards)** (Impact: 9.2)
    * *Intent:* // Compare the number of entries with what was expected
  * `checkDevEngines` **(Callbacks & Closures)** (Impact: 8.8)
    * *Intent:* // Checks the devEngines entry in the package.json at this.localPrefix
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 57 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 42`, `args: 31`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 61`
* *Architecture:* `api: 5`, `concurrency: 7`, `import: 8`
* *Defense:* `safety: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 51.359
  * `Choke Point (Betweenness):` 0.001108 | `Ripple Effect (Closeness):` 0.146957
  * `Imports (Out-Degree: 2):` cmd-list, get-workspaces.js, definitions, package-json, node:path, nopt, npm-install-checks, proc-log
  * `Imported By (In-Degree: 49):` (Excluded from Brief to save tokens)

### `test/lib/trust-cmd.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.437)
- **Top Global Matches:** file_cluster_7: 7.437, file_cluster_12: 7.603, file_cluster_10: 8.895
- **Magnitude:** 369.66 | **LOC:** 849 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (58.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read` **(Callbacks & Closures)** (Impact: 1.1)
  * `read` **(Callbacks & Closures)** (Impact: 1.1)
  * `read` **(Callbacks & Closures)** (Impact: 1.1)
  * `read` **(Callbacks & Closures)** (Impact: 1.1)
  * `read` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 40 instances
* *Concurrency (weighted view):* 297
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 117`, `args: 47`, `func_start: 10`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 47`, `duplicate_logic: 5`
* *Architecture:* `concurrency: 97`, `import: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` trust-cmd.js, mock-npm.js, mock-registry, proc-log, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/commands/cache.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.875)
- **Top Global Matches:** file_cluster_9: 6.875, file_cluster_12: 9.549, file_cluster_15: 10.271
- **Magnitude:** 359.48 | **LOC:** 364 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (99.2%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `searchCachePackage` **(Defensive Guards)** (Impact: 28.6)
  * `npxInfo` **(Defensive Guards)** (Impact: 22.3)
  * `exec` **(Compute Cores)** (Impact: 16.4)
  * `completion` **(Defensive Guards)** (Impact: 10.6)
  * `ls` **(Defensive Guards)** (Impact: 9.6)
    * *Intent:* // npm cache ls [<spec> ...]
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 29 instances
* *Concurrency (weighted view):* 122
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 65`, `args: 17`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 32`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 10`, `api: 1`, `concurrency: 42`, `import: 14`
* *Defense:* `safety: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` base-cmd.js, string-locale-compare, arborist, package-json, abbrev, cacache, json-parse-even-better-errors, promises...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/commands/publish.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.255)
- **Top Global Matches:** file_cluster_12: 7.255, file_cluster_10: 7.683, file_cluster_15: 8.53
- **Magnitude:** 338.4 | **LOC:** 1606 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (51.6%), Complexity Load (formerly Cognitive Load) (24.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cleanSnapshot` **(I/O & Config Routines)** (Impact: 29.9)
  * `init` **(Callbacks & Closures)** (Impact: 6.6)
  * `constructor` **(Defensive Guards)** (Impact: 3.2)
  * `cleanSnapshot` **(Parameter Forwarders)** (Impact: 1.9)
  * `chdir` **(Interface Declarations)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 250
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 183`, `args: 68`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 10`, `unreferenced_by_name: 3`
* *Architecture:* `io: 26`, `concurrency: 160`, `import: 11`
* *Defense:* `safety: 9`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` clean-snapshot, mock-npm, mock-oidc, arborist, mock-globals, provenance, node:fs, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/commands/view.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.88)
- **Top Global Matches:** file_cluster_12: 7.88, file_cluster_7: 8.782, file_cluster_10: 9.76
- **Magnitude:** 338.28 | **LOC:** 843 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (55.6%), Complexity Load (formerly Cognitive Load) (43.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `packument` **(Many-Argument Workhorses)** (Impact: 8.2)
  * `cleanSnapshot` **(Compute Cores)** (Impact: 3.3)
  * `loadMockNpm` **(Callbacks & Closures)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 26 instances
* *Amplified Cascading Flux:* 4 instances
* *Concurrency (weighted view):* 289
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 168`, `args: 64`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 12`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `concurrency: 159`, `import: 2`
* *Defense:* `safety: 3`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mock-npm.js, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/commands/config.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.268)
- **Top Global Matches:** file_cluster_4: 7.268, file_cluster_9: 11.126, file_cluster_12: 11.131
- **Magnitude:** 327.62 | **LOC:** 415 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `completion` **(Defensive Guards)** (Impact: 23.1)
  * `list` **(I/O & Config Routines)** (Impact: 19.8)
  * `exec` **(Compute Cores)** (Impact: 19.7)
  * `set` **(Defensive Guards)** (Impact: 15.7)
  * `isProtected` **(Compute Cores)** (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 33 instances
* *Concurrency (weighted view):* 83
* *State Mutation (weighted view):* 104
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 68`, `args: 23`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 38`, `planned_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 1`, `concurrency: 28`, `import: 11`
* *Defense:* `safety: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` base-cmd.js, string-locale-compare, definitions, package-json, redact, ini, node:child_process, promises...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/base-cmd.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.776)
- **Top Global Matches:** file_cluster_12: 6.776, file_cluster_7: 7.057, file_cluster_11: 9.08
- **Magnitude:** 311.88 | **LOC:** 680 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (63.2%), Complexity Load (formerly Cognitive Load) (47.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exec` **(Interface Declarations)** (Impact: 1.1)
  * `exec` **(Interface Declarations)** (Impact: 1.1)
  * `exec` **(Interface Declarations)** (Impact: 1.1)
  * `exec` **(Interface Declarations)** (Impact: 1.1)
  * `exec` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 191
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 120`, `args: 40`, `func_start: 16`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 53`, `fragile_debt: 1`, `duplicate_logic: 16`
* *Architecture:* `concurrency: 71`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` base-cmd.js, mock-npm, definition.js, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/commands/config.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.188)
- **Top Global Matches:** file_cluster_12: 7.188, file_cluster_10: 9.142, file_cluster_15: 9.547
- **Magnitude:** 305.02 | **LOC:** 761 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (68.3%), Guard Balance (formerly Safety Score) (54.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (5.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadMockNpm` **(Many-Argument Workhorses)** (Impact: 20.8)
  * `testComp` **(Defensive Guards)** (Impact: 6.6)
  * `loadMockNpmWithPublishConfig` **(Callbacks & Closures)** (Impact: 3.8)
  * `cleanSnapshot` **(Parameter Forwarders)** (Impact: 2.1)
  * `replaceJsonOrIni` **(Parameter Forwarders)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 229
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 167`, `args: 43`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 15`, `unreferenced_by_name: 2`
* *Architecture:* `io: 18`, `concurrency: 144`, `import: 7`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` clean-snapshot.js, mock-npm, tspawk, ini, promises, node:path, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/cli/exit-handler.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.636)
- **Top Global Matches:** file_cluster_12: 7.636, file_cluster_7: 8.844, file_cluster_10: 10.029
- **Magnitude:** 303.74 | **LOC:** 739 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (56.6%), Complexity Load (formerly Cognitive Load) (47.4%), Connectivity (formerly Api Exposure) (35.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `err` **(Defensive Guards)** (Impact: 8.6)
    * *Intent:* // Create errors with properties to be used in tests
  * `exitHandler` **(Callbacks & Closures)** (Impact: 7.6)
    * *Intent:* // Make it async to make testing ergonomics a little easier so we don't need // to t.plan() every te...
  * `formatSnapshot` **(Defensive Guards)** (Impact: 4.6)
  * `writeFileSync` **(Callbacks & Closures)** (Impact: 4.5)
  * `mockShelloutExit` **(Callbacks & Closures)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 195
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 158`, `args: 72`, `func_start: 22`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 1`, `state_mutation: 14`, `duplicate_logic: 2`
* *Architecture:* `io: 11`, `api: 7`, `concurrency: 115`, `import: 14`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` exec.js, error-message.js, package.json, clean-snapshot, mock-npm, tmock, mock-globals, fs-minipass...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/lib/commands/init.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.343)
- **Top Global Matches:** file_cluster_12: 8.343, file_cluster_7: 9.292, file_cluster_10: 9.544
- **Magnitude:** 298.28 | **LOC:** 584 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 1.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (55.3%), Complexity Load (formerly Cognitive Load) (49.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mockNpm` **(Callbacks & Closures)** (Impact: 7.7)
  * `initPackageJson` **(Callbacks & Closures)** (Impact: 3.2)
  * `libexecStub` **(Parameter Forwarders)** (Impact: 2.2)
  * `libexecStub` **(Parameter Forwarders)** (Impact: 2.0)
  * `initPackageJson` **(Callbacks & Closures)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 23 instances
* *Concurrency (weighted view):* 238
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 134`, `args: 51`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 11`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `concurrency: 123`, `import: 22`
* *Defense:* `sync_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.353
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` clean-snapshot, mock-npm, fs, promises, node:path, tap
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `test/lib/commands/restart.js` (JAVASCRIPT) | Magnitude: 18.58 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 22, core_var_decl: 8, branch: 5, design_snake_case: 5
- `test/lib/commands/start.js` (JAVASCRIPT) | Magnitude: 18.58 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 22, core_var_decl: 8, branch: 5, design_snake_case: 5
- `test/lib/commands/stop.js` (JAVASCRIPT) | Magnitude: 18.58 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 22, core_var_decl: 8, branch: 5, design_snake_case: 5
- `test/lib/commands/test.js` (JAVASCRIPT) | Magnitude: 18.58 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 22, core_var_decl: 8, branch: 5, design_snake_case: 5
- `test/lib/commands/unpublish.js` (JAVASCRIPT) | Magnitude: 655.5 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 543, structural_boundaries: 114, concurrency: 102, core_var_decl: 83

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `test/lib/commands/trust/circleci.js` (JAVASCRIPT) | Magnitude: 191.8 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 386, state_mutation: 54, structural_boundaries: 44, core_var_decl: 40
- `test/lib/commands/ls.js` (JAVASCRIPT) | Magnitude: 1126.58 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 5192, structural_boundaries: 407, concurrency: 382, bitwise_ops: 334

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `lib/commands/ll.js` (JAVASCRIPT) | Magnitude: 10.8 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 4, core_var_decl: 3, state_mutation: 2
- `bin/npm-prefix.js` (JAVASCRIPT) | Magnitude: 4.04 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, import: 3, core_var_decl: 3, safety: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `.github/actions/create-check/action.yml` (YAML) | Magnitude: 8.36 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 44, args: 11, branch: 3, structural_boundaries: 2
- `lib/commands/uninstall.js` (JAVASCRIPT) | Magnitude: 30.84 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 39, core_var_decl: 13, design_snake_case: 8, branch: 7
- `lib/commands/stars.js` (JAVASCRIPT) | Magnitude: 33.98 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 27, core_var_decl: 9, design_snake_case: 5, branch: 4
- `lib/commands/link.js` (JAVASCRIPT) | Magnitude: 96.66 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 143, core_var_decl: 33, structural_boundaries: 25, design_snake_case: 21
- `lib/utils/timers.js` (JAVASCRIPT) | Magnitude: 41.16 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 9, args: 8, core_var_decl: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `lib/commands/ping.js` (JAVASCRIPT) | Magnitude: 11.34 | Delta: **0.12** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, core_var_decl: 9, design_snake_case: 6, import: 4
- `tap-snapshots/test/lib/utils/validate-lockfile.js.test.cjs` (JAVASCRIPT) | Magnitude: 15.5 | Delta: **0.138** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: decorators: 8, sync_locks: 6, indent_spaces: 6, events: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `test/lib/arborist-cmd.js` (JAVASCRIPT) | Magnitude: 118.36 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 171, structural_boundaries: 58, concurrency: 50, core_var_decl: 23
- `test/lib/commands/deprecate.js` (JAVASCRIPT) | Magnitude: 42.62 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 155, structural_boundaries: 46, concurrency: 37, core_var_decl: 35

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `test/lib/commands/bugs.js` (JAVASCRIPT) | Magnitude: 87.12 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 14, branch: 12, concurrency: 12

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `test/lib/commands/unpublish.js` -> **Umesh More** (100.0% isolated ownership) | Magnitude: 655.5
- `test/lib/commands/completion.js` -> **Reggi** (100.0% isolated ownership) | Magnitude: 401.74
- `test/lib/npm.js` -> **Reggi** (100.0% isolated ownership) | Magnitude: 380.94
- `test/lib/trust-cmd.js` -> **Reggi** (100.0% isolated ownership) | Magnitude: 369.66
- `test/lib/commands/config.js` -> **Max Black** (100.0% isolated ownership) | Magnitude: 305.02

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/npm.js` -> **Severity: 0.777** (Bridge: 0.0079 * Flux: 98.3295%)
- `lib/utils/error-message.js` -> **Severity: 0.149** (Bridge: 0.0015 * Flux: 100.0%)
- `lib/base-cmd.js` -> **Severity: 0.111** (Bridge: 0.0011 * Flux: 100.0%)
- `lib/utils/display.js` -> **Severity: 0.098** (Bridge: 0.001 * Flux: 97.7502%)
- `lib/utils/explain-eresolve.js` -> **Severity: 0.07** (Bridge: 0.0007 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `test/fixtures/mock-npm.js` -> **Severity: 12.091** (Embedded: 0.2312 * Error Risk: 52.3023%)
- `lib/base-cmd.js` -> **Severity: 10.017** (Embedded: 0.147 * Error Risk: 68.1595%)
- `lib/utils/cmd-list.js` -> **Severity: 9.168** (Embedded: 0.1744 * Error Risk: 52.5839%)
- `test/fixtures/tmock.js` -> **Severity: 7.359** (Embedded: 0.1451 * Error Risk: 50.7142%)
- `lib/npm.js` -> **Severity: 7.345** (Embedded: 0.1352 * Error Risk: 54.3315%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `test/fixtures/mock-npm.js` -> **Severity: 6853.697** (Blast Radius: 75.627 * Doc Risk: 90.625%)
- `lib/base-cmd.js` -> **Severity: 5135.9** (Blast Radius: 51.359 * Doc Risk: 100.0%)
- `test/fixtures/tmock.js` -> **Severity: 3696.5** (Blast Radius: 36.965 * Doc Risk: 100.0%)
- `lib/utils/cmd-list.js` -> **Severity: 3329.6** (Blast Radius: 33.296 * Doc Risk: 100.0%)
- `lib/npm.js` -> **Severity: 2913.2** (Blast Radius: 29.132 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 443 literal sites + 1 sites through wrappers = 444

- `access` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `test/lib/commands/doctor.js`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 4421 call pairs -- scoped 18.2%, unique 0.0%, ambiguous 14.6%, external 67.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 4387 | 18.2% | 0.0% | 14.7% | 67.0% |
| shell | 34 | 11.8% | 0.0% | 0.0% | 88.2% |

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
