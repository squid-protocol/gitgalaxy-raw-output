# ARCHITECTURAL_BRIEF: trpc
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/trpc/trpc.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 1573 |
| Analyzed Artifacts (Scanned) | 1177 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 396 |
| Total LOC | 83010 |
| Volatility Index | 0.018 |
| % Scanned of codebase = | 74.8% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7294 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1422 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.0947 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 112 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 785 | 74762 | 66.7% |
| MARKDOWN | 178 | 0 | 15.1% |
| JSON | 79 | 6097 | 6.7% |
| PLAINTEXT | 61 | 8 | 5.2% |
| JAVASCRIPT | 26 | 871 | 2.2% |
| XML | 17 | 2 | 1.4% |
| SQLITE | 13 | 61 | 1.1% |
| YAML | 9 | 573 | 0.8% |
| CSS | 6 | 592 | 0.5% |
| HTML | 3 | 44 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 936 | 79.5% |
| Unknown | 8 | 0.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 231 | 19.6% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 396*

**Composition by Extension & Reason:**
- `.ts`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 9x Excluded (Machine-Generated Source Code Signature: 17 LOC), 9x Excluded (Machine-Generated Source Code Signature: 291 LOC)
- `.md`: 67x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 96 LOC)
- `no_extension`: 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mdx`: 29x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 8 exceeds 500 chars), 1x Excluded (Saturation: Line 60 exceeds 500 chars)
- `.yml`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 5063 LOC), 1x Excluded (Static Asset Blob without Intent: 1138 LOC)
- `.tsx`: 1x Excluded (Saturation: Line 55 exceeds 500 chars), 1x Excluded (Saturation: Line 35 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 502 LOC)
- `.mdc`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 6x Excluded (Explicitly Denied Extension: '.ico')
- `.toml`: 3x Excluded (Unsupported Extension: '.toml'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1770 LOC), 1x Excluded (Monolithic Amalgamation: 41407 LOC exceeds safe regex boundaries)
- `.prisma`: 3x Excluded (Unsupported Extension: '.prisma')
- `.example`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snap`: 1x Excluded (Unsupported Extension: '.snap')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 9.7 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.2 | 21.8 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 17.7 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 33.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 7.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 80.2 | 0.7 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 63.0 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 9.1 | 0.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 78.6 | 3.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 46.9 | 33.3 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 61.3 | 0.1 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 364 | 176 | 1 | `packages/server/src/@trpc/server/index.ts` |
| cleanup | 152 | 70 | 0 | `packages/tests/server/websockets.test.ts` |
| guards | 2863 | 428 | 7 | `packages/openapi/test/routers/appRouter.router.ts` |
| danger | 1307 | 292 | 3 | `packages/server/src/unstable-core-do-not-import/procedureBuilder.ts` |
| concurrency | 4974 | 410 | 10 | `packages/tests/server/websockets.test.ts` |
| connectivity | 1923 | 600 | 4 | `packages/openapi/test/types.ts` |
| io | 1671 | 284 | 4 | `www/src/components/TwitterWall/script.output.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 9 | 5 | 0 | `examples/next-prisma-websockets-starter/src/pages/index.tsx` |
| time | 232 | 108 | 0 | `packages/tests/server/websockets.test.ts` |
| serialization | 304 | 93 | 0 | `packages/react-query/test/withTRPC.test.tsx` |
| regex | 90 | 46 | 0 | `scripts/entrypoints.ts` |
| events | 715 | 133 | 1 | `packages/tests/server/websockets.test.ts` |
| tests | 4188 | 189 | 7 | `packages/tests/server/websockets.test.ts` |
| docs | 1321 | 321 | 3 | `eslint.config.js` |
| debt | 510 | 159 | 1 | `packages/tests/server/streaming.test.ts` |
| mutation | 10250 | 701 | 24 | `packages/tests/server/websockets.test.ts` |
| dead_code | 346 | 212 | 1 | `examples/next-prisma-websockets-starter/src/pages/index.tsx` |
| credential | 50 | 4 | 0 | `www/src/components/TwitterWall/script.output.ts` |
| threat | 86 | 37 | 0 | `packages/server/src/unstable-core-do-not-import/http/formDataToObject.test.ts` |
| ml_ai | 86 | 33 | 0 | `packages/tests/server/errorFormatting.test.ts` |
| ui | 1403 | 190 | 2 | `www/src/pages/index.tsx` |

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

1. **observable.ts** (`packages/server/src/observable/observable.ts`) — 61 inbound connections
2. **testClientResource.ts** (`packages/client/src/__tests__/testClientResource.ts`) — 53 inbound connections
3. **next.ts** (`packages/server/src/adapters/next.ts`) — 47 inbound connections
4. **__reactHelpers.tsx** (`packages/react-query/test/__reactHelpers.tsx`) — 26 inbound connections
5. **waitError.ts** (`packages/server/src/__tests__/waitError.ts`) — 22 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.tsx** (`www/src/pages/index.tsx`) — 24 outbound dependencies
2. **generate.test.ts** (`packages/openapi/test/generate.test.ts`) — 18 outbound dependencies
3. **httpSubscriptionLink.test.ts** (`packages/tests/server/httpSubscriptionLink.test.ts`) — 16 outbound dependencies
4. **validators.test.ts** (`packages/tests/server/validators.test.ts`) — 15 outbound dependencies
5. **websockets.test.ts** (`packages/tests/server/websockets.test.ts`) — 15 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getProcedureTypeName` (@ `packages/openapi/src/generate.ts`) -> Impact: **264.9** | LOC: 725
  * *Intent:* /** * Inspect `_def.type` and return the procedure type string, or null if this is * not a procedure (e.g. a nested router). */
