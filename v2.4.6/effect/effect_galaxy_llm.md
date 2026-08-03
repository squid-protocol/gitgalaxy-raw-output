# ARCHITECTURAL_BRIEF: effect
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/effect` |
| **Timestamp** | `2026-08-03T20:11:18.170285+00:00` |
| **Scan Duration** | `8.08s` |
| **Git Branch** | `main` |
| **Git Commit** | `70ce155cd73a3b4cd723fe955454b5837b428f76` |
| **Git Remote** | `https://github.com/Effect-TS/effect.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1051 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
| Total Artifacts | 2208 |
| Analyzed Artifacts (Scanned) | 1261 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 947 |
| Total LOC | 207432 |
| Volatility Index | 0.007 |
| % Scanned of codebase = | 57.1% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4153 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2504 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8925 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 43 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 1036 | 205649 | 82.2% |
| JSON | 96 | 1260 | 7.6% |
| MARKDOWN | 71 | 0 | 5.6% |
| PLAINTEXT | 38 | 0 | 3.0% |
| JAVASCRIPT | 9 | 304 | 0.7% |
| SHELL | 5 | 78 | 0.4% |
| YAML | 4 | 45 | 0.3% |
| NIX | 1 | 29 | 0.1% |
| HTML | 1 | 67 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.403`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 518 | 41.1% |
| file_cluster_16 | 295 | 23.4% |
| file_cluster_8 | 251 | 19.9% |
| file_cluster_2 | 39 | 3.1% |
| file_cluster_17 | 30 | 2.4% |
| file_cluster_4 | 6 | 0.5% |
| file_cluster_0 | 4 | 0.3% |
| file_cluster_12 | 4 | 0.3% |
| file_cluster_11 | 2 | 0.2% |
| file_cluster_1 | 1 | 0.1% |
| file_cluster_15 | 1 | 0.1% |
| file_cluster_7 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 109 | 8.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 947*

**Composition by Extension & Reason:**
- `.ts`: 731x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 4 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 1757 LOC)
- `.json`: 119x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 4x Unsupported Format (.patch), 1x Excluded (Unsupported Extension: '.patch'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 78 LOC), 1x Excluded (Machine-Generated Source Code Signature: 34 LOC)
- `.toml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 14139 LOC)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.ini`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gz`: 1x Excluded (Explicitly Denied Extension: '.gz')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 9.4 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 26.1 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 18.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 18.9 | 2.3 | 80.0 |
| API Exposure | 0.0 | 15.5 | 6.6 | 7.2 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 8.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 10.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 14.7 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 90.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 31.1 | 4.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 88.0 | 2.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 43.7 | 36.7 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 18.4 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 18.8 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 14.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/cluster/src/SqlMessageStorage.ts` (Hits: 120)
- `packages/effect/src/internal/configProvider.ts` (Hits: 84)
- `packages/sql/src/internal/statement.ts` (Hits: 82)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Layer.ts** (`packages/effect/src/Layer.ts`) — 210 inbound connections
2. **Function.ts** (`packages/effect/src/Function.ts`) — 205 inbound connections
3. **effect.ts** (`packages/effect/src/internal/opCodes/effect.ts`) — 176 inbound connections
4. **Context.ts** (`packages/effect/src/Context.ts`) — 162 inbound connections
5. **Schema.ts** (`packages/effect/src/Schema.ts`) — 145 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`packages/effect/src/index.ts`) — 178 outbound dependencies
2. **fiberRuntime.ts** (`packages/effect/src/internal/fiberRuntime.ts`) — 72 outbound dependencies
3. **Effect.ts** (`packages/effect/src/Effect.ts`) — 68 outbound dependencies
4. **Schema.ts** (`packages/effect/src/Schema.ts`) — 63 outbound dependencies
5. **index.ts** (`packages/platform/src/index.ts`) — 60 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `escapeMermaidLabel` (@ `packages/effect/src/Graph.ts`) -> Impact: **3070.8** | LOC: 1713
  * *Intent:* /** * Reverses all edge directions in a mutable graph by swapping source and target nodes.
- `decodeError` (@ `packages/ai/anthropic/src/Generated.ts`) -> Impact: **2755.5** | LOC: 639
  * *Intent:* /** * Your unique API key for authentication. *
- `go` (@ `packages/effect/src/ParseResult.ts`) -> Impact: **1266.1** | LOC: 709
- `go` (@ `packages/effect/src/JSONSchema.ts`) -> Impact: **1107.1** | LOC: 362
- `describe` (@ `packages/effect/dtslint/Schema/Schema.tst.ts`) -> Impact: **965.4** | LOC: 1295
- `intersectUnionMembers` (@ `packages/effect/src/Schema.ts`) -> Impact: **860.7** | LOC: 134
- `getSystemMessageMode` (@ `packages/ai/openai/src/OpenAiLanguageModel.ts`) -> Impact: **833.8** | LOC: 166
- `pull` (@ `packages/effect/src/internal/stream.ts`) -> Impact: **681.3** | LOC: 154
- `compile` (@ `packages/sql/src/internal/statement.ts`) -> Impact: **640.9** | LOC: 217
- `make` (@ `packages/sql-mssql/src/MssqlClient.ts`) -> Impact: **627.2** | LOC: 305

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `nextDocumentName` (@ `packages/ai/amazon-bedrock/src/AmazonBedrockLanguageModel.ts`) -> **O(2^N) [Recursive]**
- `execute` (@ `packages/cli/src/internal/cliApp.ts`) -> **O(2^N) [Recursive]**
- `parseInternal` (@ `packages/cli/src/internal/commandDescriptor.ts`) -> **O(2^N) [Recursive]**
- `sendLocal` (@ `packages/cluster/src/internal/entityManager.ts`) -> **O(2^N) [Recursive]**
- `intersectUnionMembers` (@ `packages/effect/src/Schema.ts`) -> **O(2^N) [Recursive]**
- `run` (@ `packages/effect/src/internal/channel/channelExecutor.ts`) -> **O(2^N) [Recursive]**
- `fromFlatLoop` (@ `packages/effect/src/internal/configProvider.ts`) -> **O(2^N) [Recursive]**
- `loop` (@ `packages/effect/src/internal/groupBy.ts`) -> **O(2^N) [Recursive]**
- `make` (@ `packages/effect/src/internal/groupBy.ts`) -> **O(2^N) [Recursive]**
- `pipe` (@ `packages/effect/src/internal/keyedPool.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `escapeMermaidLabel` (@ `packages/effect/src/Graph.ts`) -> DB Complexity: **235**
  * *Intent:* /** * Reverses all edge directions in a mutable graph by swapping source and target nodes.
- `table` (@ `packages/cluster/src/SqlMessageStorage.ts`) -> DB Complexity: **135**
- `makeNoop` (@ `packages/platform/src/internal/fileSystem.ts`) -> DB Complexity: **120**
  * *Intent:* /** @internal */
