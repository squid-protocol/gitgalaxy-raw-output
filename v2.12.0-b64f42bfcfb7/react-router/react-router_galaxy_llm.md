# ARCHITECTURAL_BRIEF: react-router
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/remix-run/react-router.git` |
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
- **Scope:** 1123 analyzed artifact(s), 159103 LOC.
- **Load-bearing artifact:** `integration/helpers/create-fixture.ts` -- 58 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `integration/rsc/rsc-test.ts` -- pulls in 67 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `packages/react-router-dev/vite/route-chunks-test.ts` at magnitude 20744.38 (structural weight, not risk).
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
| Total Artifacts | 1480 |
| Analyzed Artifacts (Scanned) | 1123 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 357 |
| Total LOC | 159103 |
| Volatility Index | 0.021 |
| % Scanned of codebase = | 75.9% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7225 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1879 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.728 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 108 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 738 | 153777 | 65.7% |
| MARKDOWN | 89 | 0 | 7.9% |
| JAVASCRIPT | 68 | 1817 | 6.1% |
| PLAINTEXT | 66 | 2 | 5.9% |
| JSON | 66 | 1371 | 5.9% |
| CSS | 43 | 798 | 3.8% |
| HTML | 25 | 303 | 2.2% |
| YAML | 23 | 916 | 2.0% |
| SHELL | 5 | 119 | 0.4% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 1122 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 40%, Declarative / Non-Code 20%, Callbacks & Closures Files 9%, Generic / Templated Code Files 7%, Parameter Forwarders Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 968 | 86.2% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 153 | 13.6% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 357*

**Composition by Extension & Reason:**
- `.md`: 206x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 79x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 8x Excluded (Static Asset Blob without Intent: 1476 LOC), 5x Excluded (Static Asset Blob without Intent: 1542 LOC), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 23x Excluded (Explicitly Denied Extension: '.ico')
- `.ts`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 426 LOC)
- `.gz`: 3x Excluded (Explicitly Denied Extension: '.gz')
- `.patch`: 3x Excluded (Unsupported Extension: '.patch')
- `.toml`: 2x Excluded (Unsupported Extension: '.toml')
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tgz`: 1x Excluded (Explicitly Denied Extension: '.tgz')
- `.jpeg`: 1x Excluded (Explicitly Denied Extension: '.jpeg')
- `.snap`: 1x Excluded (Unsupported Extension: '.snap')
- `.yaml`: 1x Excluded (Massive Static Asset Blob: 19359 LOC)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 1x Zero-Density Threshold (LOC: 488, Signals: 0)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 14.4 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.7 | 21.5 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.6 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 15.0 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 30.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 16.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 76.1 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 7.4 | 0.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 74.0 | 5.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 48.7 | 50.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 843 | 234 | 2 | `packages/react-router/__tests__/router/context-middleware-test.tsx` |
| cleanup | 196 | 100 | 0 | `packages/react-router/__tests__/router/should-revalidate-test.ts` |
| guards | 2592 | 309 | 5 | `packages/react-router-dev/vite/plugin.ts` |
| danger | 1877 | 249 | 3 | `packages/react-router/__tests__/dom/data-browser-router-test.tsx` |
| concurrency | 14301 | 354 | 21 | `integration/single-fetch-test.ts` |
| connectivity | 4491 | 660 | 6 | `integration/single-fetch-test.ts` |
| io | 6448 | 374 | 11 | `packages/react-router/__tests__/dom/data-browser-router-test.tsx` |
| crypto | 1 | 1 | 0 | `packages/react-router-dev/vite/plugin.ts` |
| ipc | 12 | 11 | 0 | `packages/create-react-router/__tests__/create-react-router-test.ts` |
| time | 246 | 104 | 0 | `integration/client-data-test.ts` |
| serialization | 348 | 116 | 1 | `integration/headers-test.ts` |
| regex | 353 | 91 | 0 | `packages/react-router-dev/vite/plugin.ts` |
| events | 1041 | 192 | 2 | `integration/single-fetch-test.ts` |
| tests | 13542 | 242 | 21 | `packages/react-router/__tests__/router/lazy-test.ts` |
| docs | 983 | 169 | 1 | `packages/react-router/lib/router/utils.ts` |
| debt | 1856 | 192 | 2 | `packages/react-router/__tests__/dom/data-browser-router-test.tsx` |
| mutation | 23090 | 644 | 46 | `packages/react-router/__tests__/dom/data-browser-router-test.tsx` |
| dead_code | 208 | 98 | 0 | `packages/react-router-dev/vite/route-chunks.ts` |
| credential | 50 | 6 | 0 | `tutorials/address-book/app/data.ts` |
| threat | 10 | 6 | 0 | `packages/react-router-node/__tests__/sessions-test.ts` |
| ml_ai | 63 | 24 | 0 | `examples/ssr-data-router/src/App.tsx` |
| ui | 5748 | 319 | 10 | `packages/react-router/__tests__/useNavigate-test.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/react-router/__tests__/dom/data-browser-router-test.tsx` (Hits: 391)
- `packages/react-router/__tests__/router/fetchers-test.ts` (Hits: 322)
- `packages/react-router/__tests__/router/context-middleware-test.tsx` (Hits: 240)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **create-fixture.ts** (`integration/helpers/create-fixture.ts`) — 58 inbound connections
2. **history.ts** (`packages/react-router/lib/router/history.ts`) — 57 inbound connections
3. **utils.ts** (`packages/react-router/lib/router/utils.ts`) — 57 inbound connections
4. **router.ts** (`packages/react-router/lib/router/router.ts`) — 54 inbound connections
5. **playwright-fixture.ts** (`integration/helpers/playwright-fixture.ts`) — 48 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **rsc-test.ts** (`integration/rsc/rsc-test.ts`) — 67 outbound dependencies
2. **plugin.ts** (`packages/react-router-dev/vite/plugin.ts`) — 46 outbound dependencies
3. **index.ts** (`packages/react-router/index.ts`) — 39 outbound dependencies
4. **typegen-test.ts** (`integration/typegen-test.ts`) — 33 outbound dependencies
5. **vite.ts** (`integration/helpers/vite.ts`) — 27 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `createRouter` **(Many-Argument Workhorses)** (@ `packages/react-router/lib/router/router.ts`) -> Impact: **791.0** | LOC: 2865
  * *Intent:* //#endregion //////////////////////////////////////////////////////////////////////////////// //#region createRouter /////////////////////////////////...
