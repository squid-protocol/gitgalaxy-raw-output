# ARCHITECTURAL_BRIEF: workers-sdk
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/cloudflare/workers-sdk.git` |
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
- **Scope:** 4360 analyzed artifact(s), 413616 LOC.
- **Load-bearing artifact:** `packages/wrangler/src/logger.ts` -- 288 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/wrangler/src/index.ts` -- pulls in 224 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `packages/wrangler/e2e/dev.test.ts` at magnitude 6899.26 (structural weight, not risk).
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
| Total Artifacts | 4635 |
| Analyzed Artifacts (Scanned) | 4360 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 275 |
| Total LOC | 413616 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 94.1% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7768 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1722 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.9558 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 273 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 2805 | 392157 | 64.3% |
| JSON | 750 | 9144 | 17.2% |
| PLAINTEXT | 227 | 7 | 5.2% |
| JAVASCRIPT | 208 | 7875 | 4.8% |
| MARKDOWN | 159 | 0 | 3.6% |
| HTML | 105 | 1494 | 2.4% |
| YAML | 38 | 1867 | 0.9% |
| XML | 26 | 97 | 0.6% |
| CSS | 14 | 622 | 0.3% |
| PYTHON | 9 | 58 | 0.2% |
| SQLITE | 7 | 28 | 0.2% |
| DOCKERFILE | 6 | 56 | 0.1% |
| PHP | 3 | 146 | 0.1% |
| SHELL | 2 | 36 | 0.0% |
| MAKEFILE | 1 | 29 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 4353 |
| unknown | unknown | 7 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 43%, Declarative / Non-Code 20%, Large Core Modules (2) 8%, Large Core Modules (3) 5%, Callbacks & Closures Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3963 | 90.9% |
| Unknown | 7 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 379 | 8.7% |
| Static: Minified & Vendor Opaque Mass | 11 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 275*

