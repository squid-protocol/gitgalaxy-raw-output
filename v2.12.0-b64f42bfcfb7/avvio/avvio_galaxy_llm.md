# ARCHITECTURAL_BRIEF: avvio
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `N/A` |
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
- **Scope:** 67 analyzed artifact(s), 6011 LOC.
- **Load-bearing artifact:** `package/lib/symbols.js` -- 10 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/boot.js` -- pulls in 13 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/boot.js` at magnitude 641.12 (structural weight, not risk).
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
| Total Artifacts | 70 |
| Analyzed Artifacts (Scanned) | 67 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3 |
| Total LOC | 6011 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 95.7% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4529 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1753 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7353 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 9 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 58 | 5550 | 86.6% |
| YAML | 3 | 42 | 4.5% |
| TYPESCRIPT | 2 | 410 | 3.0% |
| PLAINTEXT | 2 | 0 | 3.0% |
| MARKDOWN | 1 | 0 | 1.5% |
| JSON | 1 | 9 | 1.5% |

## 4.1 SOURCE ENCODINGS
All 67 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** State Mutators Files 25%, Declarative / Non-Code 22%, Callbacks & Closures Files 19%, Data / Markup / Trivial 18%, Large Core Modules (2) 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 64 | 95.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 4.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 85.5 | 7.7 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 67.6 | 31.4 | 42.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 95.8 | 1.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 1.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 44.1 | 6.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 53.5 | 53.3 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 13.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 48.8 | 40.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 13 | 3 | 0 | `package/lib/symbols.js` |
| cleanup | 42 | 6 | 0 | `package/test/close.test.js` |
| guards | 158 | 27 | 5 | `package/boot.js` |
| danger | 112 | 26 | 5 | `package/boot.js` |
| concurrency | 543 | 43 | 13 | `package/test/await-after.test.js` |
| connectivity | 28 | 18 | 1 | `package/lib/plugin.js` |
| io | 4 | 1 | 0 | `package/test/await-after.test.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 38 | 13 | 1 | `package/test/close.test.js` |
| serialization | 0 | 0 | 0 | - |
| regex | 31 | 5 | 0 | `package/test/to-json.test.js` |
| events | 166 | 18 | 5 | `package/test/after-and-ready.test.js` |
| tests | 1299 | 41 | 66 | `package/test/after-and-ready.test.js` |
| docs | 58 | 14 | 2 | `package/lib/plugin.js` |
| debt | 59 | 11 | 2 | `package/test/after-and-ready.test.js` |
| mutation | 1074 | 57 | 54 | `package/boot.js` |
| dead_code | 13 | 10 | 1 | `package/index.d.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 1 | 1 | 0 | `package/test/expose.test.js` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/test/await-after.test.js` (Hits: 4)
- `package/.github/dependabot.yml` (Hits: 0)
- `package/.github/release-drafter.yml` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **symbols.js** (`package/lib/symbols.js`) — 10 inbound connections
2. **errors.js** (`package/lib/errors.js`) — 7 inbound connections
3. **debug.js** (`package/lib/debug.js`) — 4 inbound connections
4. **is-promise-like.js** (`package/lib/is-promise-like.js`) — 4 inbound connections
5. **plugin.js** (`package/lib/plugin.js`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **boot.js** (`package/boot.js`) — 13 outbound dependencies
2. **plugin.js** (`package/lib/plugin.js`) — 7 outbound dependencies
3. **await-after.test.js** (`package/test/await-after.test.js`) — 5 outbound dependencies
4. **expose.test.js** (`package/test/expose.test.js`) — 4 outbound dependencies
5. **thenify.test.js** (`package/test/lib/thenify.test.js`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Boot` **(Many-Argument Workhorses)** (@ `package/boot.js`) -> Impact: **38.6** | LOC: 93
- `avvio` **(Generic / Templated Code)** (@ `package/index.d.ts`) -> Impact: **34.5** | LOC: 90
- `closeWithCbOrNextTick` **(Defensive Guards)** (@ `package/boot.js`) -> Impact: **27.6** | LOC: 32
- `encapsulateThreeParam` **(Defensive Guards)** (@ `package/boot.js`) -> Impact: **27.6** | LOC: 33
- `_encapsulateThreeParam` **(Defensive Guards)** (@ `package/boot.js`) -> Impact: **27.4** | LOC: 28
- `exec` **(Many-Argument Workhorses)** (@ `package/lib/plugin.js`) -> Impact: **22.4** | LOC: 66
  * *Intent:* /** */ /** * */
