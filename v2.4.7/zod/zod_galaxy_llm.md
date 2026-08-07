# ARCHITECTURAL_BRIEF: zod
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/zod` |
| **Timestamp** | `2026-08-07T04:20:56.185829+00:00` |
| **Scan Duration** | `1.41s` |
| **Git Branch** | `main` |
| **Git Commit** | `c7805073fef5b6b8857307c3d4b3597a70613bc2` |
| **Git Remote** | `https://github.com/colinhacks/zod.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 349 malicious artifacts.

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
| Tech Debt Exposure | 0.0 | 100.0 | 7.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 11.7 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.9 | 2.5 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 20.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 6.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 89.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 8.6 | 1.7 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 8.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 21.6 | 0.0 | 0.0 |
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

- `describe` (@ `packages/zod/src/v4/classic/tests/to-json-schema.test.ts`) -> Impact: **308.0** | LOC: 1761
- `convertBaseSchema` (@ `packages/zod/src/v4/classic/from-json-schema.ts`) -> Impact: **300.3** | LOC: 394
- `run` (@ `packages/zod/src/v4/core/schemas.ts`) -> Impact: **277.7** | LOC: 1190
  * *Intent:* /** @internal Parses input and runs all checks (refinements). */
- `parse` (@ `packages/zod/src/v4/core/schemas.ts`) -> Impact: **230.6** | LOC: 905
- `ZodErrorMap` (@ `packages/zod/src/v4/locales/he.ts`) -> Impact: **223.1** | LOC: 236
- `ZodErrorMap` (@ `packages/zod/src/v3/locales/en.ts`) -> Impact: **158.4** | LOC: 119
- `test` (@ `packages/zod/src/v4/classic/tests/firstparty.test.ts`) -> Impact: **151.6** | LOC: 88
- `test` (@ `packages/zod/src/v4/classic/tests/firstparty.test.ts`) -> Impact: **149.8** | LOC: 86
- `ZodErrorMap` (@ `packages/zod/src/v4/locales/lt.ts`) -> Impact: **140.5** | LOC: 212
- `test` (@ `packages/zod/src/v3/tests/firstparty.test.ts`) -> Impact: **135.7** | LOC: 81

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 14 | 5082.66 | 1.79% | 0.0% |
| `packages/zod/src/v4/classic/tests` | 74 | 703.31 | 12.0% | 0.0% |
| `packages/zod/src/v4/locales` | 51 | 442.62 | 14.09% | 1.35% |
| `packages/zod/src/v4/core` | 19 | 395.41 | 31.5% | 44.89% |
| `packages/zod/src/v3/tests` | 61 | 349.03 | 18.22% | 0.0% |
| `packages/zod/src/v4/classic` | 10 | 173.71 | 11.88% | 31.01% |
| `packages/zod/src/v4/mini/tests` | 15 | 104.51 | 11.13% | 0.0% |
| `packages/bench` | 33 | 96.51 | 22.61% | 24.66% |
| `packages/zod/src/v4/mini` | 7 | 96.48 | 6.92% | 11.25% |
| `packages/zod/src/v3` | 6 | 79.86 | 24.42% | 12.41% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `packages/bench/index.ts` -> **100.0%** Exposure
- `packages/bench/lazy-box.ts` -> **100.0%** Exposure
- `packages/bench/property-access.ts` -> **100.0%** Exposure
- `packages/bench/safe.ts` -> **100.0%** Exposure
- `packages/tsc/bench/index.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `packages/tsc/generate.ts` -> **100.0%** Exposure
- `packages/zod/src/v3/benchmarks/index.ts` -> **100.0%** Exposure
- `packages/zod/src/v4/core/registries.ts` -> **100.0%** Exposure
- `packages/zod/src/v4/core/json-schema-generator.ts` -> **99.9996%** Exposure
- `packages/zod/src/v3/benchmarks/object.ts` -> **99.9992%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/zod/src/v4/classic/tests/to-json-schema-methods.test.ts` -> **1** Orphaned Functions | **122** Duplicates
- `packages/zod/src/v4/classic/tests/to-json-schema.test.ts` -> **0** Orphaned Functions | **120** Duplicates
- `packages/zod/src/v4/core/api.ts` -> **98** Orphaned Functions | **5** Duplicates
- `packages/zod/src/v4/classic/tests/index.test.ts` -> **0** Orphaned Functions | **99** Duplicates
- `packages/zod/src/v4/mini/tests/index.test.ts` -> **0** Orphaned Functions | **99** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `444` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/bench/metabench.ts` (TYPESCRIPT) -> Cumulative Risk: **672.56**
- **Archetype:** `file_cluster_4` (Distance: 12.341 IQR)
- **Magnitude:** 15.69 | **LOC:** 228 | **CtrlFlow:** 49.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9944%), State Flux (99.0837%), Cognitive Load (87.4077%)
- **Heaviest Functions:** `run` (Impact: 25.7), `metabench` (Impact: 19.8), `run` (Impact: 10.1)

### 2. `packages/zod/src/v4/core/parse.ts` (TYPESCRIPT) -> Cumulative Risk: **667.41**
- **Archetype:** `file_cluster_4` (Distance: 11.328 IQR)
- **Magnitude:** 20.24 | **LOC:** 196 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `Parse` (Impact: 14.5), `ParseAsync` (Impact: 14.4), `SafeParse` (Impact: 11.1)

### 3. `packages/zod/src/v3/types.ts` (TYPESCRIPT) -> Cumulative Risk: **659.01**
- **Archetype:** `file_cluster_4` (Distance: 13.139 IQR)
- **Magnitude:** 55.71 | **LOC:** 5139 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9992%), State Flux (99.9867%), Cognitive Load (98.0833%)
- **Heaviest Functions:** `processCreateParams` (Impact: 39.0), `check` (Impact: 27.9), `ZodErrorMap` (Impact: 24.8)

### 4. `packages/zod/src/v4/core/util.ts` (TYPESCRIPT) -> Cumulative Risk: **621.23**
- **Archetype:** `file_cluster_16` (Distance: 11.651 IQR)
- **Magnitude:** 27.89 | **LOC:** 979 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (97.4762%), Verification (80.0%)
- **Heaviest Functions:** `floatSafeRemainder` (Impact: 18.1), `isPlainObject` (Impact: 10.8), `defineLazy` (Impact: 7.2)

### 5. `packages/zod/src/v4/core/core.ts` (TYPESCRIPT) -> Cumulative Risk: **619.87**
- **Archetype:** `file_cluster_11` (Distance: 15.267 IQR)
- **Magnitude:** 9.84 | **LOC:** 139 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Verification (80.0%)
- **Heaviest Functions:** `value` (Impact: 14.2), `function` (Impact: 10.8), `init` (Impact: 10.2)

### 6. `packages/zod/src/v4/core/errors.ts` (TYPESCRIPT) -> Cumulative Risk: **591.41**
- **Archetype:** `file_cluster_16` (Distance: 12.031 IQR)
- **Magnitude:** 26.15 | **LOC:** 449 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.2742%), Verification (80.0%)
- **Heaviest Functions:** `mapper` (Impact: 48.3), `toDotPath` (Impact: 33.9), `mapper` (Impact: 33.8)

### 7. `packages/zod/src/v4/classic/schemas.ts` (TYPESCRIPT) -> Cumulative Risk: **591.07**
- **Archetype:** `file_cluster_16` (Distance: 12.174 IQR)
- **Magnitude:** 107.48 | **LOC:** 2410 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 75.9%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (97.2833%), Churn (96.45%)
- **Heaviest Functions:** `slugify` (Impact: 52.2), `parse` (Impact: 24.1), `apply` (Impact: 22.3)

### 8. `packages/zod/src/v3/helpers/parseUtil.ts` (TYPESCRIPT) -> Cumulative Risk: **578.3**
- **Archetype:** `file_cluster_4` (Distance: 11.283 IQR)
- **Magnitude:** 9.88 | **LOC:** 177 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.8413%), Documentation (97.0279%), Safety Score (91.1447%)
- **Heaviest Functions:** `mergeArray` (Impact: 7.4), `addIssueToContext` (Impact: 4.2), `dirty` (Impact: 3.0)

### 9. `packages/zod/src/v4/mini/schemas.ts` (TYPESCRIPT) -> Cumulative Risk: **562.73**
- **Archetype:** `file_cluster_16` (Distance: 10.942 IQR)
- **Magnitude:** 82.03 | **LOC:** 1917 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 72.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Churn (88.92%), Verification (80.0%)
- **Heaviest Functions:** `tuple` (Impact: 10.8), `catchValue` (Impact: 9.8), `object` (Impact: 9.2)

### 10. `packages/zod/src/v4/core/json-schema-generator.ts` (TYPESCRIPT) -> Cumulative Risk: **551.27**
- **Archetype:** `file_cluster_13` (Distance: 13.232 IQR)
- **Magnitude:** 8.98 | **LOC:** 127 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9996%), Tech Debt (98.7249%), Verification (80.0%)
- **Heaviest Functions:** `constructor` (Impact: 26.7), `emit` (Impact: 11.1), `counter` (Impact: 2.1)

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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/schemas.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.174 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.232 IQR)
- **Top Global Matches:** file_cluster_16: 12.174, file_cluster_2: 12.464, file_cluster_8: 12.55
- **Magnitude:** 107.48 | **LOC:** 2410 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 75.9%
- **Risk Profile:** Cognitive Load (5.8032%), Tech Debt (97.2833%)
**Top Internal Functions/Classes:**
  * `slugify` (Impact: 52.2)
  * `parse` (Impact: 24.1)
  * `apply` (Impact: 22.3)
  * `addIssue` (Impact: 19.8)
  * `exclude` (Impact: 13.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 291`, `structural_boundaries: 1027`, `args: 552`, `func_start: 479`, `class_start: 81`
