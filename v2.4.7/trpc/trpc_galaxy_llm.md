# ARCHITECTURAL_BRIEF: trpc
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/trpc` |
| **Timestamp** | `2026-08-07T04:20:12.876536+00:00` |
| **Scan Duration** | `2.27s` |
| **Git Branch** | `main` |
| **Git Commit** | `1638ac173aac937982afe82075502596c60faa44` |
| **Git Remote** | `https://github.com/trpc/trpc.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 636 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 1573 |
| Analyzed Artifacts (Scanned) | 866 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 707 |
| Total LOC | 41270 |
| Volatility Index | 0.042 |
| % Scanned of codebase = | 55.1% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7017 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.19 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.8346 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 57 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 597 | 36984 | 68.9% |
| MARKDOWN | 70 | 0 | 8.1% |
| JSON | 64 | 2238 | 7.4% |
| PLAINTEXT | 61 | 8 | 7.0% |
| JAVASCRIPT | 26 | 847 | 3.0% |
| XML | 17 | 2 | 2.0% |
| SQLITE | 13 | 61 | 1.5% |
| YAML | 9 | 573 | 1.0% |
| CSS | 6 | 513 | 0.7% |
| HTML | 3 | 44 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.11`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 359 | 41.5% |
| file_cluster_13 | 247 | 28.5% |
| file_cluster_4 | 41 | 4.7% |
| file_cluster_16 | 38 | 4.4% |
| file_cluster_2 | 23 | 2.7% |
| file_cluster_0 | 11 | 1.3% |
| file_cluster_17 | 11 | 1.3% |
| Unknown | 8 | 0.9% |
| file_cluster_1 | 3 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 123 | 14.2% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 707*

**Composition by Extension & Reason:**
- `.ts`: 284x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 202 LOC)
- `.md`: 151x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tsx`: 73x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 55 exceeds 500 chars), 1x Excluded (Saturation: Line 35 exceeds 500 chars)
- `.mdx`: 56x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 60 exceeds 500 chars), 1x Excluded (Saturation: Line 21 exceeds 500 chars)
- `.json`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mdc`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 6x Excluded (Explicitly Denied Extension: '.ico')
- `.toml`: 3x Excluded (Unsupported Extension: '.toml'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1770 LOC), 1x Excluded (Monolithic Amalgamation: 41407 LOC exceeds safe regex boundaries)
- `.prisma`: 3x Excluded (Unsupported Extension: '.prisma')
- `.example`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.snap`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 12.7 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 96.3 | 16.9 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 10.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 3.2 | 0.0 | 0.0 |
| API Exposure | 0.0 | 18.7 | 4.7 | 5.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 25.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 4.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 80.2 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 80.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 10.9 | 0.9 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 79.2 | 2.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 12.5 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 61.3 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `www/src/components/TwitterWall/script.output.ts` (Hits: 88)
- `www/src/components/sponsors/script.output.ts` (Hits: 64)
- `packages/upgrade/src/transforms/hooksToOptions.ts` (Hits: 39)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **unstable-core-do-not-import.ts** (`packages/server/src/unstable-core-do-not-import.ts`) — 81 inbound connections
2. **next.ts** (`packages/server/src/adapters/next.ts`) — 43 inbound connections
3. **observable.ts** (`packages/server/src/observable/observable.ts`) — 42 inbound connections
4. **TRPCClientError.ts** (`packages/client/src/TRPCClientError.ts`) — 14 inbound connections
5. **TRPCError.ts** (`packages/server/src/unstable-core-do-not-import/error/TRPCError.ts`) — 14 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **unstable-core-do-not-import.ts** (`packages/server/src/unstable-core-do-not-import.ts`) — 36 outbound dependencies
2. **index.tsx** (`www/src/pages/index.tsx`) — 24 outbound dependencies
3. **[filter].tsx** (`examples/next-prisma-todomvc/src/pages/[filter].tsx`) — 14 outbound dependencies
4. **createHooksInternal.tsx** (`packages/react-query/src/shared/hooks/createHooksInternal.tsx`) — 14 outbound dependencies
5. **index.ts** (`packages/react-query/src/shared/index.ts`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `resolveResponse` (@ `packages/server/src/unstable-core-do-not-import/http/resolveResponse.ts`) -> Impact: **192.6** | LOC: 526
- `pluginLlmsTxt` (@ `www/docusaurus.config.ts`) -> Impact: **174.6** | LOC: 305
  * *Intent:* /**
- `getWSConnectionHandler` (@ `packages/server/src/adapters/ws.ts`) -> Impact: **125.0** | LOC: 457
  * *Intent:* /** * Enable heartbeat messages * @default false */
- `extractTwoslashBlocks` (@ `www/scripts/check-twoslash.ts`) -> Impact: **123.2** | LOC: 224
- `request` (@ `examples/openapi-codegen/src/client/generated/client/client.gen.ts`) -> Impact: **103.7** | LOC: 168
- `transform` (@ `packages/upgrade/src/transforms/hooksToOptions.ts`) -> Impact: **97.1** | LOC: 242
  * *Intent:* // setMutationDefaults: 'setMutationDefaults', // getMutationDefaults: 'getMutationDefaults', // isMutating: 'isMutating',
- `createStream` (@ `examples/openapi-codegen/src/client/generated/core/serverSentEvents.gen.ts`) -> Impact: **95.3** | LOC: 140
  * *Intent:* /**
- `handleRequest` (@ `packages/server/src/adapters/ws.ts`) -> Impact: **69.4** | LOC: 245
- `unstable_localLink` (@ `packages/client/src/links/localLink.ts`) -> Impact: **67.4** | LOC: 240
  * *Intent:* /**
- `name` (@ `packages/upgrade/src/transforms/hooksToOptions.ts`) -> Impact: **58.6** | LOC: 93

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `examples/next-prisma-websockets-starter` | 14 | 10098.51 | 4.01% | 0.0% |
| `examples/next-prisma-starter` | 12 | 10068.42 | 3.63% | 0.0% |
| `www` | 16 | 5221.58 | 12.4% | 20.36% |
| `__monolith__` | 12 | 5108.28 | 3.7% | 1.26% |
| `examples/next-prisma-todomvc` | 7 | 5036.51 | 4.62% | 0.0% |
| `examples/.experimental/next-app-dir` | 2 | 5001.0 | 0.0% | 0.0% |
| `packages/server/src/unstable-core-do-not-import` | 16 | 125.96 | 7.89% | 16.42% |
| `packages/client/src/links` | 12 | 108.57 | 15.1% | 12.66% |
| `packages/server/src/unstable-core-do-not-import/stream` | 6 | 105.07 | 40.59% | 9.74% |
| `packages/client/src/links/wsLink/wsClient` | 6 | 91.61 | 33.18% | 49.32% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `www/docusaurus.twitterReload.js` -> **100.0%** Exposure
- `packages/client/src/internals/signals.ts` -> **100.0%** Exposure
- `packages/client/src/links/internals/dedupeLink.ts` -> **100.0%** Exposure
- `packages/openapi/tsdown.config.ts` -> **100.0%** Exposure
- `packages/server/src/adapters/wsEncoder.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `examples/next-prisma-websockets-starter/src/pages/api/auth/[...nextauth].ts` -> **100.0%** Exposure
- `packages/client/src/links/wsLink/wsClient/wsClient.ts` -> **100.0%** Exposure
- `packages/client/src/links/wsLink/wsClient/wsConnection.ts` -> **100.0%** Exposure
- `packages/server/src/unstable-core-do-not-import/stream/utils/asyncIterable.ts` -> **100.0%** Exposure
- `packages/server/src/unstable-core-do-not-import/stream/utils/createDeferred.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/client/src/links/localLink.test.ts` -> **1** Orphaned Functions | **41** Duplicates
- `packages/server/src/unstable-core-do-not-import/clientish/serialize.test.ts` -> **0** Orphaned Functions | **29** Duplicates
- `packages/next/src/app-dir/client.test.tsx` -> **0** Orphaned Functions | **26** Duplicates
- `packages/server/src/unstable-core-do-not-import/stream/jsonl.test.ts` -> **0** Orphaned Functions | **22** Duplicates
- `packages/server/src/unstable-core-do-not-import/procedureBuilder.test.ts` -> **1** Orphaned Functions | **20** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`www/docusaurus.config.ts`** -> AI Confidence: **99.39%**
2. **`packages/server/src/unstable-core-do-not-import/http/resolveResponse.ts`** -> AI Confidence: **99.31%**
3. **`www/scripts/check-twoslash.ts`** -> AI Confidence: **99.31%**
4. **`www/src/pages/pricing.tsx`** -> AI Confidence: **99.31%**
5. **`www/src/components/sponsors/script.output.ts`** -> AI Confidence: **99.29%**
6. **`examples/next-sse-chat/src/server/db/migrations/0000_lyrical_khan.sql`** -> AI Confidence: **99.29%**
7. **`examples/next-sse-chat/src/app/channels/[channelId]/chat.tsx`** -> AI Confidence: **99.24%**
8. **`packages/client/src/links/wsLink/wsClient/wsClient.ts`** -> AI Confidence: **99.24%**
9. **`examples/.experimental/next-app-dir/src/server/trpc.ts`** -> AI Confidence: **99.18%**
10. **`examples/.experimental/next-app-dir/src/trpc/rq-client.tsx`** -> AI Confidence: **99.18%**
11. **`examples/next-prisma-websockets-starter/src/utils/trpc.ts`** -> AI Confidence: **99.18%**
12. **`examples/next-sse-chat/src/app/providers.tsx`** -> AI Confidence: **99.18%**
13. **`examples/next-websockets-encoder/src/server/prodServer.ts`** -> AI Confidence: **99.18%**
14. **`packages/client/src/__tests__/testClientResource.ts`** -> AI Confidence: **99.18%**
15. **`packages/client/src/links/httpBatchLink.ts`** -> AI Confidence: **99.18%**
16. **`packages/client/src/links/httpBatchStreamLink.ts`** -> AI Confidence: **99.18%**
17. **`packages/next/src/app-dir/links/nextCache.ts`** -> AI Confidence: **99.18%**
18. **`packages/next/src/withTRPC.tsx`** -> AI Confidence: **99.18%**
19. **`packages/react-query/src/rsc.tsx`** -> AI Confidence: **99.18%**
20. **`packages/react-query/src/shared/hooks/createHooksInternal.tsx`** -> AI Confidence: **99.18%**
21. **`packages/react-query/src/utils/createUtilityFunctions.ts`** -> AI Confidence: **99.18%**
22. **`packages/server/src/adapters/node-http/nodeHTTPRequestHandler.ts`** -> AI Confidence: **99.18%**
23. **`packages/server/src/unstable-core-do-not-import/stream/jsonl.ts`** -> AI Confidence: **99.18%**
24. **`packages/tanstack-react-query/src/internals/subscriptionOptions.ts`** -> AI Confidence: **99.18%**
25. **`packages/client/bin/intent.js`** -> AI Confidence: **99.17%**
26. **`packages/next/bin/intent.js`** -> AI Confidence: **99.17%**
27. **`packages/openapi/bin/intent.js`** -> AI Confidence: **99.17%**
28. **`packages/server/bin/intent.js`** -> AI Confidence: **99.17%**
29. **`packages/tanstack-react-query/bin/intent.js`** -> AI Confidence: **99.17%**
30. **`examples/next-prisma-starter/playwright.config.ts`** -> AI Confidence: **99.17%**
31. **`examples/openapi-codegen/src/client/generated/core/params.gen.ts`** -> AI Confidence: **99.17%**
32. **`examples/openapi-codegen/src/client/generated/core/serverSentEvents.gen.ts`** -> AI Confidence: **99.17%**
33. **`www/src/utils/handleSmoothScrollToSection.ts`** -> AI Confidence: **99.17%**
34. **`examples/next-prisma-todomvc/src/pages/[filter].tsx`** -> AI Confidence: **99.16%**
35. **`packages/next/src/app-dir/create-action-hook.tsx`** -> AI Confidence: **99.16%**
36. **`packages/next/src/app-dir/server.ts`** -> AI Confidence: **99.16%**
37. **`packages/server/src/unstable-core-do-not-import.ts`** -> AI Confidence: **99.16%**
38. **`packages/server/src/unstable-core-do-not-import/router.ts`** -> AI Confidence: **99.16%**
39. **`packages/server/src/unstable-core-do-not-import/stream/sse.ts`** -> AI Confidence: **99.16%**
40. **`packages/client/src/links/httpSubscriptionLink.ts`** -> AI Confidence: **99.15%**
41. **`packages/client/src/links/localLink.ts`** -> AI Confidence: **99.15%**
42. **`packages/next/src/ssrPrepass.ts`** -> AI Confidence: **99.15%**
43. **`packages/openapi/test/scripts/codegen.ts`** -> AI Confidence: **99.15%**
44. **`packages/react-query/src/shared/proxy/utilsProxy.ts`** -> AI Confidence: **99.15%**
45. **`packages/server/src/__tests__/trpcServerResource.ts`** -> AI Confidence: **99.15%**
46. **`packages/server/src/adapters/fastify/fastifyTRPCPlugin.ts`** -> AI Confidence: **99.15%**
47. **`packages/server/src/adapters/next-app-dir/nextAppDirCaller.ts`** -> AI Confidence: **99.15%**
48. **`packages/server/src/unstable-core-do-not-import/initTRPC.ts`** -> AI Confidence: **99.15%**
49. **`packages/server/src/unstable-core-do-not-import/procedureBuilder.ts`** -> AI Confidence: **99.15%**
50. **`packages/server/src/unstable-core-do-not-import/stream/sse.test.ts`** -> AI Confidence: **99.15%**
51. **`packages/tests/server/___testHelpers.ts`** -> AI Confidence: **99.15%**
52. **`examples/openapi-codegen/src/client/generated/client/client.gen.ts`** -> AI Confidence: **99.13%**
53. **`examples/openapi-codegen/src/client/generated/client/utils.gen.ts`** -> AI Confidence: **99.13%**
54. **`packages/openapi/src/generate.ts`** -> AI Confidence: **99.13%**
55. **`packages/server/src/adapters/fetch/fetchRequestHandler.ts`** -> AI Confidence: **99.13%**
56. **`www/og-image/next.config.js`** -> AI Confidence: **99.09%**
57. **`examples/next-sse-chat/src/app/channels/[channelId]/hooks.ts`** -> AI Confidence: **99.09%**
58. **`examples/openapi-codegen/src/client/generated/sdk.gen.ts`** -> AI Confidence: **99.09%**
59. **`packages/client/src/links.ts`** -> AI Confidence: **99.09%**
60. **`packages/react-query/src/shared/index.ts`** -> AI Confidence: **99.09%**
61. **`packages/server/src/adapters/next-app-dir/rethrowNextErrors.ts`** -> AI Confidence: **99.09%**
62. **`packages/upgrade/src/transforms/hooksToOptions.ts`** -> AI Confidence: **99.09%**
63. **`examples/.experimental/next-app-dir/src/app/server-action/ReactHookFormExample.tsx`** -> AI Confidence: **99.08%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `www/docusaurus.config.ts` -> **61.3063%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### 📡 API Network Audit (Set Theory)
- **Shadow APIs (Critical):** `1` undocumented endpoints actively listening.
- **Ghost APIs (Bloat):** `3` endpoints documented but missing from code.
- **Known Shadow Routes:** `GET /`

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1109` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/client/src/links/wsLink/wsClient/wsConnection.ts` (TYPESCRIPT) -> Cumulative Risk: **688.29**
- **Archetype:** `file_cluster_4` (Distance: 13.301 IQR)
- **Magnitude:** 25.67 | **LOC:** 256 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9995%)
- **Heaviest Functions:** `open` (Impact: 18.4), `constructor` (Impact: 11.0), `backwardCompatibility` (Impact: 9.3)

### 2. `packages/client/src/links/wsLink/wsClient/wsClient.ts` (TYPESCRIPT) -> Cumulative Risk: **676.09**
- **Archetype:** `file_cluster_4` (Distance: 13.502 IQR)
- **Magnitude:** 53.05 | **LOC:** 441 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (96.4904%)
- **Heaviest Functions:** `setupWebSocketListeners` (Impact: 34.0), `constructor` (Impact: 23.8), `close` (Impact: 17.5)

### 3. `packages/client/src/links/wsLink/wsClient/utils.ts` (TYPESCRIPT) -> Cumulative Risk: **663.81**
- **Archetype:** `file_cluster_4` (Distance: 13.057 IQR)
- **Magnitude:** 9.97 | **LOC:** 97 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `prepareUrl` (Impact: 10.6), `withResolvers` (Impact: 4.0), `reset` (Impact: 3.8)

### 4. `packages/client/src/links/internals/httpUtils.ts` (TYPESCRIPT) -> Cumulative Risk: **561.81**
- **Archetype:** `file_cluster_13` (Distance: 10.751 IQR)
- **Magnitude:** 13.72 | **LOC:** 244 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (98.1646%), Concurrency (98.1174%), Verification (80.0%)
- **Heaviest Functions:** `GetUrl` (Impact: 20.3), `fetchHTTPResponse` (Impact: 19.5), `throwIfAborted` (Impact: 10.8)

### 5. `packages/server/src/unstable-core-do-not-import/http/contentType.ts` (TYPESCRIPT) -> Cumulative Risk: **552.95**
- **Archetype:** `file_cluster_4` (Distance: 10.562 IQR)
- **Magnitude:** 27.69 | **LOC:** 321 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9999%), Tech Debt (99.0462%), Verification (80.0%)
- **Heaviest Functions:** `parse` (Impact: 58.5), `async` (Impact: 24.3), `getRawInput` (Impact: 22.0)

### 6. `packages/upgrade/src/lib/git.ts` (TYPESCRIPT) -> Cumulative Risk: **527.83**
- **Archetype:** `file_cluster_4` (Distance: 10.923 IQR)
- **Magnitude:** 4.83 | **LOC:** 55 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9999%), Cognitive Load (92.2604%), Tech Debt (86.3872%)
- **Heaviest Functions:** `filterIgnored` (Impact: 19.8), `assertCleanGitTree` (Impact: 5.6)

### 7. `packages/server/src/unstable-core-do-not-import/stream/utils/timerResource.ts` (TYPESCRIPT) -> Cumulative Risk: **527.39**
- **Archetype:** `file_cluster_4` (Distance: 10.415 IQR)
- **Magnitude:** 2.61 | **LOC:** 30 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Cognitive Load (93.7474%), Documentation (82.5715%)
- **Heaviest Functions:** `timerResource` (Impact: 7.2), `start` (Impact: 3.4)

### 8. `www/docusaurus.config.ts` (TYPESCRIPT) -> Cumulative Risk: **516.22**
- **Archetype:** `file_cluster_8` (Distance: 10.633 IQR)
- **Magnitude:** 33.39 | **LOC:** 579 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (88.6012%), Verification (80.0%), Secrets Risk (61.3063%)
- **Heaviest Functions:** `pluginLlmsTxt` (Impact: 174.6), `findMdxFilesRecursively` (Impact: 36.4), `getAllMdxContent` (Impact: 32.4)

### 9. `packages/server/src/unstable-core-do-not-import/stream/utils/asyncIterable.ts` (TYPESCRIPT) -> Cumulative Risk: **507.91**
- **Archetype:** `file_cluster_4` (Distance: 10.551 IQR)
- **Magnitude:** 4.22 | **LOC:** 63 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (79.87%)
- **Heaviest Functions:** `iteratorResource` (Impact: 5.9), `throwAbortError` (Impact: 3.1), `takeWithGrace` (Impact: 1.3)

### 10. `packages/server/src/observable/observable.ts` (TYPESCRIPT) -> Cumulative Risk: **506.25**
- **Archetype:** `file_cluster_4` (Distance: 11.453 IQR)
- **Magnitude:** 21.59 | **LOC:** 207 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Safety Score (59.9154%)
- **Heaviest Functions:** `subscribe` (Impact: 21.5), `subscribe` (Impact: 21.0), `unsubscribe` (Impact: 11.2)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.651
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.651
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.651
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.651
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.651
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.651
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.651
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.651
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/src/links/wsLink/wsClient/wsClient.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.502 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.378 IQR)
- **Top Global Matches:** file_cluster_4: 13.502, file_cluster_13: 13.722, file_cluster_11: 13.985
- **Magnitude:** 53.05 | **LOC:** 441 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (67.4734%), Tech Debt (96.4904%)
**Top Internal Functions/Classes:**
  * `setupWebSocketListeners` (Impact: 34.0)
  * `constructor` (Impact: 23.8)
  * `close` (Impact: 17.5)
  * `handleResponseMessage` (Impact: 15.1)
  * `reconnect` (Impact: 13.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 82`, `args: 37`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 221`, `duplicate_logic: 8`
* *Architecture:* `io: 3`, `api: 6`, `concurrency: 102`, `import: 16`
* *Defense:* `safety: 22`, `doc: 13`, `immutability_locks: 18`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.992
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.00185
  * `Imports (Out-Degree: 7):` subscriptions, observable, types, TRPCClientError, requestManager, utils, server, encoder...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/server/src/adapters/ws.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.947 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.964 IQR)
- **Top Global Matches:** file_cluster_13: 10.947, file_cluster_4: 11.179, file_cluster_8: 11.242
- **Magnitude:** 45.33 | **LOC:** 645 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (27.9224%), Tech Debt (99.4867%)
**Top Internal Functions/Classes:**
  * `getWSConnectionHandler` (Impact: 125.0)
    * *Intent:* /** * Enable heartbeat messages * @default false */
  * `handleRequest` (Impact: 69.4)
  * `run` (Impact: 46.9)
  * `run` (Impact: 24.8)
  * `onabort` (Impact: 24.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 129`, `args: 56`, `func_start: 38`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 22`, `dead_code: 1`, `duplicate_logic: 16`
* *Architecture:* `io: 21`, `api: 12`, `concurrency: 36`, `import: 19`
* *Defense:* `safety: 36`, `doc: 13`, `immutability_locks: 39`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.697
  * `Choke Point (Betweenness):` 0.000394 | `Ripple Effect (Closeness):` 0.01591
  * `Imports (Out-Degree: 4):` server, http, wsEncoder, ws, asyncIterable, http, rpc, unstable-core-do-not-import...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `packages/openapi/src/generate.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.757 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.912 IQR)
- **Top Global Matches:** file_cluster_8: 9.757, file_cluster_17: 10.319, file_cluster_7: 10.384
- **Magnitude:** 41.38 | **LOC:** 1539 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.2009%), Tech Debt (99.9557%)
**Top Internal Functions/Classes:**
  * `extractProcedure` (Impact: 42.9)
  * `recoverProcedureInputType` (Impact: 39.6)
  * `walkType` (Impact: 29.1)
  * `typeToJsonSchema` (Impact: 26.3)
    * *Intent:* /** State extracted from the router's root config. */
  * `getJsDocComment` (Impact: 26.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 126`, `args: 46`, `func_start: 36`, `class_start: 3`
* *Risk/State:* `state_mutation: 24`, `fragile_debt: 1`, `duplicate_logic: 16`
* *Architecture:* `io: 22`, `api: 3`, `concurrency: 3`, `import: 5`
* *Defense:* `safety: 21`, `doc: 8`, `immutability_locks: 93`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.759
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002312
  * `Imports (Out-Degree: 1):` types, schemaExtraction, node:fs, node:path, typescript
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/server/src/unstable-core-do-not-import/http/resolveResponse.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.478 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.07 IQR)
- **Top Global Matches:** file_cluster_17: 11.478, file_cluster_13: 11.517, file_cluster_8: 11.571
- **Magnitude:** 37.88 | **LOC:** 776 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (32.89%), Tech Debt (78.8108%)
**Top Internal Functions/Classes:**
  * `resolveResponse` (Impact: 192.6)
  * `create` (Impact: 13.8)
  * `formatError` (Impact: 12.6)
  * `formatError` (Impact: 12.4)
  * `onError` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 132`, `args: 33`, `func_start: 24`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 25`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 33`, `api: 5`, `concurrency: 34`, `import: 13`
* *Defense:* `safety: 71`, `doc: 10`, `immutability_locks: 75`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.276
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.089049
  * `Imports (Out-Degree: 8):` types, sse, jsonl, TRPCError, rpc, transformer, getHTTPStatusCode, procedure...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `www/src/components/sponsors/SponsorBubbles.jsx` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.12 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 3.086 IQR)
- **Top Global Matches:** file_cluster_8: 8.12, file_cluster_13: 8.57, file_cluster_2: 8.636
- **Magnitude:** 36.18 | **LOC:** 137 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (7.1366%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `SponsorBubbles` (Impact: 14.4)
  * `hierarchy` (Impact: 14.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 14`, `args: 7`, `func_start: 2`, `class_start: 3`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 3`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.694
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001156
  * `Imports (Out-Degree: 0):` script.output, responsive, react, hierarchy, tailwind-merge
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `www/src/utils/env.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.656 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.764 IQR)
- **Top Global Matches:** file_cluster_8: 10.656, file_cluster_13: 10.813, file_cluster_7: 10.993
- **Magnitude:** 35.96 | **LOC:** 59 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.078%), Tech Debt (89.5777%)
**Top Internal Functions/Classes:**
  * `parseEnv` (Impact: 23.0)
    * *Intent:* /**
  * `getOG_URL` (Impact: 11.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 6`, `args: 5`, `func_start: 2`
* *Risk/State:* `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 5`, `api: 1`, `import: 1`
* *Defense:* `doc: 2`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.651
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` zod
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `www/docusaurus.preferredTheme.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.338 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 5.751 IQR)
- **Top Global Matches:** file_cluster_8: 9.338, file_cluster_17: 9.492, file_cluster_2: 9.854
- **Magnitude:** 33.4 | **LOC:** 73 | **CtrlFlow:** 52.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.5899%), Tech Debt (99.8729%)
**Top Internal Functions/Classes:**
  * `onThemeOrClassChanged` (Impact: 7.5)
  * `resolvePreferedTheme` (Impact: 5.4)
  * `colorSchemeChangeListener` (Impact: 5.4)
  * `makeElementVisible` (Impact: 3.9)
  * `makeElementInvisible` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 10`, `args: 8`, `func_start: 11`
* *Risk/State:* `duplicate_logic: 2`
* *Architecture:* `io: 2`, `import: 1`
* *Defense:* `safety: 5`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.651
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ExecutionEnvironment
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `www/mdxToJsx.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.246 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 6.008 IQR)
- **Top Global Matches:** file_cluster_4: 10.246, file_cluster_13: 10.419, file_cluster_8: 10.649
- **Magnitude:** 33.4 | **LOC:** 38 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.8119%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `transform` (Impact: 5.5)
    * *Intent:* // @ts-ignore
  * `remarkHtmlToJsx` (Impact: 5.2)
    * *Intent:* // @ts-check
  * `visit` (Impact: 5.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 13`, `args: 4`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 5`
* *Architecture:* `api: 1`, `concurrency: 11`, `import: 4`
* *Defense:* `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.928
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001156
  * `Imports (Out-Degree: 0):` micromark-extension-mdxjs, mdast-util-mdx, unist-util-visit, mdast-util-from-markdown
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `www/docusaurus.config.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.633 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.373 IQR)
- **Top Global Matches:** file_cluster_8: 10.633, file_cluster_13: 10.88, file_cluster_4: 10.986
- **Magnitude:** 33.39 | **LOC:** 579 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (40.5416%), Tech Debt (31.0999%)
**Top Internal Functions/Classes:**
  * `pluginLlmsTxt` (Impact: 174.6)
    * *Intent:* /**
  * `findMdxFilesRecursively` (Impact: 36.4)
  * `getAllMdxContent` (Impact: 32.4)
  * `myPlugin` (Impact: 4.2)
  * `require` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 37`, `args: 17`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 37`, `duplicate_logic: 2`, `orphaned_logic: 4`
* *Architecture:* `io: 30`, `api: 1`, `concurrency: 28`, `import: 15`
* *Defense:* `safety: 26`, `doc: 2`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.651
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` shikiTwoslash.config, types, docusaurus.typedoc.js, tailwindcss, autoprefixer, fs, env, path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server/src/unstable-core-do-not-import/stream/jsonl.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.192 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.097 IQR)
- **Top Global Matches:** file_cluster_4: 10.192, file_cluster_8: 10.781, file_cluster_13: 10.838
- **Magnitude:** 33.28 | **LOC:** 738 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 15.1)
  * `test` (Impact: 12.1)
  * `test` (Impact: 11.9)
  * `serialize` (Impact: 9.7)
  * `test` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 83`, `args: 65`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 22`, `duplicate_logic: 22`
* *Architecture:* `io: 5`, `concurrency: 179`, `import: 7`
* *Defense:* `safety: 12`, `test: 44`, `immutability_locks: 64`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.651
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` superjson, fetchServerResource, createDeferred, jsonl, react, disposable, utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/server/src/unstable-core-do-not-import/router.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.507 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.722 IQR)
- **Top Global Matches:** file_cluster_16: 10.507, file_cluster_2: 10.534, file_cluster_17: 10.543
- **Magnitude:** 28.95 | **LOC:** 566 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (14.0509%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mergeRouters` (Impact: 33.9)
  * `createRouterFactory` (Impact: 28.1)
  * `createRouterInner` (Impact: 27.8)
  * `createCallerInner` (Impact: 25.1)
  * `createCaller` (Impact: 24.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 115`, `args: 24`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 6`
* *Architecture:* `io: 25`, `api: 17`, `concurrency: 26`, `import: 10`
* *Defense:* `safety: 19`, `doc: 12`, `immutability_locks: 30`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.651
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` types, procedure, TRPCError, procedureBuilder, rootConfig, transformer, createProxy, utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/src/links/localLink.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.324 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.437 IQR)
- **Top Global Matches:** file_cluster_13: 10.324, file_cluster_4: 10.398, file_cluster_8: 10.526
- **Magnitude:** 27.96 | **LOC:** 285 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (32.2324%), Tech Debt (82.7075%)
**Top Internal Functions/Classes:**
  * `unstable_localLink` (Impact: 67.4)
    * *Intent:* /**
  * `observable` (Impact: 53.3)
  * `run` (Impact: 49.0)
  * `onErrorCallback` (Impact: 27.0)
  * `coerceToTRPCClientError` (Impact: 7.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 74`, `args: 22`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`, `duplicate_logic: 4`
* *Architecture:* `io: 6`, `api: 3`, `concurrency: 32`, `import: 11`
* *Defense:* `safety: 14`, `doc: 3`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.821
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.002601
  * `Imports (Out-Degree: 7):` types, TRPCClientError, observable, subscriptions, server, signals, inputWithTrackedEventId, rpc...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/server/src/unstable-core-do-not-import/http/contentType.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_4` (Drift: 10.562 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.896 IQR)
- **Top Global Matches:** file_cluster_4: 10.562, file_cluster_8: 10.767, file_cluster_17: 10.793
- **Magnitude:** 27.69 | **LOC:** 321 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (66.8577%), Tech Debt (99.0462%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 58.5)
  * `async` (Impact: 24.3)
  * `getRawInput` (Impact: 22.0)
  * `memo` (Impact: 19.7)
    * *Intent:* /**
  * `read` (Impact: 15.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 73`, `args: 24`, `func_start: 17`
* *Risk/State:* `state_mutation: 12`, `duplicate_logic: 8`
* *Architecture:* `io: 13`, `api: 3`, `concurrency: 62`, `import: 6`
* *Defense:* `safety: 18`, `doc: 3`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.623
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.089658
  * `Imports (Out-Degree: 3):` types, TRPCError, procedure, parseConnectionParams, router, utils
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `www/vercel.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.505 IQR)
- **Top Global Matches:** file_cluster_8: 4.505, file_cluster_7: 6.29, file_cluster_1: 6.353
- **Magnitude:** 26.68 | **LOC:** 585 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.651
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/upgrade/src/transforms/hooksToOptions.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_17` (Drift: 9.929 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.277 IQR)
- **Top Global Matches:** file_cluster_17: 9.929, file_cluster_8: 10.057, file_cluster_0: 10.327
- **Magnitude:** 26.56 | **LOC:** 448 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.0364%), Tech Debt (97.5909%)
**Top Internal Functions/Classes:**
  * `transform` (Impact: 97.1)
    * *Intent:* // setMutationDefaults: 'setMutationDefaults', // getMutationDefaults: 'getMutationDefaults', // isM...
  * `name` (Impact: 58.6)
  * `migrateUseUtils` (Impact: 51.8)
  * `ensureUseTRPCCall` (Impact: 9.8)
  * `replaceHooksWithOptions` (Impact: 8.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 21`, `args: 26`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 12`, `duplicate_logic: 6`, `orphaned_logic: 1`
* *Architecture:* `io: 39`, `api: 1`, `import: 3`
* *Defense:* `safety: 9`, `doc: 4`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.651
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` jscodeshift, walkers, modifiers
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/client/src/links/wsLink/wsClient/wsConnection.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.301 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.945 IQR)
- **Top Global Matches:** file_cluster_4: 13.301, file_cluster_13: 13.667, file_cluster_8: 13.878
- **Magnitude:** 25.67 | **LOC:** 256 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (54.9817%), Tech Debt (99.9995%)
**Top Internal Functions/Classes:**
  * `open` (Impact: 18.4)
  * `constructor` (Impact: 11.0)
  * `backwardCompatibility` (Impact: 9.3)
  * `close` (Impact: 8.3)
  * `setupPingInterval` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 33`, `args: 33`, `func_start: 24`, `class_start: 3`
* *Risk/State:* `state_mutation: 99`, `duplicate_logic: 10`
* *Architecture:* `api: 12`, `concurrency: 62`, `import: 4`
* *Defense:* `safety: 8`, `doc: 13`, `immutability_locks: 10`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.772
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001927
  * `Imports (Out-Degree: 2):` observable, encoder, utils, urlWithConnectionParams
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/server/src/unstable-core-do-not-import/stream/sse.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.895 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.666 IQR)
- **Top Global Matches:** file_cluster_13: 10.895, file_cluster_2: 10.948, file_cluster_16: 11.057
- **Magnitude:** 25.62 | **LOC:** 455 | **CtrlFlow:** 33.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (25.463%), Tech Debt (58.4411%)
**Top Internal Functions/Classes:**
  * `sseStreamProducer` (Impact: 57.7)
    * *Intent:* /** * End the request immediately after data is sent * Only useful for serverless runtimes that do n...
  * `sseStreamConsumer` (Impact: 29.2)
  * `createStream` (Impact: 20.3)
  * `start` (Impact: 18.3)
  * `generator` (Impact: 11.2)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 107`, `args: 26`, `func_start: 20`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 16`, `duplicate_logic: 4`
* *Architecture:* `io: 1`, `api: 9`, `concurrency: 36`, `import: 13`
* *Defense:* `safety: 21`, `doc: 9`, `immutability_locks: 29`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.748
  * `Choke Point (Betweenness):` 0.000382 | `Ripple Effect (Closeness):` 0.091597
  * `Imports (Out-Degree: 8):` abortError, asyncIterable, readableStreamFrom, types, TRPCError, withPing, timerResource, tracked...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `examples/.experimental/next-app-dir/src/app/api/trpc/[trpc]/route.ts` (TYPESCRIPT) | Magnitude: 0.25 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, import: 3, args: 2
- `www/global.d.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, decorators: 1
- `packages/react-query/src/internals/getQueryKey.ts` (TYPESCRIPT) | Magnitude: 1.93 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 24, indent_spaces: 17, branch: 9, safety_bypasses: 8
- `examples/.test/ssg-infinite-serialization/src/pages/api/trpc/[trpc].ts` (TYPESCRIPT) | Magnitude: 0.39 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, api: 2, import: 2, indent_spaces: 2
- `examples/.test/ssg/src/pages/api/trpc/[trpc].ts` (TYPESCRIPT) | Magnitude: 0.39 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, api: 2, import: 2, indent_spaces: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `eslint.config.js` (JAVASCRIPT) | Magnitude: 6.96 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 185, doc: 46, decorators: 42, events: 29
- `examples/next-prisma-starter/eslint.config.mjs` (JAVASCRIPT) | Magnitude: 17.9 | Delta: **0.411 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, events: 16, doc: 15, decorators: 15
- `examples/next-prisma-websockets-starter/eslint.config.mjs` (JAVASCRIPT) | Magnitude: 17.9 | Delta: **0.411 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, events: 16, doc: 15, decorators: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `examples/express-minimal/src/client.ts` (TYPESCRIPT) | Magnitude: 1.06 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 5, safety: 3, concurrency: 3
- `packages/server/src/unstable-core-do-not-import/rootConfig.ts` (TYPESCRIPT) | Magnitude: 1.96 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 24, indent_spaces: 16, generics: 7, safety_bypasses: 6
- `packages/server/src/observable/behaviorSubject.ts` (TYPESCRIPT) | Magnitude: 3.64 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 21, generics: 15, ui_framework: 13
- `packages/server/src/unstable-core-do-not-import/http/abortError.ts` (TYPESCRIPT) | Magnitude: 0.85 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, api: 4, safety: 3, indent_spaces: 3
- `www/src/theme/DocVersionBanner/index.tsx` (TYPESCRIPT) | Magnitude: 2.7 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 19, branch: 13, immutability_locks: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/client/src/links/wsLink/wsClient/options.ts` (TYPESCRIPT) | Magnitude: 1.19 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 20, doc: 16, branch: 14
- `packages/server/src/unstable-core-do-not-import/transformer.ts` (TYPESCRIPT) | Magnitude: 6.7 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 95, structural_boundaries: 46, generics: 21, args: 18
- `packages/server/src/unstable-core-do-not-import/http/types.ts` (TYPESCRIPT) | Magnitude: 1.47 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 41, indent_spaces: 36, doc: 24, generics: 16
- `packages/openapi/src/types.ts` (TYPESCRIPT) | Magnitude: 4.46 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 67, branch: 45, generics: 37
- `packages/server/src/unstable-core-do-not-import/procedureBuilder.ts` (TYPESCRIPT) | Magnitude: 15.59 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 275, structural_boundaries: 85, generics: 47, branch: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `examples/next-sse-chat/src/app/channels/[channelId]/hooks.ts` (TYPESCRIPT) | Magnitude: 14.2 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 80, branch: 26, structural_boundaries: 21, args: 20
- `packages/server/src/unstable-core-do-not-import/http/resolveResponse.ts` (TYPESCRIPT) | Magnitude: 37.88 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 608, structural_boundaries: 132, branch: 125, immutability_locks: 75
- `www/src/components/TwitterWall/index.tsx` (TYPESCRIPT) | Magnitude: 1.32 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 16, ui_framework: 11, args: 7
- `examples/.experimental/next-app-dir/src/app/client/ClientGreeting.tsx` (TYPESCRIPT) | Magnitude: 0.42 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: dead_code: 3, structural_boundaries: 2, api: 2, args: 1
- `www/src/utils/searchParams.ts` (TYPESCRIPT) | Magnitude: 0.62 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, args: 4, safety: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/react-query/src/shared/hooks/types.ts` (TYPESCRIPT) | Magnitude: 3.98 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 164, structural_boundaries: 102, generics: 83, ui_framework: 72
- `packages/server/src/observable/types.ts` (TYPESCRIPT) | Magnitude: 2.75 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 54, generics: 39, ui_framework: 35, structural_boundaries: 23
- `packages/server/src/adapters/standalone.ts` (TYPESCRIPT) | Magnitude: 1.16 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 12, generics: 7, ui_framework: 6
- `packages/react-query/src/internals/context.tsx` (TYPESCRIPT) | Magnitude: 2.64 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 190, safety: 52, structural_boundaries: 50, generics: 32
- `examples/next-prisma-starter/src/pages/post/[id].tsx` (TYPESCRIPT) | Magnitude: 1.48 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 15, ui_framework: 14, branch: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `examples/express-server/src/client.ts` (TYPESCRIPT) | Magnitude: 3.46 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 22, concurrency: 14, args: 9
- `packages/server/src/unstable-core-do-not-import/stream/utils/readableStreamFrom.test.ts` (TYPESCRIPT) | Magnitude: 3.57 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 33, func_start: 12, immutability_locks: 11, args: 10
- `packages/server/src/__tests__/fetchServerResource.ts` (TYPESCRIPT) | Magnitude: 5.93 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 29, args: 16, concurrency: 16
- `examples/next-prisma-websockets-starter/prisma/seed.ts` (TYPESCRIPT) | Magnitude: 0.82 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 4, args: 4, concurrency: 3
- `packages/server/src/unstable-core-do-not-import/stream/utils/createDeferred.ts` (TYPESCRIPT) | Magnitude: 1.29 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 7, indent_spaces: 7, concurrency: 6, generics: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `www/src/components/CompaniesUsing.script.ts` (TYPESCRIPT) | Magnitude: 1.74 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: io: 9, indent_spaces: 8, immutability_locks: 7, structural_boundaries: 5
- `www/src/utils/handleSmoothScrollToSection.ts` (TYPESCRIPT) | Magnitude: 1.46 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, branch: 6, immutability_locks: 6, structural_boundaries: 2
- `www/src/components/sponsors/TopSponsors.tsx` (TYPESCRIPT) | Magnitude: 0.67 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 9, ui_framework: 9, import: 4
- `examples/openapi-codegen/src/server/index.ts` (TYPESCRIPT) | Magnitude: 2.36 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 17, immutability_locks: 7, concurrency: 6
- `www/scripts/check-twoslash.ts` (TYPESCRIPT) | Magnitude: 17.67 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 192, branch: 60, immutability_locks: 45, state_mutation: 33

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/server/src/adapters/next.ts` -> **Severity: 0.113** (Bridge: 0.0016 * Flux: 71.7751%)
- `packages/server/src/observable/observable.ts` -> **Severity: 0.065** (Bridge: 0.0013 * Flux: 49.1399%)
- `packages/server/src/observable/behaviorSubject.ts` -> **Severity: 0.019** (Bridge: 0.0004 * Flux: 50.9755%)
- `packages/server/src/unstable-core-do-not-import/stream/utils/asyncIterable.ts` -> **Severity: 0.014** (Bridge: 0.0001 * Flux: 100.0%)
- `packages/server/src/__tests__/fetchServerResource.ts` -> **Severity: 0.013** (Bridge: 0.0006 * Flux: 22.1466%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/server/src/unstable-core-do-not-import/rootConfig.ts` -> **Severity: 8.153** (Embedded: 0.0917 * Error Risk: 88.9105%)
- `packages/server/src/unstable-core-do-not-import/procedureBuilder.ts` -> **Severity: 7.671** (Embedded: 0.0959 * Error Risk: 80.0%)
- `packages/server/src/unstable-core-do-not-import/http/formDataToObject.ts` -> **Severity: 7.209** (Embedded: 0.0901 * Error Risk: 80.0%)
- `packages/server/src/unstable-core-do-not-import/http/contentTypeParsers.ts` -> **Severity: 7.154** (Embedded: 0.0894 * Error Risk: 80.0%)
- `packages/server/src/unstable-core-do-not-import/error/formatter.ts` -> **Severity: 6.036** (Embedded: 0.0919 * Error Risk: 65.7143%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/server/src/unstable-core-do-not-import.ts` -> **Severity: 8034.6** (Blast Radius: 80.346 * Doc Risk: 100.0%)
- `packages/server/src/unstable-core-do-not-import/error/TRPCError.ts` -> **Severity: 1877.573** (Blast Radius: 22.93 * Doc Risk: 81.8828%)
- `packages/server/src/@trpc/server/http.ts` -> **Severity: 1448.727** (Blast Radius: 18.438 * Doc Risk: 78.5729%)
- `packages/server/src/unstable-core-do-not-import/procedure.ts` -> **Severity: 1305.7** (Blast Radius: 13.057 * Doc Risk: 100.0%)
- `packages/server/src/unstable-core-do-not-import/parser.ts` -> **Severity: 1244.8** (Blast Radius: 12.448 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