- `createRootHooks` (@ `packages/react-query/src/shared/hooks/createHooksInternal.tsx`) -> Impact: **249.4** | LOC: 688
  * *Intent:* /** * @internal */
- `transform` (@ `packages/upgrade/src/transforms/hooksToOptions.ts`) -> Impact: **181.2** | LOC: 383
- `resolveResponse` (@ `packages/server/src/unstable-core-do-not-import/http/resolveResponse.ts`) -> Impact: **156.6** | LOC: 558
- `pluginLlmsTxt` (@ `www/docusaurus.config.ts`) -> Impact: **129.8** | LOC: 305
  * *Intent:* /** * Thank you to prisma docs for this plugin <3 * https://github.com/prisma/docs/blob/22208d52e4168028dbbe8b020b10682e6b526e50/docusaurus.config.ts#...
- `postBuild` (@ `www/docusaurus.config.ts`) -> Impact: **117.8** | LOC: 320
- `getWSConnectionHandler` (@ `packages/server/src/adapters/ws.ts`) -> Impact: **89.6** | LOC: 462
- `extractTwoslashBlocks` (@ `www/scripts/check-twoslash.ts`) -> Impact: **79.1** | LOC: 224
- `request` (@ `examples/openapi-codegen/src/client/generated/client/client.gen.ts`) -> Impact: **72.1** | LOC: 170
- `migrateUseUtils` (@ `packages/upgrade/src/transforms/hooksToOptions.ts`) -> Impact: **69.3** | LOC: 169
  * *Intent:* // Migrate trpc.useUtils() to useQueryClient()

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `examples/next-prisma-websockets-starter` | 14 | 10142.37 | 1.27% | 0.0% |
| `examples/next-prisma-starter` | 13 | 10129.19 | 1.68% | 0.0% |
| `packages/openapi/test` | 12 | 5756.58 | 8.36% | 0.0% |
| `www` | 16 | 5565.94 | 8.73% | 15.52% |
| `packages/tests/server` | 42 | 5230.46 | 10.61% | 0.0% |
| `__monolith__` | 14 | 5165.78 | 1.43% | 5.77% |
| `examples/next-prisma-todomvc` | 7 | 5051.4 | 0.92% | 0.0% |
| `examples/.experimental/next-app-dir` | 2 | 5001.0 | 0.0% | 0.0% |
| `packages/react-query/test` | 43 | 2610.14 | 11.75% | 0.0% |
| `packages/tests/server/regression` | 27 | 1257.5 | 6.73% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `packages/server/src/unstable-core-do-not-import/transformer.ts` -> **100.0%** Exposure
- `packages/server/src/adapters/aws-lambda/index.ts` -> **99.9977%** Exposure
- `packages/server/src/__tests__/trpcServerResource.ts` -> **99.9899%** Exposure
- `packages/client/src/internals/transformer.ts` -> **99.9665%** Exposure
- `packages/server/src/__tests__/suppressLogs.ts` -> **99.7527%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `examples/next-prisma-websockets-starter/src/pages/api/auth/[...nextauth].ts` -> **100.0%** Exposure
- `examples/next-sse-chat/src/components/avatar.tsx` -> **100.0%** Exposure
- `packages/server/src/unstable-core-do-not-import/stream/utils/asyncIterable.ts` -> **100.0%** Exposure
- `packages/server/src/unstable-core-do-not-import/stream/utils/disposable.ts` -> **100.0%** Exposure
- `packages/server/src/unstable-core-do-not-import/stream/utils/mergeAsyncIterables.test.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/tests/server/streaming.test.ts` -> **0** Orphaned Functions | **36** Duplicates
- `packages/react-query/test/withTRPC.test.tsx` -> **0** Orphaned Functions | **22** Duplicates
- `packages/tests/server/transformer.test.ts` -> **2** Orphaned Functions | **19** Duplicates
- `packages/tests/server/websockets.test.ts` -> **0** Orphaned Functions | **15** Duplicates
- `packages/react-query/test/regression/issue-4486-initialData-types.test.tsx` -> **0** Orphaned Functions | **10** Duplicates

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
- **Unknown Dependencies:** `2087` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/client/src/links/internals/httpUtils.ts` (TYPESCRIPT) -> Cumulative Risk: **649.37**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 131.2 | **LOC:** 244 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9928%), State Flux (89.3435%), Documentation (83.3333%)
- **Heaviest Functions:** `getUrl` (Impact: 16.9), `fetchHTTPResponse` (Impact: 14.2), `throwIfAborted` (Impact: 7.9)

### 2. `www/src/components/sponsors/script.pull.ts` (TYPESCRIPT) -> Cumulative Risk: **629.05**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 126.58 | **LOC:** 306 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `main` (Impact: 16.1), `calculateWeight` (Impact: 8.7), `flattenSponsor` (Impact: 6.4)

### 3. `packages/server/src/unstable-core-do-not-import/http/contentType.ts` (TYPESCRIPT) -> Cumulative Risk: **625.21**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 213.5 | **LOC:** 321 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9967%), Documentation (87.5%), State Flux (81.1095%)
- **Heaviest Functions:** `parse` (Impact: 48.9), `memo` (Impact: 13.2), `getRawInput` (Impact: 13.2)

### 4. `packages/upgrade/src/lib/git.ts` (TYPESCRIPT) -> Cumulative Risk: **624.56**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 32.82 | **LOC:** 55 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.95%), State Flux (97.3403%)
- **Heaviest Functions:** `filterIgnored` (Impact: 10.4), `assertCleanGitTree` (Impact: 2.5)

### 5. `scripts/entrypoints.ts` (TYPESCRIPT) -> Cumulative Risk: **611.61**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 101.6 | **LOC:** 158 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.8982%)
- **Heaviest Functions:** `generateEntrypoints` (Impact: 28.6), `writeFileSyncRecursive` (Impact: 3.8)

### 6. `packages/server/src/adapters/ws.ts` (TYPESCRIPT) -> Cumulative Risk: **606.84**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 379.1 | **LOC:** 645 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9978%), Verification (80.0%), Documentation (80.0%)
- **Heaviest Functions:** `getWSConnectionHandler` (Impact: 89.6), `handleRequest` (Impact: 59.0), `onabort` (Impact: 33.2)

### 7. `packages/server/src/adapters/fetch/fetchRequestHandler.ts` (TYPESCRIPT) -> Cumulative Risk: **602.68**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 76.14 | **LOC:** 81 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.0464%), Concurrency (87.0167%)
- **Heaviest Functions:** `fetchRequestHandler` (Impact: 25.5), `responseMeta` (Impact: 19.8), `trimSlashes` (Impact: 4.6)

### 8. `examples/next-minimal-starter/src/pages/api/trpc/[trpc].ts` (TYPESCRIPT) -> Cumulative Risk: **582.05**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 20.14 | **LOC:** 74 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.1785%)
- **Heaviest Functions:** `createContext` (Impact: 1.1)

### 9. `www/docusaurus.config.ts` (TYPESCRIPT) -> Cumulative Risk: **579.83**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 370.66 | **LOC:** 579 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (94.1252%), State Flux (81.2088%), Verification (80.0%)
- **Heaviest Functions:** `pluginLlmsTxt` (Impact: 129.8), `postBuild` (Impact: 117.8), `findMdxFilesRecursively` (Impact: 19.7)

### 10. `packages/client/src/links/wsLink/wsClient/wsClient.ts` (TYPESCRIPT) -> Cumulative Risk: **577.79**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 252.08 | **LOC:** 441 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9968%), State Flux (90.4751%), Verification (80.0%)
- **Heaviest Functions:** `setupWebSocketListeners` (Impact: 22.4), `handleCloseOrError` (Impact: 22.4), `constructor` (Impact: 17.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/.experimental/next-app-dir/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/next-prisma-starter/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/next-prisma-starter/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/next-prisma-todomvc/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/next-prisma-websockets-starter/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/next-prisma-websockets-starter/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `www/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/openapi/test/cyclicTypes.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3450.64 | **LOC:** 423 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (7.1542%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 98`, `args: 24`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`
* *Architecture:* `io: 3`, `concurrency: 4`, `import: 6`
* *Defense:* `safety: 54`, `test: 120`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` generate, types, types, validateOpenApi, node:path, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/openapi/test/edgeCases.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1912.48 | **LOC:** 338 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.3632%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 40
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 79`, `args: 37`, `func_start: 5`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 6`, `api: 1`, `concurrency: 15`, `import: 7`
* *Defense:* `safety: 12`, `test: 94`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` generate, types, types.gen, types, validateOpenApi, node:path, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/openapi/src/generate.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 868.64 | **LOC:** 1539 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.2828%), Tech Debt (8.6764%)
**Top Internal Functions/Classes:**
  * `getProcedureTypeName` (Impact: 264.9)
    * *Intent:* /** * Inspect `_def.type` and return the procedure type string, or null if this is * not a procedure...
  * `convertPlainObject` (Impact: 44.2)
  * `convertUnionType` (Impact: 36.6)
    * *Intent:* // --------------------------------------------------------------------------- // Union type convers...
  * `typeToJsonSchema` (Impact: 34.8)
    * *Intent:* // --------------------------------------------------------------------------- // Type → JSON Schema...
  * `buildOpenAPIDocument` (Impact: 32.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 279`, `structural_boundaries: 354`, `args: 77`, `func_start: 49`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 55`, `fragile_debt: 1`
* *Architecture:* `io: 23`, `api: 4`, `concurrency: 4`, `import: 5`
* *Defense:* `safety: 31`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.618
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.005098
  * `Imports (Out-Degree: 1):` schemaExtraction, types, node:fs, node:path, typescript
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `packages/react-query/src/shared/hooks/createHooksInternal.tsx` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 696.08 | **LOC:** 780 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.4145%), Tech Debt (10.3775%)
**Top Internal Functions/Classes:**
  * `createRootHooks` (Impact: 249.4)
    * *Intent:* /** * @internal */
  * `useQuery` (Impact: 53.6)
  * `useInfiniteQuery` (Impact: 51.6)
  * `useSubscription` (Impact: 49.4)
    * *Intent:* /* istanbul ignore next -- @preserve */
  * `usePrefetchInfiniteQuery` (Impact: 26.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 161`, `args: 51`, `func_start: 26`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 11`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 23`, `api: 9`, `concurrency: 2`, `import: 18`
* *Defense:* `safety: 75`, `doc: 4`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.739
  * `Choke Point (Betweenness):` 0.000101 | `Ripple Effect (Closeness):` 0.014006
  * `Imports (Out-Degree: 9):` context, getClientArgs, getQueryKey, trpcResult, useQueries, createUtilityFunctions, useQueriesProxy, types...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/tests/server/batching.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 569.25 | **LOC:** 210 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (29.9916%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Concurrency (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 49`, `args: 18`, `func_start: 7`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 2`, `concurrency: 27`, `import: 6`
* *Defense:* `safety: 16`, `test: 27`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` client, testClientResource, server, waitError, superjson, zod
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tests/server/streaming.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 565.04 | **LOC:** 1467 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (43.7549%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `nextIterable` (Impact: 9.8)
  * `nextIterable` (Impact: 8.3)
  * `nextIterable` (Impact: 8.2)
  * `nextIterable` (Impact: 8.2)
  * `nextIterable` (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 33 instances
* *Amplified Cascading Flux:* 20 instances
* *Concurrency (weighted view):* 316
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 323`, `args: 122`, `func_start: 76`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 25`, `duplicate_logic: 36`
* *Architecture:* `io: 13`, `concurrency: 151`, `import: 12`
* *Defense:* `safety: 30`, `test: 76`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` zAsyncIterable, react, client, testClientResource, server, waitError, observable, unstable-core-do-not-import...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tests/server/websockets.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 556.48 | **LOC:** 2227 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (29.8751%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `factory` (Impact: 36.5)
  * `nextIterable` (Impact: 11.1)
  * `onError` (Impact: 6.8)
  * `onopen` (Impact: 4.9)
  * `waitForClientState` (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 338
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 509`, `args: 242`, `func_start: 87`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 21`, `planned_debt: 1`, `duplicate_logic: 15`
* *Architecture:* `io: 8`, `concurrency: 273`, `import: 18`
* *Defense:* `safety: 37`, `doc: 2`, `test: 243`, `immutability_locks: 2`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` react, client, testClientResource, unstable-internals, server, trpcServerResource, waitError, ws...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server/src/unstable-core-do-not-import/stream/utils/mergeAsyncIterables.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 533.76 | **LOC:** 163 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 25 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 151
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 24`, `args: 9`, `func_start: 6`
* *Risk/State:* `state_mutation: 13`
* *Architecture:* `io: 1`, `concurrency: 26`, `import: 3`
* *Defense:* `safety: 7`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` utils, createDeferred, mergeAsyncIterables
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/react-query/src/internals/useQueries.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 481.01 | **LOC:** 216 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.7426%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 80`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 32`
* *Architecture:* `api: 10`, `import: 3`
* *Defense:* `doc: 10`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.467
  * `Choke Point (Betweenness):` 5.4e-05 | `Ripple Effect (Closeness):` 0.014608
  * `Imports (Out-Degree: 1):` shared, react-query, unstable-core-do-not-import
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/tests/server/routerMeta.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 472.09 | **LOC:** 226 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.7012%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 56`, `args: 25`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `concurrency: 20`, `import: 4`
* *Defense:* `test: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` testClientResource, server, observable, unstable-core-do-not-import
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/tests/server/httpSubscriptionLink.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 422.66 | **LOC:** 1640 | **CtrlFlow:** 5.1% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (27.6285%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createContext` (Impact: 15.1)
  * `sleep` (Impact: 14.7)
  * `getCtx` (Impact: 9.1)
  * `getCtxResource` (Impact: 8.1)
    * *Intent:* /** * Test resource */
  * `next` (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 204
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 382`, `args: 170`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 22`, `duplicate_logic: 7`, `unreferenced_by_name: 1`
* *Architecture:* `io: 10`, `concurrency: 134`, `import: 19`
* *Defense:* `safety: 45`, `doc: 1`, `test: 134`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` iterableEventEmitter, zAsyncIterable, client, testClientResource, unstable-internals, server, fakeTimersResource, suppressLogs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server/src/unstable-core-do-not-import/stream/jsonl.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 421.68 | **LOC:** 655 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (44.8311%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `jsonlStreamConsumer` (Impact: 49.4)
    * *Intent:* /** * JSON Lines stream consumer * @see https://jsonlines.org/ */
  * `createBatchStreamProducer` (Impact: 41.0)
  * `decodeChunkDefinition` (Impact: 27.7)
  * `createStreamsManager` (Impact: 12.3)
    * *Intent:* /** * Creates a handler for managing stream controllers and their lifecycle */
  * `encodeAsyncIterable` (Impact: 11.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 154`, `args: 59`, `func_start: 46`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 22`
* *Architecture:* `io: 27`, `api: 13`, `concurrency: 18`, `import: 10`
* *Defense:* `safety: 22`, `doc: 11`, `immutability_locks: 3`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.7
  * `Choke Point (Betweenness):` 0.000394 | `Ripple Effect (Closeness):` 0.099595
  * `Imports (Out-Degree: 6):` utils, asyncIterable, createDeferred, disposable, mergeAsyncIterables, readableStreamFrom, withPing, is-plain-object
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/upgrade/src/transforms/hooksToOptions.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 388.64 | **LOC:** 448 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.1429%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `transform` (Impact: 181.2)
  * `migrateUseUtils` (Impact: 69.3)
    * *Intent:* // Migrate trpc.useUtils() to useQueryClient()
  * `removeSuspenseDestructuring` (Impact: 41.5)
  * `ensureUseTRPCCall` (Impact: 8.2)
  * `replaceHooksWithOptions` (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 26`, `args: 16`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 24`
* *Architecture:* `io: 49`, `api: 2`, `import: 3`
* *Defense:* `safety: 20`, `doc: 4`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00085
  * `Imports (Out-Degree: 2):` modifiers, walkers, jscodeshift
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/server/src/unstable-core-do-not-import/http/resolveResponse.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 379.46 | **LOC:** 776 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (38.7133%), Tech Debt (9.6913%)
**Top Internal Functions/Classes:**
  * `resolveResponse` (Impact: 156.6)
  * `initResponse` (Impact: 38.9)
  * `create` (Impact: 32.5)
  * `formatError` (Impact: 12.6)
  * `formatError` (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 26
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 157`, `args: 31`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 10`, `fragile_debt: 1`
* *Architecture:* `io: 33`, `api: 2`, `concurrency: 24`, `import: 13`
* *Defense:* `safety: 51`, `doc: 8`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.463
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.097626
  * `Imports (Out-Degree: 8):` observable, TRPCError, getErrorShape, procedure, router, rpc, jsonl, sse...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/server/src/adapters/ws.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 379.1 | **LOC:** 645 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (39.0831%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getWSConnectionHandler` (Impact: 89.6)
  * `handleRequest` (Impact: 59.0)
  * `onabort` (Impact: 33.2)
  * `applyWSSHandler` (Impact: 12.7)
  * `getRawInput` (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 86
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 143`, `args: 33`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 17`, `dead_code: 1`
* *Architecture:* `io: 21`, `api: 14`, `concurrency: 21`, `import: 19`
* *Defense:* `safety: 25`, `doc: 13`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.806
  * `Choke Point (Betweenness):` 0.000344 | `Ripple Effect (Closeness):` 0.043222
  * `Imports (Out-Degree: 6):` server, http, rpc, http, observable, unstable-core-do-not-import, asyncIterable, unpromise...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `www/docusaurus.config.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 370.66 | **LOC:** 579 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (29.6104%), Tech Debt (18.158%)
**Top Internal Functions/Classes:**
  * `pluginLlmsTxt` (Impact: 129.8)
    * *Intent:* /** * Thank you to prisma docs for this plugin <3 * https://github.com/prisma/docs/blob/22208d52e416...
  * `postBuild` (Impact: 117.8)
  * `findMdxFilesRecursively` (Impact: 19.7)
    * *Intent:* // Recursive function to find all .md/.mdx files
  * `configurePostCss` (Impact: 3.3)
  * `myPlugin` (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 40`, `args: 11`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 19`, `unreferenced_by_name: 5`
* *Architecture:* `io: 30`, `api: 1`, `concurrency: 13`, `import: 15`
* *Defense:* `safety: 26`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` docusaurus.typedoc.js, mdxToJsx, shikiTwoslash.config, env, preset-classic, types, autoprefixer, cssnano...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server/src/unstable-core-do-not-import/stream/jsonl.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 359.44 | **LOC:** 738 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `[Symbol.asyncIterator]` (Impact: 3.3)
  * `[Symbol.asyncIterator]` (Impact: 3.2)
  * `[Symbol.asyncIterator]` (Impact: 2.3)
  * `serverResourceForStream` (Impact: 2.2)
  * `start` (Impact: 1.6)
    * *Intent:* // Create a ReadableStream that closes immediately with no data
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 33 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 295
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 154`, `args: 54`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 12`, `duplicate_logic: 2`, `unreferenced_by_name: 1`
* *Architecture:* `io: 11`, `concurrency: 130`, `import: 7`
* *Defense:* `safety: 7`, `test: 76`, `immutability_locks: 10`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.441
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` utils, jsonl, createDeferred, disposable, react, fetchServerResource, superjson
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/openapi/test/cyclicTypes.test.ts` -> **Nick Lucas** (100.0% isolated ownership) | Magnitude: 3450.64
- `packages/openapi/test/edgeCases.test.ts` -> **Nick Lucas** (100.0% isolated ownership) | Magnitude: 1912.48
- `packages/openapi/src/generate.ts` -> **Nick Lucas** (100.0% isolated ownership) | Magnitude: 868.64
- `packages/tests/server/routerMeta.test.ts` -> **Alex / KATT** (100.0% isolated ownership) | Magnitude: 472.09
- `www/docusaurus.config.ts` -> **Nick Lucas** (100.0% isolated ownership) | Magnitude: 370.66

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/server/src/observable/observable.ts` -> **Severity: 0.129** (Bridge: 0.0014 * Flux: 92.732%)
- `packages/server/src/adapters/next.ts` -> **Severity: 0.084** (Bridge: 0.0017 * Flux: 50.0%)
- `packages/server/src/unstable-core-do-not-import/stream/jsonl.ts` -> **Severity: 0.034** (Bridge: 0.0004 * Flux: 86.2025%)
- `packages/server/src/unstable-core-do-not-import/stream/sse.ts` -> **Severity: 0.023** (Bridge: 0.0003 * Flux: 78.4685%)
- `packages/server/src/adapters/ws.ts` -> **Severity: 0.022** (Bridge: 0.0003 * Flux: 65.2291%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/server/src/unstable-core-do-not-import/http/formDataToObject.ts` -> **Severity: 9.235** (Embedded: 0.0984 * Error Risk: 93.8527%)
- `packages/server/src/observable/observable.ts` -> **Severity: 8.319** (Embedded: 0.1062 * Error Risk: 78.3372%)
- `packages/server/src/unstable-core-do-not-import/rootConfig.ts` -> **Severity: 7.988** (Embedded: 0.0999 * Error Risk: 80.0%)
- `packages/server/src/unstable-core-do-not-import/transformer.ts` -> **Severity: 7.881** (Embedded: 0.0976 * Error Risk: 80.7279%)
- `packages/server/src/unstable-core-do-not-import/procedureBuilder.ts` -> **Severity: 7.779** (Embedded: 0.1031 * Error Risk: 75.4486%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/server/src/unstable-core-do-not-import/error/TRPCError.ts` -> **Severity: 1682.45** (Blast Radius: 19.228 * Doc Risk: 87.5%)
- `packages/client/src/__tests__/testClientResource.ts` -> **Severity: 1560.4** (Blast Radius: 15.604 * Doc Risk: 100.0%)
- `packages/server/src/observable/observable.ts` -> **Severity: 1214.813** (Blast Radius: 17.67 * Doc Risk: 68.75%)
- `packages/server/src/unstable-core-do-not-import/parser.ts` -> **Severity: 996.2** (Blast Radius: 9.962 * Doc Risk: 100.0%)
- `packages/react-query/test/__reactHelpers.tsx` -> **Severity: 783.8** (Blast Radius: 7.838 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