- `compile` (@ `packages/sql/src/internal/statement.ts`) -> DB Complexity: **115**
- `_Value` (@ `packages/effect/src/internal/scopedCache.ts`) -> DB Complexity: **98**
- `go` (@ `packages/effect/src/JSONSchema.ts`) -> DB Complexity: **79**
- `run` (@ `packages/effect/src/internal/channel/channelExecutor.ts`) -> DB Complexity: **77**
- `make` (@ `packages/sql-mysql2/src/MysqlClient.ts`) -> DB Complexity: **70**
- `execute` (@ `packages/sql/src/SqlEventJournal.ts`) -> DB Complexity: **70**
- `make` (@ `packages/sql-clickhouse/src/ClickhouseClient.ts`) -> DB Complexity: **63**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/effect/src` | 177 | 2966.29 | 6.46% | 23.64% |
| `packages/effect/src/internal` | 82 | 2795.99 | 15.1% | 46.29% |
| `packages/platform/src` | 61 | 755.92 | 8.48% | 29.92% |
| `packages/cli/src/internal` | 16 | 706.42 | 8.01% | 20.08% |
| `packages/platform/src/internal` | 29 | 450.12 | 12.65% | 24.74% |
| `packages/effect/src/internal/stm` | 21 | 329.62 | 11.75% | 35.73% |
| `packages/ai/anthropic/src` | 6 | 327.67 | 3.57% | 3.67% |
| `packages/cluster/src` | 39 | 304.69 | 9.44% | 19.13% |
| `packages/experimental/src` | 18 | 275.96 | 8.8% | 20.33% |
| `packages/rpc/src` | 12 | 264.59 | 9.35% | 25.05% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/cli/src/internal/prompt/date.ts` -> **100.0%** Exposure
- `packages/cluster/src/ClusterSchema.ts` -> **100.0%** Exposure
- `packages/effect/benchmark/SchemaArray.ts` -> **100.0%** Exposure
- `packages/effect/benchmark/SchemaTuple.ts` -> **100.0%** Exposure
- `packages/effect/src/Subscribable.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `packages/cluster/src/RunnerAddress.ts` -> **100.0%** Exposure
- `packages/cluster/src/SingletonAddress.ts` -> **100.0%** Exposure
- `packages/effect/src/Scheduler.ts` -> **100.0%** Exposure
- `packages/effect/src/internal/channel/channelExecutor.ts` -> **100.0%** Exposure
- `packages/effect/src/internal/hashMap/array.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/effect/src/internal/stream.ts` -> **0** Orphaned Functions | **122** Duplicates
- `packages/effect/src/internal/core.ts` -> **23** Orphaned Functions | **94** Duplicates
- `packages/effect/src/internal/pubsub.ts` -> **0** Orphaned Functions | **99** Duplicates
- `packages/effect/src/Schema.ts` -> **9** Orphaned Functions | **82** Duplicates
- `packages/effect/src/Micro.ts` -> **0** Orphaned Functions | **90** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/opentelemetry/src/OtlpMetrics.ts`** -> AI Confidence: **99.35%**
2. **`packages/platform/src/internal/path.ts`** -> AI Confidence: **99.34%**
3. **`packages/ai/amazon-bedrock/src/AmazonBedrockLanguageModel.ts`** -> AI Confidence: **99.31%**
4. **`packages/ai/google/src/GoogleLanguageModel.ts`** -> AI Confidence: **99.31%**
5. **`packages/ai/openai/src/OpenAiLanguageModel.ts`** -> AI Confidence: **99.31%**
6. **`packages/ai/openrouter/src/OpenRouterLanguageModel.ts`** -> AI Confidence: **99.31%**
7. **`packages/effect/src/Cron.ts`** -> AI Confidence: **99.31%**
8. **`packages/effect/src/JSONSchema.ts`** -> AI Confidence: **99.31%**
9. **`packages/effect/src/internal/redBlackTree.ts`** -> AI Confidence: **99.31%**
10. **`packages/experimental/src/Sse.ts`** -> AI Confidence: **99.31%**
11. **`packages/opentelemetry/src/Otlp.ts`** -> AI Confidence: **99.31%**
12. **`packages/opentelemetry/src/OtlpLogger.ts`** -> AI Confidence: **99.31%**
13. **`packages/platform/src/Cookies.ts`** -> AI Confidence: **99.31%**
14. **`packages/platform/src/HttpApiScalar.ts`** -> AI Confidence: **99.31%**
15. **`packages/platform/src/internal/httpServerResponse.ts`** -> AI Confidence: **99.31%**
16. **`packages/platform/src/internal/platformConfigProvider.ts`** -> AI Confidence: **99.31%**
17. **`packages/sql-pg/src/PgClient.ts`** -> AI Confidence: **99.31%**
18. **`packages/cli/src/internal/prompt/multi-select.ts`** -> AI Confidence: **99.24%**
19. **`packages/cli/src/internal/prompt/toggle.ts`** -> AI Confidence: **99.24%**
20. **`packages/effect/src/Arbitrary.ts`** -> AI Confidence: **99.24%**
21. **`packages/effect/src/Duration.ts`** -> AI Confidence: **99.24%**
22. **`packages/effect/src/HashRing.ts`** -> AI Confidence: **99.24%**
23. **`packages/effect/src/ParseResult.ts`** -> AI Confidence: **99.24%**
24. **`packages/effect/src/SchemaAST.ts`** -> AI Confidence: **99.24%**
25. **`packages/effect/src/internal/dateTime.ts`** -> AI Confidence: **99.24%**
26. **`packages/effect/src/internal/mailbox.ts`** -> AI Confidence: **99.24%**
27. **`packages/opentelemetry/src/internal/metrics.ts`** -> AI Confidence: **99.24%**
28. **`packages/opentelemetry/src/internal/tracer.ts`** -> AI Confidence: **99.24%**
29. **`packages/platform-bun/src/BunClusterSocket.ts`** -> AI Confidence: **99.24%**
30. **`packages/platform-node/src/NodeClusterHttp.ts`** -> AI Confidence: **99.24%**
31. **`packages/platform-node/src/NodeClusterSocket.ts`** -> AI Confidence: **99.24%**
32. **`packages/platform-node/src/internal/workerRunner.ts`** -> AI Confidence: **99.24%**
33. **`packages/platform/src/Runtime.ts`** -> AI Confidence: **99.24%**
34. **`packages/platform/src/internal/httpPlatform.ts`** -> AI Confidence: **99.24%**
35. **`packages/platform/src/internal/httpServerError.ts`** -> AI Confidence: **99.24%**
36. **`packages/printer/src/internal/layout.ts`** -> AI Confidence: **99.24%**
37. **`packages/rpc/src/RpcClient.ts`** -> AI Confidence: **99.24%**
38. **`packages/rpc/src/RpcServer.ts`** -> AI Confidence: **99.24%**
39. **`packages/sql-mysql2/src/MysqlMigrator.ts`** -> AI Confidence: **99.24%**
40. **`packages/sql/src/internal/statement.ts`** -> AI Confidence: **99.24%**
41. **`packages/effect/src/Graph.ts`** -> AI Confidence: **99.23%**
42. **`packages/effect/src/internal/hashMap/node.ts`** -> AI Confidence: **99.23%**
43. **`packages/vitest/src/utils.ts`** -> AI Confidence: **99.23%**
44. **`packages/ai/ai/src/LanguageModel.ts`** -> AI Confidence: **99.18%**
45. **`packages/ai/ai/src/Prompt.ts`** -> AI Confidence: **99.18%**
46. **`packages/ai/anthropic/src/AnthropicTokenizer.ts`** -> AI Confidence: **99.18%**
47. **`packages/cli/src/Prompt.ts`** -> AI Confidence: **99.18%**
48. **`packages/cli/src/internal/commandDescriptor.ts`** -> AI Confidence: **99.18%**
49. **`packages/cli/src/internal/configFile.ts`** -> AI Confidence: **99.18%**
50. **`packages/cli/src/internal/prompt.ts`** -> AI Confidence: **99.18%**
51. **`packages/cli/src/internal/prompt/date.ts`** -> AI Confidence: **99.18%**
52. **`packages/cli/src/internal/prompt/number.ts`** -> AI Confidence: **99.18%**
53. **`packages/cli/src/internal/prompt/text.ts`** -> AI Confidence: **99.18%**
54. **`packages/cluster/src/ClusterCron.ts`** -> AI Confidence: **99.18%**
55. **`packages/cluster/src/ClusterWorkflowEngine.ts`** -> AI Confidence: **99.18%**
56. **`packages/cluster/src/EntityResource.ts`** -> AI Confidence: **99.18%**
57. **`packages/cluster/src/RunnerHealth.ts`** -> AI Confidence: **99.18%**
58. **`packages/cluster/src/Runners.ts`** -> AI Confidence: **99.18%**
59. **`packages/cluster/src/SingleRunner.ts`** -> AI Confidence: **99.18%**
60. **`packages/cluster/src/SqlMessageStorage.ts`** -> AI Confidence: **99.18%**
61. **`packages/effect/src/Boolean.ts`** -> AI Confidence: **99.18%**
62. **`packages/effect/src/Chunk.ts`** -> AI Confidence: **99.18%**
63. **`packages/effect/src/Effect.ts`** -> AI Confidence: **99.18%**
64. **`packages/effect/src/Either.ts`** -> AI Confidence: **99.18%**
65. **`packages/effect/src/FiberSet.ts`** -> AI Confidence: **99.18%**
66. **`packages/effect/src/List.ts`** -> AI Confidence: **99.18%**
67. **`packages/effect/src/ManagedRuntime.ts`** -> AI Confidence: **99.18%**
68. **`packages/effect/src/Match.ts`** -> AI Confidence: **99.18%**
69. **`packages/effect/src/Micro.ts`** -> AI Confidence: **99.18%**
70. **`packages/effect/src/MutableHashMap.ts`** -> AI Confidence: **99.18%**
71. **`packages/effect/src/Pool.ts`** -> AI Confidence: **99.18%**
72. **`packages/effect/src/Pretty.ts`** -> AI Confidence: **99.18%**
73. **`packages/effect/src/Schema.ts`** -> AI Confidence: **99.18%**
74. **`packages/effect/src/internal/blockedRequests.ts`** -> AI Confidence: **99.18%**
75. **`packages/effect/src/internal/cache.ts`** -> AI Confidence: **99.18%**
76. **`packages/effect/src/internal/channel/singleProducerAsyncInput.ts`** -> AI Confidence: **99.18%**
77. **`packages/effect/src/internal/channel/subexecutor.ts`** -> AI Confidence: **99.18%**
78. **`packages/effect/src/internal/config.ts`** -> AI Confidence: **99.18%**
79. **`packages/effect/src/internal/configProvider.ts`** -> AI Confidence: **99.18%**
80. **`packages/effect/src/internal/configProvider/pathPatch.ts`** -> AI Confidence: **99.18%**
81. **`packages/effect/src/internal/groupBy.ts`** -> AI Confidence: **99.18%**
82. **`packages/effect/src/internal/managedRuntime.ts`** -> AI Confidence: **99.18%**
83. **`packages/effect/src/internal/matcher.ts`** -> AI Confidence: **99.18%**
84. **`packages/effect/src/internal/metric/keyType.ts`** -> AI Confidence: **99.18%**
85. **`packages/effect/src/internal/metric/state.ts`** -> AI Confidence: **99.18%**
86. **`packages/effect/src/internal/pool.ts`** -> AI Confidence: **99.18%**
87. **`packages/effect/src/internal/queue.ts`** -> AI Confidence: **99.18%**
88. **`packages/effect/src/internal/rcMap.ts`** -> AI Confidence: **99.18%**
89. **`packages/effect/src/internal/scopedCache.ts`** -> AI Confidence: **99.18%**
90. **`packages/effect/src/internal/stm/core.ts`** -> AI Confidence: **99.18%**
91. **`packages/effect/src/internal/stream/emit.ts`** -> AI Confidence: **99.18%**
92. **`packages/effect/src/internal/supervisor/patch.ts`** -> AI Confidence: **99.18%**
93. **`packages/experimental/src/DevTools/Client.ts`** -> AI Confidence: **99.18%**
94. **`packages/experimental/src/EventJournal.ts`** -> AI Confidence: **99.18%**
95. **`packages/experimental/src/EventLogRemote.ts`** -> AI Confidence: **99.18%**
96. **`packages/experimental/src/EventLogServer.ts`** -> AI Confidence: **99.18%**
97. **`packages/experimental/src/PersistedQueue.ts`** -> AI Confidence: **99.18%**
98. **`packages/experimental/src/Persistence/Lmdb.ts`** -> AI Confidence: **99.18%**
99. **`packages/experimental/src/Persistence/Redis.ts`** -> AI Confidence: **99.18%**
100. **`packages/opentelemetry/src/Logger.ts`** -> AI Confidence: **99.18%**
101. **`packages/platform-browser/src/Geolocation.ts`** -> AI Confidence: **99.18%**
102. **`packages/platform-browser/src/internal/httpClient.ts`** -> AI Confidence: **99.18%**
103. **`packages/platform-bun/src/internal/workerRunner.ts`** -> AI Confidence: **99.18%**
104. **`packages/platform-node-shared/src/internal/commandExecutor.ts`** -> AI Confidence: **99.18%**
105. **`packages/platform-node-shared/src/internal/fileSystem/parcelWatcher.ts`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `packages/effect/src/String.ts` -> **18.8381%** Exposure
- `packages/effect/src/Number.ts` -> **0.0008%** Exposure
### Exploit Generation Surface
- `packages/ai/ai/src/McpServer.ts` -> **100.0%** Exposure
- `packages/ai/amazon-bedrock/src/AmazonBedrockLanguageModel.ts` -> **100.0%** Exposure
- `packages/ai/anthropic/src/Generated.ts` -> **100.0%** Exposure
- `packages/ai/openai/src/OpenAiLanguageModel.ts` -> **100.0%** Exposure
- `packages/ai/openrouter/src/Generated.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `packages/cluster/src/K8sHttpClient.ts` -> **100.0%** Exposure
- `packages/effect/src/Effect.ts` -> **100.0%** Exposure
- `packages/effect/src/Predicate.ts` -> **100.0%** Exposure
- `packages/experimental/src/Reactivity.ts` -> **100.0%** Exposure
- `packages/platform-bun/src/internal/httpPlatform.ts` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `packages/ai/ai/src/Toolkit.ts` -> **100.0%** Exposure
- `packages/ai/amazon-bedrock/src/AmazonBedrockLanguageModel.ts` -> **100.0%** Exposure
- `packages/ai/openai/src/OpenAiLanguageModel.ts` -> **100.0%** Exposure
- `packages/ai/openai/src/OpenAiTokenizer.ts` -> **100.0%** Exposure
- `packages/cli/src/internal/args.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4211` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/effect/src/internal/fiberRuntime.ts` (TYPESCRIPT) -> Cumulative Risk: **875.08**
- **Archetype:** `file_cluster_17` (Distance: 13.876 IQR)
- **Magnitude:** 234.1 | **LOC:** 3861 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (96.68%)
- **Heaviest Functions:** `f` (Impact: 192.2), `runLoop` (Impact: 108.6), `forkDaemon` (Impact: 48.9)