**Composition by Extension & Reason:**
- `no_extension`: 95x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 24x Unsupported Format (.undeterminable)
- `.ts`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Machine-Generated Source Code Signature: 8 LOC), 3x Excluded (Machine-Generated Source Code Signature: 5 LOC)
- `.patch`: 15x Excluded (Unsupported Extension: '.patch')
- `.wasm`: 7x Excluded (Unsupported Extension: '.wasm'), 4x Excluded (Binary Format Detected)
- `.vars`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 308 LOC), 1x Excluded (Machine-Generated Source Code Signature: 15078 LOC)
- `.json`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3161 LOC)
- `.png`: 8x Excluded (Explicitly Denied Extension: '.png')
- `.toml`: 6x Excluded (Unsupported Extension: '.toml')
- `.gif`: 6x Excluded (Explicitly Denied Extension: '.gif')
- `.snap`: 4x Unsupported Format (.snap), 2x Excluded (Unsupported Extension: '.snap')
- `.staging`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wat`: 4x Excluded (Unsupported Extension: '.wat')
- `.ico`: 4x Excluded (Explicitly Denied Extension: '.ico')
- `.bin`: 2x Excluded (Unsupported Extension: '.bin'), 1x Unsupported Format (.bin), 1x Excluded (Binary Format Detected)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.5 | 4.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 92.6 | 18.0 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.6 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 19.5 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 33.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 16.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 64.6 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 7.5 | 1.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 70.9 | 9.0 | 4.4 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 35.5 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1880 | 517 | 1 | `packages/workers-utils/tests/config/validation/normalize-and-validate-config.test.ts` |
| cleanup | 417 | 171 | 0 | `packages/wrangler/src/__tests__/middleware.test.ts` |
| guards | 12180 | 1418 | 7 | `packages/quick-edit-extension/vscode.d.ts` |
| danger | 3669 | 810 | 2 | `packages/workers-utils/tests/config/validation/normalize-and-validate-config.test.ts` |
| concurrency | 32293 | 1688 | 16 | `packages/miniflare/test/index.spec.ts` |
| connectivity | 10522 | 2432 | 5 | `packages/quick-edit-extension/vscode.d.ts` |
| io | 14584 | 1470 | 8 | `packages/miniflare/test/index.spec.ts` |
| crypto | 70 | 64 | 0 | `fixtures/nodejs-hybrid-app/src/index.ts` |
| ipc | 1807 | 365 | 0 | `packages/wrangler/src/__tests__/versions/versions.deploy.test.ts` |
| time | 829 | 266 | 0 | `packages/wrangler/src/__tests__/metrics.test.ts` |
| serialization | 1590 | 477 | 1 | `packages/workers-utils/src/config/validation.ts` |
| regex | 971 | 349 | 0 | `packages/local-explorer-ui/src/drivers/sqlite/parsers.ts` |
| events | 3232 | 661 | 2 | `packages/wrangler/src/pipelines/cli/setup.ts` |
| tests | 25552 | 910 | 10 | `packages/workers-utils/tests/config/validation/normalize-and-validate-config.test.ts` |
| docs | 7121 | 967 | 2 | `packages/quick-edit-extension/vscode.d.ts` |
| debt | 1879 | 512 | 1 | `packages/miniflare/src/runtime/config/generated/workerd.ts` |
| mutation | 51773 | 2439 | 30 | `packages/workers-utils/src/config/validation.ts` |
| dead_code | 886 | 248 | 0 | `packages/quick-edit-extension/vscode.d.ts` |
| credential | 44 | 20 | 0 | `packages/wrangler/src/__tests__/containers/deploy.test.ts` |
| threat | 36 | 17 | 0 | `packages/quick-edit-extension/vscode.d.ts` |
| ml_ai | 405 | 121 | 0 | `packages/miniflare/test/plugins/email/index.spec.ts` |
| ui | 2710 | 230 | 0 | `packages/local-explorer-ui/src/routes/workflows/$workflowName/$instanceId.tsx` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `packages/miniflare/test/index.spec.ts` (Hits: 403)
- `packages/wrangler/src/__tests__/dev.test.ts` (Hits: 254)
- `packages/wrangler/src/__tests__/pages/deploy.test.ts` (Hits: 246)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **logger.ts** (`packages/wrangler/src/logger.ts`) — 288 inbound connections
2. **create-command.ts** (`packages/wrangler/src/core/create-command.ts`) — 218 inbound connections
3. **mock-console.ts** (`packages/wrangler/src/__tests__/helpers/mock-console.ts`) — 162 inbound connections
4. **run-in-tmp.ts** (`packages/wrangler/src/__tests__/helpers/run-in-tmp.ts`) — 155 inbound connections
5. **run-wrangler.ts** (`packages/wrangler/src/__tests__/helpers/run-wrangler.ts`) — 132 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`packages/wrangler/src/index.ts`) — 224 outbound dependencies
2. **index.ts** (`packages/containers-shared/src/client/index.ts`) — 219 outbound dependencies
3. **deploy.ts** (`packages/wrangler/src/deploy/deploy.ts`) — 54 outbound dependencies
4. **templates.ts** (`packages/create-cloudflare/src/templates.ts`) — 48 outbound dependencies
5. **upload.ts** (`packages/wrangler/src/versions/upload.ts`) — 47 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `printBindings` **(Many-Argument Workhorses)** (@ `packages/wrangler/src/utils/print-bindings.ts`) -> Impact: **443.0** | LOC: 875
  * *Intent:* /** * Print all the bindings a worker would have access to. * Accepts StartDevWorkerInput["bindings"] format */
- `generatePerEnvironmentTypes` **(Many-Argument Workhorses)** (@ `packages/wrangler/src/type-generation/index.ts`) -> Impact: **356.1** | LOC: 418
  * *Intent:* * Used when named environments exist and no `--env` flag is specified. * * */
- `createWorkerUploadForm` **(Many-Argument Workhorses)** (@ `packages/wrangler/src/deployment-bundle/create-worker-upload-form.ts`) -> Impact: **300.1** | LOC: 762
  * *Intent:* /** * Creates a `FormData` upload from Worker data and bindings */
- `generateHandler` **(Many-Argument Workhorses)** (@ `packages/pages-shared/asset-server/handler.ts`) -> Impact: **262.9** | LOC: 617
- `deploy` **(Many-Argument Workhorses)** (@ `packages/wrangler/src/deploy/deploy.ts`) -> Impact: **256.8** | LOC: 894
- `validateContainerApp` **(Many-Argument Workhorses)** (@ `packages/workers-utils/src/config/validation.ts`) -> Impact: **206.7** | LOC: 493
- `generateSimpleEnvTypes` **(Many-Argument Workhorses)** (@ `packages/wrangler/src/type-generation/index.ts`) -> Impact: **200.6** | LOC: 291
  * *Intent:* * * Used when no named environments exist or when `--env` is specified. * * */
- `convertConfigToBindings` **(Many-Argument Workhorses)** (@ `packages/wrangler/src/api/startDevWorker/utils.ts`) -> Impact: **182.5** | LOC: 290
  * *Intent:* /** * Convert Config to the StartDevWorkerInput["bindings"] format for consistent internal use. */
- `handleError` **(Many-Argument Workhorses)** (@ `packages/wrangler/src/core/handle-errors.ts`) -> Impact: **171.9** | LOC: 319
  * *Intent:* /** * Handles an error thrown during command execution. * * This can involve filtering, transforming and logging the error appropriately. */
- `collectEnvironmentBindings` **(Many-Argument Workhorses)** (@ `packages/wrangler/src/type-generation/index.ts`) -> Impact: **162.8** | LOC: 484

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/wrangler/src/__tests__` | 75 | 19434.39 | 14.33% | 1.82% |
| `packages/wrangler/e2e` | 24 | 12825.95 | 22.62% | 1.57% |
| `packages/wrangler/src/__tests__/pages` | 21 | 6854.96 | 22.18% | 0.0% |
| `packages/workflows-shared/tests` | 8 | 6827.64 | 19.21% | 0.0% |
| `packages/workers-playground` | 12 | 5206.64 | 8.79% | 0.0% |
| `packages/vite-plugin-cloudflare/playground/bindings` | 8 | 5083.52 | 0.64% | 0.0% |
| `packages/vite-plugin-cloudflare/playground/dot-env` | 8 | 5080.68 | 1.28% | 0.0% |
| `packages/vite-plugin-cloudflare/playground/sensitive-files` | 7 | 5070.34 | 0.73% | 0.0% |
| `fixtures/nodejs-hybrid-app` | 6 | 5000.07 | 0.85% | 0.0% |
| `fixtures/worker-app` | 5 | 5000.06 | 1.02% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/ISSUE_TEMPLATE/bug-template.yaml` -> **100.0%** Exposure
- `packages/miniflare/src/workers/node.d.ts` -> **100.0%** Exposure
- `packages/miniflare/src/workers/stream/binding.worker.ts` -> **100.0%** Exposure
- `packages/miniflare/types/streams.d.ts` -> **100.0%** Exposure
- `packages/quick-edit-extension/vscode.d.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `packages/create-cloudflare/templates/common/js/src/proxy.js` -> **100.0%** Exposure
- `fixtures/shared/src/mock-postgres-server.ts` -> **100.0%** Exposure
- `fixtures/shared/src/run-wrangler-long-lived.ts` -> **100.0%** Exposure
- `packages/create-cloudflare/e2e/helpers/workers-helpers.ts` -> **100.0%** Exposure
- `packages/create-cloudflare/src/helpers/__tests__/args.test.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/quick-edit-extension/vscode.d.ts` -> **306** Orphaned Functions | **69** Duplicates
- `packages/miniflare/src/runtime/config/generated/workerd.ts` -> **0** Orphaned Functions | **86** Duplicates
- `packages/miniflare/src/workers/node.d.ts` -> **60** Orphaned Functions | **0** Duplicates
- `packages/vitest-pool-workers/scripts/rtti/rtti.js` -> **0** Orphaned Functions | **53** Duplicates
- `packages/workers-shared/router-worker/tests/index.test.ts` -> **0** Orphaned Functions | **51** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `packages/vite-plugin-cloudflare/playground/node-compat/__tests__/worker-crypto/crypto.spec.ts` -> **99.9973%** Exposure
- `packages/vite-plugin-cloudflare/playground/node-compat/worker-crypto/index.ts` -> **99.9946%** Exposure
- `packages/miniflare/src/http/cert.ts` -> **99.9898%** Exposure
- `packages/wrangler/src/cloudchamber/ssh/validate.ts` -> **99.9257%** Exposure
- `packages/pages-shared/__tests__/metadata-generator/createMetadataObject.test.ts` -> **99.5623%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### 📡 API Network Audit (Set Theory)
- **Shadow APIs (Critical):** `37` undocumented endpoints actively listening.
- **Ghost APIs (Bloat):** `27` endpoints documented but missing from code.
- **Known Shadow Routes:** `DELETE /api/r2/buckets/{var}/objects`, `DELETE /api/storage/kv/namespaces/{var}/values/{var}`, `DELETE /api/workflows/{var}`, `DELETE /api/workflows/{var}/instances/{var}`, `GET /`

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `17` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5878` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `packages/wrangler/e2e/dev.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.825)
- **Top Global Matches:** file_cluster_10: 4.825, file_cluster_2: 6.229, file_cluster_13: 6.356
- **Magnitude:** 6899.26 | **LOC:** 2919 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 44.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.116; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (97.3%), Guard Balance (formerly Safety Score) (51.9%), Complexity Load (formerly Cognitive Load) (49.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 295 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 1997
* *State Mutation (weighted view):* 373
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 680`, `args: 174`, `func_start: 117`
* *Risk/State:* `state_mutation: 335`, `planned_debt: 3`, `fragile_debt: 4`
* *Architecture:* `io: 111`, `api: 40`, `concurrency: 522`, `import: 36`
* *Defense:* `safety: 28`, `doc: 1`, `test: 223`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` account-id, e2e-wrangler-test, fetch-text, fetch-with-etag, generate-resource-name, mysql-echo-handler, postgres-echo-handler, retry...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/workflows-shared/tests/engine.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.447)
- **Top Global Matches:** file_cluster_10: 6.447, file_cluster_12: 7.617, file_cluster_2: 8.552
- **Magnitude:** 6077.53 | **LOC:** 1063 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 41.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.116; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.5%), Guard Balance (formerly Safety Score) (45.4%), Complexity Load (formerly Cognitive Load) (44.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 18 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 357
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 424`, `args: 162`, `func_start: 73`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 8`, `planned_debt: 1`
* *Architecture:* `concurrency: 267`, `import: 11`
* *Defense:* `safety: 44`, `test: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` src, engine, errors, test-entry, utils, cloudflare:test, cloudflare:workers, cloudflare:workflows...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fixtures/nodejs-hybrid-app/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fixtures/pages-workerjs-app/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `fixtures/worker-app/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/vite-plugin-cloudflare/playground/bindings/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/vite-plugin-cloudflare/playground/dot-env/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/vite-plugin-cloudflare/playground/sensitive-files/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/workers-playground/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/workers-utils/src/config/validation.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.877)
- **Top Global Matches:** file_cluster_6: 6.877, file_cluster_4: 10.304, file_cluster_8: 16.197
- **Magnitude:** 3072.82 | **LOC:** 5390 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 22.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **15**; blast radius 0.35; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (65.4%), Guard Balance (formerly Safety Score) (60.8%), Connectivity (formerly Api Exposure) (37.2%)
- **Documentation Coverage:** 32.5843% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateContainerApp` **(Many-Argument Workhorses)** (Impact: 206.7)
  * `normalizeAndValidateConfig` **(Many-Argument Workhorses)** (Impact: 82.0)
    * *Intent:* * Validate the given `rawConfig` object that was loaded from `configPath`. * * The configuration is ...
  * `validateObservability` **(Many-Argument Workhorses)** (Impact: 67.2)
  * `validateMigrations` **(Many-Argument Workhorses)** (Impact: 49.9)
    * *Intent:* /** * Validate the `migrations` configuration and return the normalized values. */
  * `validateWorkflowBinding` **(Many-Argument Workhorses)** (Impact: 49.6)
    * *Intent:* /** * Check that the given field is a valid "workflow" binding object. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 397 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 1216
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 714`, `structural_boundaries: 367`, `args: 122`, `func_start: 84`
* *Risk/State:* `state_mutation: 422`, `planned_debt: 1`
* *Architecture:* `io: 60`, `api: 9`, `concurrency: 7`, `import: 16`
* *Defense:* `safety: 85`, `doc: 36`, `test: 7`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.35
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.012133
  * `Imports (Out-Degree: 9):` , misc-variables, errors, fs-helpers, types, config, config-helpers, diagnostics...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/wrangler/src/__tests__/type-generation.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.344)
- **Top Global Matches:** file_cluster_10: 5.344, file_cluster_2: 6.296, file_cluster_0: 6.73
- **Magnitude:** 2617.59 | **LOC:** 3994 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 21.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.116; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.5%), Guard Balance (formerly Safety Score) (47.8%), Mutation Surface (formerly State Flux) (21.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 71 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 514
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 809`, `args: 149`, `func_start: 75`, `class_start: 155`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 94`
* *Architecture:* `io: 177`, `api: 42`, `concurrency: 159`, `import: 65`
* *Defense:* `safety: 20`, `doc: 2`, `test: 254`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` index, index, index, type-generation, helpers, runtime, dedent, durable-2.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/type-generation/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.84)
- **Top Global Matches:** file_cluster_6: 6.84, file_cluster_4: 10.184, file_cluster_9: 16.26
- **Magnitude:** 2442.68 | **LOC:** 3520 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **20**; blast radius 0.158; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.8%), Connectivity (formerly Api Exposure) (56.8%), Guard Balance (formerly Safety Score) (51.7%)
- **Documentation Coverage:** 42.623% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generatePerEnvironmentTypes` **(Many-Argument Workhorses)** (Impact: 356.1)
    * *Intent:* * Used when named environments exist and no `--env` flag is specified. * * */
  * `generateSimpleEnvTypes` **(Many-Argument Workhorses)** (Impact: 200.6)
    * *Intent:* * * Used when no named environments exist or when `--env` is specified. * * */
  * `collectEnvironmentBindings` **(Many-Argument Workhorses)** (Impact: 162.8)
  * `collectEnvironmentBindings` **(Many-Argument Workhorses)** (Impact: 159.1)
  * `collectCoreBindingsPerEnvironment` **(Many-Argument Workhorses)** (Impact: 153.3)
    * *Intent:* /** * Collects core bindings per environment, returning a map from environment name to bindings. * *...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 127 instances
* *Concurrency (weighted view):* 65
* *State Mutation (weighted view):* 392
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 582`, `structural_boundaries: 327`, `args: 82`, `func_start: 53`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 138`
* *Architecture:* `io: 23`, `api: 12`, `concurrency: 20`, `import: 30`
* *Defense:* `safety: 155`, `doc: 37`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.158
  * `Choke Point (Betweenness):` 0.000113 | `Ripple Effect (Closeness):` 0.012292
  * `Imports (Out-Degree: 11):` $entrypointModule, $importPath, config, create-command, entry, class-names-sqlite, dev-vars, logger...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/miniflare/test/index.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.155)
- **Top Global Matches:** file_cluster_10: 7.155, file_cluster_15: 7.758, file_cluster_11: 8.393
- **Magnitude:** 2130.14 | **LOC:** 3696 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 55.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **30**; blast radius 0.116; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.0%), Guard Balance (formerly Safety Score) (45.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `STORE` **(Defensive Guards)** (Impact: 13.6)
  * `unsafeModuleFallbackService` **(Compute Cores)** (Impact: 4.8)
  * `CUSTOM` **(Defensive Guards)** (Impact: 4.7)
    * *Intent:* // Testing loopback server WebSocket coupling
  * `getState` **(Defensive Guards)** (Impact: 2.4)
  * `testEncoding` **(Callbacks & Closures)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 243 instances
* *Amplified Cascading Flux:* 10 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 1776
* *State Mutation (weighted view):* 137
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 911`, `args: 253`, `func_start: 203`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 117`, `planned_debt: 2`, `duplicate_logic: 4`, `unreferenced_by_name: 3`
* *Architecture:* `io: 403`, `api: 103`, `concurrency: 561`, `import: 41`
* *Defense:* `safety: 39`, `test: 363`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` a.mjs, c.cjs, b.mjs, d.cjs, index.js, index.js, test-shared, experimental...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/miniflare/test/plugins/r2/index.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.516)
- **Top Global Matches:** file_cluster_10: 7.516, file_cluster_15: 8.412, file_cluster_0: 9.354
- **Magnitude:** 1781.68 | **LOC:** 1633 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.116; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.6%), Guard Balance (formerly Safety Score) (35.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testList` **(Defensive Guards)** (Impact: 24.7)
  * `pass` **(Defensive Guards)** (Impact: 6.0)
    * *Intent:* // `workerd` will handle extracting `onlyIf`s from `Header`s: // https://github.com/cloudflare/worke...
  * `testValidatesKey` **(Defensive Guards)** (Impact: 4.1)
  * `fail` **(Callbacks & Closures)** (Impact: 3.1)
  * `pass` **(Callbacks & Closures)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 211 instances
* *Amplified Cascading Flux:* 25 instances
* *Concurrency (weighted view):* 1533
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 522`, `args: 81`, `func_start: 73`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 102`, `fragile_debt: 1`
* *Architecture:* `io: 12`, `api: 1`, `concurrency: 478`, `import: 12`
* *Defense:* `safety: 86`, `test: 404`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` schemas.worker, test-shared, experimental, miniflare, node:assert, node:crypto, promises, node:path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/autoconfig/details/get-details-for-auto-config.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.582)
- **Top Global Matches:** file_cluster_10: 4.582, file_cluster_2: 6.559, file_cluster_13: 6.827
- **Magnitude:** 1766.87 | **LOC:** 558 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 75.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.116; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (53.5%), Guard Balance (formerly Safety Score) (37.7%), Complexity Load (formerly Cognitive Load) (33.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 116`, `args: 38`, `func_start: 29`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 2`, `api: 3`, `concurrency: 78`, `import: 17`
* *Defense:* `safety: 30`, `test: 67`, `sync_locks: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` details, config-cache, is-interactive, output, package-manager, constants, mock-console, mock-dialogs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/miniflare/src/index.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.367)
- **Top Global Matches:** file_cluster_4: 6.367, file_cluster_15: 10.917, file_cluster_16: 11.158
- **Magnitude:** 1748.66 | **LOC:** 3062 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 22.2%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **43**; blast radius 0.145; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (97.0%), Complexity Load (formerly Cognitive Load) (82.0%), Connectivity (formerly Api Exposure) (68.2%)
- **Documentation Coverage:** 88.6957% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assembleConfig` **(Many-Argument Workhorses)** (Impact: 162.3)
  * `handleLoopback` **(Many-Argument Workhorses)** (Impact: 105.6)
  * `getExternalServiceEntrypoints` **(Many-Argument Workhorses)** (Impact: 42.8)
    * *Intent:* /** * This collects all external service bindings from all workers and overrides * it to point to th...
  * `assembleAndUpdateConfig` **(I/O & Config Routines)** (Impact: 36.6)
  * `getDurableObjectClassNames` **(Defensive Guards)** (Impact: 32.7)
    * *Intent:* // When creating user worker services, we need to know which Durable Objects // they export. Rather ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 31 instances
* *Amplified Cascading Flux:* 114 instances
* *Concurrency (weighted view):* 320
* *State Mutation (weighted view):* 356
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 468`, `structural_boundaries: 379`, `args: 150`, `func_start: 88`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 128`, `planned_debt: 4`
* *Architecture:* `io: 69`, `api: 39`, `concurrency: 165`, `import: 58`
* *Defense:* `safety: 135`, `doc: 13`, `test: 41`, `sync_locks: 3`, `immutability_locks: 12`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.145
  * `Choke Point (Betweenness):` 3.6e-05 | `Ripple Effect (Closeness):` 0.002617
  * `Imports (Out-Degree: 37):` cf, http, merge, plugins, constants, core, inspector-proxy, hyperdrive-proxy...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/wrangler/src/__tests__/dev.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.072)
- **Top Global Matches:** file_cluster_10: 7.072, file_cluster_15: 8.349, file_cluster_13: 9.279
- **Magnitude:** 1506.68 | **LOC:** 2842 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 23.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 0.116; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (86.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (60.3%), Complexity Load (formerly Cognitive Load) (49.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expectedHostAndZone` **(Defensive Guards)** (Impact: 29.1)
  * `runWranglerUntilConfig` **(Defensive Guards)** (Impact: 7.7)
  * `mockGetZones` **(Callbacks & Closures)** (Impact: 2.7)
  * `memoizeGetPort` **(Callbacks & Closures)** (Impact: 1.9)
  * `extractCustomBuildLogs` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 139 instances
* *Amplified Cascading Flux:* 35 instances
* *Concurrency (weighted view):* 1022
* *State Mutation (weighted view):* 268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 584`, `args: 210`, `func_start: 148`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 198`
* *Architecture:* `io: 254`, `api: 118`, `concurrency: 327`, `import: 28`
* *Defense:* `safety: 102`, `test: 358`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` api, ConfigController, utils, remote, logger, package-manager, helpers, runtime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/pages/deploy.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.64)
- **Top Global Matches:** file_cluster_15: 6.64, file_cluster_10: 6.823, file_cluster_2: 7.953
- **Magnitude:** 1440.3 | **LOC:** 6277 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 36.4%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **39**; blast radius 0.116; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (74.2%), Guard Balance (formerly Safety Score) (46.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `simulateServer` **(Many-Argument Workhorses)** (Impact: 8.2)
  * `mockGetProjectHandler` **(Parameter Forwarders)** (Impact: 2.9)
  * `bundleString` **(Parameter Forwarders)** (Impact: 1.8)
  * `workerHasD1Shim` **(Parameter Forwarders)** (Impact: 1.5)
  * `workerIsBundled` **(Parameter Forwarders)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 123 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 1083
* *State Mutation (weighted view):* 193
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 758`, `args: 295`, `func_start: 246`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 181`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 246`, `api: 36`, `concurrency: 468`, `import: 46`
* *Defense:* `safety: 62`, `test: 487`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` package.json, logger, constants, errors, routes-validation, types, end-event-loop, mock-account-id...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/hyperdrive.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.263)
- **Top Global Matches:** file_cluster_10: 7.263, file_cluster_15: 8.899, file_cluster_2: 9.103
- **Magnitude:** 1357.3 | **LOC:** 2206 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.116; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (95.3%), Guard Balance (formerly Safety Score) (51.7%), Complexity Load (formerly Cognitive Load) (47.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mockHyperdriveUpdate` **(Defensive Guards)** (Impact: 24.8)
    * *Intent:* /** Create a mock handler for Hyperdrive API */
  * `mockHyperdriveGetListOrDelete` **(I/O & Config Routines)** (Impact: 4.1)
    * *Intent:* /** Create a mock handler for Hyperdrive API */
  * `mockHyperdriveCreate` **(Callbacks & Closures)** (Impact: 3.0)
    * *Intent:* /** Create a mock handler for Hyperdrive API */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 160 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 1004
* *State Mutation (weighted view):* 280
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 225`, `args: 96`, `func_start: 69`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 274`
* *Architecture:* `io: 106`, `concurrency: 204`, `import: 12`
* *Defense:* `safety: 13`, `doc: 5`, `test: 188`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` client, end-event-loop, mock-account-id, mock-console, mock-dialogs, mock-istty, msw, run-in-tmp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/miniflare/src/runtime/config/generated/workerd.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.313)
- **Top Global Matches:** file_cluster_0: 6.313, file_cluster_11: 7.53, file_cluster_15: 8.658
- **Magnitude:** 1329.34 | **LOC:** 4277 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 0.471; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (94.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.5%)
- **Documentation Coverage:** 69.5983% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_initCryptoKey` **(Generic / Templated Code)** (Impact: 1.9)
  * `structuredLogging` **(State Mutators)** (Impact: 1.8)
  * `extractable` **(State Mutators)** (Impact: 1.8)
  * `_initUsages` **(Generic / Templated Code)** (Impact: 1.8)
  * `_initInnerBindings` **(Generic / Templated Code)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Concurrency (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 698`, `args: 703`, `func_start: 703`, `class_start: 38`
* *Risk/State:* `state_mutation: 13`, `planned_debt: 6`, `duplicate_logic: 86`
* *Architecture:* `io: 20`, `api: 289`, `concurrency: 25`, `import: 1`
* *Defense:* `doc: 203`, `immutability_locks: 148`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.471
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003771
  * `Imports (Out-Degree: 0):` capnp-es
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/wrangler/e2e/pages-dev.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.955)
- **Top Global Matches:** file_cluster_10: 4.955, file_cluster_2: 6.223, file_cluster_13: 6.49
- **Magnitude:** 1282.92 | **LOC:** 904 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.116; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (98.4%), Guard Balance (formerly Safety Score) (53.2%), Complexity Load (formerly Cognitive Load) (50.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 81 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 566
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 213`, `args: 59`, `func_start: 47`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 121`
* *Architecture:* `io: 36`, `api: 32`, `concurrency: 161`, `import: 16`
* *Defense:* `safety: 7`, `test: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` greetings, my-html.html, greetings, graham.html, e2e-wrangler-test, fetch-text, normalize, wait-for...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/tail.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 8.272)
- **Top Global Matches:** file_cluster_10: 8.272, file_cluster_15: 8.563, file_cluster_11: 9.072
- **Magnitude:** 1061.76 | **LOC:** 1317 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.116; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (85.1%), Guard Balance (formerly Safety Score) (46.7%), Complexity Load (formerly Cognitive Load) (40.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mockCreateTailRequest` **(Many-Argument Workhorses)** (Impact: 22.2)
    * *Intent:* /** * Mock out the API hit during Tail creation * */
  * `mockDeleteTailRequest` **(Compute Cores)** (Impact: 21.6)
    * *Intent:* /** * Mock out the API hit during Tail deletion * */
  * `generateMockRequestEvent` **(Defensive Guards)** (Impact: 15.3)
    * *Intent:* /** * Generate a mock `RequestEvent` that, in an alternate timeline, was used * to trigger a worker....
  * `serialize` **(Defensive Guards)** (Impact: 12.8)
    * *Intent:* /* helpers */ /** * The built in serialize-to-JSON feature of our mock websocket doesn't work * for ...
  * `generateMockEmailEvent` **(Defensive Guards)** (Impact: 11.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 127 instances
* *Amplified Cascading Flux:* 6 instances
* *Concurrency (weighted view):* 790
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 230`, `args: 87`, `func_start: 66`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 98`, `duplicate_logic: 2`
* *Architecture:* `io: 12`, `concurrency: 155`, `import: 18`
* *Defense:* `safety: 30`, `doc: 21`, `test: 121`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` createTail, mock-account-id, mock-console, mock-dialogs, mock-istty, mock-web-socket, msw, run-in-tmp...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/r2/bucket.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.454)
- **Top Global Matches:** file_cluster_10: 5.454, file_cluster_2: 8.199, file_cluster_13: 8.491
- **Magnitude:** 1059.3 | **LOC:** 4129 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.116; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (66.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.3%), Guard Balance (formerly Safety Score) (46.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mockBucketLockPutWithExistingRules` **(Callbacks & Closures)** (Impact: 3.8)
  * `mockBucketLockGetExistingRules` **(Callbacks & Closures)** (Impact: 2.8)
  * `mockBucketLockPutNew` **(State Mutators)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 66 instances
* *Concurrency (weighted view):* 679
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 586`, `args: 260`, `func_start: 191`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 295`, `fragile_debt: 1`
* *Architecture:* `io: 106`, `concurrency: 349`, `import: 15`
* *Defense:* `safety: 51`, `test: 505`, `sync_locks: 71`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` bucket, notification, end-event-loop, mock-account-id, mock-console, mock-dialogs, mock-istty, msw...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/email-routing.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.221)
- **Top Global Matches:** file_cluster_10: 5.221, file_cluster_13: 8.179, file_cluster_15: 8.844
- **Magnitude:** 1040.56 | **LOC:** 1643 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.116; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (91.5%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (45.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mockZoneLookup` **(Callbacks & Closures)** (Impact: 4.4)
  * `mockDisableSending` **(Callbacks & Closures)** (Impact: 3.7)
  * `mockEnableSending` **(Callbacks & Closures)** (Impact: 3.6)
  * `mockDisableSendingCapture` **(Callbacks & Closures)** (Impact: 3.0)
  * `mockEnableSendingCapture` **(Callbacks & Closures)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 115 instances
* *Concurrency (weighted view):* 788
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 357`, `args: 176`, `func_start: 115`
* *Risk/State:* `state_mutation: 158`
* *Architecture:* `io: 35`, `concurrency: 213`, `import: 11`
* *Defense:* `safety: 33`, `test: 218`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` end-event-loop, mock-account-id, mock-console, mock-dialogs, mock-istty, msw, run-in-tmp, run-wrangler...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/wrangler/src/__tests__/r2/catalog-force.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.133)
- **Top Global Matches:** file_cluster_10: 4.133, file_cluster_2: 5.818, file_cluster_13: 6.795
- **Magnitude:** 1006.89 | **LOC:** 718 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.116; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (96.7%), Complexity Load (formerly Cognitive Load) (93.3%), Guard Balance (formerly Safety Score) (49.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 28 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 181
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 103`, `args: 44`, `func_start: 16`
* *Risk/State:* `state_mutation: 69`
* *Architecture:* `io: 37`, `concurrency: 41`, `import: 10`
* *Defense:* `safety: 20`, `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.116
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` mock-account-id, mock-console, mock-dialogs, mock-istty, msw, run-in-tmp, run-wrangler, msw...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `fixtures/pages-functions-app/functions/r2/create.ts` (TYPESCRIPT) | Magnitude: 0.0 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 5, indent_tabs: 3, concurrency: 2, core_var_decl: 2
- `packages/wrangler/src/__tests__/containers/config.test.ts` (TYPESCRIPT) | Magnitude: 246.57 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 818, test: 71, structural_boundaries: 63, concurrency: 49
- `packages/vite-plugin-cloudflare/playground/spa-with-api/api/index.ts` (TYPESCRIPT) | Magnitude: 12.9 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 10, concurrency: 4, core_var_decl: 4
- `fixtures/pages-functions-app/functions/r2/get.ts` (TYPESCRIPT) | Magnitude: 0.0 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 5, indent_tabs: 3, concurrency: 2, core_var_decl: 2
- `packages/miniflare/src/workers/shared/blob.worker.ts` (TYPESCRIPT) | Magnitude: 192.86 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 155, structural_boundaries: 52, concurrency: 33, branch: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `packages/vite-plugin-cloudflare/playground/middleware-mode/server.js` (JAVASCRIPT) | Magnitude: 8.38 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 17, structural_boundaries: 9, concurrency: 4, core_var_decl: 4
- `packages/wrangler/src/__tests__/versions/secrets/bulk.test.ts` (TYPESCRIPT) | Magnitude: 316.72 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 314, structural_boundaries: 84, test: 53, concurrency: 38
- `packages/miniflare/test/shared/blob.spec.ts` (TYPESCRIPT) | Magnitude: 303.8 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 164, structural_boundaries: 73, concurrency: 50, state_mutation: 37
- `packages/miniflare/src/plugins/browser-rendering/index.ts` (TYPESCRIPT) | Magnitude: 116.52 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 188, structural_boundaries: 35, state_mutation: 35, core_var_decl: 16
- `packages/miniflare/test/plugins/email/index.spec.ts` (TYPESCRIPT) | Magnitude: 159.2 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 1184, decorators: 189, structural_boundaries: 158, core_var_decl: 129

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `packages/vite-plugin-cloudflare/playground/node-compat/worker-basic/index.ts` (TYPESCRIPT) | Magnitude: 8.78 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 24, structural_boundaries: 14, safety: 11, test: 11
- `packages/miniflare/src/plugins/version-metadata/index.ts` (TYPESCRIPT) | Magnitude: 17.14 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 32, structural_boundaries: 14, core_var_decl: 8, api: 6
- `packages/wrangler/e2e/startWorker.test.ts` (TYPESCRIPT) | Magnitude: 461.62 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 784, structural_boundaries: 210, concurrency: 143, io: 111
- `packages/vite-plugin-cloudflare/src/context.ts` (TYPESCRIPT) | Magnitude: 102.44 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 160, structural_boundaries: 75, args: 25, api: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `packages/create-cloudflare/src/helpers/__tests__/json.test.ts` (TYPESCRIPT) | Magnitude: 20.48 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 163, test: 33, structural_boundaries: 27, io: 19
- `packages/vite-plugin-cloudflare/playground/containers/src/index.ts` (TYPESCRIPT) | Magnitude: 40.2 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 53, structural_boundaries: 21, branch: 11, io: 10
- `fixtures/pages-workerjs-with-config-file-app/tests/index.test.ts` (TYPESCRIPT) | Magnitude: 0.16 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 56, structural_boundaries: 24, concurrency: 18, io: 12
- `packages/unenv-preset/src/runtime/node/console.ts` (TYPESCRIPT) | Magnitude: 19.16 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 46, structural_boundaries: 7, api: 3, import: 3
- `packages/wrangler/src/__tests__/deploy/config-remote.test.ts` (TYPESCRIPT) | Magnitude: 110.5 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 530, structural_boundaries: 82, concurrency: 40, test: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/miniflare/openapi-ts.config.ts` (TYPESCRIPT) | Magnitude: 19.44 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 19, structural_boundaries: 4, branch: 3, args: 2
- `packages/create-cloudflare/templates/react/workers/c3.ts` (TYPESCRIPT) | Magnitude: 71.78 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 137, structural_boundaries: 38, core_var_decl: 19, args: 14
- `fixtures/dev-registry/vite.exported-handler.config.ts` (TYPESCRIPT) | Magnitude: 0.02 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 7, structural_boundaries: 3, import: 2, branch: 1
- `fixtures/vitest-pool-workers-examples/workflows/vitest.config.ts` (TYPESCRIPT) | Magnitude: 0.02 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 7, structural_boundaries: 3, import: 2, branch: 1
- `packages/kv-asset-handler/vitest.config.mts` (TYPESCRIPT) | Magnitude: 16.22 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 7, structural_boundaries: 3, import: 2, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `packages/miniflare/src/plugins/kv/sites.ts` (TYPESCRIPT) | Magnitude: 56.2 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 94, structural_boundaries: 27, core_var_decl: 15, concurrency: 10
- `packages/wrangler/src/workflows/commands/instances/send-event.ts` (TYPESCRIPT) | Magnitude: 55.9 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 75, structural_boundaries: 23, import: 7, concurrency: 6
- `packages/workers-shared/utils/configuration/validateURL.ts` (TYPESCRIPT) | Magnitude: 54.48 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 58, branch: 17, core_var_decl: 17, structural_boundaries: 13
- `packages/wrangler/src/check/commands.ts` (TYPESCRIPT) | Magnitude: 199.4 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 199, structural_boundaries: 81, concurrency: 41, branch: 29
- `packages/miniflare/test/test-shared/log.ts` (TYPESCRIPT) | Magnitude: 17.38 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 19, structural_boundaries: 12, args: 7, api: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/miniflare/src/plugins/core/inspector-proxy/inspector-proxy-controller.ts` (TYPESCRIPT) | Magnitude: 153.5 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 230, structural_boundaries: 73, concurrency: 35, args: 29
- `packages/cli/select-list.ts` (TYPESCRIPT) | Magnitude: 53.98 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 57, structural_boundaries: 24, branch: 12, args: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/miniflare/src/shared/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `packages/miniflare/src/plugins/index.ts` (TYPESCRIPT) | Magnitude: 56.68 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 105, structural_boundaries: 79, import: 65, api: 38
- `packages/miniflare/src/workers/shared/index.worker.ts` (TYPESCRIPT) | Magnitude: 38.12 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 32, indent_tabs: 29, api: 22, import: 22
- `packages/containers-shared/src/client/index.ts` (TYPESCRIPT) | Magnitude: 239.4 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 382, api: 220, import: 220
- `packages/vitest-pool-workers/src/worker/lib/cloudflare/test-internal.ts` (TYPESCRIPT) | Magnitude: 22.68 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, api: 8, import: 8, io: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/pages-shared/__tests__/asset-server/responses.test.ts` (TYPESCRIPT) | Magnitude: 16.24 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 58, test: 22, structural_boundaries: 4, args: 2
- `packages/wrangler/src/tunnel/info.ts` (TYPESCRIPT) | Magnitude: 13.04 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 32, structural_boundaries: 9, telemetry: 8, concurrency: 4
- `fixtures/vitest-pool-workers-remote-bindings/run-tests.mjs` (JAVASCRIPT) | Magnitude: 0.03 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 109, structural_boundaries: 17, branch: 16, core_var_decl: 14
- `packages/create-cloudflare/templates/hello-world-with-assets/ts/vitest.config.mts` (TYPESCRIPT) | Magnitude: 16.2 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 7, structural_boundaries: 2, branch: 1, api: 1
- `packages/create-cloudflare/templates/hello-world/ts/vitest.config.mts` (TYPESCRIPT) | Magnitude: 16.2 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 7, structural_boundaries: 2, branch: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/wrangler/src/dev/miniflare/index.ts` (TYPESCRIPT) | Magnitude: 429.02 | Delta: **0.147** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 868, structural_boundaries: 165, branch: 142, core_var_decl: 72

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/workers-shared/asset-worker/tests/kv.test.ts` (TYPESCRIPT) | Magnitude: 264.36 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 91, structural_boundaries: 35, concurrency: 24, test: 23
- `fixtures/nodejs-hybrid-app/tests/index.test.ts` (TYPESCRIPT) | Magnitude: 0.19 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 114, structural_boundaries: 63, concurrency: 48, io: 32
- `packages/create-cloudflare/src/helpers/json.ts` (TYPESCRIPT) | Magnitude: 44.34 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 43, structural_boundaries: 18, generics: 8, branch: 7
- `packages/containers-shared/src/client/models/DeploymentCheckHTTPRequestBody.ts` (TYPESCRIPT) | Magnitude: 14.64 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: branch: 4, structural_boundaries: 4, doc: 4, indent_tabs: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/containers-shared/src/client/models/BadRequestWithCodeError.ts` (TYPESCRIPT) | Magnitude: 17.68 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 6, indent_tabs: 5, api: 3, doc: 3
- `packages/containers-shared/src/client/models/ImageRegistryAlreadyExistsError.ts` (TYPESCRIPT) | Magnitude: 17.68 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 6, indent_tabs: 5, doc: 4, api: 3
- `packages/containers-shared/src/client/models/ImageRegistryNotAllowedError.ts` (TYPESCRIPT) | Magnitude: 17.68 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 6, indent_tabs: 5, doc: 4, api: 3
- `packages/workers-shared/router-worker/src/limited-response.ts` (TYPESCRIPT) | Magnitude: 113.48 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1418, class_start: 896, safety_bypasses: 86, core_var_decl: 64

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/local-explorer-ui/src/routes/do/$className.tsx` (TYPESCRIPT) | Magnitude: 17.44 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 18, structural_boundaries: 13, branch: 6, core_var_decl: 4
- `packages/wrangler/src/utils/shell-quote.ts` (TYPESCRIPT) | Magnitude: 27.38 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 24, structural_boundaries: 9, branch: 6, core_var_decl: 4
- `.github/workflows/e2e-vite.yml` (YAML) | Magnitude: 17.06 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 64, branch: 9, args: 8, globals: 7
- `packages/create-cloudflare/src/help.ts` (TYPESCRIPT) | Magnitude: 62.1 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 67, structural_boundaries: 24, branch: 20, core_var_decl: 13
- `packages/create-cloudflare/src/pages.ts` (TYPESCRIPT) | Magnitude: 44.94 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 75, structural_boundaries: 18, safety: 8, import: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/wrangler/src/__tests__/autoconfig/run.test.ts` -> Churn: **67.12%** | Cog Load: 68.2288% | Debt: 0.0%
- `packages/wrangler/src/deploy/deploy.ts` -> Churn: **62.47%** | Cog Load: 80.8714% | Debt: 8.4212%
- `packages/miniflare/src/index.ts` -> Churn: **61.4%** | Cog Load: 82.0431% | Debt: 8.1969%
- `packages/create-cloudflare/e2e/tests/cli/cli.test.ts` -> Churn: **59.96%** | Cog Load: 100.0% | Debt: 0.0%
- `packages/wrangler/src/__tests__/containers/registries.test.ts` -> Churn: **54.88%** | Cog Load: 91.9523% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/wrangler/src/__tests__/email-routing.test.ts` -> **Thomas Gauvin** (100.0% isolated ownership) | Magnitude: 1040.56
- `packages/wrangler/src/__tests__/r2/catalog-force.test.ts` -> **Carol Xu** (100.0% isolated ownership) | Magnitude: 1006.89
- `packages/vitest-pool-workers/scripts/rtti/rtti.js` -> **Victor Berchet** (100.0% isolated ownership) | Magnitude: 691.72
- `packages/local-explorer-ui/src/__e2e__/r2/r2-bucket.spec.ts` -> **Ben** (100.0% isolated ownership) | Magnitude: 632.74
- `packages/miniflare/src/workers/r2/bucket.worker.ts` -> **Dario Piotrowicz** (100.0% isolated ownership) | Magnitude: 588.48

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/wrangler/src/__tests__/helpers/run-wrangler.ts` -> **Severity: 0.271** (Bridge: 0.0047 * Flux: 57.5%)
- `packages/wrangler/src/index.ts` -> **Severity: 0.114** (Bridge: 0.0057 * Flux: 19.9037%)
- `packages/wrangler/src/deploy/deploy.ts` -> **Severity: 0.113** (Bridge: 0.0012 * Flux: 90.833%)
- `packages/wrangler/e2e/helpers/e2e-wrangler-test.ts` -> **Severity: 0.079** (Bridge: 0.0009 * Flux: 89.9574%)
- `packages/wrangler/src/assets.ts` -> **Severity: 0.062** (Bridge: 0.0009 * Flux: 68.9974%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/wrangler/src/logger.ts` -> **Severity: 4.182** (Embedded: 0.0867 * Error Risk: 48.2121%)
- `packages/wrangler/src/utils/log-file.ts` -> **Severity: 3.016** (Embedded: 0.0557 * Error Risk: 54.1394%)
- `packages/wrangler/src/cfetch/index.ts` -> **Severity: 2.717** (Embedded: 0.05 * Error Risk: 54.3369%)
- `packages/wrangler/src/utils/format-message.ts` -> **Severity: 2.656** (Embedded: 0.0557 * Error Risk: 47.7159%)
- `packages/wrangler/src/dialogs.ts` -> **Severity: 2.364** (Embedded: 0.0413 * Error Risk: 57.2459%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/wrangler/src/logger.ts` -> **Severity: 4303.185** (Blast Radius: 50.01 * Doc Risk: 86.0465%)
- `packages/wrangler/src/utils/log-file.ts` -> **Severity: 1273.62** (Blast Radius: 21.227 * Doc Risk: 60.0%)
- `packages/vite-plugin-cloudflare/playground/__test-utils__/index.ts` -> **Severity: 979.467** (Blast Radius: 14.692 * Doc Risk: 66.6667%)
- `packages/wrangler/src/utils/filesystem.ts` -> **Severity: 917.7** (Blast Radius: 9.177 * Doc Risk: 100.0%)
- `packages/miniflare/src/http/websocket.ts` -> **Severity: 784.3** (Blast Radius: 7.843 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 628 literal sites + 2 sites through wrappers = 630
- **`panics_and_aborts`:** 2116 literal sites + 22 sites through wrappers = 2138

- `invalidWrapped` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `packages/miniflare/src/plugins/core/index.ts`
- `throwRemoteRequired` (function, panics_and_aborts, primitive): 3 call sites in 3 files -- `packages/miniflare/src/workers/shared/remote-bindings-utils.ts`
- `invalidWrappedAsBound` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `packages/miniflare/src/index.ts`
- `readFile` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `packages/create-cloudflare/src/helpers/files.ts`
- `writeFile` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `packages/create-cloudflare/src/helpers/files.ts`
- `appendFile` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/create-cloudflare/src/helpers/files.ts`
- `parseTs` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/codemod/src/index.ts`
- `pullImage` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/containers-shared/src/images.ts`
- `replaceReferences` (function, debug_prints, primitive): 1 call sites in 1 files -- `packages/quick-edit/bundle-dts.ts`
- `setupConsoleWarnCollector` (function, debug_prints, primitive): 1 call sites in 1 files -- `packages/vite-plugin-cloudflare/playground/vitest-setup.ts`
- `throwMultipleFrameworksNonInteractiveError` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/wrangler/src/autoconfig/details/framework-detection.ts`
- `unexpectedLastEvent` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `packages/wrangler/src/cloudchamber/cli/index.ts`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 29150 call pairs -- scoped 27.1%, unique 0.0%, ambiguous 21.2%, external 51.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 27196 | 27.3% | 0.0% | 21.4% | 51.2% |
| javascript | 1874 | 25.2% | 0.0% | 18.2% | 56.6% |
| html | 35 | 5.7% | 0.0% | 0.0% | 94.3% |
| python | 21 | 14.3% | 0.0% | 0.0% | 85.7% |
| shell | 13 | 0.0% | 0.0% | 0.0% | 100.0% |
| php | 11 | 18.2% | 0.0% | 0.0% | 81.8% |

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