- `encapsulateTwoParam` **(Defensive Guards)** (@ `package/boot.js`) -> Impact: **20.5** | LOC: 28
- `_encapsulateTwoParam` **(Defensive Guards)** (@ `package/boot.js`) -> Impact: **20.3** | LOC: 25
- `finish` **(Defensive Guards)** (@ `package/lib/plugin.js`) -> Impact: **20.2** | LOC: 58
  * *Intent:* /** */ /** * */
- `_addPlugin` **(Many-Argument Workhorses)** (@ `package/boot.js`) -> Impact: **19.8** | LOC: 35

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/test` | 32 | 1852.24 | 5.56% | 0.0% |
| `package` | 5 | 673.98 | 20.08% | 19.17% |
| `package/lib` | 12 | 445.64 | 13.94% | 0.84% |
| `package/test/lib` | 8 | 165.26 | 0.5% | 0.0% |
| `package/test/types` | 2 | 46.96 | 1.75% | 0.0% |
| `package/examples` | 1 | 38.94 | 22.13% | 0.0% |
| `package/.github` | 2 | 26.28 | 0.0% | 0.0% |
| `package/.github/workflows` | 1 | 17.56 | 5.53% | 0.0% |
| `package/test/gh-issues` | 1 | 2.68 | 0.0% | 0.0% |
| `package/test/fixtures` | 3 | 0.02 | 4.48% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/index.d.ts` -> **95.8266%** Exposure
- `package/lib/plugin.js` -> **10.0529%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/boot.js` -> **100.0%** Exposure
- `package/lib/plugin.js` -> **100.0%** Exposure
- `package/lib/time-tree.js` -> **100.0%** Exposure
- `package/lib/execute-with-thenable.js` -> **91.6827%** Exposure
- `package/lib/thenify.js` -> **83.2018%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/test/after-and-ready.test.js` -> **0** Orphaned Functions | **22** Duplicates
- `package/test/override.test.js` -> **0** Orphaned Functions | **8** Duplicates
- `package/test/async-await.test.js` -> **0** Orphaned Functions | **6** Duplicates
- `package/index.d.ts` -> **4** Orphaned Functions | **0** Duplicates
- `package/test/close.test.js` -> **0** Orphaned Functions | **3** Duplicates

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
- **Unknown Dependencies:** `58` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/boot.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.946)
- **Top Global Matches:** file_cluster_10: 7.946, file_cluster_15: 9.181, file_cluster_16: 9.68
- **Magnitude:** 641.12 | **LOC:** 622 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 27.683; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (99.9%), Complexity Load (formerly Cognitive Load) (85.5%), Guard Balance (formerly Safety Score) (61.2%)
- **Documentation Coverage:** 44.7368% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Boot` **(Many-Argument Workhorses)** (Impact: 38.6)
  * `closeWithCbOrNextTick` **(Defensive Guards)** (Impact: 27.6)
  * `encapsulateThreeParam` **(Defensive Guards)** (Impact: 27.6)
  * `_encapsulateThreeParam` **(Defensive Guards)** (Impact: 27.4)
  * `encapsulateTwoParam` **(Defensive Guards)** (Impact: 20.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 68 instances
* *Concurrency (weighted view):* 57
* *State Mutation (weighted view):* 222
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 55`, `args: 59`, `func_start: 40`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 86`
* *Architecture:* `api: 4`, `concurrency: 12`, `import: 13`
* *Defense:* `safety: 55`, `doc: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 27.683
  * `Choke Point (Betweenness):` 0.008392 | `Ripple Effect (Closeness):` 0.034091
  * `Imports (Out-Degree: 10):` debug, errors, execute-with-thenable, is-bundled-or-typescript-plugin, is-promise-like, plugin, symbols, thenify...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/test/await-after.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.223)