- `testDomRouter` **(Many-Argument Workhorses)** (@ `packages/react-router/__tests__/dom/data-browser-router-test.tsx`) -> Impact: **655.5** | LOC: 8790
- `getMatchesToLoad` **(Many-Argument Workhorses)** (@ `packages/react-router/lib/router/router.ts`) -> Impact: **277.7** | LOC: 300
- `createStaticHandler` **(Many-Argument Workhorses)** (@ `packages/react-router/lib/router/router.ts`) -> Impact: **260.2** | LOC: 944
- `handleLoaders` **(Many-Argument Workhorses)** (@ `packages/react-router/lib/router/router.ts`) -> Impact: **192.8** | LOC: 265
  * *Intent:* // Call all applicable loaders for the given matches, handling redirects, // errors, etc.
- `reactRouterRSCVitePlugin` **(I/O & Config Routines)** (@ `packages/react-router-dev/vite/rsc/plugin.ts`) -> Impact: **184.9** | LOC: 938
- `createClientRoutes` **(Many-Argument Workhorses)** (@ `packages/react-router/lib/dom/ssr/routes.tsx`) -> Impact: **164.5** | LOC: 350
- `useRoutesImpl` **(Many-Argument Workhorses)** (@ `packages/react-router/lib/hooks.tsx`) -> Impact: **135.5** | LOC: 1235
  * *Intent:* // Internal implementation with accept optional param for RouterProvider usage
- `handleFetcherAction` **(Many-Argument Workhorses)** (@ `packages/react-router/lib/router/router.ts`) -> Impact: **135.3** | LOC: 318
  * *Intent:* // Call the action for the matched fetcher.submit(), and then handle redirects, // errors, and revalidation