### 2. `packages/platform-browser/src/internal/httpClient.ts` (TYPESCRIPT) -> Cumulative Risk: **864.23**
- **Archetype:** `file_cluster_13` (Distance: 13.144 IQR)
- **Magnitude:** 36.02 | **LOC:** 325 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `sendBody` (Impact: 36.8), `makeXhr` (Impact: 22.9), `arrayBuffer` (Impact: 22.7)

### 3. `packages/platform-node/src/internal/httpClientUndici.ts` (TYPESCRIPT) -> Cumulative Risk: **859.62**
- **Archetype:** `file_cluster_13` (Distance: 13.214 IQR)
- **Magnitude:** 27.48 | **LOC:** 232 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9844%), Logic Bomb (99.9824%), Algorithmic Dos (99.9808%)
- **Heaviest Functions:** `make` (Impact: 46.3), `text` (Impact: 26.6), `formData` (Impact: 26.6)

### 4. `packages/effect/src/internal/pubsub.ts` (TYPESCRIPT) -> Cumulative Risk: **856.17**
- **Archetype:** `file_cluster_16` (Distance: 14.739 IQR)
- **Magnitude:** 236.72 | **LOC:** 1763 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `unsafeCompleteSubscribers` (Impact: 135.8), `unsafeMakeSubscription` (Impact: 56.5), `take` (Impact: 50.2)

