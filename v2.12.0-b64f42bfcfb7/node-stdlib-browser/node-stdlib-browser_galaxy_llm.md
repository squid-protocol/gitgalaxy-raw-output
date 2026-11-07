# ARCHITECTURAL_BRIEF: node-stdlib-browser
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
- **Scope:** 68 analyzed artifact(s), 3712 LOC.
- **Load-bearing artifact:** `package/cjs/proxy/process.js` -- 1 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `package/README.md` -- pulls in 8 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `package/cjs/proxy/url.js` at magnitude 1229.48 (structural weight, not risk).
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
| Total Artifacts | 126 |
| Analyzed Artifacts (Scanned) | 68 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 58 |
| Total LOC | 3712 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 54.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVASCRIPT | 32 | 2982 | 47.1% |
| TYPESCRIPT | 30 | 730 | 44.1% |
| MARKDOWN | 3 | 0 | 4.4% |
| PLAINTEXT | 3 | 0 | 4.4% |

## 4.1 SOURCE ENCODINGS
All 68 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 43%, Large Core Modules (2) 21%, State Mutators Files 13%, Declarative / Non-Code 9%, Parameter Forwarders Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 62 | 91.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 8.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 58*

**Composition by Extension & Reason:**
- `.map`: 38x Unresolved Ambiguity (No Retainable Structure), 20x Excluded (Saturation: Line 1 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 83.9 | 13.3 | 3.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 81.9 | 22.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 97.1 | 8.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 2.3 | 80.0 | 4.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 97.9 | 17.4 | 8.7 | 3.5 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 11.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 49.2 | 58.3 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 8 | 6 | 0 | `package/cjs/proxy/url.d.ts` |
| cleanup | 8 | 4 | 0 | `package/cjs/proxy/process.js` |
| guards | 300 | 16 | 4 | `package/cjs/proxy/url.js` |
| danger | 66 | 14 | 2 | `package/cjs/proxy/url.js` |
| concurrency | 73 | 7 | 0 | `package/cjs/proxy/process.js` |
| connectivity | 556 | 58 | 29 | `package/cjs/proxy/process.js` |
| io | 54 | 10 | 1 | `package/cjs/index.d.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 24 | 4 | 0 | `package/cjs/index.d.ts` |
| time | 66 | 6 | 0 | `package/cjs/proxy/process.js` |
| serialization | 0 | 0 | 0 | - |
| regex | 50 | 6 | 0 | `package/cjs/proxy/url.js` |
| events | 120 | 8 | 2 | `package/esm/proxy/process.js` |
| tests | 22 | 2 | 0 | `package/cjs/index.js` |
| docs | 93 | 26 | 4 | `package/cjs/proxy/url.js` |
| debt | 6 | 6 | 0 | `package/cjs/proxy/process.js` |
| mutation | 1590 | 38 | 53 | `package/cjs/proxy/url.js` |
| dead_code | 13 | 7 | 0 | `package/cjs/proxy/url.d.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 0 | 0 | 0 | - |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `package/cjs/index.d.ts` (Hits: 20)
- `package/esm/index.d.ts` (Hits: 20)
- `package/cjs/index.js` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **process.js** (`package/cjs/proxy/process.js`) — 1 inbound connections
2. **process.js** (`package/esm/proxy/process.js`) — 1 inbound connections
3. **CHANGELOG.md** (`package/CHANGELOG.md`) — 0 inbound connections
4. **LICENSE.md** (`package/LICENSE.md`) — 0 inbound connections
5. **README.md** (`package/README.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **README.md** (`package/README.md`) — 8 outbound dependencies
2. **index.js** (`package/cjs/index.js`) — 3 outbound dependencies
3. **process.d.ts** (`package/cjs/proxy/process.d.ts`) — 2 outbound dependencies
4. **querystring.d.ts** (`package/cjs/proxy/querystring.d.ts`) — 2 outbound dependencies
5. **process.d.ts** (`package/esm/proxy/process.d.ts`) — 2 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `resolveObject` **(Defensive Guards)** (@ `package/cjs/proxy/url.js`) -> Impact: **175.0** | LOC: 275
- `resolveObject` **(Defensive Guards)** (@ `package/esm/proxy/url.js`) -> Impact: **175.0** | LOC: 275
- `parse` **(Many-Argument Workhorses)** (@ `package/cjs/proxy/url.js`) -> Impact: **156.1** | LOC: 281
- `parse` **(Many-Argument Workhorses)** (@ `package/esm/proxy/url.js`) -> Impact: **156.1** | LOC: 281
- `format` **(Defensive Guards)** (@ `package/cjs/proxy/url.js`) -> Impact: **35.8** | LOC: 55
- `format` **(Defensive Guards)** (@ `package/esm/proxy/url.js`) -> Impact: **35.8** | LOC: 55
- `formatImportWithOverloads` **(Defensive Guards)** (@ `package/cjs/proxy/url.js`) -> Impact: **22.2** | LOC: 28
  * *Intent:* /** * ((urlObject: URL, options?: URLFormatOptions) => string) & * ((urlObject: UrlObject | string, options?: never) => string) * )} */
- `formatImportWithOverloads` **(Defensive Guards)** (@ `package/esm/proxy/url.js`) -> Impact: **22.2** | LOC: 28
  * *Intent:* /** * ((urlObject: URL, options?: URLFormatOptions) => string) & * ((urlObject: UrlObject | string, options?: never) => string) * )} */
- `normalizeArray` **(Defensive Guards)** (@ `package/cjs/proxy/url.js`) -> Impact: **16.8** | LOC: 25
  * *Intent:* // in all copies or substantial portions of the Software. // // THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS // OR IMPLIED,...
- `normalizeArray` **(Defensive Guards)** (@ `package/esm/proxy/url.js`) -> Impact: **16.8** | LOC: 25
  * *Intent:* // in all copies or substantial portions of the Software. // // THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS // OR IMPLIED,...

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `package/cjs/proxy` | 6 | 1545.6 | 30.72% | 19.06% |
| `package/esm/proxy` | 6 | 1435.4 | 31.01% | 19.08% |
| `package/cjs/proxy/process` | 2 | 296.08 | 44.13% | 4.59% |
| `package/esm/proxy/process` | 2 | 225.72 | 43.93% | 4.66% |
| `package/cjs/mock` | 18 | 196.76 | 7.96% | 6.64% |
| `package/esm/mock` | 18 | 87.4 | 4.92% | 6.64% |
| `package/helpers/esbuild` | 2 | 44.48 | 9.73% | 18.88% |
| `package/cjs` | 3 | 41.86 | 4.16% | 0.0% |
| `package/esm` | 3 | 29.38 | 3.71% | 0.0% |
| `package` | 4 | 12.24 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `package/cjs/proxy/url.d.ts` -> **97.0688%** Exposure
- `package/esm/proxy/url.d.ts` -> **97.0688%** Exposure
- `package/cjs/mock/process.d.ts` -> **81.7574%** Exposure
- `package/esm/mock/process.d.ts` -> **81.7574%** Exposure
- `package/cjs/mock/buffer.d.ts` -> **37.7541%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `package/cjs/mock/process.js` -> **100.0%** Exposure
- `package/cjs/proxy/process.js` -> **100.0%** Exposure
- `package/cjs/proxy/process/browser.js` -> **100.0%** Exposure
- `package/cjs/proxy/url.js` -> **100.0%** Exposure
- `package/esm/proxy/url.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `package/cjs/proxy/url.d.ts` -> **3** Orphaned Functions | **0** Duplicates
- `package/esm/proxy/url.d.ts` -> **3** Orphaned Functions | **0** Duplicates
- `package/cjs/mock/process.d.ts` -> **2** Orphaned Functions | **0** Duplicates
- `package/esm/mock/process.d.ts` -> **2** Orphaned Functions | **0** Duplicates
- `package/cjs/mock/buffer.d.ts` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `38` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `package/cjs/proxy/url.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.032)
- **Top Global Matches:** file_cluster_4: 8.032, file_cluster_6: 8.092, file_cluster_12: 14.355
- **Magnitude:** 1229.48 | **LOC:** 1073 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 9.285; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.7%)
- **Documentation Coverage:** 74.1935% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveObject` **(Defensive Guards)** (Impact: 175.0)
  * `parse` **(Many-Argument Workhorses)** (Impact: 156.1)
  * `format` **(Defensive Guards)** (Impact: 35.8)
  * `formatImportWithOverloads` **(Defensive Guards)** (Impact: 22.2)
    * *Intent:* /** * ((urlObject: URL, options?: URLFormatOptions) => string) & * ((urlObject: UrlObject | string, ...
  * `normalizeArray` **(Defensive Guards)** (Impact: 16.8)
    * *Intent:* // in all copies or substantial portions of the Software. // // THE SOFTWARE IS PROVIDED "AS IS", WI...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 220 instances
* *State Mutation (weighted view):* 693
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 288`, `structural_boundaries: 154`, `args: 26`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 253`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 12`, `import: 2`
* *Defense:* `safety: 92`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` punycode, qs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/proxy/url.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.821)
- **Top Global Matches:** file_cluster_6: 7.821, file_cluster_4: 8.407, file_cluster_12: 14.875
- **Magnitude:** 1199.44 | **LOC:** 1051 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 9.285; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.3%)
- **Documentation Coverage:** 73.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveObject` **(Defensive Guards)** (Impact: 175.0)
  * `parse` **(Many-Argument Workhorses)** (Impact: 156.1)
  * `format` **(Defensive Guards)** (Impact: 35.8)
  * `formatImportWithOverloads` **(Defensive Guards)** (Impact: 22.2)
    * *Intent:* /** * ((urlObject: URL, options?: URLFormatOptions) => string) & * ((urlObject: UrlObject | string, ...
  * `normalizeArray` **(Defensive Guards)** (Impact: 16.8)
    * *Intent:* // in all copies or substantial portions of the Software. // // THE SOFTWARE IS PROVIDED "AS IS", WI...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 220 instances
* *State Mutation (weighted view):* 680
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 152`, `args: 25`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 240`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 2`
* *Defense:* `safety: 90`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` punycode, qs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/proxy/process.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.259)
- **Top Global Matches:** file_cluster_10: 7.259, file_cluster_15: 8.528, file_cluster_2: 8.812
- **Magnitude:** 295.4 | **LOC:** 283 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 17.177; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (97.9%), Complexity Load (formerly Cognitive Load) (83.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runClearTimeout` **(Defensive Guards)** (Impact: 8.4)
  * `runTimeout` **(Defensive Guards)** (Impact: 8.3)
  * `nextTick` **(Defensive Guards)** (Impact: 7.7)
  * `cleanUpNextTick` **(I/O & Config Routines)** (Impact: 6.7)
  * `drainQueue` **(I/O & Config Routines)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 43`, `args: 16`, `func_start: 16`
* *Risk/State:* `state_mutation: 82`, `planned_debt: 1`
* *Architecture:* `api: 75`, `concurrency: 8`
* *Defense:* `safety: 21`, `doc: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.177
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009524
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/cjs/proxy/process/browser.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.259)
- **Top Global Matches:** file_cluster_10: 7.259, file_cluster_15: 8.528, file_cluster_2: 8.812
- **Magnitude:** 295.4 | **LOC:** 283 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (83.9%), Guard Balance (formerly Safety Score) (65.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runClearTimeout` **(Defensive Guards)** (Impact: 8.4)
  * `runTimeout` **(Defensive Guards)** (Impact: 8.3)
  * `nextTick` **(Defensive Guards)** (Impact: 7.7)
  * `cleanUpNextTick` **(I/O & Config Routines)** (Impact: 6.7)
  * `drainQueue` **(I/O & Config Routines)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 43`, `args: 16`, `func_start: 16`
* *Risk/State:* `state_mutation: 82`, `planned_debt: 1`
* *Architecture:* `api: 75`, `concurrency: 8`
* *Defense:* `safety: 21`, `doc: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/proxy/process.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.346)
- **Top Global Matches:** file_cluster_10: 7.346, file_cluster_15: 8.673, file_cluster_2: 9.029
- **Magnitude:** 225.04 | **LOC:** 262 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 17.177; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (85.7%), Complexity Load (formerly Cognitive Load) (83.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runClearTimeout` **(Defensive Guards)** (Impact: 8.4)
  * `runTimeout` **(Defensive Guards)** (Impact: 8.3)
  * `nextTick` **(Defensive Guards)** (Impact: 7.7)
  * `cleanUpNextTick` **(I/O & Config Routines)** (Impact: 6.7)
  * `drainQueue` **(I/O & Config Routines)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 63`, `args: 16`, `func_start: 16`
* *Risk/State:* `state_mutation: 46`, `planned_debt: 1`
* *Architecture:* `api: 41`, `concurrency: 8`
* *Defense:* `safety: 21`, `doc: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.177
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009524
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `package/esm/proxy/process/browser.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.346)
- **Top Global Matches:** file_cluster_10: 7.346, file_cluster_15: 8.673, file_cluster_2: 9.029
- **Magnitude:** 225.04 | **LOC:** 262 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (83.5%), Guard Balance (formerly Safety Score) (59.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runClearTimeout` **(Defensive Guards)** (Impact: 8.4)
  * `runTimeout` **(Defensive Guards)** (Impact: 8.3)
  * `nextTick` **(Defensive Guards)** (Impact: 7.7)
  * `cleanUpNextTick` **(I/O & Config Routines)** (Impact: 6.7)
  * `drainQueue` **(I/O & Config Routines)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 63`, `args: 16`, `func_start: 16`
* *Risk/State:* `state_mutation: 46`, `planned_debt: 1`
* *Architecture:* `api: 41`, `concurrency: 8`
* *Defense:* `safety: 21`, `doc: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/mock/process.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.698)
- **Top Global Matches:** file_cluster_11: 6.698, file_cluster_10: 7.438, file_cluster_15: 7.438
- **Magnitude:** 71.78 | **LOC:** 74 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.285; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (98.3%), Connectivity (formerly Api Exposure) (93.2%), Guard Balance (formerly Safety Score) (63.9%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_interopDefaultLegacy` **(Defensive Guards)** (Impact: 5.7)
  * `nextTick` **(Defensive Guards)** (Impact: 3.6)
    * *Intent:* /** */
  * `binding` **(State Mutators)** (Impact: 1.6)
    * *Intent:* /** */
  * `getChdir` **(State Mutators)** (Impact: 1.6)
    * *Intent:* /** */
  * `noop` **(State Mutators)** (Impact: 1.1)
    * *Intent:* /* globals unknown */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 13`, `args: 7`, `func_start: 6`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `io: 1`, `api: 20`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 4`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.942)
- **Top Global Matches:** file_cluster_12: 6.942, file_cluster_11: 8.817, file_cluster_15: 9.052
- **Magnitude:** 39.74 | **LOC:** 148 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 9.285; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (50.6%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (48.2%), Complexity Load (formerly Cognitive Load) (8.4%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolvePath` **(Defensive Guards)** (Impact: 12.1)
    * *Intent:* /** */
  * `_globalThis` **(Defensive Guards)** (Impact: 8.1)
  * `_interopDefaultLegacy` **(Defensive Guards)** (Impact: 5.7)
  * `get` **(Interface Declarations)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 20`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`
* *Architecture:* `io: 4`, `api: 1`, `import: 3`
* *Defense:* `safety: 9`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` create-require, pkg-dir, u
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/mock/dns.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.479)
- **Top Global Matches:** file_cluster_2: 7.479, file_cluster_15: 7.515, file_cluster_17: 7.91
- **Magnitude:** 35.96 | **LOC:** 33 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (72.0%), Complexity Load (formerly Cognitive Load) (69.8%), Guard Balance (formerly Safety Score) (59.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `api` **(Defensive Guards)** (Impact: 5.5)
    * *Intent:* /* globals unknown */ /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 4`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `api: 11`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/helpers/esbuild/plugin.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.031)
- **Top Global Matches:** file_cluster_10: 5.031, file_cluster_2: 8.333, file_cluster_13: 8.762
- **Magnitude:** 32.7 | **LOC:** 43 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 9.285; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (51.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Debt Markers (formerly Tech Debt) (37.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setup` **(Callbacks & Closures)** (Impact: 2.4)
  * `plugin` **(Callbacks & Closures)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Concurrency (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `args: 5`, `func_start: 3`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `concurrency: 5`, `import: 2`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` browser-resolve, util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.571)
- **Top Global Matches:** file_cluster_12: 6.571, file_cluster_11: 7.999, file_cluster_15: 8.734
- **Magnitude:** 27.26 | **LOC:** 141 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 9.285; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (44.7%), Complexity Load (formerly Cognitive Load) (7.0%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_globalThis` **(Defensive Guards)** (Impact: 8.1)
  * `resolvePath` **(Defensive Guards)** (Impact: 6.4)
    * *Intent:* /** */
  * `get` **(Interface Declarations)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 19`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`
* *Architecture:* `io: 4`, `api: 1`, `import: 2`
* *Defense:* `safety: 4`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` create-require, pkg-dir
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/mock/process.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.043)
- **Top Global Matches:** file_cluster_11: 7.043, file_cluster_10: 7.419, file_cluster_15: 7.951
- **Magnitude:** 26.62 | **LOC:** 47 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.285; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Concurrency Surface (formerly Concurrency) (98.8%), Guard Balance (formerly Safety Score) (53.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 14.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `nextTick` **(Defensive Guards)** (Impact: 3.6)
    * *Intent:* /** */
  * `binding` **(State Mutators)** (Impact: 1.6)
    * *Intent:* /** */
  * `getChdir` **(State Mutators)** (Impact: 1.6)
    * *Intent:* /** */
  * `noop` **(State Mutators)** (Impact: 1.1)
    * *Intent:* /* globals unknown */
  * `getCwd` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `args: 6`, `func_start: 5`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 1`, `api: 1`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 2`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/mock/console.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.663)
- **Top Global Matches:** file_cluster_12: 6.663, file_cluster_7: 8.271, file_cluster_10: 8.709
- **Magnitude:** 17.2 | **LOC:** 47 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (51.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (20.1%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_globalThis` **(Defensive Guards)** (Impact: 8.1)
  * `get` **(Interface Declarations)** (Impact: 2.2)
  * `_console[` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 12`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `api: 1`
* *Defense:* `safety: 2`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/proxy/querystring.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.285)
- **Top Global Matches:** file_cluster_10: 5.285, file_cluster_15: 7.585, file_cluster_2: 8.0
- **Magnitude:** 15.34 | **LOC:** 56 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 9.285; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (52.4%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (45.3%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `qsEscape` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** */ /** */
  * `qsUnescape` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** */
  * `get` **(Callbacks & Closures)** (Impact: 1.1)
  * `get` **(Callbacks & Closures)** (Impact: 1.1)
  * `get` **(Callbacks & Closures)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 8`, `args: 6`, `func_start: 6`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 3`, `import: 1`
* *Defense:* `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` querystring-es3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/mock/net.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.269)
- **Top Global Matches:** file_cluster_11: 5.269, file_cluster_2: 6.634, file_cluster_17: 7.227
- **Magnitude:** 14.44 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Connectivity (formerly Api Exposure) (56.4%), Guard Balance (formerly Safety Score) (54.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `noop` **(State Mutators)** (Impact: 1.1)
  * `bool` **(Interface Declarations)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/mock/console.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.718)
- **Top Global Matches:** file_cluster_12: 6.718, file_cluster_7: 8.252, file_cluster_10: 8.804
- **Magnitude:** 14.18 | **LOC:** 45 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (49.6%), Connectivity (formerly Api Exposure) (20.1%), Mutation Surface (formerly State Flux) (16.8%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_globalThis` **(Defensive Guards)** (Impact: 8.1)
  * `get` **(Interface Declarations)** (Impact: 2.2)
  * `_console[` **(Callbacks & Closures)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 13`, `args: 3`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 2`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/mock/punycode.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.098)
- **Top Global Matches:** file_cluster_15: 5.098, file_cluster_2: 5.802, file_cluster_17: 6.457
- **Magnitude:** 13.92 | **LOC:** 24 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.7%), Guard Balance (formerly Safety Score) (54.1%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (9.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `passthrough` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* /** */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 6`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/mock/empty.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.184)
- **Top Global Matches:** file_cluster_2: 3.184, file_cluster_17: 4.919, file_cluster_13: 5.606
- **Magnitude:** 13.56 | **LOC:** 7 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Mutation Surface (formerly State Flux) (16.8%), Connectivity (formerly Api Exposure) (3.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/mock/empty.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.889)
- **Top Global Matches:** file_cluster_2: 4.889, file_cluster_17: 5.956, file_cluster_13: 6.422
- **Magnitude:** 12.04 | **LOC:** 5 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (5.1%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/helpers/esbuild/shim.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.27)
- **Top Global Matches:** file_cluster_11: 6.27, file_cluster_10: 7.084, file_cluster_15: 7.495
- **Magnitude:** 11.78 | **LOC:** 25 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 9.285; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Complexity Load (formerly Cognitive Load) (19.5%), Connectivity (formerly Api Exposure) (3.5%), Test Surface (formerly Verification) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_globalThis` **(Defensive Guards)** (Impact: 8.1)
  * `get` **(Interface Declarations)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 12`, `args: 2`, `func_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` buffer, process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/mock/tls.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 10.52 | **LOC:** 4 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/esm/mock/tls.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Centroid distance: 0.0)
- **Magnitude:** 10.52 | **LOC:** 3 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/helpers/rollup/plugin.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.321)
- **Top Global Matches:** file_cluster_10: 6.321, file_cluster_2: 6.809, file_cluster_15: 6.962
- **Magnitude:** 10.48 | **LOC:** 35 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Guard Balance (formerly Safety Score) (46.2%), Mutation Surface (formerly State Flux) (19.3%), Complexity Load (formerly Cognitive Load) (4.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleCircularDependancyWarning` **(Defensive Guards)** (Impact: 8.0)
    * *Intent:* /** */ /** */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 3`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/cjs/mock/buffer.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.792)
- **Top Global Matches:** file_cluster_10: 5.792, file_cluster_2: 7.985, file_cluster_13: 8.314
- **Magnitude:** 10.44 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (52.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (50.0%), Connectivity (formerly Api Exposure) (49.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Buffer` **(State Mutators)** (Impact: 1.1)
  * `isBuffer` **(Callbacks & Closures)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `api: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `package/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 7.06 | **LOC:** 353 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 9.285; role: Isolated/Orphan
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.285
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` example, buffer.js, console.js, dns.js, net.js, process.js, tls.js, tty.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `package/cjs/mock/dns.js` (JAVASCRIPT) | Magnitude: 35.96 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: api: 11, state_mutation: 11, indent_spaces: 8, branch: 4
- `package/cjs/proxy/querystring.d.ts` (TYPESCRIPT) | Magnitude: 0.67 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 22, api: 10, import: 6, indent_spaces: 6
- `package/esm/proxy/querystring.d.ts` (TYPESCRIPT) | Magnitude: 0.67 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 22, api: 10, import: 6, indent_spaces: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `package/cjs/proxy/url.js` (JAVASCRIPT) | Magnitude: 1229.48 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 610, branch: 288, state_mutation: 253, core_var_decl: 177

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `package/cjs/proxy/process.js` -> **Severity: 0.624** (Embedded: 0.0095 * Error Risk: 65.5101%)
- `package/esm/proxy/process.js` -> **Severity: 0.568** (Embedded: 0.0095 * Error Risk: 59.67%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `package/cjs/proxy/process.js` -> **Severity: 1717.7** (Blast Radius: 17.177 * Doc Risk: 100.0%)
- `package/esm/proxy/process.js` -> **Severity: 1717.7** (Blast Radius: 17.177 * Doc Risk: 100.0%)
- `package/cjs/mock/buffer.d.ts` -> **Severity: 928.5** (Blast Radius: 9.285 * Doc Risk: 100.0%)
- `package/cjs/mock/net.d.ts` -> **Severity: 928.5** (Blast Radius: 9.285 * Doc Risk: 100.0%)
- `package/cjs/mock/tty.d.ts` -> **Severity: 928.5** (Blast Radius: 9.285 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 319 call pairs -- scoped 16.0%, unique 0.0%, ambiguous 0.0%, external 84.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| javascript | 319 | 16.0% | 0.0% | 0.0% | 84.0% |

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
