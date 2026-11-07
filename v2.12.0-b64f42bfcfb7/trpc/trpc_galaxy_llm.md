# ARCHITECTURAL_BRIEF: trpc
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/trpc/trpc.git` |
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
- **Scope:** 1219 analyzed artifact(s), 85299 LOC.
- **Load-bearing artifact:** `packages/server/src/@trpc/server/index.ts` -- 229 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/server/src/unstable-core-do-not-import.ts` -- pulls in 36 dependencies, the widest assembly point in the scan.
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
| Total Artifacts | 1573 |
| Analyzed Artifacts (Scanned) | 1219 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 354 |
| Total LOC | 85299 |
| Volatility Index | 0.007 |
| % Scanned of codebase = | 77.5% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7476 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1802 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 4.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.4197 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 138 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 793 | 75894 | 65.1% |
| MARKDOWN | 184 | 0 | 15.1% |
| JSON | 80 | 6120 | 6.6% |
| PLAINTEXT | 62 | 8 | 5.1% |
| YAML | 35 | 1707 | 2.9% |
| JAVASCRIPT | 26 | 871 | 2.1% |
| XML | 17 | 2 | 1.4% |
| SQLITE | 11 | 40 | 0.9% |
| CSS | 6 | 592 | 0.5% |
| HTML | 3 | 44 | 0.2% |
| POSTGRESQL | 2 | 21 | 0.2% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 1211 |
| unknown | unknown | 8 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 41%, Declarative / Non-Code 17%, Callbacks & Closures Files 12%, Large Core Modules (2) 7%, Large Core Modules 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 971 | 79.7% |
| Unknown | 8 | 0.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 238 | 19.5% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 354*