- **Top Global Matches:** file_cluster_10: 7.223, file_cluster_12: 9.098, file_cluster_11: 9.559
- **Magnitude:** 350.7 | **LOC:** 449 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 10.501; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (39.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fourth` **(State Mutators)** (Impact: 2.2)
  * `first` **(Callbacks & Closures)** (Impact: 1.8)
  * `first` **(Callbacks & Closures)** (Impact: 1.8)
  * `override` **(Callbacks & Closures)** (Impact: 1.7)
  * `third` **(State Mutators)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 37 instances
* *Concurrency (weighted view):* 305
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 136`, `args: 64`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 21`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `concurrency: 120`, `import: 5`
* *Defense:* `safety: 2`, `test: 110`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., promises, node:path, node:test, promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/test/await-use.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.349)
- **Top Global Matches:** file_cluster_10: 7.349, file_cluster_11: 9.126, file_cluster_12: 9.315
- **Magnitude:** 235.1 | **LOC:** 296 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 10.501; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `thenableRejects` **(Callbacks & Closures)** (Impact: 2.4)
  * `a` **(Parameter Forwarders)** (Impact: 2.0)
  * `b` **(State Mutators)** (Impact: 1.9)
  * `third` **(State Mutators)** (Impact: 1.6)
  * `setup` **(Interface Declarations)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Concurrency (weighted view):* 204
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 104`, `args: 55`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 9`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 94`, `import: 3`
* *Defense:* `test: 66`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., node:test, promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/test/close.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.679)
- **Top Global Matches:** file_cluster_10: 6.679, file_cluster_12: 9.599, file_cluster_2: 10.386
- **Magnitude:** 217.7 | **LOC:** 563 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 10.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `override` **(Callbacks & Closures)** (Impact: 2.2)
  * `override` **(Callbacks & Closures)** (Impact: 2.2)
  * `override` **(Callbacks & Closures)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 28 instances
* *Concurrency (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 126`, `args: 131`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 27`, `duplicate_logic: 3`
* *Architecture:* `concurrency: 35`, `import: 3`
* *Defense:* `safety: 2`, `test: 106`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .., errors, node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/plugin.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.285)
- **Top Global Matches:** file_cluster_10: 7.285, file_cluster_15: 8.232, file_cluster_16: 9.18
- **Magnitude:** 216.74 | **LOC:** 280 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 30.705; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.6%)
- **Documentation Coverage:** 35.2941% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `exec` **(Many-Argument Workhorses)** (Impact: 22.4)
    * *Intent:* /** */ /** * */
  * `finish` **(Defensive Guards)** (Impact: 20.2)
    * *Intent:* /** */ /** * */
  * `loadedSoFar` **(I/O & Config Routines)** (Impact: 11.2)
    * *Intent:* /** */
  * `done` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* /** */
  * `setup` **(Callbacks & Closures)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 21 instances
* *Concurrency (weighted view):* 43
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 17`, `args: 16`, `func_start: 12`
* *Risk/State:* `state_mutation: 36`, `planned_debt: 1`
* *Architecture:* `api: 6`, `concurrency: 8`, `import: 7`
* *Defense:* `safety: 4`, `doc: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 30.705
  * `Choke Point (Betweenness):` 0.004662 | `Ripple Effect (Closeness):` 0.054545
  * `Imports (Out-Degree: 5):` create-promise, debug, errors, get-plugin-name, is-promise-like, node:events, node:util
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `package/test/async-await.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.085)
- **Top Global Matches:** file_cluster_10: 7.085, file_cluster_13: 8.809, file_cluster_11: 8.897
- **Magnitude:** 184.72 | **LOC:** 324 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 10.501; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (49.9%), Guard Balance (formerly Safety Score) (36.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `override` **(Callbacks & Closures)** (Impact: 5.6)
  * `first` **(Interface Declarations)** (Impact: 2.5)
  * `second` **(Parameter Forwarders)** (Impact: 2.3)
  * `first` **(State Mutators)** (Impact: 2.2)
  * `first` **(State Mutators)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 113
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 46`, `args: 34`, `func_start: 21`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 19`, `duplicate_logic: 6`
* *Architecture:* `concurrency: 48`, `import: 3`
* *Defense:* `safety: 2`, `test: 103`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., node:test, promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/test/override.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.249)
- **Top Global Matches:** file_cluster_12: 8.249, file_cluster_10: 8.933, file_cluster_7: 9.521
- **Magnitude:** 137.02 | **LOC:** 386 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 10.501; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (47.1%), Complexity Load (formerly Cognitive Load) (46.4%), Concurrency Surface (formerly Concurrency) (36.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `override` **(Callbacks & Closures)** (Impact: 5.5)
  * `override` **(Defensive Guards)** (Impact: 4.6)
  * `add` **(Callbacks & Closures)** (Impact: 4.2)
  * `first` **(State Mutators)** (Impact: 3.4)
  * `first` **(Callbacks & Closures)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 33`, `args: 57`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 27`, `duplicate_logic: 8`
* *Architecture:* `concurrency: 6`, `import: 2`
* *Defense:* `safety: 3`, `test: 80`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/test/after-and-ready.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.011)
- **Top Global Matches:** file_cluster_10: 6.011, file_cluster_2: 9.207, file_cluster_13: 9.257
- **Magnitude:** 134.9 | **LOC:** 904 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 10.501; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (40.4%), Concurrency Surface (formerly Concurrency) (17.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `outer` **(State Mutators)** (Impact: 2.9)
  * `first` **(State Mutators)** (Impact: 2.7)
  * `outer` **(State Mutators)** (Impact: 2.6)
  * `first` **(State Mutators)** (Impact: 2.5)
  * `second` **(Callbacks & Closures)** (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 93`, `args: 164`, `func_start: 33`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 43`, `duplicate_logic: 22`
* *Architecture:* `concurrency: 4`, `import: 2`
* *Defense:* `safety: 6`, `test: 187`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/time-tree.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.185)
- **Top Global Matches:** file_cluster_11: 5.185, file_cluster_15: 6.603, file_cluster_2: 6.676
- **Magnitude:** 70.48 | **LOC:** 201 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 21.78; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (64.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (44.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prettyPrintTimeTree` **(Defensive Guards)** (Impact: 9.6)
    * *Intent:* /** */
  * `constructor` **(I/O & Config Routines)** (Impact: 1.5)
  * `toJSON` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* /** */
  * `prettyPrint` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 15`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `safety: 6`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.78
  * `Choke Point (Betweenness):` 0.000233 | `Ripple Effect (Closeness):` 0.042088
  * `Imports (Out-Degree: 1):` symbols
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/test/plugin-loaded-so-far.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.973)
- **Top Global Matches:** file_cluster_10: 4.973, file_cluster_2: 9.389, file_cluster_13: 9.558
- **Magnitude:** 69.34 | **LOC:** 82 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 10.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `after` **(Callbacks & Closures)** (Impact: 1.6)
  * `after` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Concurrency (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 14`, `args: 18`, `func_start: 2`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `concurrency: 16`, `import: 4`
