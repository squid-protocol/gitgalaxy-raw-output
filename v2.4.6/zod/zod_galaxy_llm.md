# ARCHITECTURAL_BRIEF: zod
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/zod` |
| **Timestamp** | `2026-08-03T20:00:15.024228+00:00` |
| **Scan Duration** | `1.49s` |
| **Git Branch** | `main` |
| **Git Commit** | `c7805073fef5b6b8857307c3d4b3597a70613bc2` |
| **Git Remote** | `https://github.com/colinhacks/zod.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 349 malicious artifacts.

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
| Total Artifacts | 567 |
| Analyzed Artifacts (Scanned) | 385 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 182 |
| Total LOC | 46501 |
| Volatility Index | 0.01 |
| % Scanned of codebase = | 67.9% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.75 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 348 | 46204 | 90.4% |
| JSON | 15 | 263 | 3.9% |
| MARKDOWN | 9 | 0 | 2.3% |
| PLAINTEXT | 8 | 1 | 2.1% |
| YAML | 3 | 11 | 0.8% |
| XML | 1 | 1 | 0.3% |
| JAVASCRIPT | 1 | 21 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.96`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 269 | 69.9% |
| file_cluster_13 | 47 | 12.2% |
| file_cluster_4 | 16 | 4.2% |
| file_cluster_16 | 16 | 4.2% |
| file_cluster_17 | 9 | 2.3% |
| file_cluster_9 | 4 | 1.0% |
| file_cluster_2 | 3 | 0.8% |
| file_cluster_11 | 2 | 0.5% |
| Unknown | 1 | 0.3% |
| file_cluster_0 | 1 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 16 | 4.2% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 182*

**Composition by Extension & Reason:**
- `.tsx`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 27x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mdx`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 13 exceeds 500 chars), 1x Excluded (Saturation: Line 63 exceeds 500 chars)
- `.json`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ai`: 8x Excluded (Explicitly Denied Extension: '.ai')
- `.jpg`: 8x Excluded (Explicitly Denied Extension: '.jpg')
- `.pdf`: 8x Excluded (Explicitly Denied Extension: '.pdf')
- `.svg`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 16.0 | 7.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.4 | 15.2 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 6.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 12.2 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.9 | 2.5 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 21.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 6.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 89.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 8.6 | 1.7 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 8.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 26.7 | 6.2 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 4.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/zod/src/v4/classic/tests/to-json-schema.test.ts` (Hits: 159)
- `packages/zod/src/v4/mini/tests/string.test.ts` (Hits: 53)
- `packages/zod/src/v4/classic/tests/continuability.test.ts` (Hits: 32)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **core.ts** (`packages/zod/src/v4/core/core.ts`) — 7 inbound connections
2. **AGENTS.md** (`AGENTS.md`) — 0 inbound connections
3. **CLAUDE.md** (`CLAUDE.md`) — 0 inbound connections
4. **CODE_OF_CONDUCT.md** (`CODE_OF_CONDUCT.md`) — 0 inbound connections
5. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`packages/zod/src/v4/locales/index.ts`) — 50 outbound dependencies
2. **index.ts** (`packages/zod/src/v4/core/index.ts`) — 16 outbound dependencies
3. **external.ts** (`packages/zod/src/v4/classic/external.ts`) — 12 outbound dependencies
4. **schemas.ts** (`packages/zod/src/v4/core/schemas.ts`) — 12 outbound dependencies
5. **index.ts** (`packages/zod/src/v3/benchmarks/index.ts`) — 9 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `convertBaseSchema` (@ `packages/zod/src/v4/classic/from-json-schema.ts`) -> Impact: **1142.1** | LOC: 394
- `run` (@ `packages/zod/src/v4/core/schemas.ts`) -> Impact: **932.5** | LOC: 1190
  * *Intent:* /** @internal Parses input and runs all checks (refinements). */