### 5. `packages/cluster/src/MessageStorage.ts` (TYPESCRIPT) -> Cumulative Risk: **845.44**
- **Archetype:** `file_cluster_13` (Distance: 12.444 IQR)
- **Magnitude:** 51.56 | **LOC:** 920 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (94.3238%)
- **Heaviest Functions:** `make` (Impact: 56.8), `unprocessedMessages` (Impact: 49.3), `unprocessedWith` (Impact: 45.4)

### 6. `packages/sql/src/internal/statement.ts` (TYPESCRIPT) -> Cumulative Risk: **828.62**
- **Archetype:** `file_cluster_17` (Distance: 13.167 IQR)
- **Magnitude:** 145.09 | **LOC:** 994 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.4591%)
- **Heaviest Functions:** `compile` (Impact: 640.9), `transformer` (Impact: 105.5), `transformRows` (Impact: 91.6)

### 7. `packages/platform-node-shared/src/internal/stream.ts` (TYPESCRIPT) -> Cumulative Risk: **826.62**
- **Archetype:** `file_cluster_13` (Distance: 12.94 IQR)
- **Magnitude:** 32.21 | **LOC:** 376 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `onError` (Impact: 74.8), `constructor` (Impact: 40.7), `writeEffect` (Impact: 19.4)

### 8. `packages/effect/src/internal/cache.ts` (TYPESCRIPT) -> Cumulative Risk: **825.51**
- **Archetype:** `file_cluster_13` (Distance: 13.447 IQR)
- **Magnitude:** 72.77 | **LOC:** 734 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Concurrency (92.6589%)
- **Heaviest Functions:** `refresh` (Impact: 70.1), `getEither` (Impact: 43.1), `entryStats` (Impact: 42.6)

### 9. `packages/platform-bun/src/internal/httpServer.ts` (TYPESCRIPT) -> Cumulative Risk: **823.48**
- **Archetype:** `file_cluster_13` (Distance: 12.589 IQR)
- **Magnitude:** 52.47 | **LOC:** 479 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `upgrade` (Impact: 160.1), `makeResponse` (Impact: 47.7), `text` (Impact: 28.6)