* *Defense:* `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .., plugin, fastq, node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/test/callbacks.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.929)
- **Top Global Matches:** file_cluster_10: 6.929, file_cluster_12: 8.539, file_cluster_15: 9.698
- **Magnitude:** 49.86 | **LOC:** 117 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 10.501; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.4%), Complexity Load (formerly Cognitive Load) (12.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `a` **(Callbacks & Closures)** (Impact: 6.2)
  * `b` **(Callbacks & Closures)** (Impact: 6.2)
  * `c` **(Callbacks & Closures)** (Impact: 6.2)
  * `first` **(Defensive Guards)** (Impact: 2.8)
  * `first` **(State Mutators)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Concurrency (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 15`, `args: 19`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 5`
* *Architecture:* `concurrency: 5`, `import: 2`
* *Defense:* `safety: 2`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/test/plugin-timeout.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.568)
- **Top Global Matches:** file_cluster_10: 5.568, file_cluster_15: 8.633, file_cluster_13: 8.73
- **Magnitude:** 42.3 | **LOC:** 228 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 10.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (55.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (37.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `one` **(State Mutators)** (Impact: 2.5)
  * `one` **(State Mutators)** (Impact: 2.5)
  * `one` **(State Mutators)** (Impact: 2.1)
  * `three` **(State Mutators)** (Impact: 2.1)
  * `onReadyTwo` **(State Mutators)** (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 25`, `args: 40`, `func_start: 15`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 6`, `import: 3`
* *Defense:* `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .., plugin-no-next, node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/test/basic.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.617)
- **Top Global Matches:** file_cluster_10: 7.617, file_cluster_12: 8.599, file_cluster_7: 9.787
- **Magnitude:** 41.06 | **LOC:** 460 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 10.501; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (91.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.0%), Complexity Load (formerly Cognitive Load) (5.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `default` **(Callbacks & Closures)** (Impact: 4.3)
  * `myOptsAsFunc` **(Callbacks & Closures)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Concurrency (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 75`, `args: 88`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 7`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 6`, `import: 2`
* *Defense:* `test: 84`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/examples/example.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.995)
- **Top Global Matches:** file_cluster_10: 6.995, file_cluster_2: 9.266, file_cluster_15: 9.501
- **Magnitude:** 38.94 | **LOC:** 73 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 10.501; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (97.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (22.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `a` **(Callbacks & Closures)** (Impact: 6.2)
  * `b` **(Callbacks & Closures)** (Impact: 6.2)
  * `c` **(Callbacks & Closures)** (Impact: 6.2)
  * `duplicate` **(State Mutators)** (Impact: 4.3)
  * `a` **(State Mutators)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 4`, `args: 14`, `func_start: 8`
* *Risk/State:* None
* *Architecture:* `concurrency: 6`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/test/symbol-async-dispose.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.28)
- **Top Global Matches:** file_cluster_10: 4.28, file_cluster_2: 7.01, file_cluster_13: 7.584
- **Magnitude:** 34.36 | **LOC:** 29 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 10.501; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Concurrency (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5`, `args: 3`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `concurrency: 3`, `import: 2`
* *Defense:* `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/test/lib/thenify.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.03)
- **Top Global Matches:** file_cluster_10: 5.03, file_cluster_2: 9.129, file_cluster_13: 9.228
- **Magnitude:** 33.74 | **LOC:** 141 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 10.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (43.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mockDebug` **(Callbacks & Closures)** (Impact: 2.3)
  * `_loadRegistered` **(Callbacks & Closures)** (Impact: 1.1)
  * `_loadRegistered` **(Callbacks & Closures)** (Impact: 1.1)
  * `_loadRegistered` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 33`, `args: 23`, `func_start: 4`
* *Risk/State:* `state_mutation: 2`, `duplicate_logic: 2`
* *Architecture:* `concurrency: 14`, `import: 10`
* *Defense:* `safety: 2`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` debug, symbols, thenify, node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/test/types/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.463)
- **Top Global Matches:** file_cluster_10: 6.463, file_cluster_12: 8.475, file_cluster_2: 9.027
- **Magnitude:** 32.28 | **LOC:** 413 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 10.501; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (49.5%), Complexity Load (formerly Cognitive Load) (3.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `override` **(Many-Argument Workhorses)** (Impact: 14.4)
  * `plugin` **(Callbacks & Closures)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 51`, `args: 49`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1`
* *Architecture:* `concurrency: 9`, `import: 1`
* *Defense:* `doc: 1`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ..
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/test/reentrant.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.126)
- **Top Global Matches:** file_cluster_10: 6.126, file_cluster_2: 6.992, file_cluster_13: 7.278
- **Magnitude:** 29.88 | **LOC:** 127 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 10.501; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (35.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `first` **(State Mutators)** (Impact: 2.5)
  * `second` **(State Mutators)** (Impact: 2.5)
  * `third` **(State Mutators)** (Impact: 2.5)
  * `fourth` **(State Mutators)** (Impact: 2.5)
  * `fifth` **(State Mutators)** (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `args: 12`, `func_start: 8`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `import: 2`
* *Defense:* `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/test/await-self.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.344)
- **Top Global Matches:** file_cluster_10: 5.344, file_cluster_2: 8.096, file_cluster_13: 8.372
- **Magnitude:** 28.46 | **LOC:** 32 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 10.501; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 13`, `args: 4`
* *Risk/State:* None
* *Architecture:* `concurrency: 13`, `import: 2`
* *Defense:* `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/test/to-json.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.142)
- **Top Global Matches:** file_cluster_10: 7.142, file_cluster_2: 8.048, file_cluster_13: 8.616
- **Magnitude:** 27.1 | **LOC:** 131 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 10.501; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (28.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `first` **(State Mutators)** (Impact: 3.1)
  * `one` **(State Mutators)** (Impact: 2.5)
  * `two` **(State Mutators)** (Impact: 2.5)
  * `three` **(State Mutators)** (Impact: 2.5)
  * `second` **(State Mutators)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 12`, `func_start: 10`
* *Risk/State:* `state_mutation: 3`, `unreferenced_by_name: 1`
* *Architecture:* `import: 2`
* *Defense:* `safety: 2`, `test: 60`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` .., node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/test/plugin-name.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.71)
- **Top Global Matches:** file_cluster_10: 6.71, file_cluster_15: 7.983, file_cluster_13: 8.521
- **Magnitude:** 26.38 | **LOC:** 59 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 10.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (42.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `func` **(Parameter Forwarders)** (Impact: 2.5)
  * `testPlugin` **(State Mutators)** (Impact: 2.0)
  * `testPlugin` **(State Mutators)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 11`, `args: 9`, `func_start: 3`
* *Risk/State:* `state_mutation: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 8`, `import: 3`
* *Defense:* `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .., symbols, node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/test/lib/execute-with-thenable.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.367)
- **Top Global Matches:** file_cluster_10: 6.367, file_cluster_12: 8.821, file_cluster_2: 10.047
- **Magnitude:** 25.18 | **LOC:** 87 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 10.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fn` **(Callbacks & Closures)** (Impact: 1.3)
  * `fn` **(Callbacks & Closures)** (Impact: 1.2)
  * `func` **(Callbacks & Closures)** (Impact: 1.1)
  * `fn` **(Callbacks & Closures)** (Impact: 1.1)
  * `fn` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 15`, `args: 18`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `concurrency: 6`, `import: 3`