- `setup` **(Compute Cores)** (@ `packages/react-router/__tests__/router/utils/data-router-setup.ts`) -> Impact: **130.0** | LOC: 535

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `integration` | 88 | 24697.78 | 31.64% | 6.0% |
| `packages/react-router-dev/vite` | 27 | 24651.92 | 19.17% | 1.74% |
| `packages/react-router/__tests__/router` | 28 | 9650.74 | 32.43% | 35.98% |
| `packages/react-router/lib/router` | 5 | 6877.0 | 27.75% | 11.26% |
| `integration/rsc` | 4 | 6374.3 | 43.31% | 0.0% |
| `__monolith__` | 18 | 5178.68 | 0.37% | 0.0% |
| `packages/react-router/__tests__/dom` | 25 | 3636.22 | 6.61% | 40.28% |
| `packages/react-router/__tests__` | 40 | 2312.12 | 8.82% | 22.45% |
| `packages/react-router/lib/dom/ssr` | 16 | 1901.68 | 34.68% | 1.58% |
| `packages/create-react-router` | 16 | 1830.34 | 37.99% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/react-router/__tests__/dom/client-on-error-test.tsx` -> **100.0%** Exposure
- `packages/react-router/__tests__/dom/ssr/links-test.tsx` -> **99.9999%** Exposure
- `packages/react-router/__tests__/router/instrumentation-test.ts` -> **99.9998%** Exposure
- `packages/react-router/__tests__/dom/partial-hydration-test.tsx` -> **99.9997%** Exposure
- `packages/react-router/__tests__/dom/navigate-encode-params-test.tsx` -> **99.9961%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `integration/helpers/playwright-fixture.ts` -> **100.0%** Exposure
- `integration/helpers/vite-plugin-cloudflare-template/app/entry.server.tsx` -> **100.0%** Exposure
- `packages/create-react-router/prompts-text.ts` -> **100.0%** Exposure
- `packages/react-router-dev/cli/run.ts` -> **100.0%** Exposure
- `packages/react-router-dev/config/config.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/react-router/__tests__/dom/data-browser-router-test.tsx` -> **0** Orphaned Functions | **229** Duplicates
- `packages/react-router/__tests__/router/context-middleware-test.tsx` -> **0** Orphaned Functions | **157** Duplicates
- `packages/react-router/__tests__/router/instrumentation-test.ts` -> **0** Orphaned Functions | **89** Duplicates
- `packages/react-router/__tests__/data-memory-router-test.tsx` -> **0** Orphaned Functions | **56** Duplicates
- `packages/react-router/__tests__/react-transitions-test.tsx` -> **0** Orphaned Functions | **56** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `9` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1566` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `packages/react-router-dev/vite/route-chunks-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.471)
- **Top Global Matches:** file_cluster_10: 4.471, file_cluster_2: 7.282, file_cluster_13: 7.497
- **Magnitude:** 20744.38 | **LOC:** 1636 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.567; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (34.1%), Mutation Surface (formerly State Flux) (23.3%), Concurrency Surface (formerly Concurrency) (20.9%), Connectivity (formerly Api Exposure) (15.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 725`, `args: 285`, `func_start: 200`, `class_start: 8`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* `io: 6`, `api: 275`, `concurrency: 3`, `import: 127`
* *Defense:* `safety: 123`, `test: 308`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cache, check, defaultMessage, messages, route-chunks, shared, sharedMessage, side-effect...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/rsc/rsc-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.154)
- **Top Global Matches:** file_cluster_10: 5.154, file_cluster_2: 7.001, file_cluster_13: 7.253
- **Magnitude:** 5927.65 | **LOC:** 2729 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **67**; blast radius 0.567; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.8%), Guard Balance (formerly Safety Score) (45.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 25 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 546
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 899`, `args: 259`, `func_start: 203`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 17`
* *Architecture:* `io: 120`, `api: 125`, `concurrency: 421`, `import: 156`
* *Defense:* `safety: 31`, `test: 164`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` get-context, request-context, client, dashboard.client, events, home.actions, home.client, redirect.actions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router/lib/router/router.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.05)
- **Top Global Matches:** file_cluster_6: 9.05, file_cluster_4: 9.751, file_cluster_12: 17.059
- **Magnitude:** 5340.38 | **LOC:** 7322 | **CtrlFlow:** 19.9% | **Authorship Centralization:** 82.4%
- **Blast Radius:** changing it is visible to **54** in-repo importer(s); it depends on **3**; blast radius 11.898; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.8%), Concurrency Surface (formerly Concurrency) (96.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (70.5%)
- **Documentation Coverage:** 82.7411% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createRouter` **(Many-Argument Workhorses)** (Impact: 791.0)
    * *Intent:* //#endregion //////////////////////////////////////////////////////////////////////////////// //#reg...
  * `getMatchesToLoad` **(Many-Argument Workhorses)** (Impact: 277.7)
  * `createStaticHandler` **(Many-Argument Workhorses)** (Impact: 260.2)
  * `handleLoaders` **(Many-Argument Workhorses)** (Impact: 192.8)
    * *Intent:* // Call all applicable loaders for the given matches, handling redirects, // errors, etc.
  * `handleFetcherAction` **(Many-Argument Workhorses)** (Impact: 135.3)
    * *Intent:* // Call the action for the matched fetcher.submit(), and then handle redirects, // errors, and reval...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 35 instances
* *Amplified Cascading Flux:* 265 instances
* *Concurrency (weighted view):* 357
* *State Mutation (weighted view):* 840
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1083`, `structural_boundaries: 771`, `args: 305`, `func_start: 187`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 310`, `dead_code: 2`, `planned_debt: 6`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 88`, `api: 34`, `concurrency: 182`, `import: 6`
* *Defense:* `safety: 112`, `doc: 76`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.898
  * `Choke Point (Betweenness):` 0.000899 | `Ripple Effect (Closeness):` 0.064196
  * `Imports (Out-Degree: 3):` history, instrumentation, utils
  * `Imported By (In-Degree: 54):` (Excluded from Brief to save tokens)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/single-fetch-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.786)
- **Top Global Matches:** file_cluster_10: 5.786, file_cluster_0: 7.936, file_cluster_2: 8.318
- **Magnitude:** 2361.42 | **LOC:** 4669 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.567; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (92.4%), Mutation Surface (formerly State Flux) (48.8%), Guard Balance (formerly Safety Score) (47.8%)
- **Documentation Coverage:** 92.724% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `error` **(Callbacks & Closures)** (Impact: 1.1)
  * `error` **(Callbacks & Closures)** (Impact: 1.1)
  * `error` **(Callbacks & Closures)** (Impact: 1.1)
  * `error` **(Callbacks & Closures)** (Impact: 1.1)
  * `error` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 200 instances
* *Amplified Cascading Flux:* 41 instances
* *Concurrency (weighted view):* 1713
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 1558`, `args: 454`, `func_start: 400`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 161`, `duplicate_logic: 17`
* *Architecture:* `io: 43`, `api: 304`, `concurrency: 713`, `import: 139`
* *Defense:* `safety: 7`, `test: 416`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` parent, create-fixture.js, playwright-fixture.js, vite.js, test, vite, node, get-port...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router-dev/vite/plugin.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.549)
- **Top Global Matches:** file_cluster_4: 6.549, file_cluster_15: 11.5, file_cluster_6: 11.523
- **Magnitude:** 2295.02 | **LOC:** 4372 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 23.1%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **46**; blast radius 1.156; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (72.1%), Connectivity (formerly Api Exposure) (64.8%)
- **Documentation Coverage:** 98.1707% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getEnvironmentOptionsResolvers` **(Defensive Guards)** (Impact: 98.9)
  * `handlePrerender` **(Many-Argument Workhorses)** (Impact: 59.3)
  * `handler` **(I/O & Config Routines)** (Impact: 45.5)
    * *Intent:* // After the SSR build is finished, we inspect the Vite manifest for // the SSR build and move serve...
  * `resolveId` **(Many-Argument Workhorses)** (Impact: 45.2)
  * `postProcess` **(Many-Argument Workhorses)** (Impact: 38.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 40 instances
* *Amplified Cascading Flux:* 75 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 434
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 545`, `structural_boundaries: 654`, `args: 218`, `func_start: 141`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 2`, `state_mutation: 102`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `io: 145`, `api: 60`, `concurrency: 234`, `import: 59`
* *Defense:* `safety: 136`, `doc: 3`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.156
  * `Choke Point (Betweenness):` 0.000103 | `Ripple Effect (Closeness):` 0.003967
  * `Imports (Out-Degree: 24):` $getRouteChunkModuleId(
                chunkBasePath, $getRouteChunkModuleId(
            chunkBasePath, $virtualHmrRuntime.id, ), config, routes, invariant, manifest...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/react-router/__tests__/dom/data-browser-router-test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 13.203)
- **Top Global Matches:** file_cluster_12: 13.203, file_cluster_5: 13.86, file_cluster_10: 13.925
- **Magnitude:** 2108.7 | **LOC:** 8843 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 71.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.567; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.0%), Concurrency Surface (formerly Concurrency) (98.8%), Guard Balance (formerly Safety Score) (48.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testDomRouter` **(Many-Argument Workhorses)** (Impact: 655.5)
  * `assertLocation` **(Many-Argument Workhorses)** (Impact: 12.7)
    * *Intent:* // Utility to assert location info based on the type of router
  * `setupTest` **(Many-Argument Workhorses)** (Impact: 9.7)
  * `FetcherComponent` **(Callbacks & Closures)** (Impact: 5.3)
  * `Component` **(Callbacks & Closures)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 40 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 655
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 1227`, `args: 871`, `func_start: 533`
* *Risk/State:* `safety_bypasses: 126`, `state_mutation: 46`, `duplicate_logic: 229`
* *Architecture:* `io: 391`, `concurrency: 455`, `import: 7`
* *Defense:* `safety: 67`, `test: 553`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` index, utils, getHtml, getWindow, react, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/vite-spa-mode-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.037)
- **Top Global Matches:** file_cluster_10: 6.037, file_cluster_0: 6.062, file_cluster_13: 7.164
- **Magnitude:** 1783.0 | **LOC:** 1284 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.567; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (62.8%), Guard Balance (formerly Safety Score) (46.1%), Mutation Surface (formerly State Flux) (19.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 34 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 318
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 355`, `args: 115`, `func_start: 96`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `io: 28`, `api: 83`, `concurrency: 148`, `import: 58`
* *Defense:* `safety: 16`, `test: 88`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` routeImportTracker, create-fixture.js, playwright-fixture.js, vite.js, routeImportTracker, test, routes, vite...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router/__tests__/router/context-middleware-test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.598)
- **Top Global Matches:** file_cluster_10: 8.598, file_cluster_11: 8.955, file_cluster_15: 9.266
- **Magnitude:** 1680.36 | **LOC:** 3924 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.567; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Complexity Load (formerly Cognitive Load) (96.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `respondWithJson` **(Defensive Guards)** (Impact: 4.9)
  * `pushOrderContext` **(Generic / Templated Code)** (Impact: 3.7)
  * `dataStrategy` **(Callbacks & Closures)** (Impact: 3.6)
  * `dataStrategy` **(Generic / Templated Code)** (Impact: 3.2)
  * `getOrderMiddleware` **(Callbacks & Closures)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 149 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 1213
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 706`, `args: 407`, `func_start: 357`, `class_start: 1`
* *Risk/State:* `state_mutation: 137`, `duplicate_logic: 157`
* *Architecture:* `io: 240`, `concurrency: 468`, `import: 9`
* *Defense:* `safety: 21`, `test: 260`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` components, history, router, utils, data-router-setup, utils, react
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/vite-prerender-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.336)
- **Top Global Matches:** file_cluster_10: 7.336, file_cluster_0: 7.821, file_cluster_13: 8.919
- **Magnitude:** 1650.28 | **LOC:** 3072 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.567; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (94.2%), Guard Balance (formerly Safety Score) (44.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.6%)
- **Documentation Coverage:** 92.724% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `listAllFiles` **(Callbacks & Closures)** (Impact: 6.8)
  * `recurse` **(Callbacks & Closures)** (Impact: 6.3)
  * `captureRequests` **(Callbacks & Closures)** (Impact: 4.9)
  * `createFixture` **(Defensive Guards)** (Impact: 4.7)
  * `clearRequests` **(State Mutators)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 138 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 1237
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 1079`, `args: 262`, `func_start: 239`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 111`
* *Architecture:* `io: 24`, `api: 211`, `concurrency: 547`, `import: 108`
* *Defense:* `safety: 55`, `test: 317`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` create-fixture.js, playwright-fixture.js, vite.js, test, vite, node:fs, node:path, node:stream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/middleware-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.055)
- **Top Global Matches:** file_cluster_10: 7.055, file_cluster_12: 8.21, file_cluster_15: 8.374
- **Magnitude:** 1557.48 | **LOC:** 2959 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.567; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (89.0%), Guard Balance (formerly Safety Score) (48.2%), Mutation Surface (formerly State Flux) (39.4%)
- **Documentation Coverage:** 92.724% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `log` **(Parameter Forwarders)** (Impact: 1.5)
  * `error` **(Parameter Forwarders)** (Impact: 1.5)
  * `error` **(Parameter Forwarders)** (Impact: 1.5)
  * `error` **(Parameter Forwarders)** (Impact: 1.5)
  * `error` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 126 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 1050
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 1163`, `args: 386`, `func_start: 299`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 120`, `duplicate_logic: 11`
* *Architecture:* `io: 14`, `api: 300`, `concurrency: 420`, `import: 158`
* *Defense:* `safety: 36`, `test: 227`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` context, create-fixture.js, playwright-fixture.js, vite.js, test, vite, node, node:stream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router/__tests__/router/lazy-discovery-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.15)
- **Top Global Matches:** file_cluster_10: 7.15, file_cluster_15: 7.304, file_cluster_11: 7.669
- **Magnitude:** 985.24 | **LOC:** 2617 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.567; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (98.9%), Complexity Load (formerly Cognitive Load) (87.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `patchRoutesOnNavigation` **(Compute Cores)** (Impact: 7.6)
  * `patchRoutesOnNavigation` **(Compute Cores)** (Impact: 6.9)
  * `patchRoutesOnNavigation` **(Compute Cores)** (Impact: 6.9)
  * `patchRoutesOnNavigation` **(Compute Cores)** (Impact: 6.9)
  * `patchRoutesOnNavigation` **(Compute Cores)** (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 73 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 641
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 301`, `args: 201`, `func_start: 138`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 64`, `planned_debt: 1`, `duplicate_logic: 45`
* *Architecture:* `io: 201`, `concurrency: 276`, `import: 7`
* *Defense:* `safety: 5`, `test: 251`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` history, router, utils, data-router-setup, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router/__tests__/router/ssr-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.049)
- **Top Global Matches:** file_cluster_10: 7.049, file_cluster_12: 8.661, file_cluster_11: 9.042
- **Magnitude:** 949.0 | **LOC:** 2292 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.567; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (97.8%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (50.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loader` **(Callbacks & Closures)** (Impact: 7.1)
  * `queryRoute` **(Many-Argument Workhorses)** (Impact: 5.7)
  * `setupFlexRouteTest` **(I/O & Config Routines)** (Impact: 4.9)
  * `[type]` **(Callbacks & Closures)** (Impact: 2.1)
  * `resolveLoader` **(I/O & Config Routines)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 95 instances
* *Concurrency (weighted view):* 761
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 382`, `args: 197`, `func_start: 125`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 76`, `duplicate_logic: 20`, `unreferenced_by_name: 1`
* *Architecture:* `io: 103`, `concurrency: 286`, `import: 6`
* *Defense:* `safety: 75`, `doc: 1`, `test: 341`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` router, utils, data-router-setup, urlDataStrategy, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/redirects-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.183)
- **Top Global Matches:** file_cluster_10: 5.183, file_cluster_0: 6.7, file_cluster_13: 7.3
- **Magnitude:** 934.94 | **LOC:** 309 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.567; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (86.5%), Guard Balance (formerly Safety Score) (46.9%), Mutation Surface (formerly State Flux) (27.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 98
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 120`, `args: 36`, `func_start: 22`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 2`, `api: 19`, `concurrency: 48`, `import: 19`
* *Defense:* `safety: 3`, `test: 22`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` create-fixture.js, playwright-fixture.js, vite.js, test, react, react-router
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/fetcher-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.661)
- **Top Global Matches:** file_cluster_10: 4.661, file_cluster_2: 6.86, file_cluster_13: 7.138
- **Magnitude:** 901.89 | **LOC:** 594 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.567; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (100.0%), Guard Balance (formerly Safety Score) (49.8%), Mutation Surface (formerly State Flux) (31.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 59 instances
* *Concurrency (weighted view):* 434
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 213`, `args: 73`, `func_start: 37`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* `api: 20`, `concurrency: 139`, `import: 13`
* *Defense:* `safety: 1`, `test: 20`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` create-fixture.js, playwright-fixture.js, test, react, react-router
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router/__tests__/router/fetchers-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.254)
- **Top Global Matches:** file_cluster_10: 7.254, file_cluster_12: 8.711, file_cluster_11: 8.981
- **Magnitude:** 891.72 | **LOC:** 3707 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.567; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (80.2%), Guard Balance (formerly Safety Score) (40.1%), Debt Markers (formerly Tech Debt) (36.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initializeTest` **(I/O & Config Routines)** (Impact: 13.9)
  * `patchRoutesOnNavigation` **(Callbacks & Closures)** (Impact: 3.4)
  * `loader` **(Interface Declarations)** (Impact: 1.2)
  * `action` **(Interface Declarations)** (Impact: 1.2)
  * `loader` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 28 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 729
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 649`, `args: 156`, `func_start: 109`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 53`, `planned_debt: 25`, `fragile_debt: 5`, `duplicate_logic: 8`, `unreferenced_by_name: 1`
* *Architecture:* `io: 322`, `concurrency: 589`, `import: 6`
* *Defense:* `safety: 72`, `test: 637`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` history, router, utils, data-router-setup, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/client-data-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.846)
- **Top Global Matches:** file_cluster_10: 6.846, file_cluster_15: 7.463, file_cluster_11: 7.533
- **Magnitude:** 835.02 | **LOC:** 1680 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 37.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.567; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (99.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.8%), Guard Balance (formerly Safety Score) (45.2%)
- **Documentation Coverage:** 92.724% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getFiles` **(Compute Cores)** (Impact: 10.5)
  * `clientLoader` **(Parameter Forwarders)** (Impact: 1.8)
  * `clientLoader` **(Parameter Forwarders)** (Impact: 1.8)
  * `HydrateFallback` **(Interface Declarations)** (Impact: 1.1)
  * `HydrateFallback` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 78 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 650
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 447`, `args: 141`, `func_start: 114`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 52`, `duplicate_logic: 4`
* *Architecture:* `api: 78`, `concurrency: 260`, `import: 37`
* *Defense:* `safety: 15`, `test: 180`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` create-fixture.js, playwright-fixture.js, vite.js, test, react, react-router
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration/fog-of-war-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.206)
- **Top Global Matches:** file_cluster_5: 8.206, file_cluster_12: 9.115, file_cluster_0: 9.351
- **Magnitude:** 821.32 | **LOC:** 1702 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.567; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (92.7%), Guard Balance (formerly Safety Score) (50.7%), Mutation Surface (formerly State Flux) (39.5%)
- **Documentation Coverage:** 92.724% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getFiles` **(Generic / Templated Code)** (Impact: 4.8)
  * `error` **(Callbacks & Closures)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 71 instances
* *Amplified Cascading Flux:* 22 instances
* *Concurrency (weighted view):* 642
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 537`, `args: 168`, `func_start: 98`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 31`
* *Architecture:* `io: 5`, `api: 68`, `concurrency: 287`, `import: 53`
* *Defense:* `safety: 7`, `test: 147`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` create-fixture.js, playwright-fixture.js, vite.js, test, node:stream, react, client, react-router...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router/lib/router/utils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.483)
- **Top Global Matches:** file_cluster_4: 8.483, file_cluster_0: 10.659, file_cluster_12: 10.929
- **Magnitude:** 755.74 | **LOC:** 2199 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 72.7%
- **Blast Radius:** changing it is visible to **57** in-repo importer(s); it depends on **4**; blast radius 17.697; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (96.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.6%)
- **Documentation Coverage:** 65.3846% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveTo` **(Many-Argument Workhorses)** (Impact: 51.0)
  * `flattenRoutes` **(Many-Argument Workhorses)** (Impact: 43.7)
  * `compilePath` **(Many-Argument Workhorses)** (Impact: 41.5)
  * `flattenRoute` **(Many-Argument Workhorses)** (Impact: 28.1)
  * `generatePath` **(Type Conversions)** (Impact: 25.1)
    * *Intent:* /** * Returns a path with params interpolated. * * import { generatePath } from "react-router"; * * ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 353`, `args: 74`, `func_start: 47`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 57`, `planned_debt: 3`
* *Architecture:* `io: 74`, `api: 87`, `concurrency: 11`, `import: 5`
* *Defense:* `safety: 14`, `doc: 108`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.697
  * `Choke Point (Betweenness):` 0.000129 | `Ripple Effect (Closeness):` 0.068081
  * `Imports (Out-Degree: 3):` future, utils, history, react
  * `Imported By (In-Degree: 57):` (Excluded from Brief to save tokens)

### `packages/react-router-dev/vite/rsc/plugin.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.642)
- **Top Global Matches:** file_cluster_4: 6.642, file_cluster_6: 8.099, file_cluster_15: 13.662
- **Magnitude:** 750.48 | **LOC:** 982 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **23**; blast radius 0.808; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (70.2%), Complexity Load (formerly Cognitive Load) (66.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `reactRouterRSCVitePlugin` **(I/O & Config Routines)** (Impact: 184.9)
  * `config` **(Many-Argument Workhorses)** (Impact: 85.2)
  * `postProcess` **(Many-Argument Workhorses)** (Impact: 57.9)
  * `transform` **(Many-Argument Workhorses)** (Impact: 34.0)
  * `validateConfig` **(Defensive Guards)** (Impact: 20.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 100
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 150`, `args: 53`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`, `planned_debt: 1`
* *Architecture:* `io: 18`, `api: 13`, `concurrency: 40`, `import: 29`
* *Defense:* `safety: 32`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.808
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.00089
  * `Imports (Out-Degree: 14):` $virtual.hmrRuntime.id, config, invariant, typegen, has-dependency, load-dotenv, optimize-deps-entries, plugin...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/create-react-router/__tests__/create-react-router-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.593)
- **Top Global Matches:** file_cluster_6: 8.593, file_cluster_4: 10.016, file_cluster_10: 16.408
- **Magnitude:** 716.84 | **LOC:** 1332 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.567; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (99.5%), Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `interactWithShell` **(Many-Argument Workhorses)** (Impact: 35.3)
  * `execCreateReactRouter` **(Compute Cores)** (Impact: 13.5)
  * `defer` **(Callbacks & Closures)** (Impact: 3.9)
  * `reject` **(Callbacks & Closures)** (Impact: 3.0)
  * `getProjectDir` **(Parameter Forwarders)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 62 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 422
* *State Mutation (weighted view):* 212
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 178`, `args: 89`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 188`
* *Architecture:* `io: 134`, `concurrency: 112`, `import: 20`
* *Defense:* `safety: 15`, `test: 188`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` index, msw, setupAfterEnv, execa, node:child_process, node:fs, promises, node:os...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router/lib/rsc/server.rsc.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.689)
- **Top Global Matches:** file_cluster_4: 6.689, file_cluster_12: 9.768, file_cluster_15: 11.088
- **Magnitude:** 687.76 | **LOC:** 1502 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **14**; blast radius 1.301; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Mutation Surface (formerly State Flux) (90.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.0%)
- **Documentation Coverage:** 95.9184% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processServerAction` **(Many-Argument Workhorses)** (Impact: 77.2)
  * `generateMiddlewareResponse` **(Defensive Guards)** (Impact: 30.7)
  * `getRSCRouteMatch` **(Compute Cores)** (Impact: 30.1)
  * `getRenderPayload` **(Many-Argument Workhorses)** (Impact: 25.8)
  * `generateResourceResponse` **(Many-Argument Workhorses)** (Impact: 24.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 46 instances
* *Concurrency (weighted view):* 147
* *State Mutation (weighted view):* 145
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 260`, `args: 70`, `func_start: 40`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 53`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 7`
* *Architecture:* `io: 12`, `api: 24`, `concurrency: 72`, `import: 14`
* *Defense:* `safety: 46`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.301
  * `Choke Point (Betweenness):` 0.000137 | `Ripple Effect (Closeness):` 0.01944
  * `Imports (Out-Degree: 11):` actions, components, routeModules, single-fetch, errors, history, router, utils...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `packages/react-router/__tests__/router/utils/data-router-setup.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.666)
- **Top Global Matches:** file_cluster_4: 7.666, file_cluster_12: 10.084, file_cluster_0: 10.435
- **Magnitude:** 683.46 | **LOC:** 763 | **CtrlFlow:** 15.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **4**; blast radius 3.094; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setup` **(Compute Cores)** (Impact: 130.0)
  * `getFetcherHelpers` **(Many-Argument Workhorses)** (Impact: 39.8)
  * `fetch` **(Many-Argument Workhorses)** (Impact: 30.7)
  * `navigate` **(Many-Argument Workhorses)** (Impact: 24.7)
  * `enhanceRoutes` **(Compute Cores)** (Impact: 22.0)
    * *Intent:* // Enhance routes with loaders/actions as requested that will call the // active navigation loader/a...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 52 instances
* *Concurrency (weighted view):* 104
* *State Mutation (weighted view):* 164
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 122`, `args: 65`, `func_start: 34`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 60`, `planned_debt: 5`
* *Architecture:* `io: 25`, `api: 13`, `concurrency: 39`, `import: 8`
* *Defense:* `safety: 17`, `test: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.094
  * `Choke Point (Betweenness):` 0.000144 | `Ripple Effect (Closeness):` 0.017809
  * `Imports (Out-Degree: 4):` history, router, utils, utils
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `packages/react-router/__tests__/data-memory-router-test.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.589)
- **Top Global Matches:** file_cluster_0: 8.589, file_cluster_10: 9.651, file_cluster_12: 10.264
- **Magnitude:** 641.22 | **LOC:** 3445 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.567; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Debt Markers (formerly Tech Debt) (87.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (47.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setupDeferredTest` **(Generic / Templated Code)** (Impact: 14.0)
  * `AwaitCounter` **(Generic / Templated Code)** (Impact: 4.9)
  * `Bar` **(Callbacks & Closures)** (Impact: 2.6)
  * `LazyData` **(Interface Declarations)** (Impact: 2.5)
  * `LazyFallback` **(Interface Declarations)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 41 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 366
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 365`, `args: 278`, `func_start: 164`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 43`, `dead_code: 1`, `duplicate_logic: 56`
* *Architecture:* `io: 123`, `concurrency: 161`, `import: 8`
* *Defense:* `safety: 24`, `test: 193`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` index, urlDataStrategy, utils, MemoryNavigate, getHtml, jest-dom, react, react...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-router/__tests__/router/instrumentation-test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.852)
- **Top Global Matches:** file_cluster_10: 6.852, file_cluster_15: 8.089, file_cluster_12: 8.509
- **Magnitude:** 597.28 | **LOC:** 2257 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.567; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (46.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `route` **(Compute Cores)** (Impact: 5.0)
  * `route` **(Compute Cores)** (Impact: 5.0)
  * `route` **(Compute Cores)** (Impact: 4.9)
  * `route` **(Compute Cores)** (Impact: 4.9)
  * `loader` **(Compute Cores)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 299
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 373`, `args: 218`, `func_start: 175`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 3`, `planned_debt: 2`, `duplicate_logic: 89`
* *Architecture:* `io: 69`, `concurrency: 289`, `import: 9`
* *Defense:* `safety: 4`, `test: 183`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.567
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` components, history, router, utils, server, utils, data-router-setup, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `examples/auth-router-provider/src/App.tsx` (TYPESCRIPT) | Magnitude: 45.46 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 144, structural_boundaries: 28, core_var_decl: 23, design_snake_case: 18
- `packages/react-router-fs-routes/index.ts` (TYPESCRIPT) | Magnitude: 18.62 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 9, io: 7, import: 6
- `integration/sri-test.ts` (TYPESCRIPT) | Magnitude: 142.28 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 27, concurrency: 12, core_var_decl: 10
- `examples/basic-data-router/src/app.tsx` (TYPESCRIPT) | Magnitude: 6.84 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 9, args: 4, func_start: 3
- `packages/react-router/__tests__/dom/concurrent-mode-navigations-test.tsx` (TYPESCRIPT) | Magnitude: 64.52 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 286, structural_boundaries: 84, ui_framework: 70, core_var_decl: 54

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `packages/react-router/__tests__/dom/stub-test.tsx` (TYPESCRIPT) | Magnitude: 87.64 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 330, structural_boundaries: 90, args: 70, func_start: 43
- `integration/vite-css-test.ts` (TYPESCRIPT) | Magnitude: 306.36 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 511, structural_boundaries: 145, concurrency: 70, args: 60
- `integration/cli-test.ts` (TYPESCRIPT) | Magnitude: 90.88 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 140, state_mutation: 41, test: 38, structural_boundaries: 24
- `integration/rsc/rsc-prerender-test.ts` (TYPESCRIPT) | Magnitude: 70.06 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 147, structural_boundaries: 64, concurrency: 40, core_var_decl: 19
- `integration/vite-spa-mode-test.ts` (TYPESCRIPT) | Magnitude: 1783.0 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1144, structural_boundaries: 355, concurrency: 148, args: 115

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `playground/rsc-vite/src/routes/about/about.tsx` (TYPESCRIPT) | Magnitude: 18.22 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 13, concurrency: 8, args: 6
- `examples/notes/src/notes.js` (JAVASCRIPT) | Magnitude: 63.64 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 27, indent_spaces: 21, concurrency: 10, core_var_decl: 9
- `packages/react-router-dev/vite/vite.ts` (TYPESCRIPT) | Magnitude: 33.4 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 20, core_var_decl: 8, import: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/react-router/lib/rsc/html-stream/browser.ts` (TYPESCRIPT) | Magnitude: 38.78 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 35, branch: 9, structural_boundaries: 9, args: 5
- `packages/react-router-dev/vite/profiler.ts` (TYPESCRIPT) | Magnitude: 23.62 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 29, indent_spaces: 24, core_var_decl: 8, args: 7
- `packages/react-router/__tests__/server-runtime/data-test.ts` (TYPESCRIPT) | Magnitude: 6.16 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 9, core_var_decl: 7, design_snake_case: 6
- `packages/react-router-remix-routes-option-adapter/__tests__/routeManifestToRouteConfig-test.ts` (TYPESCRIPT) | Magnitude: 8.14 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 13, args: 10, test: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `integration/vite-plugin-order-validation-test.ts` (TYPESCRIPT) | Magnitude: 57.88 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 23, decorators: 13, import: 13
- `packages/react-router/__tests__/router/TestSequences/Listen.ts` (TYPESCRIPT) | Magnitude: 2.94 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 3, core_var_decl: 2, design_snake_case: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/react-router-dev/vite/styles.ts` (TYPESCRIPT) | Magnitude: 158.04 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 187, structural_boundaries: 59, branch: 37, core_var_decl: 32
- `packages/react-router-dev/vite/rsc/virtual-route-config.ts` (TYPESCRIPT) | Magnitude: 68.32 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 48, state_mutation: 15, structural_boundaries: 12, branch: 10
- `scripts/find-release-from-changeset.js` (JAVASCRIPT) | Magnitude: 10.44 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 6, branch: 4, args: 3
- `examples/ssr/server.js` (JAVASCRIPT) | Magnitude: 84.44 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 23, core_var_decl: 14, design_snake_case: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/react-router/__tests__/router/TestSequences/ListenPopOnly.ts` (TYPESCRIPT) | Magnitude: 4.22 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 3, test: 3, core_var_decl: 2
- `packages/react-router/__tests__/setup.ts` (TYPESCRIPT) | Magnitude: 48.42 | Delta: **0.15** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 25, globals: 22, state_mutation: 14, branch: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/react-router/lib/components.tsx` (TYPESCRIPT) | Magnitude: 486.28 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 804, structural_boundaries: 193, branch: 171, ui_framework: 102

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/react-router/__tests__/dom/ssr/components-test.tsx` (TYPESCRIPT) | Magnitude: 67.52 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 379, structural_boundaries: 68, core_var_decl: 53, args: 40
- `packages/react-router/__tests__/router/utils/utils.ts` (TYPESCRIPT) | Magnitude: 123.16 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 35, args: 18, branch: 17
- `packages/react-router/lib/types/route-data.ts` (TYPESCRIPT) | Magnitude: 27.68 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 239, structural_boundaries: 146, generics: 127, args: 56

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `scripts/version.js` (JAVASCRIPT) | Magnitude: 33.5 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 13, core_var_decl: 9, io: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `examples/ssr-data-router/server.js` (JAVASCRIPT) | Magnitude: 94.0 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 26, core_var_decl: 15, design_snake_case: 13
- `packages/react-router/lib/href.ts` (TYPESCRIPT) | Magnitude: 39.18 | Delta: **0.172** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 17, branch: 16, io: 10

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/react-router/lib/rsc/server.rsc.ts` -> Churn: **74.0%** | Cog Load: 75.9505% | Debt: 48.0825%
- `packages/react-router/lib/router/router.ts` -> Churn: **69.74%** | Cog Load: 62.7606% | Debt: 10.905%
- `integration/client-data-test.ts` -> Churn: **59.82%** | Cog Load: 99.1928% | Debt: 13.6497%
- `packages/react-router-dev/vite/rsc/plugin.ts` -> Churn: **59.82%** | Cog Load: 66.7953% | Debt: 7.992%
- `packages/react-router/lib/rsc/server.ssr.tsx` -> Churn: **56.56%** | Cog Load: 45.794% | Debt: 84.4601%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `integration/rsc/rsc-test.ts` -> **Jacob Ebey** (100.0% isolated ownership) | Magnitude: 5927.65
- `packages/react-router/lib/router/router.ts` -> **Matt Brophy** (82.4% isolated ownership) | Magnitude: 5340.38
- `packages/react-router/__tests__/router/context-middleware-test.tsx` -> **Matt Brophy** (100.0% isolated ownership) | Magnitude: 1680.36
- `packages/react-router/__tests__/router/ssr-test.ts` -> **Matt Brophy** (100.0% isolated ownership) | Magnitude: 949.0
- `integration/fetcher-test.ts` -> **Jacob Ebey** (100.0% isolated ownership) | Magnitude: 901.89

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/react-router/lib/server-runtime/server.ts` -> **Severity: 0.123** (Bridge: 0.0013 * Flux: 97.9202%)
- `packages/react-router/lib/router/instrumentation.ts` -> **Severity: 0.098** (Bridge: 0.001 * Flux: 94.0786%)
- `packages/react-router/lib/router/router.ts` -> **Severity: 0.088** (Bridge: 0.0009 * Flux: 97.751%)
- `packages/react-router/lib/dom/ssr/routes.tsx` -> **Severity: 0.033** (Bridge: 0.0006 * Flux: 52.0678%)
- `packages/react-router/__tests__/router/utils/data-router-setup.ts` -> **Severity: 0.014** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/react-router/lib/router/history.ts` -> **Severity: 4.518** (Embedded: 0.0755 * Error Risk: 59.8688%)
- `packages/react-router/lib/router/utils.ts` -> **Severity: 3.853** (Embedded: 0.0681 * Error Risk: 56.5916%)
- `packages/react-router/lib/router/router.ts` -> **Severity: 3.619** (Embedded: 0.0642 * Error Risk: 56.3689%)
- `packages/react-router/lib/types/utils.ts` -> **Severity: 2.712** (Embedded: 0.0452 * Error Risk: 60.0%)
- `integration/helpers/create-fixture.ts` -> **Severity: 2.66** (Embedded: 0.0517 * Error Risk: 51.4894%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `integration/helpers/vite.ts` -> **Severity: 3771.7** (Blast Radius: 37.717 * Doc Risk: 100.0%)
- `integration/helpers/create-fixture.ts` -> **Severity: 1983.764** (Blast Radius: 24.246 * Doc Risk: 81.8182%)
- `packages/react-router/lib/router/history.ts` -> **Severity: 1535.4** (Blast Radius: 26.443 * Doc Risk: 58.0645%)
- `packages/react-router/lib/router/utils.ts` -> **Severity: 1157.111** (Blast Radius: 17.697 * Doc Risk: 65.3846%)
- `packages/react-router/lib/router/router.ts` -> **Severity: 984.454** (Blast Radius: 11.898 * Doc Risk: 82.7411%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 434 literal sites + 9 sites through wrappers = 443
- **`panics_and_aborts`:** 803 literal sites + 7 sites through wrappers = 810

- `warn` (function, debug_prints, primitive): 7 call sites in 1 files -- `scripts/docs.ts`
- `cleanupCallbacks` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `packages/react-router/lib/server-runtime/single-fetch.ts`
- `notSupportedInRR` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `packages/react-router-fs-routes/flatRoutes.ts`
- `preventEmptyChunkSnippet` (function, debug_prints, primitive): 2 call sites in 1 files -- `packages/react-router-dev/vite/plugin.ts`
- `importWrangler` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/react-router-dev/vite/cloudflare-dev-proxy.ts`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 8841 call pairs -- scoped 30.8%, unique 0.0%, ambiguous 10.0%, external 59.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 8617 | 31.3% | 0.0% | 10.1% | 58.6% |
| javascript | 202 | 13.4% | 0.0% | 5.4% | 81.2% |
| shell | 22 | 0.0% | 0.0% | 0.0% | 100.0% |

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