**Composition by Extension & Reason:**
- `.ts`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 10x Excluded (Machine-Generated Source Code Signature: 172 LOC), 9x Excluded (Machine-Generated Source Code Signature: 17 LOC)
- `.md`: 66x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 35x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mdx`: 29x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 21 exceeds 500 chars), 1x Excluded (Saturation: Line 35 exceeds 500 chars)
- `.json`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 5063 LOC), 1x Excluded (Static Asset Blob without Intent: 1138 LOC)
- `.mdc`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 6x Excluded (Explicitly Denied Extension: '.ico')
- `.toml`: 3x Excluded (Unsupported Extension: '.toml'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1770 LOC), 1x Excluded (Massive Static Asset Blob: 41407 LOC)
- `.prisma`: 3x Excluded (Unsupported Extension: '.prisma')
- `.tsx`: 1x Excluded (Saturation: Line 35 exceeds 500 chars), 1x Excluded (Saturation: Line 16 exceeds 500 chars)
- `.example`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snap`: 1x Excluded (Unsupported Extension: '.snap')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 8.7 | 4.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 19.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 1.6 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 17.2 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 32.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 7.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 96.1 | 0.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.3 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 77.1 | 3.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 47.2 | 33.3 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 61.3 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 367 | 178 | 1 | `packages/server/src/@trpc/server/index.ts` |
| cleanup | 153 | 71 | 0 | `packages/tests/server/websockets.test.ts` |
| guards | 2897 | 437 | 7 | `packages/openapi/test/routers/appRouter.router.ts` |
| danger | 1327 | 299 | 3 | `packages/server/src/unstable-core-do-not-import/procedureBuilder.ts` |
| concurrency | 5029 | 420 | 10 | `packages/tests/server/websockets.test.ts` |
| connectivity | 1982 | 620 | 4 | `packages/server/src/unstable-core-do-not-import.ts` |
| io | 1711 | 292 | 4 | `www/src/components/TwitterWall/script.output.ts` |
| crypto | 1 | 1 | 0 | `packages/openapi/test/scripts/codegen.ts` |
| ipc | 9 | 5 | 0 | `examples/next-prisma-websockets-starter/src/pages/index.tsx` |
| time | 236 | 109 | 0 | `packages/tests/server/websockets.test.ts` |
| serialization | 304 | 93 | 0 | `packages/react-query/test/withTRPC.test.tsx` |
| regex | 90 | 46 | 0 | `scripts/entrypoints.ts` |
| events | 725 | 140 | 1 | `packages/tests/server/websockets.test.ts` |
| tests | 4212 | 193 | 6 | `packages/tests/server/websockets.test.ts` |
| docs | 1402 | 344 | 3 | `eslint.config.js` |
| debt | 704 | 187 | 1 | `packages/tests/server/streaming.test.ts` |
| mutation | 10467 | 716 | 24 | `packages/tests/server/websockets.test.ts` |
| dead_code | 313 | 196 | 1 | `examples/next-prisma-starter/src/pages/index.tsx` |
| credential | 50 | 4 | 0 | `www/src/components/TwitterWall/script.output.ts` |
| threat | 18 | 10 | 0 | `.github/ISSUE_TEMPLATE/1.bug_report.yml` |
| ml_ai | 93 | 34 | 0 | `www/og-image/pages/index.tsx` |
| ui | 1473 | 194 | 2 | `www/src/pages/index.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `www/src/components/TwitterWall/script.output.ts` (Hits: 88)
- `www/src/components/sponsors/script.output.ts` (Hits: 64)
- `packages/upgrade/src/transforms/hooksToOptions.ts` (Hits: 49)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **index.ts** (`packages/server/src/@trpc/server/index.ts`) — 229 inbound connections
2. **utils.ts** (`packages/server/src/unstable-core-do-not-import/utils.ts`) — 33 inbound connections
3. **TRPCError.ts** (`packages/server/src/unstable-core-do-not-import/error/TRPCError.ts`) — 30 inbound connections
4. **__reactHelpers.tsx** (`packages/react-query/test/__reactHelpers.tsx`) — 26 inbound connections
5. **router.ts** (`packages/server/src/unstable-core-do-not-import/router.ts`) — 26 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **unstable-core-do-not-import.ts** (`packages/server/src/unstable-core-do-not-import.ts`) — 36 outbound dependencies
2. **index.tsx** (`www/src/pages/index.tsx`) — 24 outbound dependencies
3. **generate.test.ts** (`packages/openapi/test/generate.test.ts`) — 18 outbound dependencies
4. **httpSubscriptionLink.test.ts** (`packages/tests/server/httpSubscriptionLink.test.ts`) — 16 outbound dependencies
5. **validators.test.ts** (`packages/tests/server/validators.test.ts`) — 15 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `createRootHooks` **(Defensive Guards)** (@ `packages/react-query/src/shared/hooks/createHooksInternal.tsx`) -> Impact: **211.2** | LOC: 688
  * *Intent:* /** */
- `transform` **(Many-Argument Workhorses)** (@ `packages/upgrade/src/transforms/hooksToOptions.ts`) -> Impact: **181.2** | LOC: 383
- `resolveResponse` **(Defensive Guards)** (@ `packages/server/src/unstable-core-do-not-import/http/resolveResponse.ts`) -> Impact: **139.6** | LOC: 558
- `pluginLlmsTxt` **(Defensive Guards)** (@ `www/docusaurus.config.ts`) -> Impact: **117.1** | LOC: 305
  * *Intent:* /** * Thank you to prisma docs for this plugin <3 * https://github.com/prisma/docs/blob/22208d52e4168028dbbe8b020b10682e6b526e50/docusaurus.config.ts#...
- `postBuild` **(Defensive Guards)** (@ `www/docusaurus.config.ts`) -> Impact: **99.5** | LOC: 237
- `getWSConnectionHandler` **(Defensive Guards)** (@ `packages/server/src/adapters/ws.ts`) -> Impact: **85.3** | LOC: 462
- `getProcedureTypeName` **(Many-Argument Workhorses)** (@ `packages/openapi/src/generate.ts`) -> Impact: **83.0** | LOC: 725
  * *Intent:* /** * Inspect `_def.type` and return the procedure type string, or null if this is * not a procedure (e.g. a nested router). */
- `migrateUseUtils` **(Compute Cores)** (@ `packages/upgrade/src/transforms/hooksToOptions.ts`) -> Impact: **69.3** | LOC: 169
  * *Intent:* // Migrate trpc.useUtils() to useQueryClient()
- `request` **(Compute Cores)** (@ `examples/openapi-codegen/src/client/generated/client/client.gen.ts`) -> Impact: **69.2** | LOC: 168
- `handleRequest` **(Many-Argument Workhorses)** (@ `packages/server/src/adapters/ws.ts`) -> Impact: **57.3** | LOC: 245

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `examples/next-prisma-websockets-starter` | 14 | 10142.37 | 1.27% | 0.0% |
| `examples/next-prisma-starter` | 13 | 10129.19 | 1.68% | 0.0% |
| `www` | 17 | 5550.38 | 8.36% | 5.56% |
| `__monolith__` | 14 | 5165.78 | 1.41% | 4.67% |
| `examples/next-prisma-todomvc` | 7 | 5051.4 | 0.92% | 0.0% |
| `examples/.experimental/next-app-dir` | 2 | 5001.0 | 0.0% | 0.0% |
| `packages/openapi/test` | 12 | 4777.86 | 4.07% | 0.0% |
| `packages/tests/server` | 42 | 4674.04 | 9.66% | 0.0% |
| `packages/react-query/test` | 44 | 2423.38 | 10.9% | 0.0% |
| `packages/server/src/unstable-core-do-not-import/stream` | 6 | 1132.74 | 52.78% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/ISSUE_TEMPLATE/1.bug_report.yml` -> **100.0%** Exposure
- `packages/client/src/internals/transformer.ts` -> **100.0%** Exposure
- `packages/server/src/unstable-core-do-not-import/transformer.ts` -> **100.0%** Exposure
- `packages/server/src/adapters/next-app-dir/nextAppDirCaller.ts` -> **99.9993%** Exposure
- `packages/server/src/adapters/aws-lambda/index.ts` -> **99.997%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `examples/next-prisma-websockets-starter/src/pages/api/auth/[...nextauth].ts` -> **100.0%** Exposure
- `examples/next-sse-chat/src/components/avatar.tsx` -> **100.0%** Exposure
- `packages/server/src/unstable-core-do-not-import/stream/utils/asyncIterable.ts` -> **100.0%** Exposure
- `packages/server/src/unstable-core-do-not-import/stream/utils/disposable.ts` -> **100.0%** Exposure
- `packages/server/src/unstable-core-do-not-import/stream/utils/mergeAsyncIterables.test.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/tests/server/streaming.test.ts` -> **0** Orphaned Functions | **44** Duplicates
- `packages/react-query/test/withTRPC.test.tsx` -> **0** Orphaned Functions | **43** Duplicates
- `packages/tests/server/transformer.test.ts` -> **2** Orphaned Functions | **22** Duplicates
- `packages/tests/server/websockets.test.ts` -> **0** Orphaned Functions | **20** Duplicates
- `packages/client/src/links/localLink.test.ts` -> **1** Orphaned Functions | **17** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `www/docusaurus.config.ts` -> **61.3063%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### 📡 API Network Audit (Set Theory)
- **Shadow APIs (Critical):** `1` undocumented endpoints actively listening.
- **Ghost APIs (Bloat):** `3` endpoints documented but missing from code.
- **Known Shadow Routes:** `GET /`

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2135` packages imported that bypass the Zero-Trust whitelist.

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/.experimental/next-app-dir/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/next-prisma-starter/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/next-prisma-starter/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/next-prisma-todomvc/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/next-prisma-websockets-starter/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/next-prisma-websockets-starter/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `www/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/openapi/test/cyclicTypes.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.609)
- **Top Global Matches:** file_cluster_10: 4.609, file_cluster_2: 6.398, file_cluster_13: 7.021
- **Magnitude:** 3300.64 | **LOC:** 423 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.365; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (71.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.4%), Guard Balance (formerly Safety Score) (23.4%), Complexity Load (formerly Cognitive Load) (7.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 98`, `args: 24`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`
* *Architecture:* `io: 3`, `concurrency: 4`, `import: 6`
* *Defense:* `safety: 54`, `test: 120`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` generate, types, types, validateOpenApi, node:path, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/openapi/test/edgeCases.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.925)
- **Top Global Matches:** file_cluster_10: 4.925, file_cluster_2: 7.628, file_cluster_0: 7.746
- **Magnitude:** 1109.1 | **LOC:** 338 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.365; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.2%), Guard Balance (formerly Safety Score) (31.1%), Complexity Load (formerly Cognitive Load) (13.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Concurrency (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 79`, `args: 37`, `func_start: 5`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 15`, `import: 7`
* *Defense:* `safety: 12`, `test: 94`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` generate, types, types.gen, types, validateOpenApi, node:path, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/openapi/src/generate.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.802)
- **Top Global Matches:** file_cluster_4: 5.802, file_cluster_6: 9.823, file_cluster_9: 11.433
- **Magnitude:** 638.54 | **LOC:** 1539 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **5**; blast radius 1.363; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.2%), Guard Balance (formerly Safety Score) (52.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.2%), Connectivity (formerly Api Exposure) (30.5%)
- **Documentation Coverage:** 55.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getProcedureTypeName` **(Many-Argument Workhorses)** (Impact: 83.0)
    * *Intent:* /** * Inspect `_def.type` and return the procedure type string, or null if this is * not a procedure...
  * `convertPlainObject` **(Many-Argument Workhorses)** (Impact: 42.2)
  * `convertUnionType` **(Many-Argument Workhorses)** (Impact: 36.6)
    * *Intent:* // --------------------------------------------------------------------------- // Union type convers...
  * `typeToJsonSchema` **(Many-Argument Workhorses)** (Impact: 32.8)
    * *Intent:* // --------------------------------------------------------------------------- // Type → JSON Schema...
  * `convertPrimitiveOrLiteral` **(Compute Cores)** (Impact: 32.3)
    * *Intent:* // --------------------------------------------------------------------------- // Primitive & litera...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 354`, `args: 77`, `func_start: 49`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 55`, `fragile_debt: 1`
* *Architecture:* `io: 23`, `api: 4`, `concurrency: 4`, `import: 5`
* *Defense:* `safety: 31`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.363
  * `Choke Point (Betweenness):` 0.000196 | `Ripple Effect (Closeness):` 0.005029
  * `Imports (Out-Degree: 2):` schemaExtraction, types, node:fs, node:path, typescript
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `packages/react-query/src/shared/hooks/createHooksInternal.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.584)
- **Top Global Matches:** file_cluster_6: 9.584, file_cluster_4: 12.174, file_cluster_12: 17.593
- **Magnitude:** 590.58 | **LOC:** 780 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **14**; blast radius 3.381; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (44.5%), Connectivity (formerly Api Exposure) (44.2%), Mutation Surface (formerly State Flux) (22.4%), Complexity Load (formerly Cognitive Load) (17.0%)
- **Documentation Coverage:** 88.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createRootHooks` **(Defensive Guards)** (Impact: 211.2)
    * *Intent:* /** */
  * `useQuery` **(Defensive Guards)** (Impact: 47.6)
  * `useSubscription` **(Many-Argument Workhorses)** (Impact: 45.4)
  * `useInfiniteQuery` **(Defensive Guards)** (Impact: 43.6)
  * `usePrefetchQuery` **(Defensive Guards)** (Impact: 21.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 161`, `args: 51`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 11`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 23`, `api: 9`, `concurrency: 2`, `import: 18`