* *Defense:* `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` execute-with-thenable, symbols, node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/test/load-plugin.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.756)
- **Top Global Matches:** file_cluster_7: 8.756, file_cluster_12: 9.239, file_cluster_10: 10.25
- **Magnitude:** 22.48 | **LOC:** 133 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 10.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (45.6%), Complexity Load (formerly Cognitive Load) (8.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `default` **(Callbacks & Closures)** (Impact: 4.2)
  * `default` **(Callbacks & Closures)** (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 13`, `args: 31`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 5`
* *Architecture:* `concurrency: 12`, `import: 4`
* *Defense:* `safety: 4`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` .., plugin, fastq, node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/lib/execute-with-thenable.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.39)
- **Top Global Matches:** file_cluster_9: 6.39, file_cluster_15: 12.498, file_cluster_16: 12.581
- **Magnitude:** 21.24 | **LOC:** 37 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 17.317; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (51.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Concurrency Surface (formerly Concurrency) (28.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `executeWithThenable` **(Defensive Guards)** (Impact: 12.8)
    * *Intent:* /** */ /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 4`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.317
  * `Choke Point (Betweenness):` 0.000233 | `Ripple Effect (Closeness):` 0.042088
  * `Imports (Out-Degree: 2):` is-promise-like, symbols
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `package/test/lib/time-tree.test.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.7)
- **Top Global Matches:** file_cluster_10: 6.7, file_cluster_12: 7.092, file_cluster_2: 8.178
- **Magnitude:** 20.92 | **LOC:** 392 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 10.501; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (24.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 30`, `args: 30`
* *Risk/State:* `safety_bypasses: 5`
* *Architecture:* `import: 2`
* *Defense:* `safety: 28`, `test: 141`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.501
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` time-tree, node:test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `package/lib/is-bundled-or-typescript-plugin.js` (JAVASCRIPT) | Magnitude: 10.22 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, safety: 5, branch: 3, doc: 2

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `package/boot.js` -> **Severity: 0.839** (Bridge: 0.0084 * Flux: 100.0%)
- `package/lib/plugin.js` -> **Severity: 0.466** (Bridge: 0.0047 * Flux: 100.0%)
- `package/lib/get-plugin-name.js` -> **Severity: 0.035** (Bridge: 0.0007 * Flux: 50.0%)
- `package/lib/time-tree.js` -> **Severity: 0.023** (Bridge: 0.0002 * Flux: 100.0%)
- `package/lib/execute-with-thenable.js` -> **Severity: 0.021** (Bridge: 0.0002 * Flux: 91.6827%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/lib/symbols.js` -> **Severity: 8.456** (Embedded: 0.1622 * Error Risk: 52.1415%)
- `package/lib/errors.js` -> **Severity: 6.147** (Embedded: 0.1212 * Error Risk: 50.7142%)
- `package/lib/debug.js` -> **Severity: 4.126** (Embedded: 0.0818 * Error Risk: 50.4286%)
- `package/lib/is-promise-like.js` -> **Severity: 4.0** (Embedded: 0.0891 * Error Risk: 44.8752%)
- `package/lib/plugin.js` -> **Severity: 3.688** (Embedded: 0.0545 * Error Risk: 67.6178%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/test/fixtures/plugin-no-next.js` -> **Severity: 1942.6** (Blast Radius: 19.426 * Doc Risk: 100.0%)
- `package/boot.js` -> **Severity: 1238.449** (Blast Radius: 27.683 * Doc Risk: 44.7368%)
- `package/lib/plugin.js` -> **Severity: 1083.705** (Blast Radius: 30.705 * Doc Risk: 35.2941%)
- `package/examples/example.js` -> **Severity: 1050.1** (Blast Radius: 10.501 * Doc Risk: 100.0%)
- `package/test/after-and-ready.test.js` -> **Severity: 1050.1** (Blast Radius: 10.501 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 665 call pairs -- scoped 4.5%, unique 0.0%, ambiguous 10.2%, external 85.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 658 | 4.6% | 0.0% | 10.2% | 85.3% |
| typescript | 7 | 0.0% | 0.0% | 14.3% | 85.7% |

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