- `describe` (@ `packages/zod/src/v4/classic/tests/to-json-schema.test.ts`) -> Impact: **638.0** | LOC: 1761
- `ZodErrorMap` (@ `packages/zod/src/v4/locales/he.ts`) -> Impact: **434.4** | LOC: 236
- `ZodErrorMap` (@ `packages/zod/src/v3/locales/en.ts`) -> Impact: **310.8** | LOC: 119
- `describe` (@ `packages/zod/src/v4/core/tests/locales/he.test.ts`) -> Impact: **226.6** | LOC: 375
- `ZodErrorMap` (@ `packages/zod/src/v4/locales/lt.ts`) -> Impact: **205.5** | LOC: 212
- `mapper` (@ `packages/zod/src/v4/core/errors.ts`) -> Impact: **186.3** | LOC: 46
- `quotelessJson` (@ `packages/zod/src/v3/ZodError.ts`) -> Impact: **159.8** | LOC: 156
- `convertSchema` (@ `packages/zod/src/v4/classic/from-json-schema.ts`) -> Impact: **154.7** | LOC: 80

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `run` (@ `packages/bench/metabench.ts`) -> **O(2^N) [Recursive]**
- `check` (@ `packages/zod/src/v3/types.ts`) -> **O(2^N) [Recursive]**
- `convertBaseSchema` (@ `packages/zod/src/v4/classic/from-json-schema.ts`) -> **O(2^N) [Recursive]**
- `check` (@ `packages/zod/src/v4/classic/schemas.ts`) -> **O(2^N) [Recursive]**
- `mapper` (@ `packages/zod/src/v4/core/errors.ts`) -> **O(2^N) [Recursive]**
- `mapper` (@ `packages/zod/src/v4/core/errors.ts`) -> **O(2^N) [Recursive]**
- `run` (@ `packages/zod/src/v4/core/schemas.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /** @internal Parses input and runs all checks (refinements). */
- `describe` (@ `packages/zod/src/v4/core/tests/locales/be.test.ts`) -> **O(2^N) [Recursive]**
- `describe` (@ `packages/zod/src/v4/core/tests/locales/ru.test.ts`) -> **O(2^N) [Recursive]**
- `check` (@ `packages/zod/src/v4/mini/schemas.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `describe` (@ `packages/zod/src/v4/classic/tests/to-json-schema.test.ts`) -> DB Complexity: **348**
- `test` (@ `packages/zod/src/v4/classic/tests/continuability.test.ts`) -> DB Complexity: **96**
- `test` (@ `packages/zod/src/v4/mini/tests/string.test.ts`) -> DB Complexity: **81**
- `constructor` (@ `packages/zod/src/v3/types.ts`) -> DB Complexity: **49**
- `quotelessJson` (@ `packages/zod/src/v3/ZodError.ts`) -> DB Complexity: **46**
- `test` (@ `packages/zod/src/v4/classic/tests/nested-refine.test.ts`) -> DB Complexity: **42**
- `generate` (@ `packages/tsc/generate.ts`) -> DB Complexity: **39**
  * *Intent:* // Step 4: Write the generated schemas to a file
- `test` (@ `packages/zod/src/v4/classic/tests/refine.test.ts`) -> DB Complexity: **24**
- `test` (@ `packages/zod/src/v4/classic/tests/to-json-schema.test.ts`) -> DB Complexity: **23**
- `test` (@ `packages/zod/src/v4/classic/tests/transform.test.ts`) -> DB Complexity: **22**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 14 | 5082.66 | 1.79% | 0.0% |
| `packages/zod/src/v4/locales` | 51 | 609.32 | 14.09% | 0.0% |
| `packages/zod/src/v4/classic/tests` | 74 | 591.52 | 11.79% | 0.0% |
| `packages/zod/src/v4/core` | 19 | 462.36 | 30.47% | 34.48% |
| `packages/zod/src/v3/tests` | 61 | 298.34 | 17.93% | 0.0% |
| `packages/zod/src/v4/classic` | 10 | 286.23 | 11.88% | 20.33% |
| `packages/bench` | 33 | 112.0 | 22.61% | 24.66% |
| `packages/zod/src/v4/mini` | 7 | 110.46 | 6.92% | 10.34% |
| `packages/zod/src/v3` | 6 | 95.05 | 24.42% | 7.36% |
| `packages/zod/src/v4/mini/tests` | 15 | 78.88 | 11.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/bench/index.ts` -> **100.0%** Exposure
- `packages/bench/property-access.ts` -> **100.0%** Exposure
- `packages/bench/safe.ts` -> **100.0%** Exposure
- `packages/tsc/bench/index.ts` -> **100.0%** Exposure
- `packages/bench/lazy-box.ts` -> **99.9997%** Exposure
### Highest State Flux (Mutation/Volatility)
- `packages/tsc/generate.ts` -> **100.0%** Exposure
- `packages/zod/src/v3/benchmarks/index.ts` -> **100.0%** Exposure
- `packages/zod/src/v4/core/json-schema-generator.ts` -> **100.0%** Exposure
- `packages/zod/src/v4/core/registries.ts` -> **100.0%** Exposure
- `packages/zod/src/v3/benchmarks/object.ts` -> **99.9992%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/zod/src/v4/core/api.ts` -> **98** Orphaned Functions | **3** Duplicates
- `packages/zod/src/v3/tests/primitive.test.ts` -> **0** Orphaned Functions | **71** Duplicates
- `packages/zod/src/v4/classic/tests/index.test.ts` -> **0** Orphaned Functions | **60** Duplicates
- `packages/zod/src/v4/mini/tests/index.test.ts` -> **0** Orphaned Functions | **60** Duplicates
- `packages/zod/src/v4/classic/tests/object.test.ts` -> **0** Orphaned Functions | **51** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`packages/zod/src/v3/tests/firstparty.test.ts`** -> AI Confidence: **99.32%**
2. **`packages/zod/src/v4/classic/tests/firstparty.test.ts`** -> AI Confidence: **99.32%**
3. **`packages/bench/metabench.ts`** -> AI Confidence: **99.31%**
4. **`packages/zod/src/v3/benchmarks/index.ts`** -> AI Confidence: **99.31%**
5. **`packages/zod/src/v3/types.ts`** -> AI Confidence: **99.31%**
6. **`packages/zod/src/v4/locales/index.ts`** -> AI Confidence: **99.31%**
7. **`packages/zod/src/v3/locales/en.ts`** -> AI Confidence: **99.29%**
8. **`packages/zod/src/v4/classic/from-json-schema.ts`** -> AI Confidence: **99.23%**
9. **`packages/zod/src/v4/locales/he.ts`** -> AI Confidence: **99.2%**
10. **`packages/zod/src/v4/classic/schemas.ts`** -> AI Confidence: **99.18%**
11. **`scripts/check-versions.ts`** -> AI Confidence: **99.17%**
12. **`packages/tsc/generate.ts`** -> AI Confidence: **99.13%**
13. **`packages/zod/src/v4/core/json-schema-processors.ts`** -> AI Confidence: **99.13%**
14. **`packages/zod/src/v3/tests/catch.test.ts`** -> AI Confidence: **99.09%**
15. **`packages/zod/src/v4/classic/external.ts`** -> AI Confidence: **99.09%**
16. **`packages/zod/src/v4/core/index.ts`** -> AI Confidence: **99.09%**
17. **`packages/zod/src/v4/core/tests/locales/es.test.ts`** -> AI Confidence: **99.09%**
18. **`packages/zod/src/v4/core/tests/locales/hr.test.ts`** -> AI Confidence: **99.09%**
19. **`packages/zod/src/v4/locales/ar.ts`** -> AI Confidence: **99.09%**
20. **`packages/zod/src/v4/locales/az.ts`** -> AI Confidence: **99.09%**
21. **`packages/zod/src/v4/locales/be.ts`** -> AI Confidence: **99.09%**
22. **`packages/zod/src/v4/locales/bg.ts`** -> AI Confidence: **99.09%**
23. **`packages/zod/src/v4/locales/ca.ts`** -> AI Confidence: **99.09%**
24. **`packages/zod/src/v4/locales/cs.ts`** -> AI Confidence: **99.09%**
25. **`packages/zod/src/v4/locales/da.ts`** -> AI Confidence: **99.09%**
26. **`packages/zod/src/v4/locales/de.ts`** -> AI Confidence: **99.09%**
27. **`packages/zod/src/v4/locales/en.ts`** -> AI Confidence: **99.09%**
28. **`packages/zod/src/v4/locales/eo.ts`** -> AI Confidence: **99.09%**
29. **`packages/zod/src/v4/locales/es.ts`** -> AI Confidence: **99.09%**
30. **`packages/zod/src/v4/locales/fa.ts`** -> AI Confidence: **99.09%**
31. **`packages/zod/src/v4/locales/fi.ts`** -> AI Confidence: **99.09%**
32. **`packages/zod/src/v4/locales/fr-CA.ts`** -> AI Confidence: **99.09%**
33. **`packages/zod/src/v4/locales/fr.ts`** -> AI Confidence: **99.09%**
34. **`packages/zod/src/v4/locales/hr.ts`** -> AI Confidence: **99.09%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `packages/zod/src/v3/ZodError.ts` -> **100.0%** Exposure
- `packages/zod/src/v3/types.ts` -> **100.0%** Exposure
- `packages/zod/src/v4/classic/from-json-schema.ts` -> **100.0%** Exposure
- `packages/zod/src/v4/classic/schemas.ts` -> **100.0%** Exposure
- `packages/zod/src/v4/classic/tests/to-json-schema.test.ts` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `packages/bench/metabench.ts` -> **100.0%** Exposure
- `packages/tsc/generate.ts` -> **100.0%** Exposure
- `packages/zod/src/v3/ZodError.ts` -> **100.0%** Exposure
- `packages/zod/src/v3/types.ts` -> **100.0%** Exposure
- `packages/zod/src/v4/classic/from-json-schema.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `444` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/bench/metabench.ts` (TYPESCRIPT) -> Cumulative Risk: **916.56**
- **Archetype:** `file_cluster_4` (Distance: 12.337 IQR)
- **Magnitude:** 22.54 | **LOC:** 228 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9988%)
- **Heaviest Functions:** `run` (Impact: 70.7), `run` (Impact: 30.9), `metabench` (Impact: 19.8)