* *Defense:* `safety: 75`, `doc: 4`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.381
  * `Choke Point (Betweenness):` 5.8e-05 | `Ripple Effect (Closeness):` 0.007817
  * `Imports (Out-Degree: 9):` context, getClientArgs, getQueryKey, trpcResult, useQueries, createUtilityFunctions, useQueriesProxy, types...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/tests/server/websockets.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.979)
- **Top Global Matches:** file_cluster_10: 7.979, file_cluster_12: 9.152, file_cluster_15: 9.613
- **Magnitude:** 564.78 | **LOC:** 2227 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.365; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (43.5%), Complexity Load (formerly Cognitive Load) (34.9%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 97.6744% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `factory` **(Defensive Guards)** (Impact: 29.4)
  * `waitForClientState` **(Type Conversions)** (Impact: 4.9)
  * `createContext` **(Defensive Guards)** (Impact: 4.7)
  * `next` **(Compute Cores)** (Impact: 4.5)
  * `next` **(Compute Cores)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 23 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 388
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 509`, `args: 242`, `func_start: 87`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 21`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 20`
* *Architecture:* `io: 8`, `concurrency: 273`, `import: 18`
* *Defense:* `safety: 37`, `doc: 2`, `test: 243`, `immutability_locks: 2`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` react, client, testClientResource, unstable-internals, server, trpcServerResource, waitError, ws...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tests/server/streaming.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.418)
- **Top Global Matches:** file_cluster_10: 6.418, file_cluster_15: 7.958, file_cluster_2: 8.72
- **Magnitude:** 505.94 | **LOC:** 1467 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.365; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (47.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.2%), Complexity Load (formerly Cognitive Load) (30.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `client` **(Parameter Forwarders)** (Impact: 2.7)
  * `client` **(Parameter Forwarders)** (Impact: 2.7)
  * `client` **(Parameter Forwarders)** (Impact: 2.7)
  * `client` **(Parameter Forwarders)** (Impact: 2.6)
  * `client` **(Parameter Forwarders)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 34 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 321
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 323`, `args: 122`, `func_start: 76`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 25`, `duplicate_logic: 44`
* *Architecture:* `io: 13`, `concurrency: 151`, `import: 12`
* *Defense:* `safety: 30`, `test: 76`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` zAsyncIterable, react, client, testClientResource, server, waitError, observable, unstable-core-do-not-import...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server/src/unstable-core-do-not-import/stream/utils/mergeAsyncIterables.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.304)
- **Top Global Matches:** file_cluster_10: 4.304, file_cluster_2: 6.116, file_cluster_13: 6.882
- **Magnitude:** 502.14 | **LOC:** 163 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.365; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (48.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 25 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 151
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 24`, `args: 9`, `func_start: 6`
* *Risk/State:* `state_mutation: 13`
* *Architecture:* `io: 1`, `concurrency: 26`, `import: 3`
* *Defense:* `safety: 7`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` utils, createDeferred, mergeAsyncIterables
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server/src/unstable-core-do-not-import/stream/jsonl.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.637)
- **Top Global Matches:** file_cluster_4: 7.637, file_cluster_12: 9.44, file_cluster_15: 10.715
- **Magnitude:** 410.58 | **LOC:** 655 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **8**; blast radius 4.161; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (98.5%), Mutation Surface (formerly State Flux) (86.2%), Connectivity (formerly Api Exposure) (53.8%), Guard Balance (formerly Safety Score) (53.0%)
- **Documentation Coverage:** 71.9298% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `jsonlStreamConsumer` **(Defensive Guards)** (Impact: 46.5)
    * *Intent:* /** * JSON Lines stream consumer */
  * `createBatchStreamProducer` **(Defensive Guards)** (Impact: 41.0)
  * `decodeChunkDefinition` **(Defensive Guards)** (Impact: 24.9)
  * `createStreamsManager` **(Callbacks & Closures)** (Impact: 12.3)
    * *Intent:* /** * Creates a handler for managing stream controllers and their lifecycle */
  * `encodeAsyncIterable` **(Defensive Guards)** (Impact: 11.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 154`, `args: 59`, `func_start: 46`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 22`
* *Architecture:* `io: 27`, `api: 13`, `concurrency: 18`, `import: 10`
* *Defense:* `safety: 22`, `doc: 11`, `immutability_locks: 3`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.161
  * `Choke Point (Betweenness):` 0.000603 | `Ripple Effect (Closeness):` 0.100604
  * `Imports (Out-Degree: 7):` utils, asyncIterable, createDeferred, disposable, mergeAsyncIterables, readableStreamFrom, withPing, is-plain-object
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/upgrade/src/transforms/hooksToOptions.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.932)
- **Top Global Matches:** file_cluster_8: 9.932, file_cluster_3: 16.605, file_cluster_6: 21.363
- **Magnitude:** 388.64 | **LOC:** 448 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.469; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.8%), Complexity Load (formerly Cognitive Load) (31.1%)
- **Documentation Coverage:** 93.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `transform` **(Many-Argument Workhorses)** (Impact: 181.2)
  * `migrateUseUtils` **(Compute Cores)** (Impact: 69.3)
    * *Intent:* // Migrate trpc.useUtils() to useQueryClient()
  * `removeSuspenseDestructuring` **(Defensive Guards)** (Impact: 41.5)
  * `ensureUseTRPCCall` **(Compute Cores)** (Impact: 8.2)
  * `replaceHooksWithOptions` **(I/O & Config Routines)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 26`, `args: 16`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 24`
* *Architecture:* `io: 49`, `api: 2`, `import: 3`
* *Defense:* `safety: 20`, `doc: 4`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.469
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000821
  * `Imports (Out-Degree: 2):` modifiers, walkers, jscodeshift
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/tests/server/httpSubscriptionLink.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.904)
- **Top Global Matches:** file_cluster_10: 6.904, file_cluster_15: 8.447, file_cluster_12: 8.509
- **Magnitude:** 385.46 | **LOC:** 1640 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.365; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (44.9%), Complexity Load (formerly Cognitive Load) (28.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.7%)
- **Documentation Coverage:** 97.2973% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createContext` **(Defensive Guards)** (Impact: 15.1)
  * `getCtx` **(Defensive Guards)** (Impact: 7.7)
  * `next` **(Defensive Guards)** (Impact: 7.7)
  * `getCtxResource` **(I/O & Config Routines)** (Impact: 7.1)
    * *Intent:* /** * Test resource */
  * `createContext` **(Defensive Guards)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 204
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 382`, `args: 170`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 22`, `duplicate_logic: 12`, `unreferenced_by_name: 1`
* *Architecture:* `io: 10`, `concurrency: 134`, `import: 19`
* *Defense:* `safety: 45`, `doc: 1`, `test: 134`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` iterableEventEmitter, zAsyncIterable, client, testClientResource, unstable-internals, server, fakeTimersResource, suppressLogs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server/src/unstable-core-do-not-import/stream/jsonl.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.348)
- **Top Global Matches:** file_cluster_12: 8.348, file_cluster_0: 8.534, file_cluster_10: 8.641
- **Magnitude:** 359.44 | **LOC:** 738 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.365; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (47.1%), Mutation Surface (formerly State Flux) (41.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `[Symbol.asyncIterator]` **(Compute Cores)** (Impact: 3.3)
  * `[Symbol.asyncIterator]` **(Compute Cores)** (Impact: 3.2)
  * `[Symbol.asyncIterator]` **(I/O & Config Routines)** (Impact: 2.3)
  * `serverResourceForStream` **(Generic / Templated Code)** (Impact: 2.2)
  * `start` **(State Mutators)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 33 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 295
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 154`, `args: 54`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 12`, `dead_code: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 11`, `concurrency: 130`, `import: 7`
* *Defense:* `safety: 7`, `test: 76`, `immutability_locks: 10`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` utils, jsonl, createDeferred, disposable, react, fetchServerResource, superjson
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tests/server/batching.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.514)
- **Top Global Matches:** file_cluster_10: 4.514, file_cluster_13: 6.554, file_cluster_2: 6.868
- **Magnitude:** 351.3 | **LOC:** 210 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.365; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (35.8%), Complexity Load (formerly Cognitive Load) (28.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Concurrency (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 49`, `args: 18`, `func_start: 7`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 2`, `concurrency: 27`, `import: 6`
* *Defense:* `safety: 16`, `test: 27`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` client, testClientResource, server, waitError, superjson, zod
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `www/docusaurus.config.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.504)
- **Top Global Matches:** file_cluster_8: 7.504, file_cluster_6: 17.55, file_cluster_3: 20.265
- **Magnitude:** 335.96 | **LOC:** 579 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.365; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (94.1%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (78.8%), Credential Material (formerly Secrets Risk) (61.3%)
- **Documentation Coverage:** 41.9147% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pluginLlmsTxt` **(Defensive Guards)** (Impact: 117.1)
    * *Intent:* /** * Thank you to prisma docs for this plugin <3 * https://github.com/prisma/docs/blob/22208d52e416...
  * `postBuild` **(Defensive Guards)** (Impact: 99.5)
  * `findMdxFilesRecursively` **(Defensive Guards)** (Impact: 18.0)
    * *Intent:* // Recursive function to find all .md/.mdx files
  * `configurePostCss` **(Compute Cores)** (Impact: 3.3)
  * `myPlugin` **(Interface Declarations)** (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 40`, `args: 11`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 19`, `unreferenced_by_name: 4`
* *Architecture:* `io: 30`, `api: 1`, `concurrency: 13`, `import: 15`
* *Defense:* `safety: 26`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` docusaurus.typedoc.js, mdxToJsx, shikiTwoslash.config, env, preset-classic, types, autoprefixer, cssnano...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tests/server/middlewares.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.376)
- **Top Global Matches:** file_cluster_10: 4.376, file_cluster_2: 6.096, file_cluster_17: 6.523
- **Magnitude:** 327.36 | **LOC:** 546 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.365; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (36.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 86`, `args: 47`, `func_start: 5`
* *Risk/State:* None
* *Architecture:* `concurrency: 9`, `import: 1`
* *Defense:* `test: 21`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` server
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server/src/adapters/ws.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.228)
- **Top Global Matches:** file_cluster_6: 8.228, file_cluster_4: 11.724, file_cluster_8: 16.152
- **Magnitude:** 324.8 | **LOC:** 645 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.476; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (65.2%), Connectivity (formerly Api Exposure) (61.6%), Complexity Load (formerly Cognitive Load) (58.2%)
- **Documentation Coverage:** 77.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getWSConnectionHandler` **(Defensive Guards)** (Impact: 85.3)
  * `handleRequest` **(Many-Argument Workhorses)** (Impact: 57.3)
  * `applyWSSHandler` **(Defensive Guards)** (Impact: 11.3)
  * `createCtxPromise` **(Defensive Guards)** (Impact: 8.5)
  * `handleKeepAlive` **(Callbacks & Closures)** (Impact: 3.9)
    * *Intent:* /** * Handle WebSocket keep-alive messages */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 86
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 143`, `args: 33`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 17`
* *Architecture:* `io: 21`, `api: 12`, `concurrency: 21`, `import: 19`
* *Defense:* `safety: 25`, `doc: 13`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.476
  * `Choke Point (Betweenness):` 3.6e-05 | `Ripple Effect (Closeness):` 0.001095
  * `Imports (Out-Degree: 18):` server, http, rpc, http, observable, unstable-core-do-not-import, asyncIterable, unpromise...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/server/src/unstable-core-do-not-import/http/resolveResponse.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.786)
- **Top Global Matches:** file_cluster_4: 8.786, file_cluster_6: 9.989, file_cluster_12: 13.737
- **Magnitude:** 324.36 | **LOC:** 776 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **13**; blast radius 2.4; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (96.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.9%), Guard Balance (formerly Safety Score) (46.3%), Complexity Load (formerly Cognitive Load) (35.6%)
- **Documentation Coverage:** 89.4737% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveResponse` **(Defensive Guards)** (Impact: 139.6)
  * `initResponse` **(Defensive Guards)** (Impact: 36.0)
  * `formatError` **(Defensive Guards)** (Impact: 11.2)
  * `formatError` **(Defensive Guards)** (Impact: 10.9)
  * `caughtErrorToData` **(Generic / Templated Code)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 157`, `args: 31`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 10`, `fragile_debt: 1`
* *Architecture:* `io: 33`, `api: 2`, `concurrency: 24`, `import: 13`
* *Defense:* `safety: 51`, `doc: 8`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.000368 | `Ripple Effect (Closeness):` 0.098012
  * `Imports (Out-Degree: 13):` observable, TRPCError, getErrorShape, procedure, router, rpc, jsonl, sse...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/tests/server/routerMeta.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.68)