### 10. `packages/effect/src/internal/effect/circular.ts` (TYPESCRIPT) -> Cumulative Risk: **815.97**
- **Archetype:** `file_cluster_17` (Distance: 13.256 IQR)
- **Magnitude:** 57.49 | **LOC:** 904 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (98.7041%)
- **Heaviest Functions:** `take` (Impact: 45.9), `makeSemaphore` (Impact: 30.5), `fromFiberEffect` (Impact: 28.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `packages/effect/src/internal/stream.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.033 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.816 IQR)
- **Top Global Matches:** file_cluster_16: 13.033, file_cluster_17: 13.243, file_cluster_2: 13.259
- **Magnitude:** 472.12 | **LOC:** 8803 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (5.7444%), Tech Debt (95.9145%)
**Top Internal Functions/Classes:**
  * `pull` (Impact: 681.3 | O(2^N))
  * `pull` (Impact: 478.5 | O(2^N))
  * `flatMap` (Impact: 271.9 | O(2^N) | DB: 10)
  * `next` (Impact: 146.6 | O(2^N) | DB: 2)
  * `merge` (Impact: 124.5 | O(N^3) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 693`, `structural_boundaries: 2918`, `args: 1967`, `func_start: 1018`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 177`, `planned_debt: 1`, `duplicate_logic: 122`
* *Architecture:* `api: 319`, `concurrency: 16`, `import: 62`
* *Defense:* `safety: 734`, `doc: 315`, `immutability_locks: 1135`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Deferred.js, Tuple.js, ringBuffer.js, take.js, sinkEndReason.js, executionPlan.js, MergeDecision.js, Function.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/Graph.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.633 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.735 IQR)
- **Top Global Matches:** file_cluster_13: 12.633, file_cluster_16: 12.643, file_cluster_0: 12.65
- **Magnitude:** 406.3 | **LOC:** 3736 | **CtrlFlow:** 45.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 235
- **Risk Profile:** Cognitive Load (37.5218%), Tech Debt (20.3879%)
**Top Internal Functions/Classes:**
  * `escapeMermaidLabel` (Impact: 3070.8 | O(2^N) | DB: 235)
    * *Intent:* /** * Reverses all edge directions in a mutable graph by swapping source and target nodes.
  * `removeNode` (Impact: 40.1 | O(N^2) | DB: 5)
    * *Intent:* * * const graph = Graph.mutate(Graph.directed<string, number>(), (mutable) => { * Graph.addNode(muta...
  * `neighborsDirected` (Impact: 26.9 | O(N^2) | DB: 1)
    * *Intent:* /** * Updates a single edge's data by applying a transformation function. * * @example
  * `toGraphViz` (Impact: 24.2 | O(N^1) | DB: 4)
    * *Intent:* /** * Creates a new graph with transformed node data using the provided mapping function. * * @examp...
  * `addEdge` (Impact: 23.8 | O(N^1) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 405`, `structural_boundaries: 489`, `args: 151`, `func_start: 106`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 74`, `state_mutation: 521`, `duplicate_logic: 11`
* *Architecture:* `io: 40`, `api: 84`, `import: 37`
* *Defense:* `safety: 53`, `doc: 91`, `immutability_locks: 540`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Types.js, Hash.js, Data.js, Inspectable.js, Function.js, Option.js, Pipeable.js, effect...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/ai/anthropic/src/Generated.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.129 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.346 IQR)
- **Top Global Matches:** file_cluster_16: 12.129, file_cluster_8: 12.168, file_cluster_2: 12.33
- **Magnitude:** 311.64 | **LOC:** 7226 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (5.8151%), Tech Debt (22.0171%)
**Top Internal Functions/Classes:**
  * `decodeError` (Impact: 2755.5 | O(2^N))
    * *Intent:* /** * Your unique API key for authentication. *
  * `default` (Impact: 10.6 | O(2^N))
  * `readonly` (Impact: 8.8 | O(2^N))
  * `unexpectedStatus` (Impact: 8.6 | O(N^3) | DB: 2)
    * *Intent:* /** * Object type. * * For Skill Versions, this is always `"skill_version"`.
  * `default` (Impact: 5.6 | O(N^1))
    * *Intent:* * [{"role": "user", "content": "Hello, Claude"}] * ``` * * Example with multiple conversational turn...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 541`, `structural_boundaries: 926`, `args: 216`, `func_start: 55`, `class_start: 198`
* *Risk/State:* `safety_bypasses: 45`, `duplicate_logic: 16`
* *Architecture:* `io: 29`, `api: 199`, `import: 15`
* *Defense:* `safety: 331`, `doc: 425`, `immutability_locks: 133`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` Data, HttpClientResponse, Effect, Schema, HttpClientRequest, HttpClientError, ParseResult, HttpClient
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/Schema.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.058 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.974 IQR)
- **Top Global Matches:** file_cluster_16: 13.058, file_cluster_2: 13.16, file_cluster_13: 13.296
- **Magnitude:** 310.94 | **LOC:** 10915 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 51
- **Risk Profile:** Cognitive Load (8.7495%), Tech Debt (96.3759%)
**Top Internal Functions/Classes:**
  * `intersectUnionMembers` (Impact: 860.7 | O(2^N) | DB: 51)
  * `go` (Impact: 312.1 | O(N^4) | DB: 46)
  * `TemplateLiteral` (Impact: 113.2 | O(2^N) | DB: 7)
    * *Intent:* /** * @category encoding
  * `TemplateLiteralParser` (Impact: 65.5 | O(2^N) | DB: 9)
    * *Intent:* /** * Tests if a value is a `Schema`. *
  * `defaultValue` (Impact: 64.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 520`, `structural_boundaries: 1675`, `args: 549`, `func_start: 423`, `class_start: 86`
* *Risk/State:* `safety_bypasses: 106`, `state_mutation: 171`, `duplicate_logic: 82`, `orphaned_logic: 9`
* *Architecture:* `io: 41`, `api: 293`, `concurrency: 6`, `import: 82`
* *Defense:* `safety: 236`, `doc: 308`, `immutability_locks: 561`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.291
  * `Choke Point (Betweenness):` 9.5e-05 | `Ripple Effect (Closeness):` 0.133287
  * `Imports (Out-Degree: 2):` Types.js, Simplify<I>, Boolean.js, util.js, 
export interface Class<Self, cause.js, C, DateTime.js...
  * `Imported By (In-Degree: 145):` (Excluded from Brief to save tokens)

### `packages/cli/src/internal/options.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.618 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.743 IQR)
- **Top Global Matches:** file_cluster_16: 11.618, file_cluster_8: 11.723, file_cluster_13: 11.77
- **Magnitude:** 257.41 | **LOC:** 2220 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (7.8797%), Tech Debt (41.8646%)
**Top Internal Functions/Classes:**
  * `parseInternal` (Impact: 596.7 | O(2^N))
  * `parseCommandLine` (Impact: 381.8 | O(N^5) | DB: 11)
  * `wizardInternal` (Impact: 265.1 | O(2^N) | DB: 4)
  * `getHelpInternal` (Impact: 239.6 | O(2^N))
  * `getFishCompletions` (Impact: 118.4 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 299`, `structural_boundaries: 635`, `args: 323`, `func_start: 192`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 46`, `planned_debt: 1`, `duplicate_logic: 11`
* *Architecture:* `io: 10`, `api: 74`, `import: 41`
* *Defense:* `safety: 51`, `doc: 78`, `immutability_locks: 308`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` Options.js, usage.js, Console, Either, list.js, Path, CliConfig.js, Primitive.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/internal/pubsub.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.739 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.701 IQR)
- **Top Global Matches:** file_cluster_16: 14.739, file_cluster_11: 14.758, file_cluster_13: 14.828
- **Magnitude:** 236.72 | **LOC:** 1763 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 49
- **Risk Profile:** Cognitive Load (47.7928%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `unsafeCompleteSubscribers` (Impact: 135.8 | O(2^N) | DB: 15)
  * `unsafeMakeSubscription` (Impact: 56.5 | O(N^2) | DB: 49)
    * *Intent:* /** @internal */
  * `take` (Impact: 50.2 | O(2^N) | DB: 19)
  * `takeRemainderLoop` (Impact: 37.4 | O(2^N))
    * *Intent:* /** @internal */
  * `unsafeStrategyCompletePollers` (Impact: 34.5 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 334`, `args: 249`, `func_start: 200`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 1316`, `duplicate_logic: 99`
* *Architecture:* `api: 26`, `concurrency: 67`, `import: 18`
* *Defense:* `safety: 73`, `doc: 53`, `immutability_locks: 157`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Queue.js, Deferred.js, Number.js, Chunk.js, queue.js, core.js, Function.js, Effectable.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/internal/fiberRuntime.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.876 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.136 IQR)
- **Top Global Matches:** file_cluster_17: 13.876, file_cluster_13: 13.943, file_cluster_16: 13.977
- **Magnitude:** 234.1 | **LOC:** 3861 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 57.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (25.6669%), Tech Debt (96.68%)
**Top Internal Functions/Classes:**
  * `f` (Impact: 192.2 | O(N^6) | DB: 22)
  * `runLoop` (Impact: 108.6 | O(N^4) | DB: 18)
  * `forkDaemon` (Impact: 48.9 | O(N^5))
  * `restore` (Impact: 46.3 | O(N^4))
  * `resume` (Impact: 45.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 581`, `structural_boundaries: 1056`, `args: 662`, `func_start: 326`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 196`, `state_mutation: 602`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 47`
* *Architecture:* `io: 3`, `api: 126`, `concurrency: 32`, `import: 78`
* *Defense:* `safety: 234`, `doc: 89`, `immutability_locks: 509`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` core-effect.js, FiberStatus.js, patch.js, FiberRefs.js, blockedRequests.js, ExecutionStrategy.js, completedRequestMap.js, Function.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/ParseResult.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.1 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.686 IQR)
- **Top Global Matches:** file_cluster_16: 13.1, file_cluster_11: 13.115, file_cluster_17: 13.127
- **Magnitude:** 225.19 | **LOC:** 2031 | **CtrlFlow:** 43.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 53
- **Risk Profile:** Cognitive Load (32.3203%), Tech Debt (76.1067%)
**Top Internal Functions/Classes:**
  * `go` (Impact: 1266.1 | O(N^6) | DB: 53)
  * `getLiterals` (Impact: 116.2 | O(2^N) | DB: 4)
  * `getArrayFormatterIssues` (Impact: 110.1 | O(2^N) | DB: 42)
  * `formatTree` (Impact: 96.1 | O(2^N) | DB: 3)
  * `getFinalTransformation` (Impact: 69.6 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 414`, `structural_boundaries: 534`, `args: 261`, `func_start: 137`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 204`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 14`
* *Architecture:* `io: 20`, `api: 70`, `concurrency: 6`, `import: 20`
* *Defense:* `safety: 114`, `doc: 90`, `immutability_locks: 306`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.998
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.069242
  * `Imports (Out-Degree: 0):` Types.js, Schema.js, Data.js, GlobalValue.js, util.js, Inspectable.js, Exit.js, Function.js...
  * `Imported By (In-Degree: 63):` (Excluded from Brief to save tokens)

### `packages/effect/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 198.06 | **LOC:** 9903 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/internal/channel/channelExecutor.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.564 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.685 IQR)
- **Top Global Matches:** file_cluster_17: 14.564, file_cluster_13: 14.754, file_cluster_11: 14.824
- **Magnitude:** 180.21 | **LOC:** 1201 | **CtrlFlow:** 37.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 77
- **Risk Profile:** Cognitive Load (89.6464%), Tech Debt (15.1277%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 577.2 | O(2^N) | DB: 77)
  * `onFailure` (Impact: 131.7 | O(2^N) | DB: 4)
  * `onEmitted` (Impact: 74.0 | O(2^N) | DB: 6)
  * `runScopedInterpret` (Impact: 63.9 | O(2^N))
  * `performPullFromUpstream` (Impact: 51.3 | O(N^4) | DB: 30)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 248`, `args: 148`, `func_start: 62`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 548`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 9`, `concurrency: 4`, `import: 25`
* *Defense:* `safety: 191`, `doc: 7`, `immutability_locks: 79`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` channel.js, Function.js, Cause.js, continuation.js, UpstreamPullStrategy.js, continuation.js, channelUpstreamPullStrategy.js, channelState.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/SchemaAST.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.473 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.796 IQR)
- **Top Global Matches:** file_cluster_13: 11.473, file_cluster_16: 11.652, file_cluster_17: 11.683
- **Magnitude:** 160.5 | **LOC:** 3048 | **CtrlFlow:** 40.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (12.9911%), Tech Debt (27.4692%)
**Top Internal Functions/Classes:**
  * `pick` (Impact: 141.8 | O(2^N) | DB: 5)
    * *Intent:* /** * @category model * @since 3.10.0
  * `typeAST` (Impact: 136.9 | O(2^N))
    * *Intent:* /**
  * `encodedAST_` (Impact: 133.1 | O(2^N) | DB: 1)
  * `mutable` (Impact: 115.9 | O(2^N))
    * *Intent:* /**
  * `onTransformation` (Impact: 97.5 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 446`, `args: 136`, `func_start: 76`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 78`, `duplicate_logic: 6`
* *Architecture:* `io: 4`, `api: 88`, `import: 28`
* *Defense:* `safety: 12`, `doc: 91`, `immutability_locks: 189`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.735
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.044704
  * `Imports (Out-Degree: 0):` Types.js, ParseResult.js, GlobalValue.js, util.js, RegExp.js, Inspectable.js, Function.js, Equivalence.js...
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `packages/effect/src/Micro.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.759 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.096 IQR)
- **Top Global Matches:** file_cluster_16: 13.759, file_cluster_11: 14.08, file_cluster_13: 14.113
- **Magnitude:** 160.11 | **LOC:** 4406 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (20.6902%), Tech Debt (99.845%)
**Top Internal Functions/Classes:**
  * `withMicroFiber` (Impact: 113.8 | O(N^4) | DB: 9)
  * `runLoop` (Impact: 63.8 | O(2^N) | DB: 7)
    * *Intent:* /** * @since 3.4.6
  * `resume` (Impact: 40.9 | O(N^2) | DB: 3)
  * `suspend` (Impact: 29.3 | O(2^N) | DB: 1)
  * `evaluate` (Impact: 29.0 | O(2^N) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 398`, `structural_boundaries: 1196`, `args: 628`, `func_start: 337`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 173`, `high_risk_execution: 9`, `state_mutation: 319`, `duplicate_logic: 90`
* *Architecture:* `api: 229`, `concurrency: 38`, `import: 29`
* *Defense:* `safety: 313`, `doc: 219`, `immutability_locks: 418`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Types.js, effectable.js, Utils.js, Stream.js, Context.js, Either.js, Pipeable.js, Channel.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/JSONSchema.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.613 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.369 IQR)
- **Top Global Matches:** file_cluster_8: 10.613, file_cluster_13: 10.85, file_cluster_16: 10.914
- **Magnitude:** 156.94 | **LOC:** 1045 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 79
- **Risk Profile:** Cognitive Load (20.9126%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `go` (Impact: 1107.1 | O(N^5) | DB: 79)
  * `isJsonValue` (Impact: 74.3 | O(2^N) | DB: 2)
    * *Intent:* * - `target`: Which spec to target. Possible values are: * - `'jsonSchema7'`: JSON Schema draft-07 (...
  * `getIdentifierAnnotation` (Impact: 42.8 | O(2^N))
  * `compactUnion` (Impact: 37.0 | O(N^2) | DB: 1)
    * *Intent:* // --------------------------------------------- // handle index signatures // ---------------------...
  * `getRef` (Impact: 28.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 270`, `structural_boundaries: 265`, `args: 75`, `func_start: 67`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 24`
* *Architecture:* `io: 28`, `api: 25`, `import: 11`
* *Defense:* `safety: 34`, `doc: 25`, `immutability_locks: 86`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.904
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005714
  * `Imports (Out-Degree: 0):` ParseResult.js, Schema.js, Record.js, Option.js, schemaId.js, Predicate.js, errors.js, Array.js...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/sql/src/internal/statement.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.167 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.037 IQR)
- **Top Global Matches:** file_cluster_17: 13.167, file_cluster_11: 13.182, file_cluster_13: 13.192
- **Magnitude:** 145.09 | **LOC:** 994 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 115
- **Risk Profile:** Cognitive Load (59.8373%), Tech Debt (99.4591%)
**Top Internal Functions/Classes:**
  * `compile` (Impact: 640.9 | O(2^N) | DB: 115)
  * `transformer` (Impact: 105.5 | O(2^N) | DB: 2)
  * `transformRows` (Impact: 91.6 | O(2^N) | DB: 16)
  * `transformRows` (Impact: 67.3 | O(2^N) | DB: 5)
  * `placeholder` (Impact: 36.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 232`, `args: 116`, `func_start: 91`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 237`, `duplicate_logic: 27`
* *Architecture:* `io: 82`, `api: 27`, `import: 13`
* *Defense:* `safety: 75`, `doc: 23`, `immutability_locks: 162`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` SqlConnection.js, Layer, Stream, Option, Function, SqlError.js, Statement.js, Tracer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/cli/src/internal/commandDescriptor.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.297 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.224 IQR)
- **Top Global Matches:** file_cluster_8: 10.297, file_cluster_13: 10.557, file_cluster_16: 10.562
- **Magnitude:** 129.56 | **LOC:** 1409 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (5.4824%), Tech Debt (29.3514%)
**Top Internal Functions/Classes:**
  * `parseInternal` (Impact: 599.0 | O(2^N))
  * `getHelpInternal` (Impact: 187.2 | O(2^N))
    * *Intent:* // ============================================================================= // Internals // ===...
  * `getZshSubcommandCases` (Impact: 148.1 | O(2^N))
  * `wizardInternal` (Impact: 59.8 | O(N^4))
  * `getUsageInternal` (Impact: 41.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 358`, `args: 172`, `func_start: 80`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 1`, `fragile_debt: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 29`, `import: 37`
* *Defense:* `safety: 25`, `doc: 29`, `immutability_locks: 196`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` SynchronizedRef, Options.js, usage.js, Console, Either, Path, CliConfig.js, builtInOptions.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/platform/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 127.5 | **LOC:** 6375 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/platform-node/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 120.24 | **LOC:** 6012 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/ai/openai/src/OpenAiLanguageModel.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.279 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.46 IQR)
- **Top Global Matches:** file_cluster_13: 12.279, file_cluster_0: 12.347, file_cluster_8: 12.424
- **Magnitude:** 117.2 | **LOC:** 1452 | **CtrlFlow:** 56.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (38.4462%), Tech Debt (41.2477%)
**Top Internal Functions/Classes:**
  * `getSystemMessageMode` (Impact: 833.8 | O(2^N) | DB: 20)
  * `catch` (Impact: 18.6 | O(N^6))
  * `prepareInclude` (Impact: 15.2 | O(N^1) | DB: 2)
  * `annotateStreamResponse` (Impact: 14.2 | O(N^2))
  * `annotateResponse` (Impact: 13.9 | O(N^2))
    * *Intent:* // ============================================================================= // Telemetry
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 245`, `args: 45`, `func_start: 32`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 182`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 26`, `import: 26`
* *Defense:* `safety: 82`, `doc: 27`, `immutability_locks: 144`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` utilities.js, Generated.js, Model, LanguageModel, OpenAiTokenizer.js, Function, Tracer, OpenAiTool.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/cli/src/internal/args.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.448 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.124 IQR)
- **Top Global Matches:** file_cluster_16: 11.448, file_cluster_13: 11.583, file_cluster_8: 11.637
- **Magnitude:** 113.02 | **LOC:** 1112 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (4.9539%), Tech Debt (18.8889%)
**Top Internal Functions/Classes:**
  * `validateInternal` (Impact: 230.8 | O(2^N))
  * `wizardInternal` (Impact: 184.1 | O(2^N) | DB: 2)
  * `getHelpInternal` (Impact: 171.5 | O(2^N))
  * `getFishCompletions` (Impact: 91.1 | O(2^N))
    * *Intent:* /** @internal */
  * `getUsageInternal` (Impact: 61.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 386`, `args: 189`, `func_start: 111`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 9`, `duplicate_logic: 4`
* *Architecture:* `io: 12`, `api: 58`, `import: 33`
* *Defense:* `safety: 50`, `doc: 56`, `immutability_locks: 141`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` usage.js, Console, Either, Path, CliConfig.js, Primitive.js, Array, ValidationError.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/internal/redBlackTree.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.144 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.976 IQR)
- **Top Global Matches:** file_cluster_16: 12.144, file_cluster_11: 12.452, file_cluster_13: 12.455
- **Magnitude:** 112.61 | **LOC:** 1246 | **CtrlFlow:** 47.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (21.6457%), Tech Debt (23.5547%)
**Top Internal Functions/Classes:**
  * `fixDoubleBlack` (Impact: 199.4 | O(N^3) | DB: 4)
    * *Intent:* /**
  * `getOrder` (Impact: 165.2 | O(N^3) | DB: 6)
    * *Intent:* /** @internal */
  * `at` (Impact: 60.7 | O(N^3) | DB: 2)
  * `visit` (Impact: 58.6 | O(2^N) | DB: 3)
  * `visit` (Impact: 53.4 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 277`, `args: 141`, `func_start: 53`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 199`, `duplicate_logic: 6`
* *Architecture:* `api: 41`, `import: 15`
* *Defense:* `safety: 43`, `doc: 38`, `immutability_locks: 139`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` RedBlackTree.js, Chunk.js, Inspectable.js, Ordering.js, node.js, stack.js, Order.js, Equal.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/internal/core.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.821 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.433 IQR)
- **Top Global Matches:** file_cluster_16: 12.821, file_cluster_2: 13.178, file_cluster_13: 13.181
- **Magnitude:** 111.84 | **LOC:** 3167 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (7.7123%), Tech Debt (99.9514%)
**Top Internal Functions/Classes:**
  * `callback` (Impact: 38.0 | O(N^2) | DB: 7)
  * `isTimeoutException` (Impact: 25.0 | O(N^2) | DB: 1)
  * `flatMap` (Impact: 17.9 | O(N^3))
  * `flatMap` (Impact: 17.7 | O(N^5))
  * `capture` (Impact: 16.6 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 1360`, `args: 756`, `func_start: 400`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 131`, `duplicate_logic: 94`, `orphaned_logic: 23`
* *Architecture:* `api: 276`, `concurrency: 3`, `import: 52`
* *Defense:* `safety: 231`, `doc: 145`, `immutability_locks: 424`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Deferred.js, FiberStatus.js, blockedRequests.js, ExecutionStrategy.js, Function.js, RequestBlock.js, RuntimeFlagsPatch.js, Either.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/Effect.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.282 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 6.381 IQR)
- **Top Global Matches:** file_cluster_16: 13.282, file_cluster_2: 13.53, file_cluster_13: 13.659
- **Magnitude:** 105.62 | **LOC:** 14816 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (6.8399%), Tech Debt (95.853%)
**Top Internal Functions/Classes:**
  * `make` (Impact: 232.1 | O(2^N) | DB: 6)
  * `f` (Impact: 56.0 | O(N^2))
    * *Intent:* * * const program = Effect.reduce( * [1, 2, 3, 4], * 0, * (acc, id, i) => * processOrder(id) * .pipe...
  * `f` (Impact: 24.7 | O(N^1))
    * *Intent:* * ]) * * Effect.runPromiseExit(program).then(console.log) * // Output: * // Task1 * // { * // _id: '...
  * `body` (Impact: 19.2 | O(2^N))
    * *Intent:* /** * Reduces an `Iterable<A>` using an effectual function `f`, working * sequentially from right to...
  * `f` (Impact: 18.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 508`, `structural_boundaries: 1389`, `args: 591`, `func_start: 265`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 346`, `state_mutation: 41`, `planned_debt: 2`, `duplicate_logic: 38`
* *Architecture:* `api: 207`, `concurrency: 3`, `import: 64`
* *Defense:* `safety: 390`, `doc: 218`, `immutability_locks: 479`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Types.js, Tracer.js, Utils.js, circular.js, cause.js, RequestResolver.js, Clock.js, defaultServices.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/effect/src/internal/core-effect.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.504 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.537 IQR)
- **Top Global Matches:** file_cluster_16: 12.504, file_cluster_17: 12.656, file_cluster_13: 12.827
- **Magnitude:** 104.86 | **LOC:** 2305 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (10.2681%), Tech Debt (93.8721%)
**Top Internal Functions/Classes:**
  * `unsafeMakeSpan` (Impact: 80.4 | O(N^2) | DB: 3)
    * *Intent:* /** @internal */
  * `predicate` (Impact: 44.7 | O(2^N) | DB: 4)
  * `predicate` (Impact: 35.7 | O(2^N) | DB: 4)
  * `tryPromise` (Impact: 34.2 | O(N^2))
  * `fail` (Impact: 30.9 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 242`, `structural_boundaries: 949`, `args: 551`, `func_start: 220`
* *Risk/State:* `safety_bypasses: 95`, `state_mutation: 111`, `duplicate_logic: 42`
* *Architecture:* `api: 148`, `concurrency: 4`, `import: 41`
* *Defense:* `safety: 185`, `doc: 26`, `immutability_locks: 290`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FiberRefs.js, Function.js, Clock.js, RuntimeFlagsPatch.js, Effect.js, FiberRef.js, cause.js, patch.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/platform-bun/CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 104.76 | **LOC:** 5238 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/platform/README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 103.14 | **LOC:** 5157 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.468
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/ai/openai/src/internal/utilities.ts` (TYPESCRIPT) | Magnitude: 1.28 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 10, func_start: 6, immutability_locks: 5
- `packages/ai/ai/src/AiError.ts` (TYPESCRIPT) | Magnitude: 23.52 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 292, structural_boundaries: 144, state_mutation: 81, decorators: 78
- `packages/sql/src/SqlError.ts` (TYPESCRIPT) | Magnitude: 0.82 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 7, doc: 5, api: 4
- `scripts/package-scalar.mjs` (JAVASCRIPT) | Magnitude: 18.68 | Delta: **0.154 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, io: 3, concurrency: 3, decorators: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `eslint.config.mjs` (JAVASCRIPT) | Magnitude: 28.96 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 131, decorators: 30, structural_boundaries: 29, doc: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/effect/src/HashRing.ts` (TYPESCRIPT) | Magnitude: 16.71 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 141, structural_boundaries: 65, state_mutation: 52, immutability_locks: 48
- `packages/effect/src/internal/stm/journal.ts` (TYPESCRIPT) | Magnitude: 10.43 | Delta: **0.161 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 48, immutability_locks: 26, state_mutation: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/ai/openrouter/scripts/generate.sh` (SHELL) | Magnitude: 1.69 | Delta: **0.115 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 12, reflection_metaprogramming: 9, safety: 8, io: 6
- `packages/ai/google/scripts/generate.sh` (SHELL) | Magnitude: 1.89 | Delta: **0.125 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 9, reflection_metaprogramming: 8, io: 6, branch: 5
- `packages/ai/openai/scripts/generate.sh` (SHELL) | Magnitude: 1.48 | Delta: **0.129 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 10, reflection_metaprogramming: 9, safety: 8, io: 6
- `packages/ai/anthropic/scripts/generate.sh` (SHELL) | Magnitude: 1.48 | Delta: **0.218 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 10, io: 8, reflection_metaprogramming: 8, safety: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/platform/src/HttpClientResponse.ts` (TYPESCRIPT) | Magnitude: 2.76 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 66, indent_spaces: 51, immutability_locks: 32, args: 25
- `packages/cluster/src/ShardingConfig.ts` (TYPESCRIPT) | Magnitude: 2.14 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 140, doc: 27, structural_boundaries: 26, immutability_locks: 26
- `packages/experimental/examples/machine.ts` (TYPESCRIPT) | Magnitude: 15.73 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 18, lazy_evaluation: 11, immutability_locks: 10
- `packages/cli/src/Usage.ts` (TYPESCRIPT) | Magnitude: 3.31 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 41, immutability_locks: 24, indent_spaces: 21, doc: 18
- `packages/platform-bun/src/BunClusterSocket.ts` (TYPESCRIPT) | Magnitude: 1.0 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 32, branch: 27, import: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/effect/src/GlobalValue.ts` (TYPESCRIPT) | Magnitude: 1.75 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 8, state_mutation: 6, branch: 4, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/platform/src/MsgPack.ts` (TYPESCRIPT) | Magnitude: 30.3 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 243, structural_boundaries: 68, generics: 68, ui_framework: 52
- `packages/effect/src/internal/schedule.ts` (TYPESCRIPT) | Magnitude: 85.75 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 1578, structural_boundaries: 835, generics: 655, args: 503
- `packages/platform/src/Template.ts` (TYPESCRIPT) | Magnitude: 16.35 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 115, structural_boundaries: 43, branch: 38, state_mutation: 30
- `packages/cluster/src/ClusterError.ts` (TYPESCRIPT) | Magnitude: 3.34 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 40, doc: 24, generics: 20
- `packages/effect/src/TestConfig.ts` (TYPESCRIPT) | Magnitude: 0.56 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: immutability_locks: 10, doc: 8, indent_spaces: 8, structural_boundaries: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/effect/src/internal/cause.ts` (TYPESCRIPT) | Magnitude: 78.43 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 676, structural_boundaries: 319, generics: 237, state_mutation: 200
- `packages/effect/src/internal/pool.ts` (TYPESCRIPT) | Magnitude: 39.83 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 350, state_mutation: 223, structural_boundaries: 149, args: 79
- `packages/effect/dtslint/Chunk.tst.ts` (TYPESCRIPT) | Magnitude: 4.62 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 385, structural_boundaries: 235, func_start: 180, test: 165
- `packages/platform/src/HttpApiClient.ts` (TYPESCRIPT) | Magnitude: 39.27 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 437, structural_boundaries: 150, immutability_locks: 99, generics: 81
- `packages/experimental/src/Persistence.ts` (TYPESCRIPT) | Magnitude: 36.33 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 270, structural_boundaries: 164, args: 76, immutability_locks: 64

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/typeclass/src/data/Duration.ts` (TYPESCRIPT) | Magnitude: 2.25 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 9, doc: 8, api: 7
- `packages/effect/src/Schedule.ts` (TYPESCRIPT) | Magnitude: 11.94 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: generics: 353, ui_framework: 303, indent_spaces: 236, structural_boundaries: 222
- `packages/workflow/src/DurableDeferred.ts` (TYPESCRIPT) | Magnitude: 6.1 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 325, structural_boundaries: 146, generics: 100, immutability_locks: 85
- `packages/effect/src/MetricPolling.ts` (TYPESCRIPT) | Magnitude: 2.64 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 45, generics: 41, ui_framework: 38, structural_boundaries: 33
- `packages/effect/src/internal/differ/orPatch.ts` (TYPESCRIPT) | Magnitude: 4.91 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 193, structural_boundaries: 67, generics: 61, ui_framework: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/cluster/src/internal/resourceRef.ts` (TYPESCRIPT) | Magnitude: 9.22 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 69, state_mutation: 42, structural_boundaries: 32, concurrency: 18
- `packages/platform-node-shared/src/internal/runtime.ts` (TYPESCRIPT) | Magnitude: 2.24 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 6, concurrency: 6, args: 4
- `scripts/package-swagger.mjs` (JAVASCRIPT) | Magnitude: 24.34 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 10, io: 7, concurrency: 7, immutability_locks: 6
- `packages/sql-sqlite-wasm/src/OpfsWorker.ts` (TYPESCRIPT) | Magnitude: 11.35 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 31, concurrency: 18, branch: 17
- `packages/effect/test/utils/latch.ts` (TYPESCRIPT) | Magnitude: 2.24 | Delta: **0.192 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 18, concurrency: 13, func_start: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/effect/src/internal/errors.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `scripts/codemods/ts-fence.ts` (TYPESCRIPT) | Magnitude: 2.55 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 23, branch: 7, structural_boundaries: 7, immutability_locks: 7
- `packages/platform-node/examples/cluster.ts` (TYPESCRIPT) | Magnitude: 2.02 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, lazy_evaluation: 13, structural_boundaries: 8, immutability_locks: 6
- `packages/effect/dtslint/Schema/Schema.tst.ts` (TYPESCRIPT) | Magnitude: 76.78 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 3728, structural_boundaries: 1715, func_start: 1520, test: 1430
- `packages/effect/dtslint/Unify.tst.ts` (TYPESCRIPT) | Magnitude: 3.97 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 262, structural_boundaries: 67, ui_framework: 54, generics: 52
- `packages/effect/src/internal/channel/mergeStrategy.ts` (TYPESCRIPT) | Magnitude: 1.72 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, structural_boundaries: 31, immutability_locks: 17, args: 13

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/ai/anthropic/src/Generated.ts` -> **Maxwell Brown** (100.0% isolated ownership) | Magnitude: 311.64
- `packages/cli/src/internal/options.ts` -> **Cristian Velasquez Ramos** (100.0% isolated ownership) | Magnitude: 257.41
- `packages/effect/src/ParseResult.ts` -> **Giulio Canti** (100.0% isolated ownership) | Magnitude: 225.19
- `packages/effect/src/JSONSchema.ts` -> **Giulio Canti** (100.0% isolated ownership) | Magnitude: 156.94
- `packages/cli/src/internal/commandDescriptor.ts` -> **Cristian Velasquez Ramos** (100.0% isolated ownership) | Magnitude: 129.56

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/platform/src/HttpLayerRouter.ts` -> **Severity: 0.012** (Bridge: 0.0004 * Flux: 26.1364%)
- `packages/experimental/src/Reactivity.ts` -> **Severity: 0.01** (Bridge: 0.0001 * Flux: 85.0002%)
- `packages/platform/src/Error.ts` -> **Severity: 0.008** (Bridge: 0.0001 * Flux: 99.9982%)
- `packages/rpc/src/RpcGroup.ts` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 92.179%)
- `packages/rpc/src/Rpc.ts` -> **Severity: 0.005** (Bridge: 0.0002 * Flux: 32.1783%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/effect/src/Function.ts` -> **Severity: 15.727** (Embedded: 0.1961 * Error Risk: 80.1921%)
- `packages/effect/src/Context.ts` -> **Severity: 13.143** (Embedded: 0.1552 * Error Risk: 84.6836%)
- `packages/effect/src/Schema.ts` -> **Severity: 6.425** (Embedded: 0.1333 * Error Risk: 48.2034%)
- `packages/effect/src/Data.ts` -> **Severity: 3.952** (Embedded: 0.0494 * Error Risk: 80.0%)
- `packages/effect/src/ParseResult.ts` -> **Severity: 3.753** (Embedded: 0.0692 * Error Risk: 54.2013%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/effect/src/internal/opCodes/effect.ts` -> **Severity: 15727.6** (Blast Radius: 157.276 * Doc Risk: 100.0%)
- `packages/effect/src/HKT.ts` -> **Severity: 530.986** (Blast Radius: 9.139 * Doc Risk: 58.1011%)
- `packages/effect/src/Inspectable.ts` -> **Severity: 404.0** (Blast Radius: 4.04 * Doc Risk: 100.0%)
- `packages/effect/src/Function.ts` -> **Severity: 376.038** (Blast Radius: 31.546 * Doc Risk: 11.9203%)
- `packages/effect/src/Layer.ts` -> **Severity: 360.649** (Blast Radius: 24.204 * Doc Risk: 14.9004%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