### 2. `packages/zod/src/v3/types.ts` (TYPESCRIPT) -> Cumulative Risk: **828.68**
- **Archetype:** `file_cluster_4` (Distance: 13.124 IQR)
- **Magnitude:** 63.3 | **LOC:** 5139 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `check` (Impact: 105.8), `processCreateParams` (Impact: 39.0), `check` (Impact: 24.6)

### 3. `packages/zod/src/v4/classic/schemas.ts` (TYPESCRIPT) -> Cumulative Risk: **756.98**
- **Archetype:** `file_cluster_16` (Distance: 12.194 IQR)
- **Magnitude:** 126.21 | **LOC:** 2410 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Logic Bomb (100.0%), Churn (98.35%)
- **Heaviest Functions:** `slugify` (Impact: 100.7), `exclude` (Impact: 50.2), `parse` (Impact: 35.3)

### 4. `packages/zod/src/v3/ZodError.ts` (TYPESCRIPT) -> Cumulative Risk: **727.81**
- **Archetype:** `file_cluster_16` (Distance: 11.078 IQR)
- **Magnitude:** 24.44 | **LOC:** 331 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `quotelessJson` (Impact: 159.8)

### 5. `packages/zod/src/v4/core/errors.ts` (TYPESCRIPT) -> Cumulative Risk: **713.08**
- **Archetype:** `file_cluster_16` (Distance: 12.088 IQR)
- **Magnitude:** 49.36 | **LOC:** 449 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `mapper` (Impact: 186.3), `mapper` (Impact: 129.8), `toDotPath` (Impact: 33.9)

### 6. `packages/zod/src/v4/core/checks.ts` (TYPESCRIPT) -> Cumulative Risk: **701.76**
- **Archetype:** `file_cluster_11` (Distance: 12.916 IQR)
- **Magnitude:** 47.23 | **LOC:** 1294 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Documentation (96.1943%), Tech Debt (92.6844%)
- **Heaviest Functions:** `check` (Impact: 49.5), `check` (Impact: 26.9), `check` (Impact: 14.3)

### 7. `packages/zod/src/v4/mini/schemas.ts` (TYPESCRIPT) -> Cumulative Risk: **679.77**
- **Archetype:** `file_cluster_16` (Distance: 10.953 IQR)
- **Magnitude:** 95.44 | **LOC:** 1917 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Logic Bomb (100.0%), Churn (90.54%)
- **Heaviest Functions:** `check` (Impact: 28.4), `tuple` (Impact: 20.8), `check` (Impact: 10.9)

### 8. `packages/zod/src/v4/core/schemas.ts` (TYPESCRIPT) -> Cumulative Risk: **675.36**
- **Archetype:** `file_cluster_16` (Distance: 12.5 IQR)
- **Magnitude:** 109.27 | **LOC:** 4557 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 58.8%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `run` (Impact: 932.5)