- **Top Global Matches:** file_cluster_10: 4.68, file_cluster_13: 7.061, file_cluster_2: 7.384
- **Magnitude:** 319.12 | **LOC:** 226 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.365; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.7%), Guard Balance (formerly Safety Score) (41.0%), Complexity Load (formerly Cognitive Load) (8.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 56`, `args: 25`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `concurrency: 20`, `import: 4`
* *Defense:* `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.365
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` testClientResource, server, observable, unstable-core-do-not-import
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `examples/.test/ssg-infinite-serialization/src/utils/trpc.ts` (TYPESCRIPT) | Magnitude: 7.8 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 10, import: 4, globals: 3
- `packages/tests/server/regression/issue-2856-middleware-infer.test.ts` (TYPESCRIPT) | Magnitude: 43.88 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 7, concurrency: 3, args: 2
- `examples/cloudflare-workers/src/client.ts` (TYPESCRIPT) | Magnitude: 15.5 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 12, concurrency: 11, thread_sleeps: 6
- `examples/vercel-edge-runtime/src/client.ts` (TYPESCRIPT) | Magnitude: 15.5 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 12, concurrency: 11, thread_sleeps: 6
- `examples/openapi-codegen/src/client/generated/core/auth.gen.ts` (TYPESCRIPT) | Magnitude: 17.16 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 13, branch: 7, concurrency: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `www/src/utils/searchParams.ts` (TYPESCRIPT) | Magnitude: 0.31 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 8, args: 4, func_start: 2
- `packages/openapi/test/generate.test.ts` (TYPESCRIPT) | Magnitude: 134.16 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 787, test: 165, structural_boundaries: 159, core_var_decl: 116
- `packages/upgrade/test/__fixtures__/hooks/optimistic-update.tsx` (TYPESCRIPT) | Magnitude: 19.44 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 9, args: 7, core_var_decl: 5
- `examples/next-prisma-starter/src/server/routers/post.ts` (TYPESCRIPT) | Magnitude: 30.64 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 17, safety: 10, core_var_decl: 9
- `packages/react-query/test/useMutation.test.tsx` (TYPESCRIPT) | Magnitude: 15.58 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 92, structural_boundaries: 30, args: 12, core_var_decl: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/client/src/links/wsLink/wsClient/requestManager.ts` (TYPESCRIPT) | Magnitude: 50.98 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 38, args: 17, doc: 14
- `packages/react-query/test/regression/issue-4360-useInfiniteQuery-placeHolderData.test.tsx` (TYPESCRIPT) | Magnitude: 13.72 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 21, args: 13, func_start: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/tests/server/regression/issue-4947-merged-middleware-inputs.test.ts` (TYPESCRIPT) | Magnitude: 56.68 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 16, core_var_decl: 13, safety: 8
- `packages/react-query/test/regression/issue-1645-setErrorStatusSSR.test.tsx` (TYPESCRIPT) | Magnitude: 32.02 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 14, test: 7, core_var_decl: 6
- `packages/client/src/getFetch.ts` (TYPESCRIPT) | Magnitude: 13.54 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 11, branch: 6, io: 5
- `packages/openapi/test/amazonIon.test.ts` (TYPESCRIPT) | Magnitude: 15.04 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 29, concurrency: 12, args: 9
- `packages/openapi/test/mongoEjson.test.ts` (TYPESCRIPT) | Magnitude: 15.04 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 29, concurrency: 12, args: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `www/src/components/TwitterWall/tweetsOld.ts` (TYPESCRIPT) | Magnitude: 17.96 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 96, decorators: 15, io: 14, sec_entropy: 8
- `examples/minimal-content-types/client/vite.config.ts` (TYPESCRIPT) | Magnitude: 16.22 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 3, import: 2, branch: 1
- `examples/minimal-react/client/vite.config.ts` (TYPESCRIPT) | Magnitude: 16.22 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 3, import: 2, branch: 1
- `examples/nuxt/app.vue` (HTML) | Magnitude: 15.36 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 8, ui_framework: 4, structural_boundaries: 2, func_start: 2
- `www/src/theme/DocItem/Metadata/index.tsx` (TYPESCRIPT) | Magnitude: 5.46 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 7, core_var_decl: 6, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/client/src/internals/inputWithTrackedEventId.ts` (TYPESCRIPT) | Magnitude: 10.7 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 5, branch: 4, args: 1
- `examples/lambda-api-gateway-streaming/src/client.ts` (TYPESCRIPT) | Magnitude: 9.18 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 10, safety: 6, concurrency: 6
- `examples/.experimental/next-app-dir/src/app/api/trpc/[trpc]/route.ts` (TYPESCRIPT) | Magnitude: 3.02 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, import: 3, explicit_casts: 2
- `examples/next-sse-chat/src/app/api/trpc/[trpc]/route.ts` (TYPESCRIPT) | Magnitude: 7.34 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 6, doc: 3, import: 3
- `examples/next-formdata/src/utils/trpc.ts` (TYPESCRIPT) | Magnitude: 26.86 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 19, api: 7, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/client/src/links/wsLink/wsClient/wsClient.ts` (TYPESCRIPT) | Magnitude: 221.18 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 324, structural_boundaries: 87, branch: 44, args: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/server/src/unstable-core-do-not-import.ts` (TYPESCRIPT) | Magnitude: 51.72 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 69, api: 36, import: 36, io: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/minimal-content-types/client/src/SendMultipartFormDataButton.tsx` (TYPESCRIPT) | Magnitude: 6.64 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 5, state_mutation: 3, core_var_decl: 3
- `examples/next-sse-chat/src/server/db/migrations/0000_lyrical_khan.sql` (POSTGRESQL) | Magnitude: 0.47 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: safety: 11, indent_tabs: 10, time_date_logic: 4, branch: 3
- `examples/next-prisma-starter/src/server/prisma.ts` (TYPESCRIPT) | Magnitude: 19.28 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, branch: 4, structural_boundaries: 3, import: 2
- `packages/client/src/index.ts` (TYPESCRIPT) | Magnitude: 22.2 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 9, api: 7, import: 7, doc: 2
- `packages/tanstack-react-query/src/index.ts` (TYPESCRIPT) | Magnitude: 24.52 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 15, api: 9, import: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `www/src/theme/DocVersionBanner/index.tsx` (TYPESCRIPT) | Magnitude: 20.94 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 19, branch: 11, core_var_decl: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `examples/.experimental/next-app-dir/src/app/server-action/FormWithUseActionExample.tsx` (TYPESCRIPT) | Magnitude: 4.98 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 7, core_var_decl: 7, design_snake_case: 5
- `www/src/components/TwitterWall/script.ts` (TYPESCRIPT) | Magnitude: 43.08 | Delta: **0.141** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 24, core_var_decl: 17, design_snake_case: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/client/src/internals/signals.ts` (TYPESCRIPT) | Magnitude: 35.08 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 15, branch: 12, args: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/openapi/test/cyclicTypes.test.ts` -> **Nick Lucas** (100.0% isolated ownership) | Magnitude: 3300.64
- `packages/openapi/test/edgeCases.test.ts` -> **Nick Lucas** (100.0% isolated ownership) | Magnitude: 1109.1
- `packages/openapi/src/generate.ts` -> **Nick Lucas** (100.0% isolated ownership) | Magnitude: 638.54
- `www/docusaurus.config.ts` -> **Nick Lucas** (100.0% isolated ownership) | Magnitude: 335.96
- `packages/openapi/src/schemaExtraction.ts` -> **Nick Lucas** (100.0% isolated ownership) | Magnitude: 268.06

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/server/src/unstable-core-do-not-import/stream/jsonl.ts` -> **Severity: 0.052** (Bridge: 0.0006 * Flux: 86.2025%)
- `packages/server/src/unstable-core-do-not-import/stream/sse.ts` -> **Severity: 0.036** (Bridge: 0.0005 * Flux: 78.4685%)
- `packages/server/src/unstable-core-do-not-import/router.ts` -> **Severity: 0.033** (Bridge: 0.0008 * Flux: 43.0919%)
- `packages/server/src/observable/observable.ts` -> **Severity: 0.029** (Bridge: 0.0003 * Flux: 92.732%)
- `packages/openapi/src/schemaExtraction.ts` -> **Severity: 0.021** (Bridge: 0.0002 * Flux: 96.7475%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/server/src/@trpc/server/index.ts` -> **Severity: 10.335** (Embedded: 0.2018 * Error Risk: 51.2147%)
- `packages/server/src/unstable-core-do-not-import/rootConfig.ts` -> **Severity: 8.286** (Embedded: 0.1036 * Error Risk: 80.0%)
- `packages/server/src/unstable-core-do-not-import/transformer.ts` -> **Severity: 8.108** (Embedded: 0.1055 * Error Risk: 76.875%)
- `packages/server/src/unstable-core-do-not-import/clientish/serialize.ts` -> **Severity: 6.923** (Embedded: 0.0981 * Error Risk: 70.5405%)
- `packages/server/src/unstable-core-do-not-import/http/formDataToObject.ts` -> **Severity: 6.897** (Embedded: 0.0984 * Error Risk: 70.0867%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/server/src/unstable-core-do-not-import/error/TRPCError.ts` -> **Severity: 1106.875** (Blast Radius: 12.65 * Doc Risk: 87.5%)
- `packages/server/src/unstable-core-do-not-import/parser.ts` -> **Severity: 693.0** (Blast Radius: 6.93 * Doc Risk: 100.0%)
- `packages/server/src/unstable-core-do-not-import/utils.ts` -> **Severity: 653.655** (Blast Radius: 22.411 * Doc Risk: 29.1667%)
- `packages/server/src/unstable-core-do-not-import/procedureBuilder.ts` -> **Severity: 549.45** (Blast Radius: 7.326 * Doc Risk: 75.0%)
- `packages/server/src/unstable-core-do-not-import/error/formatter.ts` -> **Severity: 485.8** (Blast Radius: 4.858 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 263 literal sites + 5 sites through wrappers = 268
- **`panics_and_aborts`:** 345 literal sites + 5 sites through wrappers = 350

- `errorToAsyncIterable` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `packages/server/src/unstable-core-do-not-import/http/resolveResponse.ts`
- `next` (function, debug_prints, primitive): 2 call sites in 1 files -- `examples/express-server/src/client.ts`
- `suppressLogs` (function, debug_prints, primitive): 2 call sites in 1 files -- `packages/server/src/__tests__/suppressLogs.ts`
- `cancel` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/server/src/unstable-core-do-not-import/http/resolveResponse.ts`
- `suppressLogs` (function, debug_prints, primitive): 1 call sites in 1 files -- `packages/tanstack-react-query/test/useSubscription.test.tsx`
- `throwAbortError` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/server/src/unstable-core-do-not-import/http/abortError.ts`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 5752 call pairs -- scoped 18.7%, unique 0.0%, ambiguous 14.9%, external 66.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 5695 | 18.8% | 0.0% | 15.0% | 66.2% |
| javascript | 57 | 7.0% | 0.0% | 0.0% | 93.0% |

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