* *Risk/State:* `safety_bypasses: 116`, `state_mutation: 14`, `dead_code: 5`, `duplicate_logic: 46`
* *Architecture:* `io: 3`, `api: 279`, `concurrency: 23`, `import: 8`
* *Defense:* `safety: 88`, `doc: 112`, `test: 1`, `immutability_locks: 137`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` to-json-schema.js, checks.js, parse.js, json-schema-processors.js, standard-schema.js, index.js, iso.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/to-json-schema.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.405 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.251 IQR)
- **Top Global Matches:** file_cluster_8: 10.405, file_cluster_7: 11.125, file_cluster_1: 11.308
- **Magnitude:** 99.61 | **LOC:** 2991 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (7.4769%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 308.0)
  * `test` (Impact: 120.7)
  * `test` (Impact: 108.4)
  * `test` (Impact: 26.5)
  * `test` (Impact: 10.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 436`, `args: 291`, `func_start: 278`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 11`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 120`
* *Architecture:* `io: 159`, `concurrency: 3`, `import: 3`
* *Defense:* `safety: 134`, `doc: 1`, `test: 267`, `immutability_locks: 144`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, openapi-schema-validator, zod, core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/schemas.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.503 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 5.594 IQR)
- **Top Global Matches:** file_cluster_16: 12.503, file_cluster_11: 12.59, file_cluster_13: 12.714
- **Magnitude:** 85.8 | **LOC:** 4557 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 57.6%
- **Risk Profile:** Cognitive Load (16.9803%), Tech Debt (99.4613%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 277.7)
    * *Intent:* /** @internal Parses input and runs all checks (refinements). */
  * `parse` (Impact: 230.6)
  * `handleCodecAResult` (Impact: 15.2)
  * `handleRefineResult` (Impact: 14.1)
  * `parse` (Impact: 11.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 534`, `args: 114`, `func_start: 42`, `class_start: 61`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 27`, `dead_code: 9`, `planned_debt: 4`, `duplicate_logic: 19`
* *Architecture:* `io: 3`, `api: 91`, `concurrency: 23`, `import: 12`
* *Defense:* `safety: 76`, `doc: 24`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` checks.js, errors.js, parse.js, core.js, versions.js, doc.js, standard-schema.js, regexes.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/api.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.442 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.194 IQR)
- **Top Global Matches:** file_cluster_16: 10.442, file_cluster_8: 10.605, file_cluster_13: 10.891
- **Magnitude:** 84.03 | **LOC:** 1799 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 71.4%
- **Risk Profile:** Cognitive Load (8.5136%), Tech Debt (99.4803%)
**Top Internal Functions/Classes:**
  * `addIssue` (Impact: 24.9)
  * `_superRefine` (Impact: 20.8)
  * `transform` (Impact: 12.3)
  * `_tuple` (Impact: 12.0)
    * *Intent:* // export function _tuple( // Class: util.SchemaClass<schemas.$ZodTuple>, // items: [], // params?: ...
  * `catchValue` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 736`, `args: 139`, `func_start: 132`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 24`, `dead_code: 8`, `duplicate_logic: 5`, `orphaned_logic: 98`
* *Architecture:* `io: 1`, `api: 250`, `concurrency: 1`, `import: 6`
* *Defense:* `safety: 42`, `doc: 11`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` schemas.js, checks.js, core.js, registries.js, errors.js, util.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/mini/schemas.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.942 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.361 IQR)
- **Top Global Matches:** file_cluster_16: 10.942, file_cluster_8: 11.271, file_cluster_2: 11.284
- **Magnitude:** 82.03 | **LOC:** 1917 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 72.7%
- **Risk Profile:** Cognitive Load (7.4591%), Tech Debt (78.7323%)
**Top Internal Functions/Classes:**
  * `tuple` (Impact: 10.8)
  * `catchValue` (Impact: 9.8)
  * `object` (Impact: 9.2)
    * *Intent:* // @__NO_SIDE_EFFECTS__
  * `check` (Impact: 7.6)
  * `check` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 797`, `args: 222`, `func_start: 150`, `class_start: 74`
* *Risk/State:* `safety_bypasses: 104`, `state_mutation: 4`, `dead_code: 4`, `duplicate_logic: 22`
* *Architecture:* `io: 2`, `api: 303`, `concurrency: 5`, `import: 3`
* *Defense:* `safety: 60`, `doc: 8`, `immutability_locks: 117`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` util.js, parse.js, index.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/types.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.139 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.238 IQR)
- **Top Global Matches:** file_cluster_4: 13.139, file_cluster_11: 13.366, file_cluster_13: 13.414
- **Magnitude:** 55.71 | **LOC:** 5139 | **CtrlFlow:** 50.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.0833%), Tech Debt (74.4868%)
**Top Internal Functions/Classes:**
  * `processCreateParams` (Impact: 39.0)
  * `check` (Impact: 27.9)
  * `ZodErrorMap` (Impact: 24.8)
  * `safeParse` (Impact: 14.7)
  * `getIssueProperties` (Impact: 12.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 170`, `args: 66`, `func_start: 63`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 181`, `duplicate_logic: 7`, `orphaned_logic: 3`
* *Architecture:* `io: 19`, `api: 20`, `concurrency: 103`, `import: 9`
* *Defense:* `safety: 45`, `doc: 1`, `test: 1`, `immutability_locks: 37`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` typeAliases.js, standard-schema.js, parseUtil.js, enumUtil.js, ZodError.js, util.js, errorUtil.js, errors.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/json-schema-processors.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.127 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.711 IQR)
- **Top Global Matches:** file_cluster_8: 10.127, file_cluster_13: 10.523, file_cluster_17: 10.534
- **Magnitude:** 51.44 | **LOC:** 668 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (17.7906%), Tech Debt (64.6305%)
**Top Internal Functions/Classes:**
  * `numberProcessor` (Impact: 53.4)
  * `literalProcessor` (Impact: 51.1)
  * `tupleProcessor` (Impact: 42.9)
  * `stringProcessor` (Impact: 39.7)
    * *Intent:* // ==================== SIMPLE TYPE PROCESSORS ====================
  * `recordProcessor` (Impact: 29.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 143`, `args: 70`, `func_start: 58`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 12`, `duplicate_logic: 7`
* *Architecture:* `io: 22`, `api: 43`, `import: 6`
* *Defense:* `safety: 15`, `immutability_locks: 128`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` schemas.js, checks.js, registries.js, to-json-schema.js, json-schema.js, util.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/tests/locales/he.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.017 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.129 IQR)
- **Top Global Matches:** file_cluster_8: 11.017, file_cluster_13: 11.725, file_cluster_7: 11.73
- **Magnitude:** 47.5 | **LOC:** 380 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (6.6646%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 88.0)
  * `describe` (Impact: 14.9)
  * `describe` (Impact: 12.7)
  * `describe` (Impact: 10.5)
  * `describe` (Impact: 10.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 65`, `args: 137`, `func_start: 122`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `duplicate_logic: 84`
* *Architecture:* `import: 3`
* *Defense:* `safety: 28`, `test: 121`, `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest, index.js, he.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/from-json-schema.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.506 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.078 IQR)
- **Top Global Matches:** file_cluster_8: 10.506, file_cluster_13: 10.881, file_cluster_17: 10.883
- **Magnitude:** 45.59 | **LOC:** 644 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (39.9575%), Tech Debt (13.0519%)
**Top Internal Functions/Classes:**
  * `convertBaseSchema` (Impact: 300.3)
  * `convertSchema` (Impact: 54.2)
  * `fromJSONSchema` (Impact: 18.3)
    * *Intent:* /**
  * `resolveRef` (Impact: 13.3)
  * `detectVersion` (Impact: 12.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 66`, `args: 13`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 46`, `planned_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 7`, `api: 1`, `import: 6`
* *Defense:* `safety: 21`, `doc: 1`, `test: 1`, `immutability_locks: 59`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` schemas.js, checks.js, json-schema.js, registries.js, iso.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/tests/error.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.77 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.128 IQR)
- **Top Global Matches:** file_cluster_8: 12.77, file_cluster_0: 13.121, file_cluster_17: 13.145
- **Magnitude:** 41.36 | **LOC:** 552 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.9142%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 43.6)
  * `test` (Impact: 35.0)
  * `expect` (Impact: 34.9)
  * `expect` (Impact: 19.0)
    * *Intent:* // expect(error.inner?.name?._errors).toEqual(["Invalid input"]); // expect(error.inner?.name?.[0]._...
  * `expect` (Impact: 10.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 76`, `args: 146`, `func_start: 133`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `dead_code: 4`, `planned_debt: 1`, `duplicate_logic: 63`
* *Architecture:* `io: 8`, `import: 4`
* *Defense:* `safety: 103`, `test: 126`, `immutability_locks: 65`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest, util.js, ZodError.js, v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/checks.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_11` (Drift: 12.917 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.485 IQR)
- **Top Global Matches:** file_cluster_11: 12.917, file_cluster_16: 13.088, file_cluster_0: 13.148
- **Magnitude:** 39.01 | **LOC:** 1294 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (24.1148%), Tech Debt (95.6856%)
**Top Internal Functions/Classes:**
  * `check` (Impact: 27.0)
  * `check` (Impact: 10.0)
  * `check` (Impact: 9.6)
  * `check` (Impact: 9.4)
  * `check` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 352`, `args: 71`, `func_start: 23`, `class_start: 66`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 127`, `dead_code: 15`, `duplicate_logic: 20`
* *Architecture:* `api: 93`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 40`, `doc: 3`, `immutability_locks: 78`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` schemas.js, core.js, regexes.js, errors.js, util.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/to-json-schema-methods.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.686 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.291 IQR)
- **Top Global Matches:** file_cluster_8: 11.686, file_cluster_7: 12.444, file_cluster_15: 12.466
- **Magnitude:** 32.24 | **LOC:** 439 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (6.0343%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 37.0)
  * `describe` (Impact: 14.2)
  * `describe` (Impact: 5.6)
  * `describe` (Impact: 5.4)
  * `test` (Impact: 5.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 117`, `args: 198`, `func_start: 193`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `duplicate_logic: 122`, `orphaned_logic: 1`
* *Architecture:* `import: 2`
* *Defense:* `safety: 65`, `test: 103`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest, v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/mini/tests/index.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.8 IQR)
- **Local Micro-Species:** `Cluster 6: Async Testing & Verification` (Drift: 6.73 IQR)
- **Top Global Matches:** file_cluster_17: 13.8, file_cluster_8: 13.823, file_cluster_0: 14.085
- **Magnitude:** 31.6 | **LOC:** 964 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (12.1658%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 16.4)
  * `test` (Impact: 11.0)
  * `test` (Impact: 10.9)
  * `test` (Impact: 10.8)
  * `test` (Impact: 8.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 313`, `args: 400`, `func_start: 374`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 12`, `dead_code: 4`, `duplicate_logic: 99`
* *Architecture:* `io: 5`, `concurrency: 22`, `import: 3`
* *Defense:* `safety: 341`, `test: 340`, `immutability_locks: 119`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, mini, core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/index.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.737 IQR)
- **Local Micro-Species:** `Cluster 6: Async Testing & Verification` (Drift: 6.725 IQR)
- **Top Global Matches:** file_cluster_17: 13.737, file_cluster_8: 13.774, file_cluster_4: 14.03
- **Magnitude:** 31.35 | **LOC:** 940 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (12.3991%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 16.4)
  * `test` (Impact: 12.3)
  * `test` (Impact: 11.0)
  * `test` (Impact: 10.9)
  * `test` (Impact: 8.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 320`, `args: 401`, `func_start: 376`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 12`, `dead_code: 4`, `duplicate_logic: 99`
* *Architecture:* `io: 5`, `concurrency: 22`, `import: 3`
* *Defense:* `safety: 318`, `test: 342`, `immutability_locks: 117`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, v4, core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/firstparty.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.541 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.293 IQR)
- **Top Global Matches:** file_cluster_8: 8.541, file_cluster_7: 9.467, file_cluster_13: 9.528
- **Magnitude:** 30.49 | **LOC:** 180 | **CtrlFlow:** 92.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (29.5836%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 151.6)
  * `test` (Impact: 149.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 13`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 2`
* *Architecture:* `import: 3`
* *Defense:* `safety: 11`, `test: 2`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, v4, core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v3/tests/async-parsing.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.196 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.634 IQR)
- **Top Global Matches:** file_cluster_4: 12.196, file_cluster_8: 12.631, file_cluster_17: 12.888
- **Magnitude:** 28.68 | **LOC:** 389 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 9.6)
  * `test` (Impact: 9.4)
  * `base` (Impact: 6.3)
  * `test` (Impact: 5.9)
  * `test` (Impact: 5.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 85`, `args: 76`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1`, `dead_code: 5`, `fragile_debt: 7`, `duplicate_logic: 30`
* *Architecture:* `concurrency: 111`, `import: 2`
* *Defense:* `safety: 20`, `test: 102`, `immutability_locks: 110`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest, v3
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/util.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.651 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 6.248 IQR)
- **Top Global Matches:** file_cluster_16: 11.651, file_cluster_17: 11.941, file_cluster_11: 12.014
- **Magnitude:** 27.89 | **LOC:** 979 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (25.9675%), Tech Debt (97.4762%)
**Top Internal Functions/Classes:**
  * `floatSafeRemainder` (Impact: 18.1)
  * `isPlainObject` (Impact: 10.8)
  * `defineLazy` (Impact: 7.2)
  * `void` (Impact: 6.7)
  * `hexToUint8Array` (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 264`, `args: 53`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 27`, `orphaned_logic: 24`
* *Architecture:* `io: 3`, `api: 93`, `concurrency: 9`, `import: 5`
* *Defense:* `safety: 35`, `immutability_locks: 34`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` schemas.js, checks.js, errors.js, core.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/refine.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.271 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.09 IQR)
- **Top Global Matches:** file_cluster_8: 10.271, file_cluster_0: 10.868, file_cluster_17: 11.014
- **Magnitude:** 27.61 | **LOC:** 571 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (8.783%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `describe` (Impact: 33.7)
  * `test` (Impact: 17.5)
  * `describe` (Impact: 16.8)
  * `test` (Impact: 9.7)
  * `test` (Impact: 8.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 71`, `args: 104`, `func_start: 76`
* *Risk/State:* `safety_bypasses: 2`, `dead_code: 3`, `planned_debt: 2`, `duplicate_logic: 48`
* *Architecture:* `io: 19`, `concurrency: 11`, `import: 2`
* *Defense:* `safety: 26`, `test: 74`, `immutability_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest, v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/locales/he.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.656 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.091 IQR)
- **Top Global Matches:** file_cluster_8: 10.656, file_cluster_13: 11.316, file_cluster_7: 11.414
- **Magnitude:** 27.1 | **LOC:** 247 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (22.4868%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ZodErrorMap` (Impact: 223.1)
  * `verbFor` (Impact: 16.1)
  * `typeLabel` (Impact: 13.5)
  * `getSizing` (Impact: 12.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 49`, `args: 10`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `api: 1`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 42`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` errors.js, util.js, checks.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/core/errors.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.031 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.938 IQR)
- **Top Global Matches:** file_cluster_16: 12.031, file_cluster_11: 12.125, file_cluster_13: 12.202
- **Magnitude:** 26.15 | **LOC:** 449 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (60.6693%), Tech Debt (99.2742%)
**Top Internal Functions/Classes:**
  * `mapper` (Impact: 48.3)
  * `toDotPath` (Impact: 33.9)
    * *Intent:* /** Format a ZodError as a human-readable string in the following form.
  * `mapper` (Impact: 33.8)
  * `prettifyError` (Impact: 16.7)
    * *Intent:* * * ```ts * ZodError { * issues: [ * { * expected: 'string', * code: 'invalid_type', * path: [ 'user...
  * `mapper` (Impact: 10.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 139`, `args: 25`, `func_start: 27`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 54`, `dead_code: 1`, `duplicate_logic: 10`
* *Architecture:* `io: 22`, `api: 43`, `import: 5`
* *Defense:* `safety: 27`, `doc: 6`, `immutability_locks: 81`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` schemas.js, checks.js, core.js, standard-schema.js, util.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/object.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.523 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.583 IQR)
- **Top Global Matches:** file_cluster_8: 12.523, file_cluster_16: 12.751, file_cluster_2: 12.816
- **Magnitude:** 25.75 | **LOC:** 641 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (12.3055%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 7.7)
  * `test` (Impact: 7.6)
  * `test` (Impact: 5.6)
  * `test` (Impact: 5.6)
  * `test` (Impact: 5.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 132`, `args: 149`, `func_start: 136`
* *Risk/State:* `safety_bypasses: 8`, `duplicate_logic: 98`
* *Architecture:* `concurrency: 20`, `import: 3`
* *Defense:* `safety: 152`, `test: 104`, `immutability_locks: 84`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vitest, v4, core
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/codec.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.156 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.203 IQR)
- **Top Global Matches:** file_cluster_8: 10.156, file_cluster_7: 10.927, file_cluster_4: 11.058
- **Magnitude:** 25.74 | **LOC:** 563 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (15.441%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 36.6)
  * `test` (Impact: 34.4)
  * `expect` (Impact: 26.2)
  * `test` (Impact: 6.6)
  * `expect` (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 92`, `args: 138`, `func_start: 124`
* *Risk/State:* `safety_bypasses: 1`, `duplicate_logic: 48`
* *Architecture:* `io: 9`, `concurrency: 20`, `import: 2`
* *Defense:* `safety: 32`, `test: 77`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest, v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/mini/tests/codec.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.9%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.129 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.256 IQR)
- **Top Global Matches:** file_cluster_8: 10.129, file_cluster_7: 10.898, file_cluster_13: 10.957
- **Magnitude:** 25.15 | **LOC:** 530 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.4605%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 36.6)
  * `test` (Impact: 34.5)
  * `expect` (Impact: 26.2)
  * `test` (Impact: 6.6)
  * `expect` (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 86`, `args: 126`, `func_start: 114`
* *Risk/State:* `safety_bypasses: 1`, `duplicate_logic: 46`
* *Architecture:* `io: 8`, `concurrency: 20`, `import: 3`
* *Defense:* `safety: 29`, `test: 71`, `immutability_locks: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest, locales, mini
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/zod/src/v4/classic/tests/async-parsing.test.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.759 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.87 IQR)
- **Top Global Matches:** file_cluster_4: 12.759, file_cluster_8: 13.269, file_cluster_17: 13.402
- **Magnitude:** 24.91 | **LOC:** 382 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `base` (Impact: 6.7)
  * `test` (Impact: 6.4)
  * `test` (Impact: 5.9)
  * `test` (Impact: 5.8)
  * `test` (Impact: 5.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 81`, `args: 78`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1`, `dead_code: 6`, `fragile_debt: 6`, `duplicate_logic: 26`, `orphaned_logic: 1`
* *Architecture:* `concurrency: 106`, `import: 2`
* *Defense:* `safety: 21`, `test: 97`, `immutability_locks: 102`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.558
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vitest, v4
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/zod/src/v4/core/json-schema.ts` (TYPESCRIPT) | Magnitude: 2.8 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 79, branch: 64, structural_boundaries: 38, generics: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/zod/src/v4/core/core.ts` (TYPESCRIPT) | Magnitude: 9.84 | Delta: **0.119 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 55, branch: 29, generics: 25
- `packages/zod/src/v4/core/checks.ts` (TYPESCRIPT) | Magnitude: 39.01 | Delta: **0.171 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 705, structural_boundaries: 352, generics: 141, branch: 139

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/treeshake/example.ts` (TYPESCRIPT) | Magnitude: 1.1 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, safety: 1, decorators: 1
- `packages/zod/src/v4/core/regexes.ts` (TYPESCRIPT) | Magnitude: 10.97 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 147, structural_boundaries: 74, immutability_locks: 65, api: 61
- `packages/zod/src/v3/tests/masking.test.ts` (TYPESCRIPT) | Magnitude: 0.18 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, test: 1
- `packages/treeshake/valibot-boolean.ts` (TYPESCRIPT) | Magnitude: 1.16 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, safety: 1, import: 1, debug_prints: 1
- `packages/treeshake/zod-mini-string.ts` (TYPESCRIPT) | Magnitude: 1.16 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 1, safety: 1, import: 1, debug_prints: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/zod/src/v3/tests/branded.test.ts` (TYPESCRIPT) | Magnitude: 0.81 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 12, generics: 11, immutability_locks: 7
- `packages/zod/src/v4/core/standard-schema.ts` (TYPESCRIPT) | Magnitude: 4.66 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 75, indent_spaces: 63, generics: 52, doc: 45
- `packages/zod/src/v3/ZodError.ts` (TYPESCRIPT) | Magnitude: 16.84 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 218, structural_boundaries: 119, generics: 51, state_mutation: 46
- `packages/zod/src/v4/core/schemas.ts` (TYPESCRIPT) | Magnitude: 85.8 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 756, structural_boundaries: 534, generics: 265, branch: 136
- `packages/zod/src/v4/classic/compat.ts` (TYPESCRIPT) | Magnitude: 1.6 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 26, structural_boundaries: 25, indent_spaces: 24, api: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/zod/src/v4/core/zsf.ts` (TYPESCRIPT) | Magnitude: 3.46 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 83, indent_spaces: 45, dead_code: 39, generics: 24
- `packages/zod/src/v4/mini/tests/index.test.ts` (TYPESCRIPT) | Magnitude: 31.6 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 642, args: 400, func_start: 374, safety: 341
- `packages/zod/src/v4/classic/tests/index.test.ts` (TYPESCRIPT) | Magnitude: 31.35 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 631, args: 401, func_start: 376, test: 342
- `packages/zod/src/v3/tests/generics.test.ts` (TYPESCRIPT) | Magnitude: 1.04 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 10, safety: 6, args: 5
- `packages/zod/src/v4/core/doc.ts` (TYPESCRIPT) | Magnitude: 4.59 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 34, state_mutation: 14, args: 13, structural_boundaries: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/zod/src/v3/standard-schema.ts` (TYPESCRIPT) | Magnitude: 2.87 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 27, doc: 23, generics: 18
- `packages/zod/src/v4/classic/tests/brand.test.ts` (TYPESCRIPT) | Magnitude: 2.94 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 53, args: 30, func_start: 28, structural_boundaries: 26
- `packages/zod/src/v4/mini/tests/brand.test.ts` (TYPESCRIPT) | Magnitude: 2.52 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 48, args: 26, func_start: 24, structural_boundaries: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/zod/src/v3/tests/readonly.test.ts` (TYPESCRIPT) | Magnitude: 5.61 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 92, immutability_locks: 43, safety: 35, concurrency: 31
- `packages/zod/src/v3/tests/tuple.test.ts` (TYPESCRIPT) | Magnitude: 4.21 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 24, args: 21, func_start: 19
- `packages/bench/union.ts` (TYPESCRIPT) | Magnitude: 2.35 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 11, concurrency: 6, immutability_locks: 6
- `packages/zod/src/v3/tests/function.test.ts` (TYPESCRIPT) | Magnitude: 16.61 | Delta: **0.176 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 171, structural_boundaries: 72, args: 69, concurrency: 47
- `packages/zod/src/v3/tests/async-refinements.test.ts` (TYPESCRIPT) | Magnitude: 3.54 | Delta: **0.179 IQR** | Secondary Pull: `file_cluster_8`
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
- `packages/bench/safe.ts` (TYPESCRIPT) | Magnitude: 2.29 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 13, args: 7, func_start: 7
- `packages/tsc/extend.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/zod/src/v4/core/schemas.ts` -> Churn: **100.0%** | Cog Load: 16.9803% | Debt: 99.4613%
- `packages/zod/src/v4/classic/schemas.ts` -> Churn: **96.45%** | Cog Load: 5.8032% | Debt: 97.2833%
- `packages/zod/src/v4/mini/schemas.ts` -> Churn: **88.92%** | Cog Load: 7.4591% | Debt: 78.7323%
- `packages/zod/src/v4/core/util.ts` -> Churn: **78.62%** | Cog Load: 25.9675% | Debt: 97.4762%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/zod/src/v4/core/json-schema-processors.ts` -> **Colin McDonnell** (83.3% isolated ownership) | Magnitude: 51.44

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
- `packages/zod/src/v4/classic/external.ts` -> **Severity: 255.8** (Blast Radius: 2.558 * Doc Risk: 100.0%)
- `packages/zod/src/v4/classic/parse.ts` -> **Severity: 255.8** (Blast Radius: 2.558 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