### 9. `packages/zod/src/v4/core/parse.ts` (TYPESCRIPT) -> Cumulative Risk: **671.59**
- **Archetype:** `file_cluster_4` (Distance: 11.328 IQR)
- **Magnitude:** 21.11 | **LOC:** 196 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `SafeParse` (Impact: 16.3), `Parse` (Impact: 14.5), `ParseAsync` (Impact: 14.4)

### 10. `packages/zod/src/v4/core/json-schema-processors.ts` (TYPESCRIPT) -> Cumulative Risk: **651.83**
- **Archetype:** `file_cluster_8` (Distance: 10.135 IQR)
- **Magnitude:** 61.05 | **LOC:** 668 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 83.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9997%)
- **Heaviest Functions:** `stringProcessor` (Impact: 77.7), `literalProcessor` (Impact: 75.7), `tupleProcessor` (Impact: 63.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/from-json-schema.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.506 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.078 IQR)
- **Top Global Matches:** file_cluster_8: 10.506, file_cluster_13: 10.881, file_cluster_17: 10.883
- **Magnitude:** 139.82 | **LOC:** 644 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (39.9575%), Tech Debt (13.0519%)
**Top Internal Functions/Classes:**
  * `convertBaseSchema` (Impact: 1142.1 | O(2^N) | DB: 12)
  * `convertSchema` (Impact: 154.7 | O(2^N) | DB: 4)
  * `fromJSONSchema` (Impact: 18.3 | O(N^1))
    * *Intent:* /**
  * `resolveRef` (Impact: 13.3 | O(N^1) | DB: 12)
  * `detectVersion` (Impact: 12.9 | O(N^1) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 66`, `args: 13`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 46`, `planned_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 7`, `api: 1`, `import: 6`
* *Defense:* `safety: 21`, `doc: 1`, `test: 1`, `immutability_locks: 59`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` schemas.js, json-schema.js, registries.js, checks.js, iso.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/schemas.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.194 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.23 IQR)
- **Top Global Matches:** file_cluster_16: 12.194, file_cluster_2: 12.483, file_cluster_8: 12.568
- **Magnitude:** 126.21 | **LOC:** 2410 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (5.8032%), Tech Debt (90.5242%)
**Top Internal Functions/Classes:**
  * `slugify` (Impact: 100.7 | O(2^N))
  * `exclude` (Impact: 50.2 | O(2^N))
  * `parse` (Impact: 35.3 | O(N^2) | DB: 2)
  * `check` (Impact: 28.5 | O(2^N))
  * `apply` (Impact: 22.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 291`, `structural_boundaries: 1027`, `args: 531`, `func_start: 479`, `class_start: 81`
* *Risk/State:* `safety_bypasses: 116`, `state_mutation: 14`, `dead_code: 5`, `duplicate_logic: 36`
* *Architecture:* `io: 3`, `api: 278`, `concurrency: 23`, `import: 8`
* *Defense:* `safety: 88`, `doc: 112`, `test: 1`, `immutability_locks: 137`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` standard-schema.js, to-json-schema.js, parse.js, index.js, checks.js, iso.js, json-schema-processors.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/schemas.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.5 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.641 IQR)
- **Top Global Matches:** file_cluster_16: 12.5, file_cluster_11: 12.593, file_cluster_13: 12.723
- **Magnitude:** 109.27 | **LOC:** 4557 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 58.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (11.3154%), Tech Debt (9.1779%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 932.5 | O(2^N) | DB: 18)
    * *Intent:* /** @internal Parses input and runs all checks (refinements). */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 534`, `args: 109`, `func_start: 42`, `class_start: 61`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 27`, `dead_code: 9`, `planned_debt: 4`
* *Architecture:* `io: 3`, `api: 91`, `concurrency: 23`, `import: 12`
* *Defense:* `safety: 76`, `doc: 24`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.js, to-json-schema.js, json-schema.js, doc.js, versions.js, parse.js, api.js, regexes.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/mini/schemas.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.953 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.363 IQR)
- **Top Global Matches:** file_cluster_16: 10.953, file_cluster_8: 11.282, file_cluster_2: 11.295
- **Magnitude:** 95.44 | **LOC:** 1917 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (7.4591%), Tech Debt (72.3643%)
**Top Internal Functions/Classes:**
  * `check` (Impact: 28.4 | O(2^N))
  * `tuple` (Impact: 20.8 | O(2^N))
  * `check` (Impact: 10.9 | O(N^2) | DB: 7)
  * `object` (Impact: 10.6 | O(2^N))
    * *Intent:* // @__NO_SIDE_EFFECTS__
  * `string` (Impact: 9.9 | O(2^N))
    * *Intent:* // @__NO_SIDE_EFFECTS__
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 797`, `args: 209`, `func_start: 150`, `class_start: 74`
* *Risk/State:* `safety_bypasses: 104`, `state_mutation: 4`, `dead_code: 4`, `duplicate_logic: 20`
* *Architecture:* `io: 2`, `api: 303`, `concurrency: 5`, `import: 3`
* *Defense:* `safety: 60`, `doc: 8`, `immutability_locks: 117`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, parse.js, util.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/to-json-schema.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.417 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.192 IQR)
- **Top Global Matches:** file_cluster_8: 10.417, file_cluster_7: 11.137, file_cluster_1: 11.318
- **Magnitude:** 87.98 | **LOC:** 2991 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 348
- **Risk Profile:** Cognitive Load (7.4505%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 638.0 | O(N^4) | DB: 348)
  * `test` (Impact: 45.5 | O(N^3) | DB: 6)
  * `test` (Impact: 9.5 | O(N^1) | DB: 18)
  * `test` (Impact: 8.0 | O(N^4) | DB: 23)
  * `test` (Impact: 6.9 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 436`, `args: 291`, `func_start: 278`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 11`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 25`
* *Architecture:* `io: 159`, `concurrency: 3`, `import: 3`
* *Defense:* `safety: 134`, `doc: 1`, `test: 267`, `immutability_locks: 144`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` core, openapi-schema-validator, zod, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/api.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.456 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.196 IQR)
- **Top Global Matches:** file_cluster_16: 10.456, file_cluster_8: 10.618, file_cluster_13: 10.905
- **Magnitude:** 84.94 | **LOC:** 1799 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (8.5136%), Tech Debt (99.2634%)
**Top Internal Functions/Classes:**
  * `_superRefine` (Impact: 37.4 | O(N^2) | DB: 2)
  * `transform` (Impact: 21.7 | O(N^2) | DB: 2)
  * `reverseTransform` (Impact: 13.3 | O(N^2))
  * `describe` (Impact: 12.6 | O(2^N) | DB: 1)
  * `meta` (Impact: 12.6 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 736`, `args: 138`, `func_start: 132`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 24`, `dead_code: 8`, `duplicate_logic: 3`, `orphaned_logic: 98`
* *Architecture:* `io: 1`, `api: 250`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 42`, `doc: 11`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.js, schemas.js, errors.js, checks.js, core.js, registries.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/types.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.124 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.259 IQR)
- **Top Global Matches:** file_cluster_4: 13.124, file_cluster_11: 13.349, file_cluster_13: 13.398
- **Magnitude:** 63.3 | **LOC:** 5139 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 49
- **Risk Profile:** Cognitive Load (98.0947%), Tech Debt (44.1472%)
**Top Internal Functions/Classes:**
  * `check` (Impact: 105.8 | O(2^N) | DB: 1)
  * `processCreateParams` (Impact: 39.0 | O(N^1))
  * `check` (Impact: 24.6 | O(2^N) | DB: 1)
  * `safeParse` (Impact: 21.6 | O(N^2) | DB: 14)
  * `safeParseAsync` (Impact: 16.6 | O(N^2) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 170`, `args: 63`, `func_start: 63`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 181`, `duplicate_logic: 4`, `orphaned_logic: 3`
* *Architecture:* `io: 19`, `api: 20`, `concurrency: 103`, `import: 9`
* *Defense:* `safety: 45`, `doc: 1`, `test: 1`, `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` errorUtil.js, partialUtil.js, typeAliases.js, util.js, parseUtil.js, ZodError.js, enumUtil.js, standard-schema.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/json-schema-processors.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.135 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.752 IQR)
- **Top Global Matches:** file_cluster_8: 10.135, file_cluster_13: 10.538, file_cluster_17: 10.553
- **Magnitude:** 61.05 | **LOC:** 668 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(N^3) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (26.0371%), Tech Debt (16.6107%)
**Top Internal Functions/Classes:**
  * `stringProcessor` (Impact: 77.7 | O(N^3))
    * *Intent:* // ==================== SIMPLE TYPE PROCESSORS ====================
  * `literalProcessor` (Impact: 75.7 | O(N^2) | DB: 2)
  * `tupleProcessor` (Impact: 63.1 | O(N^2) | DB: 13)
  * `numberProcessor` (Impact: 53.4 | O(N^1))
  * `recordProcessor` (Impact: 42.6 | O(N^2) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 143`, `args: 70`, `func_start: 58`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 12`, `duplicate_logic: 2`
* *Architecture:* `io: 22`, `api: 43`, `import: 6`
* *Defense:* `safety: 15`, `immutability_locks: 128`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.js, schemas.js, json-schema.js, checks.js, to-json-schema.js, registries.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/errors.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.088 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.974 IQR)
- **Top Global Matches:** file_cluster_16: 12.088, file_cluster_11: 12.183, file_cluster_13: 12.265
- **Magnitude:** 49.36 | **LOC:** 449 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (38.6148%), Tech Debt (43.1807%)
**Top Internal Functions/Classes:**
  * `mapper` (Impact: 186.3 | O(2^N) | DB: 22)
  * `mapper` (Impact: 129.8 | O(2^N) | DB: 16)
  * `toDotPath` (Impact: 33.9 | O(N^1) | DB: 15)
    * *Intent:* /** Format a ZodError as a human-readable string in the following form.
  * `mapper` (Impact: 20.6 | O(2^N) | DB: 14)
  * `prettifyError` (Impact: 16.7 | O(N^1) | DB: 15)
    * *Intent:* * * ```ts * ZodError { * issues: [ * { * expected: 'string', * code: 'invalid_type', * path: [ 'user...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 139`, `args: 25`, `func_start: 27`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 54`, `dead_code: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 22`, `api: 43`, `import: 5`
* *Defense:* `safety: 27`, `doc: 6`, `immutability_locks: 81`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.js, schemas.js, standard-schema.js, checks.js, core.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/checks.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_11` (Drift: 12.916 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.482 IQR)
- **Top Global Matches:** file_cluster_11: 12.916, file_cluster_16: 13.087, file_cluster_0: 13.148
- **Magnitude:** 47.23 | **LOC:** 1294 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (24.1148%), Tech Debt (92.6844%)
**Top Internal Functions/Classes:**
  * `check` (Impact: 49.5 | O(N^3) | DB: 5)
  * `check` (Impact: 26.9 | O(2^N) | DB: 1)
  * `check` (Impact: 14.3 | O(N^2) | DB: 2)
  * `check` (Impact: 13.7 | O(N^2) | DB: 1)
  * `check` (Impact: 13.7 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 352`, `args: 71`, `func_start: 23`, `class_start: 66`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 127`, `dead_code: 15`, `duplicate_logic: 18`
* *Architecture:* `api: 93`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 40`, `doc: 3`, `immutability_locks: 78`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.js, schemas.js, regexes.js, errors.js, core.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/locales/he.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.57 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.091 IQR)
- **Top Global Matches:** file_cluster_8: 10.57, file_cluster_13: 11.239, file_cluster_7: 11.335
- **Magnitude:** 44.03 | **LOC:** 247 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (22.4868%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ZodErrorMap` (Impact: 434.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 49`, `args: 10`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 42`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.js, checks.js, errors.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/locales/en.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.468 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 2.795 IQR)
- **Top Global Matches:** file_cluster_8: 7.468, file_cluster_7: 8.371, file_cluster_13: 8.39
- **Magnitude:** 31.72 | **LOC:** 125 | **CtrlFlow:** 82.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (24.7738%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ZodErrorMap` (Impact: 310.8 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 19`, `args: 1`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ZodError.js, util.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/firstparty.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.541 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.293 IQR)
- **Top Global Matches:** file_cluster_8: 8.541, file_cluster_7: 9.467, file_cluster_13: 9.528
- **Magnitude:** 30.49 | **LOC:** 180 | **CtrlFlow:** 92.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (29.5836%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 151.6 | O(N^1))
  * `test` (Impact: 149.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 13`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 2`
* *Architecture:* `import: 3`
* *Defense:* `safety: 11`, `test: 2`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` core, v4, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/util.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.683 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 6.247 IQR)
- **Top Global Matches:** file_cluster_16: 11.683, file_cluster_17: 11.971, file_cluster_11: 12.044
- **Magnitude:** 28.55 | **LOC:** 979 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 56.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (25.9675%), Tech Debt (97.4762%)
**Top Internal Functions/Classes:**
  * `floatSafeRemainder` (Impact: 18.1 | O(N^1) | DB: 1)
  * `defineLazy` (Impact: 11.3 | O(N^2) | DB: 1)
  * `value` (Impact: 10.8 | O(2^N))
  * `isPlainObject` (Impact: 10.8 | O(N^1))
  * `void` (Impact: 6.7 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 264`, `args: 55`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 27`, `orphaned_logic: 24`
* *Architecture:* `io: 3`, `api: 93`, `concurrency: 9`, `import: 5`
* *Defense:* `safety: 35`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checks.js, errors.js, core.js, schemas.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/tests/error.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.777 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.072 IQR)
- **Top Global Matches:** file_cluster_8: 12.777, file_cluster_0: 13.136, file_cluster_17: 13.163
- **Magnitude:** 26.68 | **LOC:** 552 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (11.9142%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 43.6 | O(N^1))
  * `test` (Impact: 35.0 | O(N^1))
  * `test` (Impact: 9.5 | O(N^1))
  * `ZodErrorMap` (Impact: 9.2 | O(N^1))
  * `test` (Impact: 8.4 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 76`, `args: 146`, `func_start: 133`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `dead_code: 4`, `planned_debt: 1`, `duplicate_logic: 29`
* *Architecture:* `io: 8`, `import: 4`
* *Defense:* `safety: 103`, `test: 126`, `immutability_locks: 65`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v3, ZodError.js, vitest, util.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/tests/async-parsing.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.203 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.613 IQR)
- **Top Global Matches:** file_cluster_4: 12.203, file_cluster_8: 12.633, file_cluster_17: 12.893
- **Magnitude:** 26.6 | **LOC:** 389 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 13.9 | O(N^2))
  * `test` (Impact: 9.4 | O(N^1))
  * `test` (Impact: 6.6 | O(N^2) | DB: 1)
  * `test` (Impact: 5.9 | O(N^1))
  * `test` (Impact: 5.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 85`, `args: 76`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`, `dead_code: 5`, `fragile_debt: 7`, `duplicate_logic: 24`
* *Architecture:* `concurrency: 111`, `import: 2`
* *Defense:* `safety: 20`, `test: 102`, `immutability_locks: 110`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v3, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/index.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.726 IQR)
- **Local Micro-Species:** `Cluster 6: Async Testing & Verification` (Drift: 6.666 IQR)
- **Top Global Matches:** file_cluster_17: 13.726, file_cluster_8: 13.756, file_cluster_0: 14.021
- **Magnitude:** 25.88 | **LOC:** 940 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (12.3166%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 16.4 | O(N^1))
  * `test` (Impact: 15.4 | O(N^2) | DB: 2)
  * `test` (Impact: 12.3 | O(N^1) | DB: 1)
  * `test` (Impact: 11.0 | O(N^1))
  * `test` (Impact: 8.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 320`, `args: 365`, `func_start: 376`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 12`, `dead_code: 4`, `duplicate_logic: 60`
* *Architecture:* `io: 5`, `concurrency: 22`, `import: 3`
* *Defense:* `safety: 318`, `test: 342`, `immutability_locks: 117`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` core, v4, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/mini/tests/index.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.789 IQR)
- **Local Micro-Species:** `Cluster 6: Async Testing & Verification` (Drift: 6.672 IQR)
- **Top Global Matches:** file_cluster_17: 13.789, file_cluster_8: 13.805, file_cluster_0: 14.071
- **Magnitude:** 25.51 | **LOC:** 964 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (12.0871%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 16.4 | O(N^1))
  * `test` (Impact: 15.4 | O(N^2) | DB: 2)
  * `test` (Impact: 11.0 | O(N^1))
  * `test` (Impact: 10.8 | O(N^1) | DB: 1)
  * `test` (Impact: 8.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 313`, `args: 365`, `func_start: 374`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 12`, `dead_code: 4`, `duplicate_logic: 60`
* *Architecture:* `io: 5`, `concurrency: 22`, `import: 3`
* *Defense:* `safety: 341`, `test: 340`, `immutability_locks: 119`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` mini, core, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/ZodError.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.078 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.267 IQR)
- **Top Global Matches:** file_cluster_16: 11.078, file_cluster_11: 11.159, file_cluster_13: 11.266
- **Magnitude:** 24.44 | **LOC:** 331 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (28.7517%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `quotelessJson` (Impact: 159.8 | O(N^3) | DB: 46)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 119`, `args: 26`, `func_start: 23`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 46`, `dead_code: 1`
* *Architecture:* `io: 9`, `api: 33`, `import: 3`
* *Defense:* `safety: 8`, `test: 1`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, typeAliases.js, util.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/async-parsing.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.76 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.859 IQR)
- **Top Global Matches:** file_cluster_4: 12.76, file_cluster_8: 13.268, file_cluster_17: 13.403
- **Magnitude:** 24.07 | **LOC:** 382 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 14.2 | O(N^4))
  * `test` (Impact: 6.6 | O(N^2) | DB: 1)
  * `test` (Impact: 5.9 | O(N^1))
  * `test` (Impact: 5.8 | O(N^1))
  * `test` (Impact: 5.8 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 81`, `args: 78`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1`, `dead_code: 6`, `fragile_debt: 6`, `duplicate_logic: 23`
* *Architecture:* `concurrency: 106`, `import: 2`
* *Defense:* `safety: 21`, `test: 97`, `immutability_locks: 102`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` v4, vitest
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/tests/locales/he.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.997 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.906 IQR)
- **Top Global Matches:** file_cluster_8: 10.997, file_cluster_7: 11.716, file_cluster_13: 11.746
- **Magnitude:** 23.94 | **LOC:** 380 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (6.6646%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 226.6 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 65`, `args: 137`, `func_start: 122`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`
* *Architecture:* `import: 3`
* *Defense:* `safety: 28`, `test: 121`, `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` index.js, vitest, he.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/bench/metabench.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.337 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.257 IQR)
- **Top Global Matches:** file_cluster_4: 12.337, file_cluster_11: 12.599, file_cluster_13: 12.604
- **Magnitude:** 22.54 | **LOC:** 228 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (87.4077%), Tech Debt (80.3174%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 70.7 | O(2^N) | DB: 5)
  * `run` (Impact: 30.9 | O(2^N) | DB: 7)
  * `metabench` (Impact: 19.8 | O(N^1) | DB: 1)
  * `run` (Impact: 10.8 | O(2^N) | DB: 2)
  * `_bench` (Impact: 3.3 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 36`, `args: 19`, `func_start: 10`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 48`, `dead_code: 2`, `duplicate_logic: 3`
* *Architecture:* `api: 5`, `concurrency: 32`, `import: 6`
* *Defense:* `safety: 7`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` chalk, mitata, benchmark, benchUtil.js, index.js, console-table-printer, tinybench
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/locales/lt.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.518 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.452 IQR)
- **Top Global Matches:** file_cluster_8: 9.518, file_cluster_13: 10.31, file_cluster_7: 10.362
- **Magnitude:** 22.39 | **LOC:** 240 | **CtrlFlow:** 66.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (13.2823%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ZodErrorMap` (Impact: 205.5 | O(N^2))
  * `getUnitTypeFromNumber` (Impact: 10.4 | O(N^1))
  * `capitalizeFirstCharacter` (Impact: 2.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 39`, `args: 9`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 25`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.js, checks.js, errors.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/parse.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.328 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.217 IQR)
- **Top Global Matches:** file_cluster_4: 11.328, file_cluster_16: 11.711, file_cluster_11: 11.88
- **Magnitude:** 21.11 | **LOC:** 196 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (98.1139%)
**Top Internal Functions/Classes:**
  * `SafeParse` (Impact: 16.3 | O(N^2))
  * `Parse` (Impact: 14.5 | O(N^1))
  * `ParseAsync` (Impact: 14.4 | O(N^1) | DB: 1)
  * `SafeParseAsync` (Impact: 11.0 | O(N^2) | DB: 1)
  * `Parse` (Impact: 5.2 | O(N^1))
    * *Intent:* /////////// METHODS ///////////
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 133`, `args: 52`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 6`, `duplicate_logic: 4`
* *Architecture:* `api: 37`, `concurrency: 76`, `import: 4`
* *Defense:* `safety: 11`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.js, errors.js, core.js, schemas.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/zod/src/v4/core/json-schema.ts` (TYPESCRIPT) | Magnitude: 2.8 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 79, branch: 64, structural_boundaries: 38, generics: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/zod/src/v4/core/core.ts` (TYPESCRIPT) | Magnitude: 8.16 | Delta: **0.122 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 55, branch: 29, generics: 25
- `packages/zod/src/v4/core/checks.ts` (TYPESCRIPT) | Magnitude: 47.23 | Delta: **0.171 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 705, structural_boundaries: 352, generics: 141, branch: 139

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/treeshake/example.ts` (TYPESCRIPT) | Magnitude: 1.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, safety: 1, decorators: 1
- `packages/zod/src/v4/core/regexes.ts` (TYPESCRIPT) | Magnitude: 10.97 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 147, structural_boundaries: 74, immutability_locks: 65, api: 61
- `packages/zod/src/v3/tests/masking.test.ts` (TYPESCRIPT) | Magnitude: 0.35 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, test: 1
- `packages/treeshake/valibot-boolean.ts` (TYPESCRIPT) | Magnitude: 1.16 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, safety: 1, import: 1, debug_prints: 1
- `packages/treeshake/zod-mini-string.ts` (TYPESCRIPT) | Magnitude: 1.16 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, safety: 1, import: 1, debug_prints: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/zod/src/v3/tests/branded.test.ts` (TYPESCRIPT) | Magnitude: 0.48 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 12, generics: 11, immutability_locks: 7
- `packages/zod/src/v4/core/standard-schema.ts` (TYPESCRIPT) | Magnitude: 4.66 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 75, indent_spaces: 63, generics: 52, doc: 45
- `packages/zod/src/v3/ZodError.ts` (TYPESCRIPT) | Magnitude: 24.44 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 218, structural_boundaries: 119, generics: 51, state_mutation: 46
- `packages/zod/src/v4/classic/compat.ts` (TYPESCRIPT) | Magnitude: 1.6 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 26, structural_boundaries: 25, indent_spaces: 24, api: 11
- `packages/zod/src/v4/core/schemas.ts` (TYPESCRIPT) | Magnitude: 109.27 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 756, structural_boundaries: 534, generics: 265, branch: 136

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/zod/src/v4/core/zsf.ts` (TYPESCRIPT) | Magnitude: 3.46 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 83, indent_spaces: 45, dead_code: 39, generics: 24
- `packages/zod/src/v4/mini/tests/index.test.ts` (TYPESCRIPT) | Magnitude: 25.51 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 642, func_start: 374, args: 365, safety: 341
- `packages/zod/src/v4/classic/tests/index.test.ts` (TYPESCRIPT) | Magnitude: 25.88 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 631, func_start: 376, args: 365, test: 342
- `packages/zod/src/v4/classic/tests/readonly.test.ts` (TYPESCRIPT) | Magnitude: 7.59 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 147, immutability_locks: 112, func_start: 74, safety: 48
- `packages/zod/src/v3/tests/generics.test.ts` (TYPESCRIPT) | Magnitude: 0.79 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 10, safety: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/zod/src/v3/standard-schema.ts` (TYPESCRIPT) | Magnitude: 2.87 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 27, doc: 23, generics: 18
- `packages/zod/src/v4/classic/tests/brand.test.ts` (TYPESCRIPT) | Magnitude: 2.16 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 53, func_start: 28, structural_boundaries: 26, generics: 24
- `packages/zod/src/v4/mini/tests/brand.test.ts` (TYPESCRIPT) | Magnitude: 1.74 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 48, func_start: 24, structural_boundaries: 23, generics: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/zod/src/v3/tests/tuple.test.ts` (TYPESCRIPT) | Magnitude: 3.12 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 24, args: 21, func_start: 19
- `packages/bench/union.ts` (TYPESCRIPT) | Magnitude: 2.35 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 11, concurrency: 6, immutability_locks: 6
- `packages/zod/src/v3/tests/readonly.test.ts` (TYPESCRIPT) | Magnitude: 5.18 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 92, immutability_locks: 43, concurrency: 36, safety: 35
- `packages/zod/src/v3/tests/function.test.ts` (TYPESCRIPT) | Magnitude: 13.6 | Delta: **0.17 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 171, structural_boundaries: 72, args: 69, concurrency: 47
- `packages/zod/src/v3/tests/async-refinements.test.ts` (TYPESCRIPT) | Magnitude: 4.07 | Delta: **0.179 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 31, concurrency: 26, indent_spaces: 22, args: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `packages/zod/src/v3/tests/complex.test.ts` (TYPESCRIPT) | Magnitude: 0.62 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, args: 13, func_start: 12, structural_boundaries: 11
- `packages/treeshake/zod-locales.ts` (TYPESCRIPT) | Magnitude: 1.16 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 1, safety: 1, import: 1
- `packages/zod/src/v4/mini/tests/assignability.test.ts` (TYPESCRIPT) | Magnitude: 1.85 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: safety: 63, structural_boundaries: 54, indent_spaces: 45, generics: 7
- `packages/zod/src/v3/benchmarks/discriminatedUnion.ts` (TYPESCRIPT) | Magnitude: 4.14 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, state_mutation: 24, structural_boundaries: 23, safety: 13
- `packages/zod/src/v3/benchmarks/union.ts` (TYPESCRIPT) | Magnitude: 4.14 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, state_mutation: 24, structural_boundaries: 21, safety: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/bench/object-setup.ts` (TYPESCRIPT) | Magnitude: 1.83 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 7, scientific: 6, safety: 3
- `packages/zod/src/v3/tests/language-server.test.ts` (TYPESCRIPT) | Magnitude: 0.18 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: sec_high_risk_execution: 8, dead_code: 6, structural_boundaries: 2, args: 1
- `packages/bench/safe.ts` (TYPESCRIPT) | Magnitude: 2.71 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 13, args: 7, func_start: 7
- `packages/tsc/extend.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/zod/src/v4/classic/schemas.ts` -> Churn: **98.35%** | Cog Load: 5.8032% | Debt: 90.5242%
- `packages/zod/src/v4/mini/schemas.ts` -> Churn: **90.54%** | Cog Load: 7.4591% | Debt: 72.3643%
- `packages/zod/src/v4/core/util.ts` -> Churn: **79.69%** | Cog Load: 25.9675% | Debt: 97.4762%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/zod/src/v4/classic/from-json-schema.ts` -> **Colin McDonnell** (100.0% isolated ownership) | Magnitude: 139.82
- `packages/zod/src/v4/core/json-schema-processors.ts` -> **Colin McDonnell** (83.3% isolated ownership) | Magnitude: 61.05

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/zod/src/v4/core/core.ts` -> **Severity: 1.351** (Embedded: 0.0182 * Error Risk: 74.1176%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/zod/src/v4/core/core.ts` -> **Severity: 1777.7** (Blast Radius: 17.777 * Doc Risk: 100.0%)
- `packages/bench/benchUtil.ts` -> **Severity: 255.8** (Blast Radius: 2.558 * Doc Risk: 100.0%)
- `packages/zod/src/v3/ZodError.ts` -> **Severity: 255.8** (Blast Radius: 2.558 * Doc Risk: 100.0%)
- `packages/zod/src/v4/classic/coerce.ts` -> **Severity: 255.8** (Blast Radius: 2.558 * Doc Risk: 100.0%)
- `packages/zod/src/v4/classic/external.ts` -> **Severity: 255.8** (Blast Radius: 2.558 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
